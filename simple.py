from fastapi import FastAPI
import math

app = FastAPI()
import random

@app.post("/game")
async def game(player1_choice: str, player1_name_input: str, player2_name_input: str):
    round_number = 0
    player1_score = 0
    player2_score = 0
    computer_score = 0

    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    if player1_choice == computer_choice:
        winner = "It's a tie! Both chose " + player1_choice
    elif player1_choice == "rock" and computer_choice == "scissors":
        winner = player1_name_input + " wins this round."
        player1_score += 1
    elif player1_choice == "rock" and computer_choice == "paper":
        winner = "The computer wins this round."
        computer_score += 1
    elif player1_choice == "paper" and computer_choice == "rock":
        winner = player1_name_input + " wins this round."
        player1_score += 1
    elif player1_choice == "paper" and computer_choice == "scissors":
        winner = "The computer wins this round."
        computer_score += 1
    elif player1_choice == "scissors" and computer_choice == "paper":
        winner = player1_name_input + " wins this round."
        player1_score += 1
    elif player1_choice == "scissors" and computer_choice == "rock":
        winner = "The computer wins this round."
        computer_score += 1

    round_number += 1

    return {"winner": winner, "round_number": round_number, "player1_score": player1_score, "computer_score": computer_score}
