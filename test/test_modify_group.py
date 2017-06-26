from model.group import Group

def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test group", header="test group", footer="test group"))
    app.group.modify_group(Group(name="modified group", header="jhgfds", footer="mnbbvvcsdaf"))
