
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment
import datetime

from sqlalchemy.orm import backref
db = SQLAlchemy()



class Show(db.Model):
  __tablename__ = 'shows'
  id = db.Column(db.Integer, primary_key = True)
  start_time = db.Column(db.DateTime, nullable = False)


  venue = db.relationship('Venue')
  venue_id = db.Column(db.Integer, db.ForeignKey('venues.id', ondelete = 'CASCADE'), nullable = False)

  artist = db.relationship('Artist')
  artist_id = db.Column(db.Integer, db.ForeignKey('artists.id', ondelete = 'CASCADE') ,  nullable = False)

#Venue Model

class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, default = False)
    seeking_description = db.Column(db.String(500))
    shows = db.relationship('Show', backref='venues', lazy = 'joined', cascade = 'all,delete')
    



#Artist Model

class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, default = False)
    seeking_description = db.Column(db.String(500))


    shows = db.relationship('Show', backref = 'artists',lazy = 'joined', cascade = 'all,delete')
    