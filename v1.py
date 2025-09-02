from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import random
from PIL import Image, ImageTk
import os
import json

bg = "black"
fg = "#C68642"
font = ("",17,"")
choice = ["0","1","2","3","4","5","6"]
int_choice = [1,2,3,4,5,6]
spl_choice = ["bat","ball"]
user_points = 0
computer_points = 0
game_phase = "first innings"

def get_path(*subfolders):
    return os.path.join(BASE_DIR, *subfolders)

BASE_DIR = os.path.dirname(__file__)
logo_path = get_path("logo.ico")

start = Tk()
start.config(bg = bg)
start.title("Odd Or Even")
start.resizable(False, False)
width = start.winfo_screenwidth()
height = start.winfo_screenheight()
start.geometry(f"{width}x{height}+0+0")
start.iconbitmap(logo_path)
label_title = Label(start, text = "Odd Or Even Game", font = ("Arial",30,""), bg = bg, fg = fg)
label_title.place(relx = 0.5, rely=0.04, anchor="center")

def info():
    showinfo(title = "Understand the Game", message = "First choose Odd or Even\n\nThen choose any number\n\nComputer also chooses a number\n\n"
    "If the sum of yours and computer's number is even, and you choose even, then you get chance to choose Bat or Ball\n\n"
    "If the sum of yours and computer's choice is odd, and you choose odd, then you get chance to choose Bat or Ball\n\n"
    "If you choose odd and sum is even, and if you choose even and sum is odd, then computer will choose Bat or Ball\n\n"
    "If you do Batting first, then you set a target to the computer and if you do balling first computer will give you a target\n\n"
    "You must pass the target or shouldn't leave the computer to finish the target to win the game\n\n"
    "Batters get out when both the ballers and batters put the same number")

button_game_info = Button(start, text = "?", font = font, fg = fg, bg = bg, command = info)
button_game_info.place(relx=0.96, rely=0.02, height = 40, width = 35)

def choose_oddoreven():
    global button_even, button_odd

    label_choose = Label(start, text = "Choose", font = font, bg = bg, fg = fg)
    label_choose.place(x=1, y=80)

    button_odd = Button(start, text = "Odd", font = font, bg = bg, fg = fg, command = lambda : info_choose_oddoreven("Odd"))
    button_odd.place(x=100,y=80, height = 35, width=50)

    label_or = Label(start, text = "or", font = font, fg = fg, bg = bg)
    label_or.place(x=155,y=80)

    button_even = Button(start, text = "Even", font = font, fg = fg, bg = bg, command = lambda : info_choose_oddoreven("Even"))
    button_even.place(x=187,y=80,height = 35, width = 58)

def info_choose_oddoreven(value):
    global user_choose_oddoreven, button_even, button_odd
    user_choose_oddoreven = value
    button_odd.config(state = 'disabled')
    button_even.config(state = 'disabled')

    if user_choose_oddoreven == "Odd":
        computer_choose_oddoreven = "Even"
    elif user_choose_oddoreven == "Even":
        computer_choose_oddoreven = "Odd"

    label_choose_oddoreven = Label(start, text = f"You choose {user_choose_oddoreven}. Computer choose {computer_choose_oddoreven}", font = font, bg = bg, fg = fg)
    label_choose_oddoreven.place(x=1100,y=80)
    choose_number()

def choose_number():
    global choose_zero, choose_one, choose_two, choose_three, choose_four, choose_five, choose_six

    choose_a_number = Label(start, text = "Choose a number :-", font = font, fg = fg, bg = bg)
    choose_a_number.place(x=1,y=130)

    choose_zero = Button(start, text = "0", font = font, fg = fg, bg = bg, command = lambda : choose_number_function("0"))
    choose_zero.place(x=215, y=130, height = "35", width = "30")

    choose_one = Button(start, text = "1", font = font, fg = fg, bg = bg, command = lambda : choose_number_function("1"))
    choose_one.place(x=250, y=130, height = "35", width = "30")

    choose_two = Button(start, text = "2", font = font, fg = fg, bg = bg, command = lambda : choose_number_function("2"))
    choose_two.place(x=285, y=130, height = "35", width = "30")

    choose_three = Button(start, text = "3", font = font, fg = fg, bg = bg, command = lambda : choose_number_function("3"))
    choose_three.place(x=320, y=130, height = "35", width = "30")

    choose_four = Button(start, text = "4", font = font, fg = fg, bg = bg, command = lambda : choose_number_function("4"))
    choose_four.place(x=355, y=130, height = "35", width = "30")

    choose_five = Button(start, text = "5", font = font, fg = fg, bg = bg, command = lambda : choose_number_function("5"))
    choose_five.place(x=390, y=130, height = "35", width = "30")

    choose_six = Button(start, text = "6", font = font, fg = fg, bg = bg, command = lambda : choose_number_function("6"))
    choose_six.place(x=425, y=130, height = "35", width = "30")


def choose_number_function(value):
    global user_choose_oddoreven, choose_zero, choose_one, choose_two, choose_three, choose_four, choose_five, choose_six, user_choose_batorball, computer_splchoice, user_choose_oddoreven
    computer_choose_initial_number = int(random.choice(choice))
    user_choose_intial_number = int(value)

    label_choose_initial_number_info = Label(start, text = f"You choose {user_choose_intial_number} and computer choose {computer_choose_initial_number}", fg = fg, bg = bg, font = font)
    label_choose_initial_number_info.place(x=1100,y=130)

    label_down = Label(start, text = f"{user_choose_intial_number}  +  {computer_choose_initial_number}  =  {'Even' if (user_choose_intial_number + computer_choose_initial_number) % 2 == 0 else 'Odd'}", fg = fg, bg = bg, font = font)
    label_down.place(x=1100,y=175)

    label_choose_batorball_info = Label(start, text = "", font = font, bg = bg, fg = fg)
    label_choose_batorball_info.place(x=1100,y=220)

    choose_zero.config(state = 'disabled'); choose_one.config(state = 'disabled'); choose_two.config(state = 'disabled'); choose_three.config(state = 'disabled')
    choose_four.config(state = 'disabled'); choose_five.config(state = 'disabled'); choose_six.config(state = 'disabled')

    if user_choose_oddoreven == "Even":
        if (computer_choose_initial_number + user_choose_intial_number) % 2 == 0:
            choose_bat_or_ball()

        elif (computer_choose_initial_number + user_choose_intial_number) % 2 != 0:
            computer_splchoice = random.choice(spl_choice)
            if computer_splchoice == "bat":
                user_choose_batorball = "ball"
                label_choose_batorball_info.config(text = "Computer choose Bat. So you will do Ball")
                started()

            elif computer_splchoice == "ball":
                user_choose_batorball = "bat"
                label_choose_batorball_info.config(text = "Computer choose Ball. So you will do Bat")
                started()

    elif user_choose_oddoreven == "Odd":
        if (computer_choose_initial_number + user_choose_intial_number) % 2 == 0:
            computer_splchoice = random.choice(spl_choice)
            if computer_splchoice == "bat":
                user_choose_batorball = "ball"
                label_choose_batorball_info.config(text = "Computer choose Bat. So you will do Ball")
                started()

            elif computer_splchoice == "ball":
                user_choose_batorball = "bat"
                label_choose_batorball_info.config(text = "Computer choose Ball. So you will do Bat")
                started()

        elif (computer_choose_initial_number + user_choose_intial_number) % 2 != 0:
            choose_bat_or_ball()

def choose_bat_or_ball():
    global button_choose_bat, button_choose_ball
    label_wantto = Label(start, text = "Want to", font = font, fg = fg, bg = bg)
    label_wantto.place(x=1,y=220)

    button_choose_bat = Button(start, text = "Bat", font = font, fg = fg, bg = bg, command = lambda : choose_batorball_function("bat"))
    button_choose_bat.place(x=95,y=220, height = 35, width = 50)

    label_or2 = Label(start, text = "or", font = font, fg = fg, bg = bg)
    label_or2.place(x=150,y=220)

    button_choose_ball = Button(start, text = "Ball", font = font, fg = fg, bg = bg, command = lambda : choose_batorball_function("ball"))
    button_choose_ball.place(x=185,y=220, height = 35, width = 50)

def choose_batorball_function(value):
    global button_choose_bat, button_choose_ball, computer_splchoice, user_choose_batorball

    user_choose_batorball = value
    button_choose_bat.config(state='disabled')
    button_choose_ball.config(state='disabled')

    if user_choose_batorball == "bat":
        computer_splchoice = "ball"
        label_choose_batorball_info = Label(start, text = "You choose Bat. So Computer will do Ball", font = font, bg = bg, fg = fg)
        label_choose_batorball_info.place(x=1100,y=220)
        started()

    elif user_choose_batorball == "ball":
        computer_splchoice = "bat"
        label_choose_batorball_info = Label(start, text = "You choose Ball. So Computer will do Bat", font = font, bg = bg, fg = fg)
        label_choose_batorball_info.place(x=1100,y=220)
        started()

def started():
    global computer_splchoice, user_choose_batorball, label_user, label_computer, button_one, button_two, button_three, button_four, button_five, button_six, button_zero

    label_user = Label(start, text = f"User({user_choose_batorball})".upper(), font = font, fg = fg, bg = bg)
    label_user.place(x=1, y=340)

    label_computer = Label(start, text = f"Computer({computer_splchoice})".upper(), font = font, fg = fg, bg = bg)
    label_computer.place(x=1200,y=340)

    button_one = Button(start, text = "1", font = font, fg = fg, bg = bg, command = lambda : (photo_game("1"), setup_game("1")))
    button_one.place(x=80, y=390, height = 35, width = 30)

    button_two = Button(start, text = "2", font = font, fg = fg, bg = bg, command = lambda : (photo_game("2"), setup_game("2")))
    button_two.place(x=120, y=390, height = 35, width = 30)

    button_three = Button(start, text = "3", font = font, fg = fg, bg = bg, command = lambda : (photo_game("3"), setup_game("3")))
    button_three.place(x=160, y=390, height = 35, width = 30)

    button_four = Button(start, text = "4", font = font, fg = fg, bg = bg, command = lambda : (photo_game("4"), setup_game("4")))
    button_four.place(x=80, y=435, height = 35, width = 30)

    button_five = Button(start, text = "5", font = font, fg = fg, bg = bg, command = lambda : (photo_game("5"), setup_game("5")))
    button_five.place(x=120, y=435, height = 35, width = 30)

    button_six = Button(start, text = "6", font = font, fg = fg, bg = bg, command = lambda : (photo_game("6"), setup_game("6")))
    button_six.place(x=160, y=435, height = 35, width = 30)

    button_zero = Button(start, text = "0", font = font, fg = fg, bg = bg, command = lambda : (photo_game("0"), setup_game("0")))
    button_zero.place(x=120, y=480, height = 35, width = 30)

def photo_game(value):
    global computer_choice
    user_choice = value
    computer_choice = random.choice(choice)

    img_human_path = get_path("images", "human image", f"human_{user_choice}.jpg")
    img_human = Image.open(img_human_path)
    img_human = img_human.resize((300, 300), Image.LANCZOS)
    photo_human = ImageTk.PhotoImage(img_human)
    start.human_photo = photo_human
    label_human_photo = Label(start,image = photo_human)
    label_human_photo.place(x=300,y=340, height = 300, width = 300)

    img_robot_path = get_path("images", "robot image", f"robot_{computer_choice}.png")
    img_robot = Image.open(img_robot_path)
    img_robot = img_robot.resize((300, 300), Image.LANCZOS)
    photo_robot = ImageTk.PhotoImage(img_robot)
    start.robot_photo = photo_robot
    label_robot_photo = Label(start, image = photo_robot)
    label_robot_photo.place(x=850,y=340, height = 300, width = 300)

def setup_game(value):
    global user_choose_batorball, computer_splchoice, user_points, computer_points, computer_choice, user_choice, label_user, label_computer, game_phase
    user_choice = value
    label_user_choice = Label(start, text = f"You choose :- {user_choice}", font = font, fg = fg, bg = bg)
    label_user_choice.place(x=1,y=535)
    label_computer_choice = Label(start, text = f"Computer choose :- {computer_choice}", font = font, fg = fg, bg = bg)
    label_computer_choice.place(x=1200,y=535)

    if game_phase == "first innings":
        if user_choose_batorball == "bat":
            if user_choice != computer_choice:
                user_points = user_points + int(user_choice)
                label_user_points = Label(start, text = f"Your Points :- {user_points}", font = font, fg = fg, bg = bg)
                label_user_points.place(x=1, y=565)
            elif user_choice == computer_choice:
                label_info_game = Label(start, text = "You lost. Now you start doing balling. Don't let computer score more than you", font = font, fg = fg, bg = bg)
                label_info_game.place(x=340,y=650)
                game_phase = "second innings"
                user_choose_batorball = "ball"
        elif user_choose_batorball == "ball":
            if user_choice != computer_choice:
                computer_points = computer_points + int(computer_choice)
                label_computer_points = Label(start, text = f"Computer Points :- {computer_points}", font = font, fg = fg, bg = bg)
                label_computer_points.place(x=1200, y=565)
            elif user_choice == computer_choice:
                label_info_game = Label(start, text = "Computer lost. Now you start doing batting. Score more than computer to win", font = font, fg = fg, bg = bg)
                label_info_game.place(x=320,y=650)
                game_phase = "second innings"
                user_choose_batorball = "bat"

    elif game_phase == "second innings":
        if user_choose_batorball == "bat":
            label_user.config(text = "USER(BAT)")
            label_computer.config(text = "COMPUTER(BALL)")
            if user_choice == computer_choice:
                if computer_points > user_points:
                    label_info_game = Label(start, text = "Oh no! Computer won the game. Better luck next time :(", font = font, fg = fg, bg = bg)
                    label_info_game.place(x=500,y=700)
                elif user_points == computer_points:
                    label_info_game = Label(start, text = "Oh! It's a tie.", font = font, fg = fg, bg = bg)
                    label_info_game.place(x=550,y=700)
                end() 
            elif user_choice != computer_choice:
                user_points = user_points + int(user_choice)
                label_user_points = Label(start, text = f"Your Points :- {user_points}", font = font, fg = fg, bg = bg)
                label_user_points.place(x=1, y=565)
                if user_points > computer_points:
                    label_info_game = Label(start, text = "Hurray! You won the game :)", font = font, fg = fg, bg = bg)
                    label_info_game.place(x=560,y=700)
                    end() 
            label_target_user = Label(start, text = f"Target is {computer_points - user_points} to win", font = font, bg = bg, fg = fg)
            label_target_user.place(x=1,y=610)
        elif user_choose_batorball == "ball":
            label_user.config(text = "USER(BALL)")
            label_computer.config(text = "COMPUTER(BAT)")
            if user_choice == computer_choice:
                if user_points > computer_points:
                    label_info_game = Label(start, text = "Hurray! You won the game :)", font = font, fg = fg, bg = bg)
                    label_info_game.place(x=560,y=700)
                elif user_points == computer_points:
                    label_info_game = Label(start, text = "Oh! It's a tie.", font = font, fg = fg, bg = bg)
                    label_info_game.place(x=550,y=700)
                end()  
            elif user_choice != computer_choice:
                computer_points = computer_points + int(computer_choice)
                label_computer_points = Label(start, text = f"Computer Points :- {computer_points}", font = font, fg = fg, bg = bg)
                label_computer_points.place(x=1200, y=565)
                if computer_points > user_points:
                    label_info_game = Label(start, text = "Oh no! Computer won the game. Better luck next time :(", font = font, fg = fg, bg = bg)
                    label_info_game.place(x=500,y=700)
                    end()
            label_target_computer = Label(start, text = f"Target {user_points - computer_points} to win", font = font, bg = bg, fg = fg)
            label_target_computer.place(x=1200,y=610)

def end():
    global button_one, button_two, button_three, button_four, button_five, button_six
    button_one.config(state = 'disabled'); button_two.config(state = 'disabled'); button_three.config(state = 'disabled'); button_four.config(state = 'disabled')
    button_five.config(state = 'disabled'); button_six.config(state = 'disabled'); button_zero.config(state = 'disabled')

choose_oddoreven()
start.mainloop()
