class Product:

    def __init__(self):
        self.entries = {}

    def __init__(self, url, title, name):
        self.url = url
        self.title = title
        self.name = name

    def add(self, url, title, name):
        self.url = url
        self.title = title
        self.name = name


    def __eq__(self,other):
        return self.url, self.title, self.name == other.url, other.title, other.name


    def __hash__(self):
        return hash((self.url, self.title, self.name))


    def __repr__(self):
        return "%s %s %s" % (self.url, self.title, self.name)
