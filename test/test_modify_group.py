from model.group import Group

def test_modify_group(app):
    app.session.login(user="admin", password="secret")
    app.group.modify_group(Group(name="modified group", header="jhgfds", footer="mnbbvvcsdaf"))
    app.session.logout()