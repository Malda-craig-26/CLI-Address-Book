from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.connection import Base, Session
from models.contact import Contact

class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    location = Column(String, nullable=False)
    contact_id = Column(Integer, ForeignKey('contacts.id'), nullable=False)

    contact = relationship("Contact", back_populates="addresses")

    def __repr__(self):
        return f"<Address(id={self.id}, location='{self.location}', contact_id={self.contact_id})>"

    @classmethod
    def create(cls, location, contact_id):
        session = Session()
        contact = session.query(Contact).get(contact_id)
        if not contact:
            session.close()
            return None
        address = cls(location=location, contact_id=contact_id)
        session.add(address)
        session.commit()
        session.refresh(address)
        session.close()
        return address

    @classmethod
    def delete(cls, address_id):
        session = Session()
        address = session.query(cls).get(address_id)
        if address:
            session.delete(address)
            session.commit()
            session.close()
            return True
        session.close()
        return False

    @classmethod
    def get_all(cls):
        session = Session()
        addresses = session.query(cls).all()
        session.close()
        return addresses

    @classmethod
    def get_by_contact(cls, contact_id):
        session = Session()
        addresses = session.query(cls).filter(cls.contact_id == contact_id).all()
        session.close()
        return addresses
