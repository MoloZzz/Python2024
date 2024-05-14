class Discipline:
    def __init__(self, id, name, teacher, credits, hours):
        self.id = id
        self.name = name
        self.teacher = teacher
        self.credits = credits
        self.hours = hours
    def __str__(self):
        return f"Дисципліна: {self.name}\nID: {self.id}\nВикладач: {self.teacher}\nКредити: {self.credits}\nГодин: {self.hours}"