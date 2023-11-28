import random
import tkinter as tk
from tkinter import messagebox

def update_player_cards():
    player_cards_var.set(f"玩家的牌为 {p_cards}, 总点数为 {sum(p_cards)}")

def update_dealer_cards():
    dealer_cards_var.set(f"庄家的牌为 {d_cards}, 总点数为 {sum(d_cards)}")

def display_result(message):
    messagebox.showinfo("游戏结果", message)
    window.destroy()

def dealer_choice():
    while sum(d_cards) < 17:
        random.shuffle(deck)
        d_cards.append(deck.pop())
    update_dealer_cards()

    if sum(p_cards) == sum(d_cards):
        display_result("游戏平局！")

    elif sum(d_cards) == 21:
        if sum(p_cards) < 21:
            display_result("庄家是赢家！")
        elif sum(p_cards) == 21:
            display_result("平局！")
        else:
            display_result("庄家是赢家！")

    elif sum(d_cards) < 21:
        if sum(p_cards) < 21 and sum(p_cards) < sum(d_cards):
            display_result("庄家是赢家！")
        if sum(p_cards) == 21:
            display_result("玩家是赢家！")
        if sum(p_cards) < 21 and sum(p_cards) > sum(d_cards):
            display_result("玩家是赢家！")

    else:
        if sum(p_cards) < 21:
            display_result("玩家是赢家！")
        elif sum(p_cards) == 21:
            display_result("玩家是赢家！")
        else:
            display_result("庄家是赢家！")

def hit():
    random.shuffle(deck)
    p_cards.append(deck.pop())
    update_player_cards()

    if sum(p_cards) > 21:
        display_result("你爆牌了！庄家赢了！")

    elif sum(p_cards) == 21:
        display_result("你是赢家！")

def stand():
    dealer_choice()

# 初始化一副牌
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
random.shuffle(deck)

# 创建GUI窗口
window = tk.Tk()
window.title("黑杰克 - 赌场")

# 初始化庄家和玩家的牌
d_cards = []
p_cards = []

# 创建变量以便在GUI中显示牌和总点数
player_cards_var = tk.StringVar()
dealer_cards_var = tk.StringVar()

# 创建标签显示庄家和玩家的牌
dealer_label = tk.Label(window, textvariable=dealer_cards_var)
dealer_label.pack()

player_label = tk.Label(window, textvariable=player_cards_var)
player_label.pack()

# 创建按钮，使玩家能够选择要牌或停牌
hit_button = tk.Button(window, text="要牌", command=hit)
hit_button.pack(side="left")

stand_button = tk.Button(window, text="停牌", command=stand)
stand_button.pack(side="right")

# 初始化庄家和玩家的初始牌
while len(d_cards) != 2:
    random.shuffle(deck)
    d_cards.append(deck.pop())

while len(p_cards) != 2:
    random.shuffle(deck)
    p_cards.append(deck.pop())

update_dealer_cards()
update_player_cards()

# 运行GUI
window.mainloop()
