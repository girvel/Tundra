class Monologue:
    def __init__(self, name="Monologue"):
        self.name = name
        self.replicas = []  # [ Replica* ]
        self.choices = []  # [ Choice* ]

    def __repr__(self):
        return f'<Monologue {self.name}>'
