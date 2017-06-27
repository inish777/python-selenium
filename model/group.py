class Group(object):
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __eq__(self, other):
        return self.name == other.name and self.header == other.header and self.id == other.id
