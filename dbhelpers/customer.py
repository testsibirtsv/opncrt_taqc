"""
Contains DbCustomer class for interacting
with a table oc_address from opencart database.
"""
from db.customer import Customer
from db.base import session_factory
from models.personaldetails import PersonalDetails


# pylint: disable=too-few-public-methods
class DbCustomer:
    """
    Contains methods for obtaining information from oc_customer table.
    """

    @staticmethod
    def get_from_db_by_email(user: PersonalDetails) -> PersonalDetails:
        """
        Receives email data from the PersonalDetails object,
        on their basis searches for records in the oc_customer table
        and returns them as an PersonalDetails object.

        :param user: object PersonalDetails with user's email.
        :return: object PersonalDetails with data from oc_customer table.
        """
        session = session_factory()
        query = session.query(Customer)
        customer = query.filter(Customer.email == user.email).first()
        session.close()
        return PersonalDetails(first_name=customer.firstname,
                               last_name=customer.lastname,
                               email=customer.email,
                               telephone=customer.telephone)
