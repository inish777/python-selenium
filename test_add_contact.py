# -*- coding: utf-8 -*-
import time, unittest
import pytest

from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test_add_contact(app):
    app.open_homepage()
    app.login(user="admin", password="secret")
    app.open_create_contact_page()

    contact = app.build_contact_object()

    app.create_contact(contact)