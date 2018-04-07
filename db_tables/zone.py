from .base import BASE
from sqlalchemy import Column, String, Integer


class Zone(BASE):
    __tablename__ = 'oc_zone'

    zone_id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'
