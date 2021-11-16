from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q_data in question_data:
    que = Question(q_data['text'], q_data['answer'])
    question_bank.append(que)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've Completed The Quiz!")
print(f"Your Final score was: [{quiz.score}/{len(question_bank)}]")
