class Place:
    def __init__(self, name, content, description=""):
        self.name = name
        self.content = content
        self.description = description
        self.explored = description == ""
        self.connected_places = set()

    def connect(self, place):
        self.connected_places.add(place)
        place.connected_places.add(self)
