def test_modify_contact(app):
    app.session.login(user="admin", password="secret")
    app.contact.modify_first_contact()
    app.session.logout()