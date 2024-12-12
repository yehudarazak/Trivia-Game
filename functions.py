import random
from constants import *
def check_player_answer(player_answer, correct_answer):
    if player_answer == "exit":
        return "exiting..."
    if player_answer == correct_answer:
        return "correct answer"
    if player_answer != correct_answer:
        return "wrong answer"
    
def random_question_and_answer():
    random_question_and_answer = random.choice(list(GAME_QUESTIONS.items()))
            
    question, correct_answer = random_question_and_answer
    return question, correct_answer
