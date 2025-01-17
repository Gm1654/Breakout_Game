from turtle import Turtle
import csv



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(240, 240)
        self.color("white")
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(240, 240)
        self.write(f"{self.score}", font=("Arial", 24, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def end_game(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over! Score: {self.score}", align="center", font=("Arial", 24, "bold"))
        self.save_score_to_csv()
    
    def save_score_to_csv(self):
        with open('scores.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.score])
        print("Score saved to scores.csv")    
 

