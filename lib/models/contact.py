from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.connection import Base, Session

class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    addresses = relationship("Address", back_populates="contact", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Contact(id={self.id}, name='{self.name}', email='{self.email}')>"

    @classmethod
    def create(cls, name, email):
        session = Session()
        contact = cls(name=name, email=email)
        session.add(contact)
        session.commit()
        session.refresh(contact)
        session.close()
        return contact

    @classmethod
    def delete(cls, contact_id):
        session = Session()
        contact = session.query(cls).get(contact_id)
        if contact:
            session.delete(contact)
            session.commit()
            session.close()
            return True
        session.close()
        return False

    @classmethod
    def get_all(cls):
        session = Session()
        contacts = session.query(cls).all()
        session.close()
        return contacts

    @classmethod
    def find_by_id(cls, contact_id):
        session = Session()
        contact = session.query(cls).get(contact_id)
        session.close()
        return contact

    @classmethod
    def find_by_name(cls, name):
        session = Session()
        contact = session.query(cls).filter(cls.name.ilike(f"%{name}%")).first()
        session.close()
        return contact
