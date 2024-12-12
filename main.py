import random
from functions import *
from constants import *

print("welcome to trivia master!!!")

ask_if_playing = input("do you want to play? (yes/no)").strip().lower()
if ask_if_playing == "yes":
    GAME_ON = True

def main_game():
    global USER_SCORE, GAME_ON
    while GAME_ON:
        
        while len(GAME_QUESTIONS) > 0:
            random_question_and_answer = random.choice(list(GAME_QUESTIONS.items()))
            
            question, correct_answer = random_question_and_answer
            user_answer = input(f"""{question} (type "exit" to exit the game)""").lower()

            if user_answer == "exit":
                print("exiting...")
                GAME_ON = False
                break  

            result = check_player_answer(user_answer, correct_answer)
            print(result)

            if result == "correct answer":
                USER_SCORE += 1

            # don't repeat questions
            del GAME_QUESTIONS[question]

        if len(GAME_QUESTIONS) == 0:
            print("no more questions left!")
            break
            
    print(f"you got {USER_SCORE} answers correct")
    # play_again = input("do you want to play again? (yes/no)\n").strip().lower()
    # if play_again != "yes":
    #     print("thanks for playing!")
    #     GAME_ON = False
    # else:
    #     GAME_ON = True


if __name__ == "__main__":
    main_game()