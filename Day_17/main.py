from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import subprocess
import platform

def clear():
    command = "cls" if platform.system() == "Windows" else "clear"

    subprocess.run(command, shell=True)

# Contains all the questions as an object stored into an array
question_bank = []

for items in question_data:
    text = items['text']
    answer = items['answer']
    new_question = Question(text = text, answer = answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_list=question_bank)

clear()

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")