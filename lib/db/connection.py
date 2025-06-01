from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

engine = create_engine('sqlite:///address_book.db', echo=False)
Session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()


def setup_db():
    from models.contact import Contact
    from models.address import Address
    Base.metadata.create_all(engine)

def get_connection():
    return Session()
