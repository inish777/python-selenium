# -*- coding: utf-8 -*-
from model.group import Group


def test_create_group(app):
    app.group.create(Group(name="asdfsdf", header="fsgurghur", footer="fiwrwgin"))


def test_create_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

