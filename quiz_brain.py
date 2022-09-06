class QuizBrain:
    """QuizBrain logic"""

    def __init__(self, question_list):
        self._question_number = 0
        self._question_list = question_list
        self._score = 0

    def get_score(self):
        """Return Score"""
        return self._score

    def get_question_number(self):
        """Return Current Question #"""
        return self._question_number

    def still_has_questions(self):
        """Return Bool of True/False if questions remain"""
        return self._question_number + 1 <= len(self._question_list)

    def play(self):
        """Play Game method"""
        while self.still_has_questions():
            current_question = self._question_list[self._question_number]
            self._question_number += 1
            answer = input(f"Q.{self._question_number}: {current_question.get_text()} (true/false): ")
            self.check_answer(answer, current_question.get_answer())
        print("You've completed the quiz")
        print(f"Your score was {self.get_score()}/{self.get_question_number()}")

    def check_answer(self, answer, correct_answer):
        """Check Answer and increment score method"""
        if answer.upper() == correct_answer.upper():
            print("You got it right!")
            self._score += 1
        else:
            print("You got it wrong.")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is {self._score}/{self._question_number}.\n")

