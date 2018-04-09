"""
TODO
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

WAMP_SERVER_DB = 'mysql://root@localhost/opencart'

ENGINE = create_engine(WAMP_SERVER_DB)
SESSION = sessionmaker(bind=ENGINE)

BASE = declarative_base()


def session_factory():
    """
    TODO
    """
    BASE.metadata.create_all(ENGINE)
    return SESSION()
