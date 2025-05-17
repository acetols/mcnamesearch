import requests


def is_username_available(username):

    base_url = "https://api.mojang.com/users/profiles/minecraft/"

    response = requests.get(base_url + username)

    if response.status_code == 404:
        return True
    else:
        return False


with open(
    "/Users/jirodaronville/Desktop/Coding/mc name checker/words.txt", "r"
) as file:

    for word in file:

        word = word.strip()

        if is_username_available(word):
            print(f"{word} is available")
