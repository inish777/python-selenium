def test_del_group(app):
    app.session.login(user="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()