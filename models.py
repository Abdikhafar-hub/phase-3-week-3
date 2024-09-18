from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Association table for many-to-many relationship
bands_venues = db.Table('bands_venues',
    db.Column('band_id', db.Integer, db.ForeignKey('band.id')),
    db.Column('venue_id', db.Integer, db.ForeignKey('venue.id'))
)

class Band(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    hometown = db.Column(db.String(100), nullable=False)
    concerts = db.relationship('Concert', backref='band', lazy=True)
    venues = db.relationship('Venue', secondary=bands_venues, backref='bands')

    def get_concerts(self):
        return Concert.query.filter_by(band_id=self.id).all()

    def get_venues(self):
        return Venue.query.join(bands_venues).filter(bands_venues.c.band_id == self.id).all()

    def play_in_venue(self, venue, date):
        concert = Concert(band_id=self.id, venue_id=venue.id, date=date)
        db.session.add(concert)
        db.session.commit()

    def all_introductions(self):
        return [f"Hello {concert.venue.city}!!!!! We are {self.name} and we're from {self.hometown}" for concert in self.get_concerts()]

    @classmethod
    def most_performances(cls):
        bands = cls.query.all()
        return max(bands, key=lambda band: len(band.get_concerts()))

class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    concerts = db.relationship('Concert', backref='venue', lazy=True)

    def get_concerts(self):
        return Concert.query.filter_by(venue_id=self.id).all()

    def get_bands(self):
        return Band.query.join(bands_venues).filter(bands_venues.c.venue_id == self.id).all()

    def concert_on(self, date):
        return Concert.query.filter_by(venue_id=self.id, date=date).first()

    def most_frequent_band(self):
        bands = {}
        for concert in self.get_concerts():
            band = Band.query.get(concert.band_id)
            if band not in bands:
                bands[band] = 0
            bands[band] += 1
        return max(bands, key=bands.get)

class Concert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(100), nullable=False)
    band_id = db.Column(db.Integer, db.ForeignKey('band.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)

    def get_band(self):
        return Band.query.get(self.band_id)

    def get_venue(self):
        return Venue.query.get(self.venue_id)

    def hometown_show(self):
        band = self.get_band()
        return self.get_venue().city == band.hometown

    def introduction(self):
        return f"Hello {self.get_venue().city}!!!!! We are {self.get_band().name} and we're from {self.get_band().hometown}"
