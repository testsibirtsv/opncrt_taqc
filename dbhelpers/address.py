from db.country import Country
from db.zone import Zone
from db.address import Address
from db.base import session_factory
from models.addressbook import AddressBook


class DbAddress:

    @staticmethod
    def get_address_by_id(user):
        session = session_factory()
        query = session.query(Address)
        address = query.filter(Address.address_id == user.address_id).first()
        zone = session.query(Zone.name).filter(Zone.zone_id == address.zone_id).first()
        country = session.query(Country.name).filter(Country.country_id == address.country_id).first()
        session.close()
        return AddressBook(address_id=address.address_id,
                           first_name=address.firstname,
                           last_name=address.lastname,
                           company=address.company,
                           address_1=address.address_1,
                           address_2=address.address_2,
                           city=address.city,
                           country=country[0],
                           region_state=zone[0])


# print(DbAddress.get_address_by_id(AddressBook(address_id=67)))
