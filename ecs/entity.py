class Entity:
    def __init__(self, *components):
        self.__components = components

    def get_component(self, type_):
        return next(c for c in self.__components if isinstance(c, type_))
