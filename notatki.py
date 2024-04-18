users: list[dict] = [
    {"name": "Szymon", "surname": "Potrec", "posts": 10},
    {"name": "Maciej", "surname": "Przybytek", "posts": 45},
    {"name": "Bartosz", "surname": "Pietrasik", "posts": 60},
    {"name": "Tymoteusz", "surname": "Miszczak", "posts": 21},
    {"name": "Mateusz", "surname": "Matysiak", "posts": 33},
]


def creates_user(users: list[dict])->None:
    name: str = input("Podaj imie uzytkownika: ")
    surname: str = input("Podaj nazwisko uzytkownika: ")
    posts: int = int(input("Podaj liczbe postow: "))
    user: dict = {"name": name, "surname": surname, "posts": posts}
    users.append(user)

creates_user(users)

print(users)