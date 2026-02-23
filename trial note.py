# import threading
# import time
#
# def walk_dog():
#     time.sleep(8)
#     print("You finish walking the dog")
#
# def take_out_trash():
#     time.sleep(2)
#     print("You take out the trash")
#
# def get_mail():
#     time.sleep(4)
#     print("You get the mail")
#
# # Correct threading calls
# chore1 = threading.Thread(target=walk_dog)
# chore2 = threading.Thread(target=take_out_trash)
# chore3 = threading.Thread(target=get_mail)
#
# chore1.start()
# chore2.start()
# chore3.start()
#
# print("All chores are complete")

# Now getting to the real works
# How to connect  to an API using python

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json() # convert to a python dictionary
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

pokemon_name = "typhlosion"
pokemon_info = get_pokemon_info(pokemon_name)


if pokemon_info:
    print(f"Name: {pokemon_info['name'].capitalize()}")
    print(f"Id: {pokemon_info['id']}")
    print(f"Height:{pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")





