def check_player_answer(player_answer, correct_answer):
    if player_answer == "exit":
        return "exiting..."
    if player_answer == correct_answer:
        return "correct answer"
    if player_answer != correct_answer:
        return "wrong answer"
    

