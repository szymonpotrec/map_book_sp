
def read(users:list[dict])->None:
    for user in users[1:]:
        print(f'Twoj znajomy {user["name"]} opublikowal: {user["posts"]}')

def creates_user(users: list[dict])->None:
    name: str = input("Podaj imie uzytkownika: ")
    surname: str = input("Podaj nazwisko uzytkownika: ")
    posts: int = int(input("Podaj liczbe postow: "))
    user: dict = {"name": name, "surname": surname, "posts": posts}
    users.append(user)

