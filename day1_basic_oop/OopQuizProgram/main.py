import requests
from data import question_data
from quiz_brain import quiz_flow
from question_model import question

question_bank = []

#Local Questions...AND Local quiz...
# for q in question_data:
#     question_bank.append(question(q["text"],q["answer"]))

#Api questions...POWER OF MUDULARITY...PLUG AND PLAY...SCALABILITY..CHANGES...
api_questions = requests.get("https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean")
for q in api_questions.json()["results"]:
    question_bank.append(question(q["question"],q["correct_answer"]))

my_quiz = quiz_flow(question_bank)
my_quiz.run_quiz()
