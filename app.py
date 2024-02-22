from flask import Flask, redirect, render_template, request

import db_manager

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("layout.html")


@app.route("/contacts/<id>")
def contact(id):
    contact = db_manager.get_contact(int(id))
    print(contact)
    return render_template("contact.html", contact=contact)


@app.route("/contacts/")
def contacts():
    contacts = db_manager.get_contacts()
    return render_template("contacts.html", contacts=contacts)


@app.route("/contacts/<id>", methods=["DELETE"])
def delete_contact(id):
    db_manager.delete_contact(int(id))
    contacts = db_manager.get_contacts()
    return render_template("contacts.html", contacts=contacts)


@app.route("/contacts/new", methods=["POST"])
def contacts_new():
    name = request.form["name"]
    phone = request.form["phone"]
    address = request.form["address"]

    db_manager.create_contact(name, phone, address)
    return redirect("/contacts")


@app.route("/contacts/new", methods=["GET"])
def contacts_new_get():
    return render_template("new_contact.html")
