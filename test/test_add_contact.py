# -*- coding: utf-8 -*-

def test_test_add_contact(app):
    app.session.login(user="admin", password="secret")
    app.contact.create()
    app.session.logout()