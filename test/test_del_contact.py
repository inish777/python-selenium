def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create()
    app.contact.delete_first()
