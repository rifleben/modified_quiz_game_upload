class Question:
    """QUESTION FOR GAME"""
    def __init__(self, text, answer):
        self._text = text
        self._answer = answer

    def get_text(self):
        """Return Question Text"""
        return self._text

    def get_answer(self):
        """Return Question Answer string (True/False)"""
        return self._answer
