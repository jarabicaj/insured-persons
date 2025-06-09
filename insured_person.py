class InsuredPerson:
    all_insured = []

    def __init__(self, name, surname, phone, age):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.age = age

    def __str__(self):
        return f"{self.name:<10} {self.surname:<10} {self.phone:<12} {self.age}"

    @classmethod
    def add_person(cls, person):
        cls.all_insured.append(person)

    @classmethod
    def get_one(cls, person):
        for item in cls.all_insured:
            if (item.name == person[0]) and (item.surname == person[1]):
                return item
        return None

    @classmethod
    def get_all(cls):
        return cls.all_insured