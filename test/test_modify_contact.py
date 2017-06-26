def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create()
    app.contact.modify_first_contact()
