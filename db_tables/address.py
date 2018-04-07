from .base import BASE
from sqlalchemy import Column, String, Integer


class Address(BASE):
    __tablename__ = 'oc_address'

    address_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer)
    firstname = Column(String)
    lastname = Column(String)
    company = Column(String)
    address_1 = Column(String)
    address_2 = Column(String)
    city = Column(String)
    postcode = Column(String)
    country_id = Column(Integer)
    zone_id = Column(Integer)

    def __init__(self,
                 address_id,
                 customer_id,
                 firstname,
                 lastname,
                 company,
                 address_1,
                 address_2,
                 city,
                 postcode,
                 country_id,
                 zone_id):
        self.address_id = address_id
        self.customer_id = customer_id
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.address_1 = address_1
        self.address_2 = address_2
        self.city = city
        self.postcode = postcode
        self.country_id = country_id
        self.zone_id = zone_id

    def __repr__(self):
        return f"{self.firstname}, " \
               f"{self.lastname}, " \
               f"{self.company}, " \
               f"{self.address_1}, " \
               f"{self.address_2}, " \
               f"{self.city}, " \
               f"{self.postcode}, " \
               f"{self.country_id}, " \
               f"{self.zone_id}"

    def __eq__(self, other):
        return (self.firstname == other.firstname and
                self.lastname == other.lastname and
                self.company == other.company and
                self.address_1 == other.address_1 and
                self.address_2 == other.address_2 and
                self.city == other.city and
                self.country_id == other.country_id and
                self.zone_id == other.zone_id)
