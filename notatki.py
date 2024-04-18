users: list[dict] = [
    {"name": "Szymon", "surname": "Potrec", "posts": 10},
    {"name": "Maciej", "surname": "Przybytek", "posts": 45},
    {"name": "Bartosz", "surname": "Pietrasik", "posts": 60},
    {"name": "Tymoteusz", "surname": "Miszczak", "posts": 21},
    {"name": "Mateusz", "surname": "Matysiak", "posts": 33},
]

    def read(users:list[dict])->None:
        for user in users[1:]:
            print(f'Twoj znajomy {user["name"]} opublikowal: {user["posts"]}')

read(users)