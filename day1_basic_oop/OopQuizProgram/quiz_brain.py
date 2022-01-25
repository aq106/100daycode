class quiz_flow:
    def __init__(self,Qbank):
        self.question_number = 0
        self.question_list = Qbank
        self.current_ans = ""
        self.score = 0
    def ask_question(self):
        qi=self.question_number
        self.current_ans = input(f"Question {qi+1}: {self.question_list[qi].text}? 'True' or 'False'?\nAnswer: ")
    def validate_answer(self):
        if self.question_list[self.question_number].answer==self.current_ans:
            self.score+=1
            print(f"Your right!  Score: {self.score}/{self.question_number+1}")
        else:
            print(f"Your wrong! Score: {self.score}/{self.question_number+1}")
        self.question_number+=1
    def run_quiz(self):
        for _ in self.question_list:
            self.ask_question()
            self.validate_answer()
        print("Quiz Over!")
        if self.score/(self.question_number+1) > 0.5:
            print("Congrats! You passed with more than 50 percent score!")
        else:
            print("You failed sorry! Less than 50 percent score!")


