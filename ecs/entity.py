class Entity:
    def __init__(self, *components):
        self.__components = components

    def get_component(self, type_):
        return next((c for c in self.__components if isinstance(c, type_)), None)

    def has_component(self, type_):
        return self.get_component(type_) is not None

    def __getattr__(self, item):
        for c in self.__components:
            name = c.__class__.__name__
            if name[0].lower() + name[1:] == item:
                return c
        raise AttributeError
