import turtle as t
import time
import random

# ---------------- SPEED SELECTION ----------------
print("Choose Snake Speed:")
print("1. Fast")
print("2. Normal")
print("3. Slow")
print("4. Very Fast")
print("5. Extreme")

choice = input("Enter number between (1-5): ")

if choice == "1":
    delay = 0.05        # Fast
elif choice == "2":
    delay = 0.10        # Normal
elif choice == "3":
    delay = 0.20        # Slow
elif choice == "4":
    delay = 0.02        # Very Fast
elif choice == "5":
    delay = 0.01        # Extreme
else:
    delay = 0.10        # Default
    print("Invalid choice! Using Normal speed.")
# --------------------------------------------------

score = 0
high_score = 0

# Screen
sc = t.Screen()
sc.title("Snake Game by ChatGPT")
sc.bgcolor("blue")
sc.setup(width=600, height=600)
sc.tracer(0)

# Snake head
head = t.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = t.Turtle()
food.speed(0)
food.shape(random.choice(['square', 'triangle', 'circle']))
food.color(random.choice(['red', 'green', 'black']))
food.penup()
food.goto(0, 100)

# Scoreboard
pen = t.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score : 0  High Score : 0", align="center", font=("candara", 24, "bold"))

# Functions
def quit_game():
    sc.bye()
sc.onkeypress(quit_game, "Escape")

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

# Keyboard Controls
sc.listen()
sc.onkeypress(go_up, "Up")
sc.onkeypress(go_down, "Down")
sc.onkeypress(go_left, "Left")
sc.onkeypress(go_right, "Right")

segments = []

# Main game loop
while True:
    sc.update()

    # Border collision
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        score = 0
        pen.clear()
        pen.write(f"Score : {score}  High Score : {high_score}", align="center", font=("candara", 24, "bold"))

    # Food collision
    if head.distance(food) < 20:
        food.goto(random.randint(-270, 270), random.randint(-270, 270))

        new_segment = t.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write(f"Score : {score}  High Score : {high_score}", align="center", font=("candara", 24, "bold"))

    # Move body
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Body collision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            score = 0
            pen.clear()
            pen.write(f"Score : {score}  High Score : {high_score}", align="center", font=("candara", 24, "bold"))

    time.sleep(delay)

sc.mainloop()
