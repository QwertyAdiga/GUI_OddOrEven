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
spl_choice = ["bat","ball"]
user_points = 0
computer_points = 0
user_runs_log = []
computer_runs_log = []
user_balls_log = []
computer_balls_log = []
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

def initial():
    label_title = Label(start, text = "Odd Or Even Game", font = ("Arial",30,""), bg = bg, fg = fg)
    label_title.place(relx=0.4, rely=0.01)

    button_game_info = Button(start, text = "?", font = font, fg = fg, bg = bg, command = info)
    button_game_info.place(relx=0.96, rely=0.01, height = 40, width = 35)

    button_restart = Button(start, text="Restart", font=font, fg=fg, bg=bg, command=restart_game)
    button_restart.place(relx=0.85, rely=0.01, height=40, width=80)
    choose_oddoreven()

def info():
    showinfo(title = "Understand the Game", message = "First choose Odd or Even\n\nThen choose any number\n\nComputer also chooses a number\n\n"
    "If the sum of yours and computer's number is even, and you choose even, then you get chance to choose Bat or Ball\n\n"
    "If the sum of yours and computer's choice is odd, and you choose odd, then you get chance to choose Bat or Ball\n\n"
    "If you choose odd and sum is even, and if you choose even and sum is odd, then computer will choose Bat or Ball\n\n"
    "If you do Batting first, then you set a target to the computer and if you do balling first computer will give you a target\n\n"
    "You must pass the target or shouldn't leave the computer to finish the target to win the game\n\n"
    "Batters get out when both the ballers and batters put the same number")

def choose_oddoreven():
    global button_even, button_odd

    label_choose = Label(start, text = "Choose", font = font, bg = bg, fg = fg)
    label_choose.place(relx=0.007, rely=0.09)

    button_odd = Button(start, text = "Odd", font = font, bg = bg, fg = fg, command = lambda : info_choose_oddoreven("Odd"))
    button_odd.place(relx=0.065, rely=0.09, height=35, width=50)

    label_or = Label(start, text = "or", font = font, fg = fg, bg = bg)
    label_or.place(relx = 0.1, rely=0.09)

    button_even = Button(start, text = "Even", font = font, fg = fg, bg = bg, command = lambda : info_choose_oddoreven("Even"))
    button_even.place(relx=0.12,rely=0.09,height = 35, width = 58)

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
    label_choose_oddoreven.place(relx=0.7,rely=0.09)
    choose_number()

def choose_number():
    global choose, choose_list

    choose_a_number = Label(start, text = "Choose a number :", font = font, fg = fg, bg = bg)
    choose_a_number.place(relx=0.007,rely=0.15)

    relx_value = 0.145
    choose_list = []
    for i in range(0,7):
        choose = Button(start, text = i, font=font, bg=bg, fg=fg, command=lambda v=i:choose_number_function(v))
        choose.place(relx= relx_value, rely=0.15, height=35, width=30)
        choose_list.append(choose)
        relx_value = relx_value + 0.025

def choose_number_function(value):
    global user_choose_oddoreven, choose, user_choose_batorball, computer_splchoice, user_choose_oddoreven, choose_list, label_down, label_choose_batorball_info, label_choose_initial_number_info

    computer_choose_initial_number = int(random.choice(choice))
    user_choose_intial_number = int(value)
    computer_splchoice = random.choice(spl_choice)

    label_choose_initial_number_info = Label(start, text = f"You choose {user_choose_intial_number} and computer choose {computer_choose_initial_number}", fg = fg, bg = bg, font = font)
    label_choose_initial_number_info.place(relx=0.7,rely=0.15)

    label_down = Label(start, text = f"{user_choose_intial_number}  +  {computer_choose_initial_number}  =  {'Even' if (user_choose_intial_number + computer_choose_initial_number) % 2 == 0 else 'Odd'}", fg = fg, bg = bg, font = font)
    label_down.place(relx=0.7,rely=0.21)

    label_choose_batorball_info = Label(start, text = "", font = font, bg = bg, fg = fg)
    label_choose_batorball_info.place(relx=0.7,rely=0.27)

    for buttn in choose_list:
        buttn.config(state = 'disabled')

    if user_choose_oddoreven == "Even":
        if (computer_choose_initial_number + user_choose_intial_number) % 2 == 0:
            choose_bat_or_ball()

        elif (computer_choose_initial_number + user_choose_intial_number) % 2 != 0:
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
    label_wantto.place(relx=0.007,rely=0.27)

    button_choose_bat = Button(start, text = "Bat", font = font, fg = fg, bg = bg, command = lambda : choose_batorball_function("bat"))
    button_choose_bat.place(relx=0.065,rely=0.27, height = 35, width = 50)

    label_or2 = Label(start, text = "or", font = font, fg = fg, bg = bg)
    label_or2.place(relx=0.1,rely=0.27)

    button_choose_ball = Button(start, text = "Ball", font = font, fg = fg, bg = bg, command = lambda : choose_batorball_function("ball"))
    button_choose_ball.place(relx=0.12,rely=0.27, height = 35, width = 50)

def choose_batorball_function(value):
    global button_choose_bat, button_choose_ball, computer_splchoice, user_choose_batorball

    user_choose_batorball = value

    button_choose_bat.config(state='disabled')
    button_choose_ball.config(state='disabled')

    label_choose_batorball_info = Label(start, text = "", font = font, bg = bg, fg = fg)
    label_choose_batorball_info.place(relx=0.7,rely=0.27)

    if user_choose_batorball == "bat":
        computer_splchoice = "ball"
        label_choose_batorball_info.config(text = "You choose Bat. So Computer will do Ball")
        started()

    elif user_choose_batorball == "ball":
        computer_splchoice = "bat"
        label_choose_batorball_info.config(text = "You choose Ball. So Computer will do Bat")
        started()

def started():
    global computer_splchoice, user_choose_batorball, label_user, label_computer, buttons_list

    label_user = Label(start, text = f"User({user_choose_batorball})".upper(), font = font, fg = fg, bg = bg)
    label_user.place(relx=0.007, rely=0.39)

    label_computer = Label(start, text = f"Computer({computer_splchoice})".upper(), font = font, fg = fg, bg = bg)
    label_computer.place(relx=0.8,rely=0.39)

    positions = [(0.05, 0.59), (0.02, 0.47), (0.05, 0.47), (0.08, 0.47), (0.02, 0.53), (0.05, 0.53), (0.08, 0.53)]
    buttons_list = []

    for index, (x,y) in enumerate(positions):
        button_number = Button(start, text = index, font=font, bg=bg, fg=fg, command = lambda v=str(index): (photo_game(v), setup_game(v)))
        button_number.place(relx = x, rely = y, height=40, width=40)
        buttons_list.append(button_number)

def photo_game(value):
    global computer_choice, label_human_photo, label_robot_photo

    user_choice = value
    computer_choice = random.choice(choice)

    img_human = Image.open(get_path("images", "human image", f"human_{user_choice}.jpg"))
    img_human = img_human.resize((300, 300), Image.LANCZOS)
    photo_human = ImageTk.PhotoImage(img_human)
    start.human_photo = photo_human
    label_human_photo = Label(start,image = photo_human)
    label_human_photo.place(relx=0.2,rely=0.39, height = 300, width = 300)

    img_robot = Image.open(get_path("images", "robot image", f"robot_{computer_choice}.png"))
    img_robot = img_robot.resize((300, 300), Image.LANCZOS)
    photo_robot = ImageTk.PhotoImage(img_robot)
    start.robot_photo = photo_robot
    label_robot_photo = Label(start, image = photo_robot)
    label_robot_photo.place(relx=0.55,rely=0.39, height = 300, width = 300)

def setup_game(value):
    global user_choose_batorball, computer_splchoice, user_points, computer_points, computer_choice, user_choice, label_user, label_computer
    global game_phase, label_user_choice, label_computer_choice, label_computer_points, label_user_points, label_info_game1
    global label_info_game2, label_target_computer, label_target_user, user_balls_log, computer_balls_log, user_runs_log, computer_runs_log

    user_choice = value

    label_user_choice = Label(start, text = f"You choose : {user_choice}", font = font, fg = fg, bg = bg)
    label_user_choice.place(relx=0.007,rely=0.64)

    label_computer_choice = Label(start, text = f"Computer choose : {computer_choice}", font = font, fg = fg, bg = bg)
    label_computer_choice.place(relx=0.78,rely=0.64)

    label_info_game1 = Label(start, text = "", font = font, fg = fg, bg = bg)
    label_info_game1.place(relx=0.25,rely=0.75)

    label_info_game2 = Label(start, text = "", font = font, fg = fg, bg = bg)
    label_info_game2.place(relx=0.25,rely=0.79)

    if game_phase == "first innings":
        if user_choose_batorball == "bat":
            user_runs_log.append(user_choice)
            computer_balls_log.append(computer_choice)

            if user_choice != computer_choice:
                user_points = user_points + int(user_choice)
                label_user_points = Label(start, text = f"Your Points : {user_points}", font = font, fg = fg, bg = bg)
                label_user_points.place(relx=0.007, rely=0.69)

            elif user_choice == computer_choice:
                label_info_game1.config(text = "You lost. Now you start doing balling. Don't let computer score more than you")
                game_phase = "second innings"
                user_choose_batorball = "ball"

        elif user_choose_batorball == "ball":
            user_balls_log.append(user_choice)
            computer_runs_log.append(computer_choice)

            if user_choice != computer_choice:
                computer_points = computer_points + int(computer_choice)
                label_computer_points = Label(start, text = f"Computer Points : {computer_points}", font = font, fg = fg, bg = bg)
                label_computer_points.place(relx=0.78, rely=0.69)
    
            elif user_choice == computer_choice:
                label_info_game1.config(text = "Computer lost. Now you start doing batting. Score more than computer to win")
                game_phase = "second innings"
                user_choose_batorball = "bat"

    elif game_phase == "second innings":
        if user_choose_batorball == "bat":
            user_runs_log.append(user_choice)
            computer_balls_log.append(computer_choice)

            label_user.config(text = "USER(BAT)")
            label_computer.config(text = "COMPUTER(BALL)")

            if user_choice == computer_choice:
                if computer_points > user_points:
                    label_info_game2.config(text = "Oh no! Computer won the game. Better luck next time :(")
                elif user_points == computer_points:
                    label_info_game2.config(text = "Oh! It's a tie.")
                end() 

            elif user_choice != computer_choice:
                user_points = user_points + int(user_choice)
                label_user_points = Label(start, text = f"Your Points : {user_points}", font = font, fg = fg, bg = bg)
                label_user_points.place(relx=0.007, rely=0.69)

                if user_points > computer_points:
                    label_info_game2.config(text = "Hurray! You won the game :)")
                    end()
            needed = (computer_points - user_points) + 1
            if needed > 0:
                label_target_user = Label(start, text = f"Target is {needed} to win", font = font, bg = bg, fg = fg)
                label_target_user.place(relx=0.007,rely=0.75)
            else:
                label_target_user = Label(start, text = f"Target is Achieved", font = font, bg = bg, fg = fg)
                label_target_user.place(relx=0.007,rely=0.75)

        elif user_choose_batorball == "ball":
            user_balls_log.append(user_choice)
            computer_runs_log.append(computer_choice)

            label_user.config(text = "USER(BALL)")
            label_computer.config(text = "COMPUTER(BAT)")

            if user_choice == computer_choice:
                if user_points > computer_points:
                    label_info_game2.config(text = "Hurray! You won the game :)")
                elif user_points == computer_points:
                    label_info_game2.config(text = "Oh! It's a tie.")
                end() 

            elif user_choice != computer_choice:
                computer_points = computer_points + int(computer_choice)
                label_computer_points = Label(start, text = f"Computer Points : {computer_points}", font = font, fg = fg, bg = bg)
                label_computer_points.place(relx=0.78, rely=0.69)

                if computer_points > user_points:
                    label_info_game2.config(text = "Oh no! Computer won the game. Better luck next time :(")
                    end()
            needed = (user_points - computer_points) + 1
            if needed > 0:
                label_target_computer = Label(start, text = f"Target is {needed} to win", font = font, bg = bg, fg = fg)
                label_target_computer.place(relx=0.78,rely=0.75)
            else:
                label_target_computer = Label(start, text = "Target is Achieved", font = font, bg = bg, fg = fg)
                label_target_computer.place(relx=0.78,rely=0.75)                

def end():
    global buttons_list, user_points, computer_points, user_choose_oddoreven, user_choose_batorball, computer_splchoice
    global user_balls_log, computer_balls_log, user_runs_log, computer_runs_log, result, json_path

    for btn in buttons_list:
        btn.config(state='disabled')

    if user_points > computer_points:
        winner = "user"
    elif computer_points > user_points:
        winner = "computer"
    else:
        winner = "tie"

    game_log = {
        "user_choice_oddoreven": user_choose_oddoreven,
        "user_first_batorball": "bat" if user_choose_batorball == "ball" else "ball",
        "user_points": user_points,
        "computer_points": computer_points,
        "User runs" : user_runs_log,
        "Computer balls" : computer_balls_log,
        "Computer runs" : computer_runs_log,
        "Users balls" : user_balls_log,
        "winner": winner
    }

    json_path = get_path("points.json")

    with open(json_path, "r") as f:
        data = json.load(f)

    if winner == "user":
        data["user_won"] += 1
    elif winner == "computer":
        data["computer_won"] += 1

    data["matches"].append(game_log)

    with open(json_path, "w") as f:
        json.dump(data, f, indent=4)

    result = Button(start, text="Results", fg=fg, bg=bg, font=font, command = result_show)
    result.place(relx=0.4, rely=0.84)

def result_show():
    global json_path
    with open(json_path, "r") as f:
        file_content = f.read()

    summary_win = Toplevel(start)
    summary_win.title("Game Summary")
    summary_win.geometry("600x400")
    summary_win.config(bg=bg)
    summary_win.iconbitmap(logo_path)

    scrollbar = Scrollbar(summary_win)
    scrollbar.pack(side=RIGHT, fill=Y)

    text_box = Text(summary_win, wrap="word", font=("Consolas", 12), fg=fg, bg=bg, yscrollcommand=scrollbar.set)
    text_box.insert("1.0", file_content)
    text_box.config(state="disabled")
    text_box.pack(expand=True, fill="both")
    scrollbar.config(command=text_box.yview)

def restart_game():
    global user_points, computer_points, game_phase, user_choose_batorball, user_choose_oddoreven, computer_splchoice, computer_choice
    global user_choice, choose_list, buttons_list, label_choose_initial_number_info, label_down, label_choose_batorball_info
    global label_user, label_computer, label_user_choice, label_computer_choice, computer_runs_log
    global label_user_points, label_computer_points, label_info_game1, label_info_game2, label_target_user, label_target_computer
    global label_human_photo, label_robot_photo, button_odd, button_even, user_balls_log, user_runs_log, computer_balls_log, result

    user_points = 0
    computer_points = 0
    game_phase = "first innings"
    user_choose_batorball = None
    user_choose_oddoreven = None
    computer_splchoice = None
    computer_choice = None
    user_choice = None

    for w in start.winfo_children():
        w.destroy()

    choose_list = []
    buttons_list = []
    user_balls_log = []
    user_runs_log = []
    computer_runs_log = []
    computer_balls_log = []
    result = None
    label_choose_initial_number_info = None
    label_down = None
    label_choose_batorball_info = None
    label_user = None
    label_computer = None
    label_user_choice = None
    label_computer_choice = None
    label_user_points = None
    label_computer_points = None
    label_info_game1 = None
    label_info_game2 = None
    label_target_computer = None
    label_target_user = None
    label_human_photo = None
    label_robot_photo = None
    button_odd = None
    button_even = None

    initial()

initial()
start.mainloop()
