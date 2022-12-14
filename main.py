"""
Modification of QuizBrain project from 100 days of Python.
Used private data members and wrote additional "get()" methods,
as best practice.
"""


from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(question["text"], question["answer"]) for question in question_data]

if __name__ == '__main__':
    quiz = QuizBrain(question_bank)
    quiz.play()
