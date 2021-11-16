class QuizBrain:

    def __init__(self, que_list):
        self.question_number = 0
        self.question_list = que_list
        self.score = 0

    def still_has_question(self):
        return self.question_number != len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} [ True / False ]\n>> ").lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_ans, actual_answer):
        if user_ans == actual_answer.lower():
            self.score += 1
            print("You Got It Right!")
        else:
            print("That's Wrong!")
        print(f"The Correct Answer is [{actual_answer}]")
        print(f"Your Current score is [{self.score}/{self.question_number}]\n")
