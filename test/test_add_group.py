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
    app.session.login("admin", "secret")
    app.group.create(Group(name="asdfsdf", header="fsgurghur", footer="fiwrwgin"))
    app.session.logout()


def test_create_empty_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
