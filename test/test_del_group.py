from model.group import Group


def test_del_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test group", header="test group", footer="test group"))
    app.group.delete_first_group()
