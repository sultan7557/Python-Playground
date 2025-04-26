import tkinter as tk
from quiz_brain import Quiz

THEME_COLOR = "#375362"


class UserInterface:
    def __init__(self, quiz: Quiz):
        self.quiz = quiz
        self.window = tk.Tk()
        self.window.title("Quizzly")
        self.window.config(height = 900, width = 600,padx = 20, pady=20,  bg = THEME_COLOR)


        #CREATING CANVAS OBJECT
        self.canvas = tk.Canvas(width = 300, height = 250, bg = "white", highlightthickness = 0)
        self.text = self.canvas.create_text(150, 70, text = "Question here", font = ("Arial", 20, "italic"), fill = THEME_COLOR, width = 280)
        self.canvas.grid(column = 0, row = 1, columnspan = 2, pady = 30)

        # #CREATING BUTTONS
        self.right_image = tk.PhotoImage(file = "right.png")
        self.right_button = tk.Button(image = self.right_image, highlightthickness = 0, bg= THEME_COLOR, command = self.right_button_click)
        self.right_button.grid(column = 1, row = 3)
        self.left_image = tk.PhotoImage(file = "wrong.png")
        self.wrong_button = tk.Button(image = self.left_image,highlightthickness = 0, bg= THEME_COLOR, command = self.wrong_button_click)
        self.wrong_button.grid(column = 0, row = 3)


        #LABEL SCORE
        self.score = tk.Label(text = "score", bg = THEME_COLOR, fg = "white")
        self.score.grid(column = 1, row = 0)


        
        #call the next question
        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="You've completed the quiz!")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")



    def right_button_click(self):
        is_correct = self.quiz.check_answer("True")
        self.give_feedback(is_correct)

    def wrong_button_click(self):
        is_correct = self.quiz.check_answer("False")
        self.give_feedback(is_correct)

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        self.window.after(1000, self.get_next_question)
    


