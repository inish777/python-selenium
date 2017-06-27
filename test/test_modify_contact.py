def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create()
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert old_contacts[0] != new_contacts[0]
