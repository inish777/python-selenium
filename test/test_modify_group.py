from model.group import Group


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test group", header="test group", footer="test group"))
    old_groups = app.group.get_group_list()
    app.group.modify_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    assert old_groups[0] != new_groups[0]