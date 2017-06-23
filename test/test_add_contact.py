# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test_add_contact(app):
    app.session.login(user="admin", password="secret")
    app.contact.open_create_contact_page()
    app.contact.create()
    app.session.logout()