import tkinter as tk
from tkinter import messagebox
import random
import pygame

# 🎧 Initialize sound mixer
pygame.mixer.init()

# 🎯 Load sound effects
click_sound = "assets/click_sound.wav"

# 🎨 Create main window
root = tk.Tk()
root.title("Rock Paper Scissors - Ultimate Edition")
root.geometry("600x600")
root.resizable(False, False)
root.configure(bg="#1e1e2e")

# 🖼️ Header
title_label = tk.Label(
    root, text="Rock 🪨  Paper 📃  Scissors ✂️",
    font=("Arial", 28, "bold"), fg="#ffcc00", bg="#1e1e2e"
)
title_label.pack(pady=10)

# 🛠️ Choices and emojis
choices = ["Rock", "Paper", "Scissors"]
emoji_dict = {"Rock": "🪨", "Paper": "📃", "Scissors": "✂️"}

# 🔄 Game variables
player_score = 0
bot_score = 0
rounds = 3
current_round = 1

# 🎯 Play sound function
def play_sound(sound_file):
    pygame.mixer.Sound(sound_file).play()


# 🎯 Bot's random choice
def bot_choice():
    return random.choice(choices)


# 🎯 Determine winner
def determine_winner(player, bot):
    global player_score, bot_score, current_round

    if player == bot:
        return "It's a Tie! 🤝"
    elif (player == "Rock" and bot == "Scissors") or \
         (player == "Paper" and bot == "Rock") or \
         (player == "Scissors" and bot == "Paper"):
        player_score += 1
        return "You Win! 🎉"
    else:
        bot_score += 1
        return "You Lose! 😢"


# 🎯 Update scoreboard
def update_scoreboard():
    score_label.config(text=f"Score: You {player_score} - Bot {bot_score}")
    round_label.config(text=f"Round {current_round} / {rounds}")


# 🔄 Reset game function
def reset_game():
    global player_score, bot_score, current_round
    player_score, bot_score, current_round = 0, 0, 1
    update_scoreboard()
    result_label.config(text="Let's Play!", fg="#ffffff")


# 🎯 Check if the game is over
def check_game_over():
    if current_round > rounds:
        if player_score > bot_score:
            messagebox.showinfo("Game Over", "🏅 You won the match!")
        elif bot_score > player_score:
            messagebox.showinfo("Game Over", "🤖 Bot wins the match!")
        else:
            messagebox.showinfo("Game Over", "🤝 It's a tie!")
        reset_game()


# 🎮 Player's play action
def play(player_choice):
    global current_round
    play_sound(click_sound)

    bot_move = bot_choice()
    result = determine_winner(player_choice, bot_move)

    # 🎉 Display results
    player_label.config(text=f"You: {emoji_dict[player_choice]}")
    bot_label.config(text=f"Bot: {emoji_dict[bot_move]}")
    result_label.config(text=result, fg="#00ff00" if "Win" in result else "#ff4444")

    # 🎯 Update score and round
    current_round += 1
    update_scoreboard()
    check_game_over()


# 🎮 Create buttons with hover effect
def create_button(choice):
    btn = tk.Button(
        button_frame,
        text=f"{emoji_dict[choice]} {choice}",
        font=("Arial", 18),
        bg="#44475a",
        fg="#ffffff",
        activebackground="#ff79c6",
        activeforeground="#1e1e2e",
        relief="flat",
        command=lambda: play(choice)
    )
    # 🎯 Hover animation effect
    def on_enter(e):
        btn.config(bg="#6272a4")

    def on_leave(e):
        btn.config(bg="#44475a")

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

    return btn


# 🎯 Buttons layout
button_frame = tk.Frame(root, bg="#1e1e2e")
button_frame.pack(pady=20)

rock_btn = create_button("Rock")
paper_btn = create_button("Paper")
scissors_btn = create_button("Scissors")

rock_btn.grid(row=0, column=0, padx=10)
paper_btn.grid(row=0, column=1, padx=10)
scissors_btn.grid(row=0, column=2, padx=10)

# 🏅 Scoreboard
score_label = tk.Label(
    root, text=f"Score: You {player_score} - Bot {bot_score}",
    font=("Arial", 18), fg="#ffffff", bg="#1e1e2e"
)
score_label.pack(pady=10)

# 🔄 Round tracker
round_label = tk.Label(
    root, text=f"Round {current_round} / {rounds}",
    font=("Arial", 16), fg="#ffcc00", bg="#1e1e2e"
)
round_label.pack(pady=5)

# 📺 Player & Bot display
player_label = tk.Label(
    root, text="You: ❓", font=("Arial", 22), fg="#ffffff", bg="#1e1e2e"
)
player_label.pack(side="left", padx=20)

bot_label = tk.Label(
    root, text="Bot: ❓", font=("Arial", 22), fg="#ffffff", bg="#1e1e2e"
)
bot_label.pack(side="right", padx=20)

# 🔥 Result display
result_label = tk.Label(
    root, text="Let's Play!", font=("Arial", 24, "bold"), fg="#ffffff", bg="#1e1e2e"
)
result_label.pack(pady=20)

# 🚀 Run the main loop
root.mainloop()
