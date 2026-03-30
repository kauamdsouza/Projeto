import random
import requests

#Sorteando um pokémon
id_pokemon = random.randint(1, 151)
url = f"https://pokeapi.co/api/v2/pokemon/{id_pokemon}"
response = requests.get(url).json()
pokemon_cpu = response["name"].capitalize()

#Jogo
opcoes = ["Pedra", "Papel", "Tesoura"]
cpu_choice = random.choice(opcoes)

print(f"Um {pokemon_cpu} selvagem apareceu!")
escolha = input("Escolha pedra, papel ou tesoura: ").title()
player = escolha

#Lógica de vitória
print(f"{pokemon_cpu} escolheu: {cpu_choice}")

if player == cpu_choice:
    print("Empate!")
elif (player == "Pedra" and cpu_choice =="Tesoura") or \
     (player == "Papel" and cpu_choice =="Pedra") or \
     (player == "Tesoura" and cpu_choice == "Papel"):
    print(f"Incrivel você venceu o {pokemon_cpu}!")
else:
    ("Pokemon massacrou sua familia")
    
