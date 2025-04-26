from question_model import Question
from data import question_data
from quiz_brain import Quiz
from ui import UserInterface

question_bank = []

for item in question_data:
    new_question = Question(item["question"], item["correct_answer"])
    question_bank.append(new_question)


quiz = Quiz(question_bank)
interface = UserInterface(quiz)



while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
