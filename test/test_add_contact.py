# -*- coding: utf-8 -*-

def test_test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)