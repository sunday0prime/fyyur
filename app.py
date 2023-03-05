# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#

from models import Artist, Venue, Show, Album, Song
from dataclasses import dataclass
from datetime import timezone
import json
import re
from wtforms import ValidationError
import sys
import dateutil.parser
import babel
from flask import Flask, abort, render_template, request, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from sqlalchemy import or_
from forms import *
# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)


# Configure Migrate
migrate = Migrate(app, db)

# ----------------------------------------------------------------------------#
# Filters.
# ----------------------------------------------------------------------------#


def format_datetime(value, format='medium'):
    date = dateutil.parser.parse(value)
    if format == 'full':
        format = "EEEE MMMM, d, y 'at' h:mma"
    elif format == 'medium':
        format = "EE MM, dd, y h:mma"
    return babel.dates.format_datetime(date, format, locale='en')


app.jinja_env.filters['datetime'] = format_datetime

# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#


@app.route('/')
def index():
    venues, artists = [], []
    for artist in Artist.query.order_by(Artist.date_listed.desc()).limit(10).all():
        artists.append(artist.format())
    for venue in Venue.query.order_by(Venue.date_listed.desc()).limit(10).all():
        venues.append(venue.format())

    data = {'recent_artists': artists, 'recent_venues': venues}
    return render_template('pages/home.html', data=data)


#  Venues
#  ----------------------------------------------------------------

@app.route('/venues')
def venues():
    data = []
    # Get all Venues, loop through to format() to serializable dictionary
    # If not group exists, create it and add venue, find and add it
    # num_upcoming_show is defined in Venue.format()

    for venue in Venue.query.order_by(Venue.city).all():
        venue = venue.format()
        if (list(filter(lambda d: d['city'] == venue['city'], data))):
            list(filter(lambda d: d['city'] == venue['city'], data))[
                0]['venues'].append(venue)
        else:
            new_group = {'city': venue['city'],
                         'state': venue['state'], 'venues': [venue]}
            data.append(new_group)

    return render_template('pages/venues.html', areas=data)


@app.route('/venues/search', methods=['POST'])
def search_venues():
    # algorithm
    # Get string query from request, filter all venues by name, city and state with search string
    # return result
    # Use SQLAlchemy filter method to filter items
    # Use ilike to ensure search is case insensity.
    search = f"%{request.form.get('search_term')}%"
    res = Venue.query.filter(or_(Venue.name.ilike(search), Venue.city.ilike(
        search), Venue.state.ilike(search))).order_by(Venue.name).limit(100).all()
    response = {'count': len(res), 'data': res}
    return render_template('pages/search_venues.html', results=response, search_term=request.form.get('search_term', ''))


@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
    # Algorithm
    # Get venue id from param
    # Use SQLAlchemy get method to get venue with specified id.

    data = Venue.query.get(venue_id).format()
    return render_template('pages/show_venue.html', venue=data)

#  Create Venue
#  ----------------------------------------------------------------


@app.route('/venues/create', methods=['GET'])
def create_venue_form():
    form = VenueForm()
    return render_template('forms/new_venue.html', form=form)


@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
    # Algorithm
    # Validate the form
    # Create a new venue instance with the submitted param
    # Add it to the data base and commit it.
    # redirect to the home page
    err = False
    if (re.match(r'[0-9]{3}-[0-3]{3}-[0-9]{4}', request.form['phone'])):
        err = True
        raise ValidationError(
            "Error! Phone number must be in format xxx-xxx-xxxx")

    form = VenueForm(request.form)
    venue = Venue(
        name=form.name.data,
        genres=form.genres.data,
        address=form.address.data,
        city=form.city.data,
        state=form.state.data,
        phone=form.phone.data,
        facebook_link=form.facebook_link.data,
        image_link=form.image_link.data,
        website=form.website_link.data,
        seeking_talent=bool(form.seeking_talent.data),
        seeking_description=form.seeking_description.data
    )
    try:
        db.session.add(venue)
        db.session.commit()
    except:
        err = True
        db.session.rollback()
        print(sys.exc_info())
        flash(
            f'An error occured. Venue {request.form["name"]} could not be added.')
    finally:
        db.session.close()
        flash(f'Venue {request.form["name"]} was successfully listed!')
    # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
    return render_template('pages/home.html')


@app.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
    # Algorith
    # Check if venue with the given ID exists
    # If it exists, remove it else, raise an error
    err = False
    try:
        db.session.delete(Venue.query.get(venue_id))
        db.session.commit()
    except:
        err = True
        db.session.rollback()
    finally:
        db.session.close()
    if (err == True):
        abort(500)
    else:
        return redirect('/venues')


#  Artists
#  ----------------------------------------------------------------
@app.route('/artists')
def artists():
    # TODO: replace with real data returned from querying the database
    # **For Inspection** DONE
    data = []
    for artist in Artist.query.order_by(Artist.name).all():
        data.append(artist.format())

    return render_template('pages/artists.html', artists=data)


@app.route('/artists/search', methods=['POST'])
def search_artists():
    # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
    # seach for "A" should return "Guns N Petals", "Matt Quevado", and "The Wild Sax Band".
    # search for "band" should return "The Wild Sax Band".
    # **For Inspection** DONE
    # limited to the first 100 results
    search = f"%{request.form.get('search_term')}%"
    res = Artist.query.filter(or_(Artist.name.ilike(search), Artist.city.ilike(
        search), Artist.state.ilike(search))).order_by(Artist.name).limit(100).all()
    response = {'count': len(res), 'data': res}
    return render_template('pages/search_artists.html', results=response, search_term=request.form.get('search_term', ''))


@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
    # shows the artist page with the given artist_id
    # TODO: replace with real artist data from the artist table, using artist_id
    # **For Inspection** DONE
    # data = Artist.query.get(artist_id).format()
    data = Artist.query.get(artist_id).format()
    return render_template('pages/show_artist.html', artist=data)

#  Update
#  ----------------------------------------------------------------


@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
    form = ArtistForm()
    # TODO: populate form with fields from artist with ID <artist_id>
    # **For Inspection** DONE
    artist = Artist.query.get(artist_id).format()
    return render_template('forms/edit_artist.html', form=form, artist=artist)


@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
    # TODO: take values from the form submitted, and update existing
    # artist record with ID <artist_id> using the new attributes
    # **For Inspection** Untested
    err = False
    if (re.match(r'[0-9]{3}-[0-9]{3}-[0-9]{4}', request.form['phone'])):
        err = True
        raise ValidationError(
            "Error! Phone number must be in format xxx-xxx-xxxx")
    form = ArtistForm(request.form)
    artist = Artist.query.get(artist_id)
    artist.name = form.name.data
    artist.city = form.city.data
    artist.state = form.state.data
    artist.phone = form.phone.data
    artist.genres = form.genres.data
    artist.website = form.website_link.data
    artist.image_link = form.image_link.data
    artist.facebook_link = form.facebook_link.data
    artist.seeking_venue = form.seeking_venue.data
    artist.seeking_description = form.seeking_description.data
    try:
        # db.session.add(artist) This statement is not required for an update task
        db.session.commit()
    except:
        err = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
        if (err):
            abort(500)
        else:
            return redirect(url_for('show_artist', artist_id=artist_id))


@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
    form = VenueForm()
    # TODO: populate form with values from venue with ID <venue_id>
    # **For Inspection** Untested
    venue = Venue.query.get(venue_id)
    return render_template('forms/edit_venue.html', form=form, venue=venue.format())


@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
    # TODO: take values from the form submitted, and update existing
    # venue record with ID <venue_id> using the new attributes
    venue = Venue.query.get(venue_id)
    venue.name = request.form['name']
    venue.city = request.form['city']
    venue.state = request.form['state']
    venue.address = request.form['address']
    venue.phone = request.form['phone']
    venue.image_link = request.form['image_link']
    venue.facebook_link = request.form['facebook_link']
    venue.genres = request.form['genres']
    venue.website = request.form['website_link']
    return redirect(url_for('show_venue', venue_id=venue_id))

#  Create Artist
#  ----------------------------------------------------------------


@app.route('/artists/create', methods=['GET'])
def create_artist_form():
    form = ArtistForm()
    return render_template('forms/new_artist.html', form=form)


@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
    # called upon submitting the new artist listing form
    # TODO: insert form data as a new Venue record in the db, instead
    # TODO: modify data to be the data object returned from db insertion
    err = False
    if (re.match(r'[0-9]{3}-[0-3]{3}-[0-9]{4}', request.form['phone'])):
        err = True
        raise ValidationError(
            'Error! Phone number must be in format xxx-xxx-xxxx')
    form = ArtistForm(request.form)
    artist = Artist(
        name=form.name.data,
        city=form.city.data,
        state=form.state.data,
        phone=form.phone.data,
        genres=form.genres.data,
        website=form.website_link.data,
        image_link=form.image_link.data,
        facebook_link=form.facebook_link.data,
        seeking_venue=bool(form.seeking_venue.data),
        seeking_description=form.seeking_description.data
    )
    try:
        db.session.add(artist)
        db.session.commit()
    except:
        err = True
        db.session.rollback()
        print(sys.exc_info())
        flash(
            f'An error occured. Artist {request.form["name"]} could not be added.')
    finally:
        db.session.close()
    # on successful db insert, flash success
    # TODO: on unsuccessful db insert, flash an error instead.
    # e.g., flash('An error occurred. Artist ' + data.name + ' could not be listed.')
    if (err == True):
        abort(500)
    else:
        flash('Artist ' + request.form['name'] + ' was successfully listed!')
        return render_template('pages/home.html')


#  Shows
#  ----------------------------------------------------------------

@app.route('/shows')
def shows():
    # displays list of shows at /shows
    # TODO: replace with real venues data.
    # **For Inspection** Done!
    # Appends dictionary for each query result item to data list
    data = []
    for dat in Show.query.order_by(Show.start_time).all():
        data.append(dat.format())

    return render_template('pages/shows.html', shows=data)


@app.route('/shows/create')
def create_shows():
    # renders form. do not touch.
    form = ShowForm()
    return render_template('forms/new_show.html', form=form)


@app.route('/shows/create', methods=['POST'])
def create_show_submission():
    # called to create new shows in the db, upon submitting new show listing form
    # TODO: insert form data as a new Show record in the db, instead
    err = False
    msg = ''
    form = ShowForm()
    show = Show(artist_id=request.form.get('artist_id'), venue_id=request.form.get(
        'venue_id'), start_time=request.form.get('start_time'))
    artist = Artist.query.get(show.artist_id)
    if not (str(artist.book_from) < show.start_time and str(artist.book_till) > show.start_time):
        err = True
        msg = f'{ artist.name } is only available for bookings from {artist.book_from} to {artist.book_till}.'
        flash(msg)
        abort(500)
    try:
        db.session.add(show)
        db.session.commit()
    except:
        err = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    # on successful db insert, flash success
    # TODO: on unsuccessful db insert, flash an error instead.
    # e.g., flash('An error occurred. Show could not be listed.')
    # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
    if (err == True):
        flash('Something unexpected happened')
        abort(500)
    else:
        flash('Show was successfully listed!')
        return render_template('pages/home.html')


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

# ----------------------------------------------------------------------------#
# Launch.
# ----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
