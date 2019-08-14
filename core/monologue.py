class Monologue:
    def __init__(self, name="Monologue"):
        self.name = name
        self.replicas = []  # [ Replica* ]
        self.choices = []  # [ (variant, next monologue)* ]

    def __str__(self):
        return f'<Monologue {self.name}>'
