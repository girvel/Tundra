class WorldClocks:
    def __init__(self, iteration_size, systems=None):
        self.iteration_size = iteration_size
        self.__systems = [] if systems is None else systems

    def register_entity(self, entity):
        for system in self.__systems:
            required_part = (entity.get_component(component_type) for component_type in system.requirements)

            if all(c is not None for c in required_part):
                system.__subjects.append(required_part)

    def __call__(self, delta_time):
        for _ in range(delta_time // self.iteration_size):
            for system in self.__systems:
                system.update()
