from db_tables.country import Country
from db_tables.zone import Zone
from db_tables.address import Address
from db_tables.base import session_factory


def get_country_by_id(id):
    session = session_factory()
    query = session.query(Country.name)
    country = query.filter(Country.country_id == id)
    session.close()
    return country.all()


def get_zone_by_id(id):
    session = session_factory()
    query = session.query(Zone.name)
    zone = query.filter(Zone.zone_id == id)
    session.close()
    return zone.all()


def get_zone_by_name(name):
    session = session_factory()
    zone = session.query(Address.zone_id).filter(Zone.name == name)
    session.close()
    return zone.first()


def get_country_by_name(name):
    session = session_factory()
    query = session.query(Address.zone_id)
    country = query.filter(Zone.name == name)
    session.close()
    return country.first()
