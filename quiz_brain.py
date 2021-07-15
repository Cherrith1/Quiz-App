import html

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):

        self.question_text = self.question_list[self.question_number].text
        self.question_answer = self.question_list[self.question_number].answer

        q_text = html.unescape(self.question_text)

        self.question_number += 1

        return f"Q.{self.question_number}  {q_text}"

    def check_answer(self, answer):

        if answer == self.question_answer.lower() :
            self.score += 1
            return True
        else:
            return False

    def questions_remaining(self):
        return self.question_number < len(self.question_list)

