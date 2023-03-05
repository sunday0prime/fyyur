from models import Artist, Venue, Show, Album, Song
from datetime import datetime, timezone

artist1 = Artist(
    name='Faouzia',
    city='Casablanca',
    state='CA',
    phone='182-390-2389',
    genres='Pop, Soul, R&B',
    book_from=datetime(2022, 2, 1, 0, 0, 0, 0, timezone.utc),
    book_till=datetime(2023, 5, 27, 0, 0, 0, 0, timezone.utc),
    website='https://officialfaouzia.com',
    image_link='https://en.vogue.me/wp-content/uploads/2021/01/faouzia-feature2.jpg',
    facebook_link='https://facebook.com/faouziaofficial.com',
    date_listed=datetime(2022, 1, 31),
    seeking_venue=True,
    seeking_description='Faouzia\'s tour is coming to New York and she is looking for a venue to host her show.'
)
artist2 = Artist(
    name='Dua Lipa',
    city='New York',
    state='NY',
    phone='121-382-0983',
    genres='Pop, R&B, Electronic',
    book_from=datetime(2021, 11, 30, 23, 59, 0, 0, timezone.utc),
    book_till=datetime(2024, 11, 30, 23, 59, 59, 0, timezone.utc),
    website='https://dualipaofficial.com',
    image_link='https://ichef.bbci.co.uk/news/976/cpsprodpb/D760/production/_120763155_gettyimages-1342887921.jpg',
    facebook_link='https://facebook.com/dualipa',
    date_listed=datetime(2022, 8, 1),
    seeking_venue=False,
    seeking_description=''
)
artist3 = Artist(
    name='Chris Brown',
    city='Houston',
    state='TX',
    phone='121-382-0983',
    genres='Pop, R&B, Electronic',
    book_from=datetime(2022, 4, 23, 23, 59, 0, 0, timezone.utc),
    book_till=datetime(2022, 8, 30, 23, 59, 59, 0, timezone.utc),
    website='https://chrisbrownmusic.com',
    image_link='https://www.aceshowbiz.com/display/images/photo/2019/10/04/00142341.jpg',
    facebook_link='https://facebook.com/chrisbrown_official',
    date_listed=datetime(2022, 8, 14),
    seeking_venue=False,
    seeking_description=''
)
artist4 = Artist(
    name='Carrie Underwood',
    city='Los Angeles',
    state='CF',
    phone='121-382-0983',
    genres='Pop, R&B, Electronic',
    book_from=datetime(2021, 11, 30, 23, 59, 0, 0, timezone.utc),
    book_till=datetime(2022, 5, 30, 23, 59, 59, 0, timezone.utc),
    website='https://carrieunderwood.com',
    image_link='https://parade.com/.image/t_share/MTkxNTA0OTYwMzc3MDcxMjY3/2022-iheartcountry-festival-presented-by-capital-one--red-carpet.jpg',
    facebook_link='https://facebook.com/dualipa',
    date_listed=datetime(2022, 6, 20),
    seeking_venue=False,
    seeking_description='')
artist5 = Artist(
    name='Ed Sheeran',
    city='Chicago',
    state='IL',
    phone='121-382-0983',
    genres='Pop, Synth-Pop',
    book_from=datetime(2022, 8, 16, 23, 59, 0, 0, timezone.utc),
    book_till=datetime(2024, 11, 30, 23, 59, 59, 0, timezone.utc),
    website='https://edsheeranofficial.com',
    image_link='https://static.independent.co.uk/s3fs-public/thumbnails/image/2014/12/05/18/Ed-Sheeran.jpg',
    facebook_link='https://facebook.com/ed_sheeran',
    date_listed=datetime(2022, 5, 21),
    seeking_venue=True,
    seeking_description='Ed Sheeran is coming to Houston Texas for his tour and is seeking a venue to perform.')

venue1 = Venue(
    name='Country Pines',
    city='San Antonio',
    state='CF',
    address='6305 Adams St, Lincoln',
    phone='402-441-6545',
    image_link='http://images.alltimefavorites.com/large-mobile-concert-stage-production-rental-44125.jpg',
    facebook_link='https://facebook.com/countrypines',
    genres='Pop, Blues, Jazz',
    website='https://countrypines.event',
    seeking_talent=False,
    seeking_description='',
    date_listed=datetime(2022, 1, 21)
)
venue2 = Venue(
    name='Lancaster Event Center',
    city='Tampa',
    state='FL',
    address='84th St, Lincoln',
    phone='402-441-6545',
    image_link='https://www.ldsystems.com/wp-content/uploads/2022/02/sanantoniorodeo-1-2.jpg',
    facebook_link='https://facebook.com/lancaster_event_center',
    genres='Jazz, Raggea, Blues',
    website='https://lancasterbookings.com',
    seeking_talent=True,
    seeking_description='We are seeking fresh talents to perform on friday nights',
    date_listed=datetime(2022, 4, 1))

venue3 = Venue(
    name='Park Centers Banquet Hall',
    city='Miami',
    state='FL',
    address='2608 Park Blvd, Lincoln',
    phone='402-440-1513',
    image_link='https://media2.sacurrent.com/sacurrent/imager/u/slideshow/27249883/720a0934.jpg',
    facebook_link='https://facebook.com/park_centers_banquet',
    genres='Jazz, Rap, Hip-hop',
    website='https://park_centers.com',
    seeking_talent=True,
    seeking_description='We are seeking instrumentalist to join our friday night band',
    date_listed=datetime(2022, 5, 13))

venue4 = Venue(
    name='Roca Ridge Events',
    city='Austin',
    state='Texas',
    address='5265 Prairie Sage Dr, Roca',
    phone='402-405-9212',
    image_link='https://www.americanrunwayrental.com/images/TX-LED-runway-rentals.jpg',
    facebook_link='https://facebook.com/rocaridegesevents',
    genres='Jazz, Blues, Raggea',
    website='https://rocaridge.event',
    seeking_talent=True,
    seeking_description='We are seeking backup singers for out friday night shows.',
    date_listed=datetime(2022, 8, 1))

venue5 = Venue(
    name='Havelock Social Hall',
    city='San Francisco',
    state='CF',
    address='62nd St, Lincoln',
    phone='402-441-6545',
    image_link='https://www.ldsystems.com/wp-content/uploads/2022/02/sanantoniorodeo-2-1.jpg',
    facebook_link='',
    genres='Rap, Hip-Hop, Spoken words',
    website='https://havelockhalls.com',
    seeking_talent=False,
    seeking_description='',
    date_listed=datetime(2022, 7, 30))

show1 = Show(
    start_time=datetime(2022, 1, 2, 10, 0, 0, 0, timezone.utc)
)
show2 = Show(
    start_time=datetime(2022, 4, 21, 22, 59, 0, 0, timezone.utc)
)
show3 = Show(
    start_time=datetime(2022, 10, 10, 23, 0, 0, 0, timezone.utc)
)
show4 = Show(
    start_time=datetime(2023, 3, 30, 23, 0, 0, 0, timezone.utc)
)
show5 = Show(
    start_time=datetime(2022, 12, 3, 23, 59, 0, 0, timezone.utc)
)

album1 = Album(
    name="Exclusive",
    released=datetime(2008, 3, 13, 0, 0, 0, 0, timezone.utc),
    cover='https://i.scdn.co/image/ab67616d0000b27331bbeed21ba6c049b29a6198',
)
album2 = Album(
    name='Citizen',
    released=datetime(2022, 2, 1, 0, 0, 0, 0, timezone.utc),
    cover='https://cdns-images.dzcdn.net/images/cover/00416fcf91ff4547250e20f0b00b9e6b/500x500.jpg'

)
album3 = Album(
    name='Saweetie',
    released=datetime(2020, 2, 1, 0, 0 , 0, 0, timezone.utc),
    cover='https://is3-ssl.mzstatic.com/image/thumb/Music115/v4/ff/f3/06/fff3062e-3d63-d7f8-30dd-2ee49010b731/190295559472.jpg/400x400bb.jpg'
)
album4 = Album(
    name='Cry Pretty',
    released=datetime(2018, 9, 1, 0, 0, 0, 0, timezone.utc),
    cover='https://upload.wikimedia.org/wikipedia/en/d/dc/Carrie_Underwood_-_Cry_Pretty_%28Official_Album_Cover%29.png'
)
album5 = Album(
    name='No.6 Collaboration Project',
    released=datetime(2019, 1, 1, 0, 0, 0, 0, timezone.utc),
    cover='https://th.bing.com/th/id/OIP.Ry2eOCRp0LoTh7Z2w11xzwHaHa?pid=ImgDet&rs=1'
)

song1 = Song(
    title='With you',
    duration=193,
    url='https://cdn.pixabay.com/download/audio/2022/08/03/audio_54ca0ffa52.mp3?filename=milk-shake-116330.mp3'
)
song2 = Song(
    title='Loneliness of the Winter',
    duration=208.38,
    url='https://cdn.pixabay.com/download/audio/2022/04/30/audio_3c7238ff32.mp3?filename=loneliness-of-the-winner-110416.mp3'
)
song3 = Song(
    title='Electronic Rock (King Around Here)',
    duration=143,
    url='https://cdn.pixabay.com/download/audio/2022/01/18/audio_d0a13f69d2.mp3?filename=electronic-rock-king-around-here-15045.mp3'
)
song4 = Song(
    title='Chill Abstract (Intention)',
    duration=123,
    url='https://cdn.pixabay.com/download/audio/2021/12/13/audio_b9c0dc9e48.mp3?filename=chill-abstract-intention-12099.mp3'
)
song5 = Song(
    title='Cinematic Dramatic',
    duration=139,
    url='https://cdn.pixabay.com/download/audio/2021/11/23/audio_035a943c87.mp3?filename=cinematic-dramatic-11120.mp3'
)
song6 = Song(
    title='WatR Fluid',
    duration=161,
    url='https://cdn.pixabay.com/download/audio/2021/11/01/audio_67c5757bac.mp3?filename=watr-fluid-10149.mp3'
)
song7 = Song(
    title='Battle of the Dragons',
    duration = 237,
    url='https://cdn.pixabay.com/download/audio/2021/09/06/audio_14fb3b6893.mp3?filename=battle-of-the-dragons-8037.mp3'
)
song8 = Song(
    title='Triumphant',
    duration=118,
    url='https://cdn.pixabay.com/download/audio/2021/08/08/audio_6e054b59f6.mp3?filename=triumphant-long-6673.mp3'
)
song9 = Song(
    title='Milk Shake',
    duration=133,
    url='https://cdn.pixabay.com/download/audio/2022/08/03/audio_54ca0ffa52.mp3?filename=milk-shake-116330.mp3'
)
song10 = Song(
    title='Lofi Study',
    duration=147,
    url='https://cdn.pixabay.com/download/audio/2022/05/27/audio_1808fbf07a.mp3?filename=lofi-study-112191.mp3'
)

album1.songs.append(song1)
album1.songs.append(song6)
album2.songs.append(song2)
album3.songs.append(song3)
album3.songs.append(song7)
album4.songs.append(song4)
album4.songs.append(song8)
album5.songs.append(song5)
album5.songs.append(song9)

venue1.shows.append(show2)
venue2.shows.append(show5)
venue3.shows.append(show1)
venue4.shows.append(show4)
venue5.shows.append(show5)

artist1.shows.append(show3)
artist2.shows.append(show5)
artist3.shows.append(show4)
artist4.shows.append(show1)
artist5.shows.append(show1)

artist1.albums.append(album1)
artist2.albums.append(album2)
artist3.albums.append(album3)
artist4.albums.append(album4)
artist5.albums.append(album5)

def initialize_db(db):
    db.create_all()
    db.session.add(artist1)
    db.session.add(artist2)
    db.session.add(artist3)
    db.session.add(artist4)
    db.session.add(artist5)
    db.session.commit()
    db.session.close()