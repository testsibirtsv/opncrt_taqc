from db_tables.customer import Customer
from db_tables.base import session_factory
from models.personaldetails import PersonalDetails


def get_from_db_by_email(user):
    """
    TODO
    """
    session = session_factory()
    query = session.query(Customer)
    customer = query.filter(Customer.email == user.email).first()
    session.close()
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


print(get_from_db_by_email(PersonalDetails(email="taqc296@gmail.com")))
