def test_delete_first_contact(app):
    app.open_homepage()
    app.contact.delete_first()
