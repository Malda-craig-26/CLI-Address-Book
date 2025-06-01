from models.contact import Contact
from models.address import Address
from models.phone import PhoneNumber
from db.connection import session, Base, engine


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


john = Contact(name="John Spikes", email="johnspikes28@gmail.com")
jane = Contact(name="Jane Smith", email="janesmith34@gmail.com")
kimberly = Contact(name="Kimberly Johnson", email="kimberlyjohnson228@gmail.com")
ryan = Contact(name="Ryan Lee", email="ryanlee27@gmail.com")         

home_address = Address(street="123 Main St", city="New York", state="NY", contact=john)
home_address = Address(street="456 Broadway", city="New York", state="NY", contact=jane)
home_address = Address(street="789 Elm St", city="Los Angeles", state="CA", contact=kimberly)
home_address = Address(street="321 Oak St", city="Los Angeles", state="CA", contact=ryan)

phone1 = PhoneNumber(number="123-456-7890", type="Home", contact=john)
phone2 = PhoneNumber(number="987-654-3210", type="Work", contact=jane)
phone3 = PhoneNumber(number="557-437-8333", type="Mobile", contact=kimberly)
phone4 = PhoneNumber(number="444-657-4415", type="Home", contact=ryan)

# Add to session
session.add_all([john, jane,kimberly,ryan, home_address, phone1, phone2,phone3, phone4])
session.commit()

print("Seed data created successfully!")
