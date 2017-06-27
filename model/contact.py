class Contact(object):
    def __init__(self, name=None, middlename=None, lastname=None, nickname=None, id=None):
        self.name = name
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = ''
        self.company = ''
        self.address = ''
        self.home = ''
        self.fax = ''
        self.mobile = ''
        self.work = ''
        self.email = ''
        self.email2 = ''
        self.email3 = ''
        self.homepage = ''
        self.born_year = ''
        self.anniversiary_year = ''
        self.address2 = ''
        self.phone2 = ''
        self.notes = ''
        self.id = id

    def __eq__(self, other):
        return self.name == other.name and self.lastname == other.lastname and self.id == other.id
