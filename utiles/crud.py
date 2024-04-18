
def read(users:list[dict])->None:
    for user in users[1:]:
        print(f'Twoj znajomy {user["name"]} opublikowal: {user["posts"]}')

