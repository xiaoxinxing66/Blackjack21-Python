import random
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

def update_player_cards():
    player_cards_var.set(f"玩家的牌为 {player_cards}, 总点数为 {sum(player_cards)}")

def update_banker_cards():
    banker_cards_var.set(f"庄家的牌为 X  {banker_cards[1]}")

def display_result(message):
    banker_cards_var.set(f"庄家的牌为 {banker_cards}, 总点数为 {sum(banker_cards)}")
    messagebox.showinfo("游戏结果", message)
    window.destroy()

def banker_choice():
    while sum(banker_cards) < 17:
        random.shuffle(deck)
        banker_cards.append(deck.pop())
    update_banker_cards()

    if sum(player_cards) == sum(banker_cards):
        display_result("游戏平局！")

    elif sum(banker_cards) == 21:
        if sum(player_cards) < 21:
            display_result("庄家是赢家！")
        elif sum(player_cards) == 21:
            display_result("平局！")
        else:
            display_result("庄家是赢家！")

    elif sum(banker_cards) < 21:
        if sum(player_cards) < 21 and sum(player_cards) < sum(banker_cards):
            display_result("庄家是赢家！")
        if sum(player_cards) == 21:
            display_result("玩家是赢家！")
        if sum(player_cards) < 21 and sum(player_cards) > sum(banker_cards):
            display_result("玩家是赢家！")

    else:
        if sum(player_cards) < 21:
            display_result("玩家是赢家！")
        elif sum(player_cards) == 21:
            display_result("玩家是赢家！")
        else:
            display_result("庄家是赢家！")

def hit():
    random.shuffle(deck)
    player_cards.append(deck.pop())
    update_player_cards()

    if sum(player_cards) > 21:
        display_result("你爆牌了！庄家赢了！")

    elif sum(player_cards) == 21:
        display_result("你是赢家！")

def stand():
    banker_choice()

# 初始化一副牌
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
random.shuffle(deck)

# 设计GUI窗口
window = tk.Tk()

# 设置窗口的初始大小为800x600像素
window_width = 800
window_height = 600

# 将窗口居中
center_window(window, window_width, window_height)

# 打开图像并将其转换为Tkinter PhotoImage对象
original_image = Image.open("VCG211132459410.jpg")
photo = ImageTk.PhotoImage(original_image)

# 创建标签，使用PhotoImage作为背景
background_label = tk.Label(window, image=photo)
background_label.place(relwidth=1, relheight=1)

window.title("21点 - 赌场")

# 初始化庄家和玩家的牌
banker_cards = []
player_cards = []

# 创建变量以便在GUI中显示牌和总点数
player_cards_var = tk.StringVar()
banker_cards_var = tk.StringVar()

# 创建标签显示庄家和玩家的牌
banker_label = tk.Label(window, textvariable=banker_cards_var)
banker_label.pack()

player_label = tk.Label(window, textvariable=player_cards_var)
player_label.pack()

# 创建按钮样式
button_style = ttk.Style()
# 设置按钮字体为微软雅黑，字体大小为12
button_style.configure("TButton", padding=10, font=("Microsoft YaHei", 12))

# 设置按钮背景颜色为绿色
button_style.map("TButton", background=[("active", "#4CAF50"), ("!active", "#008000")])

# 创建按钮，使用TButton样式
hit_button = ttk.Button(window, text="要牌", command=hit, style="TButton")
hit_button.pack(side="left", padx=10, pady=10)

stand_button = ttk.Button(window, text="停牌", command=stand, style="TButton")
stand_button.pack(side="right", padx=10, pady=10)

# 初始化庄家和玩家的初始牌
while len(banker_cards) != 2:
    random.shuffle(deck)
    banker_cards.append(deck.pop())

while len(player_cards) != 2:
    random.shuffle(deck)
    player_cards.append(deck.pop())

update_banker_cards()
update_player_cards()

window.mainloop()
