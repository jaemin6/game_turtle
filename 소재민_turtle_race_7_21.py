# test

import turtle
import random

s = turtle.getscreen()

# 플레이어1
player_one = turtle.Turtle()
player_one.color("sky blue")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200, 100)

# 플레이어2
player_two = player_one.clone()
player_two.color("red")
player_two.penup()
player_two.goto(-200, 0)

# 플레이어3 추가
player_three = player_one.clone()
player_three.color("green")
player_three.penup()
player_three.goto(-200, -100)


# 초록색 블럭 위치 설정 (x, y)
green_blocks = [
    (-100, 90),
    (0, 10),
    (100, -110)
]

# 블럭 그리기
block_drawer = turtle.Turtle()
block_drawer.hideturtle()
block_drawer.penup()

for x, y in green_blocks:
    block_drawer.goto(x, y)
    block_drawer.pendown()
    block_drawer.color("green")
    block_drawer.begin_fill()
    for _ in range(4):
        block_drawer.forward(20)
        block_drawer.left(90)
    block_drawer.end_fill()
    block_drawer.penup()

die = [1, 2, 3, 4, 5, 6]

def check_and_jump(player, blocks, idx):
   # 플레이어가 초록색 블럭 위치에 도착하면 앞으로 40칸 점프
    for bx, by in blocks:
        if abs(player.ycor() - by) < 20 and abs(player.xcor() - bx) < 15:
            print(f"{player.color()[0]} turtle hits green block! Jumps forward!")
            player.forward(40)

players = [player_one, player_two, player_three]

for i in range(20):
    for idx, player in enumerate(players):
        if player.xcor() >= 300:
            print(f"{player.color()[0].capitalize()} Player Wins!")
            exit()

        input(f"Press 'Enter' to roll the die for {player.color()[0]} turtle.")
        die_outcome = random.choice(die)
        print("The result of the die roll is:", die_outcome)
        steps = 20 * die_outcome
        print("The number of steps will be:", steps)
        player.forward(steps)

        check_and_jump(player, green_blocks, idx)

