from fastapi import FastAPI
from models import Contact, CreateContact

app = FastAPI()

# Simulation of DB
db = []
current_id = 0

@app.get("/")
# Base endpoint (GET)
def read_root():
    return "{'Bonjour': 'tout le monde', 'Status': 'API Running'}"

# Add a contact (POST)
@app.post("/contacts/", response_model=Contact)
def create_contact(contact_data: CreateContact):
    global current_id
    current_id += 1

    # Contact object creation
    new_contact = Contact(
        id=current_id,
        firstname=contact_data.firstname,
        lastname=contact_data.lastname,
        phone=contact_data.phone,
        email=contact_data.email,
    )

    db.append(new_contact)
    return new_contact

