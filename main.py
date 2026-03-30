from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import random
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def get_random_pokemon():
    id_pokemon = random.randint(1, 1025)
    url = f"https://pokeapi.co/api/v2/pokemon/{id_pokemon}"
    dados = requests.get(url).json()
    
    return {
        "nome" : dados["name"], # Aqui pega o nome (ex: pikachu)
        "imagem" : dados["sprites"]["front_default"] # Aqui pega a URL da foto
    }

@app.get("/", response_class= HTMLResponse)
async def home(request: Request):
    pokemon = get_random_pokemon()
    return templates.TemplateResponse(
    request=request, 
    name="index.html", 
    context={"pokemon": pokemon}
)

@app.post("/jogar", response_class=HTMLResponse)
async def jogar(request: Request, player_choice: str = Form(...), poke_nome: str = Form(...), poke_img: str = Form(...)):
#Jogo
    opcoes = ["Pedra", "Papel", "Tesoura"]
    cpu_choice = random.choice(opcoes)


# Lógica de vitória
    if player_choice == cpu_choice:
        msg = "Empate!"
    elif (player_choice == "Pedra" and cpu_choice =="Tesoura") or \
        (player_choice == "Papel" and cpu_choice =="Pedra") or \
        (player_choice == "Tesoura" and cpu_choice == "Papel"):
        msg = f"Incrível! Você venceu o {poke_nome}!"
    else:
        msg = f"O {poke_nome} massacrou você!"

    # No return, envie a variável 'msg'
    return templates.TemplateResponse(
    request=request, 
    name="index.html", 
    context={
        "pokemon": {"nome": poke_nome, "imagem": poke_img},
        "resultado": msg,
        "escolha_player": player_choice,
        "cpu_choice": cpu_choice
    }
)
    
