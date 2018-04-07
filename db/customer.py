"""
TODO
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer
from models.personaldetails import PersonalDetails

ENGINE = create_engine('mysql://root@localhost/opencart')
SESSION = sessionmaker(bind=ENGINE)

BASE = declarative_base()


def session_factory():
    """
    TODO
    """
    BASE.metadata.create_all(ENGINE)
    return SESSION()

# pylint: disable=too-few-public-methods
class Customer(BASE):
    """
    TODO
    """
    __tablename__ = 'oc_customer'

    customer_id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String, unique=True)
    telephone = Column(String)

    def __init__(self, firstname, lastname, email, telephone):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.telephone = telephone

    def __repr__(self):
        return f'{self.firstname} {self.lastname} {self.email} {self.telephone}'

    @staticmethod
    def get_from_db_by_email(user):
        """
        TODO
        """
        session = session_factory()
        query = session.query(Customer)
        customer = query.filter(Customer.email == user.email).first()
        return PersonalDetails(first_name=customer.firstname,
                               last_name=customer.lastname,
                               email=customer.email,
                               telephone=customer.telephone)


def get_people():
    """
    TODO
    """
    session = session_factory()
    people_query = session.query(Customer)
    session.close()
    return people_query.all()
