# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_group(app):
    app.open_homepage("http://localhost:4000/")
    app.login("admin", "secret")
    app.create_new_group(Group(name="asdfsdf", header="fsgurghur", footer="fiwrwgin"))
    app.logout()

def test_create_empty_group(app):
    app.open_homepage("http://localhost:4000/")
    app.login("admin", "secret")
    app.create_new_group(Group(name="", header="", footer=""))
    app.logout()