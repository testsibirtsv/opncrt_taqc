from db.customer import Customer
from db.base import session_factory
from models.personaldetails import PersonalDetails


class DbCustomer:

    @staticmethod
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


print(DbCustomer.get_from_db_by_email(PersonalDetails(email="taqc296@gmail.com")))
