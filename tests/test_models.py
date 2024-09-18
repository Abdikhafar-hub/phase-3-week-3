import unittest
from app import app, db
from models import Band, Venue, Concert

class TestModels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = app
        cls.app.config['TESTING'] = True
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_concerts.db'
        cls.client = cls.app.test_client()
        cls.db = db
        with cls.app.app_context():
            cls.db.create_all()

    @classmethod
    def tearDownClass(cls):
        with cls.app.app_context():
            cls.db.drop_all()

    def setUp(self):
        with self.app.app_context():
            self.db.session.begin()  # Remove subtransactions=True
    
    def tearDown(self):
        with self.app.app_context():
            self.db.session.rollback()

    def test_band_creation(self):
        band = Band(name='The Rockers', hometown='New York')
        self.db.session.add(band)
        self.db.session.commit()
        retrieved_band = Band.query.first()
        self.assertEqual(retrieved_band.name, 'The Rockers')
        self.assertEqual(retrieved_band.hometown, 'New York')

    def test_venue_creation(self):
        venue = Venue(title='Madison Square Garden', city='New York')
        self.db.session.add(venue)
        self.db.session.commit()
        retrieved_venue = Venue.query.first()
        self.assertEqual(retrieved_venue.title, 'Madison Square Garden')
        self.assertEqual(retrieved_venue.city, 'New York')

    def test_concert_creation(self):
        band = Band(name='The Rockers', hometown='New York')
        venue = Venue(title='Madison Square Garden', city='New York')
        self.db.session.add(band)
        self.db.session.add(venue)
        self.db.session.commit()
        
        concert = Concert(date='2024-09-16', band_id=band.id, venue_id=venue.id)
        self.db.session.add(concert)
        self.db.session.commit()
        
        retrieved_concert = Concert.query.first()
        self.assertEqual(retrieved_concert.date, '2024-09-16')
        self.assertEqual(retrieved_concert.band_id, band.id)
        self.assertEqual(retrieved_concert.venue_id, venue.id)

    def test_band_venues(self):
        band = Band(name='The Rockers', hometown='New York')
        venue1 = Venue(title='Madison Square Garden', city='New York')
        venue2 = Venue(title='The Forum', city='Los Angeles')
        self.db.session.add(band)
        self.db.session.add(venue1)
        self.db.session.add(venue2)
        self.db.session.commit()
        
        band.play_in_venue(venue1, '2024-09-16')
        band.play_in_venue(venue2, '2024-09-17')
        
        self.assertEqual(len(band.venues()), 2)

    def test_venue_bands(self):
        band1 = Band(name='The Rockers', hometown='New York')
        band2 = Band(name='The Singers', hometown='Los Angeles')
        venue = Venue(title='Madison Square Garden', city='New York')
        self.db.session.add(band1)
        self.db.session.add(band2)
        self.db.session.add(venue)
        self.db.session.commit()
        
        band1.play_in_venue(venue, '2024-09-16')
        band2.play_in_venue(venue, '2024-09-17')
        
        self.assertEqual(len(venue.bands()), 2)

    def test_hometown_show(self):
        band = Band(name='The Rockers', hometown='New York')
        venue = Venue(title='Madison Square Garden', city='New York')
        self.db.session.add(band)
        self.db.session.add(venue)
        self.db.session.commit()
        
        concert = Concert(date='2024-09-16', band_id=band.id, venue_id=venue.id)
        self.db.session.add(concert)
        self.db.session.commit()
        
        self.assertTrue(concert.hometown_show())

    def test_band_most_performances(self):
        band1 = Band(name='The Rockers', hometown='New York')
        band2 = Band(name='The Singers', hometown='Los Angeles')
        venue = Venue(title='Madison Square Garden', city='New York')
        self.db.session.add(band1)
        self.db.session.add(band2)
        self.db.session.add(venue)
        self.db.session.commit()
        
        band1.play_in_venue(venue, '2024-09-16')
        band1.play_in_venue(venue, '2024-09-17')
        band2.play_in_venue(venue, '2024-09-18')
        
        self.assertEqual(Band.most_performances(), band1)

    def test_venue_concert_on(self):
        band = Band(name='The Rockers', hometown='New York')
        venue = Venue(title='Madison Square Garden', city='New York')
        self.db.session.add(band)
        self.db.session.add(venue)
        self.db.session.commit()
        
        concert = Concert(date='2024-09-16', band_id=band.id, venue_id=venue.id)
        self.db.session.add(concert)
        self.db.session.commit()
        
        self.assertEqual(venue.concert_on('2024-09-16'), concert)

    def test_venue_most_frequent_band(self):
        band1 = Band(name='The Rockers', hometown='New York')
        band2 = Band(name='The Singers', hometown='Los Angeles')
        venue = Venue(title='Madison Square Garden', city='New York')
        self.db.session.add(band1)
        self.db.session.add(band2)
        self.db.session.add(venue)
        self.db.session.commit()
        
        band1.play_in_venue(venue, '2024-09-16')
        band1.play_in_venue(venue, '2024-09-17')
        band2.play_in_venue(venue, '2024-09-18')
        
        self.assertEqual(venue.most_frequent_band(), band1)

if __name__ == '__main__':
    unittest.main()
