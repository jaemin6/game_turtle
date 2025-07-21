import turtle
import random

# 터틀 화면 설정
s = turtle.Screen()
s.title("거북이 경주 게임")

# 플레이어 생성 함수
def create_player(color, y):
    player = turtle.Turtle()
    player.shape("turtle")
    player.color(color)
    player.penup()
    player.goto(-200, y)
    return player

# 플레이어 3명 생성
player_one = create_player("sky blue", 100)
player_two = create_player("red", 0)
player_three = create_player("green", -100)
players = [player_one, player_two, player_three]

# 초록 블럭 좌표
green_blocks = [
    (-100, 90),
    (0, 10),
    (100, -110)
]

# 초록 블럭 그리기
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

# 도착선 그리기
finish_line = turtle.Turtle()
finish_line.hideturtle()
finish_line.penup()
finish_line.goto(300, 150)
finish_line.right(90)
finish_line.pendown()
finish_line.forward(300)

# 메시지 출력용 터틀
msg_writer = turtle.Turtle()
msg_writer.hideturtle()
msg_writer.penup()

# 주사위
die = [1, 2, 3, 4, 5, 6]

# 중복 점프 방지를 위한 기록
jumped_set = set()

# 블럭 점프 확인 함수
def check_and_jump(player, blocks, idx):
    for bx, by in blocks:
        if abs(player.ycor() - by) < 20 and abs(player.xcor() - bx) < 15:
            if (idx, bx, by) not in jumped_set:
                print(f"{player.color()[0]} turtle hits green block! Jumps forward!")
                player.forward(40)
                jumped_set.add((idx, bx, by))

# 게임 시작
game_over = False

for turn in range(20):
    if game_over:
        break

    for idx, player in enumerate(players):
        if player.xcor() >= 300:
            color = player.color()[0].capitalize()
            print(f"{color} Player Wins!")
            msg_writer.goto(-80, 200)
            msg_writer.write(f"{color} Player Wins!", font=("Arial", 24, "bold"))
            game_over = True
            break

        input(f"Press Enter to roll the die for {player.color()[0]} turtle.")
        die_outcome = random.choice(die)
        print("🎲 주사위 결과:", die_outcome)
        steps = 20 * die_outcome
        print("👉 이동 거리:", steps)

        player.forward(steps)
        check_and_jump(player, green_blocks, idx)

# 화면 닫기 방지
turtle.done()
