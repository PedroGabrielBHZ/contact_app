import json


def load_data():
    """Loads data from the JSON file."""
    with open("db.json", "r") as f:
        return json.load(f)


def save_data(data):
    """Saves data to the JSON file."""
    with open("db.json", "w") as f:
        json.dump(data, f, indent=4)


def get_contacts():
    """Returns all contacts."""
    data = load_data()
    return data["contacts"]


def get_contact(contact_id):
    """Returns a specific contact by ID."""
    data = load_data()
    for contact in data["contacts"]:
        if contact["id"] == contact_id:
            return contact
    return None


def create_contact(name, phone, address):
    """Creates a new contact."""
    data = load_data()
    new_id = max(contact["id"] for contact in data["contacts"]) + 1
    new_contact = {"id": new_id, "name": name, "phone": phone, "address": address}
    data["contacts"].append(new_contact)
    save_data(data)


def update_contact(contact_id, name, phone, address):
    """Updates a contact."""
    data = load_data()
    for contact in data["contacts"]:
        if contact["id"] == contact_id:
            contact["name"] = name
            contact["phone"] = phone
            contact["address"] = address
            save_data(data)
            return
    raise ValueError("Contact not found")


def delete_contact(contact_id):
    """Deletes a contact."""
    data = load_data()
    for i, contact in enumerate(data["contacts"]):
        if contact["id"] == contact_id:
            del data["contacts"][i]
            save_data(data)
            return
    raise ValueError("Contact not found")
