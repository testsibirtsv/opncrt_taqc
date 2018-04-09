"""
Contains the Customer class for interacting with the database.
"""
from .base import BASE
from sqlalchemy import Column, String, Integer


# pylint: disable=too-few-public-methods
class Customer(BASE):
    """
    Representing the oc_customer table from the opencart database.
    """
    __tablename__ = 'oc_customer'

    customer_id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String, unique=True)
    telephone = Column(String)

    def __init__(self, customer_id, firstname, lastname, email, telephone):
        self.customer_id = customer_id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.telephone = telephone

    def __repr__(self):
        return f'{self.firstname} {self.lastname} {self.email} {self.telephone}'
