from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()

@app.get("/game")
async def game(player1_choice: str, player1_name_input: str, player2_name_input: str):
    import random
    round_number = 1
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    if player1_choice == computer_choice:
        winner = "It's a tie! Both chose {}".format(player1_choice)
        player1_score = 0
        computer_score = 0
    elif (player1_choice == "rock" and computer_choice == "scissors") or (player1_choice == "paper" and computer_choice == "rock") or (player1_choice == "scissors" and computer_choice == "paper"):
        winner = "{} wins! {} chose {}, {} chose {}".format(player1_name_input, player1_name_input, player1_choice, player2_name_input, computer_choice)
        player1_score = 1
        computer_score = 0
    else:
        winner = "{} wins! {} chose {}, {} chose {}".format(player2_name_input, player1_name_input, player1_choice, player2_name_input, computer_choice)
        player1_score = 0
        computer_score = 1
    response = {"winner": winner, "round_number": round_number, "player1_score": player1_score, "computer_score": computer_score, "computer_choice": computer_choice}
    return JSONResponse(content=response, headers={"Access-Control-Allow-Origin": "*"})
