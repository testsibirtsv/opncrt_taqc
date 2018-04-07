from .base import BASE
from sqlalchemy import Column, String, Integer


class Country(BASE):
    __tablename__ = 'oc_country'

    country_id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'
