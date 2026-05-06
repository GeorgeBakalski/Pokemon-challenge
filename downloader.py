#downloader.py

import urllib.request


def download_sprites(pokemon_id):
    front_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_id}.png"
    back_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/{pokemon_id}.png"
    
    front_path = f"assets/sprites/{pokemon_id}.png"
    back_path = f"assets/sprites/back/{pokemon_id}.png"
    
    print(f"Downloading ID {pokemon_id}...")
    

    urllib.request.urlretrieve(front_url, front_path)

    urllib.request.urlretrieve(back_url, back_path)

# List of Pokedex IDs for your starters and Rhyhorn
# Bulbasaur(1), Charmander(4), Squirtle(7), Pikachu(25), Rhyhorn(111)
ids_to_download = [1, 4, 7, 25, 111]

for p_id in ids_to_download:
    download_sprites(p_id)

print("Done! Check your assets/sprites folder.")