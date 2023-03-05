from app import db, datetime, timezone

# TODO: connect to a local postgresql database
# DONE in config file
#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#


class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    genres = db.Column(db.String())
    website = db.Column(db.String(225))
    seeking_talent = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(500))
    date_listed = db.Column(db.DateTime(timezone.utc), nullable=False)
    shows = db.relationship('Show', backref='Venue', lazy='dynamic')

    def format(self):
      out_pst = []
      out_upc = []
      for show in self.shows:
        if (show.start_time > datetime.now(timezone.utc)):
          out_upc.append(show.format())
        else:
          out_pst.append(show.format())

      return {
        'id': self.id,
        'name': self.name,
        'city': self.city,
        'state': self.state,
        'address': self.address,
        'phone': self.phone,
        'image_link': self.image_link,
        'facebook_link': self.facebook_link,
        'date_listed': str(self.date_listed),
        'genres': self.genres.split(', '),
        'website': self.website,
        'seeking_talent': self.seeking_talent,
        'seeking_description': self.seeking_description,
        'past_shows': out_pst,
        'past_shows_count': len(out_pst),
        'upcoming_shows': out_upc,
        'upcoming_shows_count': len(out_upc),
        'num_upcoming_shows': len(out_upc)
      }

    def __repr__(self) -> str:
        return f'<Venue ID:{self.id}, Name:{self.name}, City:{self.city}, State:{self.state}, Address:{self.address}, Phone:{self.phone}, Genre:{self.genres}, Shows:{len(self.shows)}>'

class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    website = db.Column(db.String(500))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, nullable=False)
    seeking_description = db.Column(db.String(500), nullable=True)
    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    book_from = db.Column(db.DateTime(timezone.utc), nullable=False)
    book_till = db.Column(db.DateTime(timezone.utc), nullable=False)
    date_listed = db.Column(db.DateTime(timezone.utc), nullable=False)
    albums = db.relationship('Album', backref='aritst', lazy='dynamic')
    shows = db.relationship('Show', backref='Artist', lazy='dynamic')
    
    def format(self):
      out_pst = []
      out_upc = []
      albums = []
      for album in self.albums:
        albums.append(album.format())

      for show in self.shows:
        if (show.start_time > datetime.now(timezone.utc)):
          out_upc.append(show.format())
        else:
          out_pst.append(show.format())
      
      return {
        'id': self.id,
        'name': self.name,
        'city': self.city,
        'state': self.state,
        'phone': self.phone,
        'date_listed': self.date_listed,
        'genres': self.genres.split(', '),
        'website': self.website,
        'image_link': self.image_link,
        'facebook_link': self.facebook_link,
        'seeking_venue': self.seeking_venue,
        'seeking_description': self.seeking_description,
        'albums': albums,
        'albums_count': len(albums),
        'past_shows': out_pst,
        'past_shows_count': len(out_pst),
        'upcoming_shows': out_upc,
        'upcoming_shows_count': len(out_upc),
        'num_upcoming_shows': len(out_upc),
        'book_from': str(self.book_from),
        'book_till': str(self.book_till)
      }

    def __repr__(self) -> str:
        return f'<Artist ID:{self.id}, Name:{self.name}, City:{self.city}, Genre:{self.genres}, Seeking_V:{self.seeking_venue}, Shows:{len(self.shows)}>'


# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
class Show(db.Model):
  __tablename__ = 'shows'

  id = db.Column(db.Integer, primary_key=True)
  venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=False)
  artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
  start_time = db.Column(db.DateTime(timezone.utc), nullable=False)

  def format(self):
    #sub queries were maintained so that dictionary can be easily expanded if needed.
    return {
        'id':self.id,
        'venue_id':self.venue_id,
        'artist_id':self.artist_id,
        'start_time': str(self.start_time),
        'venue_name': self.Venue.name,
        'artist_name': self.Artist.name,
        'venue_image': self.Venue.image_link,
        'artist_image_link': self.Artist.image_link
    }
  
  def __repr__(self) -> str:
      return f'<Show ID:{self.id} Venue_ID:{self.venue_id} Artist_ID:{self.artist_id} start_time:{self.start_time}>'


class Album(db.Model):
    __tablename__ = 'albums'

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=True)
    name = db.Column(db.String(50), nullable=False)
    released = db.Column(db.DateTime(timezone.utc), nullable=True)
    cover = db.Column(db.String(500), nullable=True)
    songs = db.relationship('Song', backref='album')

    #returns the collection of songs classes in album
    def getSongs(self):
      return db.session.query(Song).filter_by(Song.album_id==self.id).all()

    def getSongs_dict(self):
      songs = []
      for song in self.songs:
        songs.append(song.format())
      
      return songs

    def format(self):
      return {
        'id': self.id,
        'artist_id': self.artist_id,
        'name': self.name,
        'released': self.released,
        'cover': self.cover,
        'songs': self.getSongs_dict(),
        'songs_count': len(self.songs)
      }
    
    def __repr__(self) -> str:
        return f'<Album ID:{self.id}, Name:{self.name}, Genres:{self.genres}, Released:{self.released}, Cover:{self.cover} >'
        
class Song(db.Model):
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    duration = db.Column(db.Float, nullable=False)
    url = db.Column(db.String(255), nullable=True)
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id'), nullable=False)

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'duration': self.duration,
            'url': self.url,
            'album_id': self.album_id,
            'album_name': self.album.name,
            'album_cover': self.album.cover
        }

    def __repr__(self) -> str:
        return f'<Song ID:{self.id}, Title:{self.title}, Duration:{self.duration} URL:{self.url} >'
