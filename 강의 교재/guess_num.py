import random
import tkinter as tk
from tkinter import messagebox

class GuessNumberGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("숫자 맞추기 게임")
        self.difficulty = None
        self.max_number = 50
        self.score = 0
        self.attempts = 0
        self.answer = None

        self.label_intro = tk.Label(master, text="숫자 맞추기 게임에 오신 것을 환영합니다!\n난이도를 선택하세요.")
        self.label_intro.pack(pady=10)

        # 난이도 선택 프레임
        self.difficulty_frame = tk.Frame(master)
        self.difficulty_frame.pack(pady=5)

        self.difficulty_var = tk.StringVar(value="Normal")
        tk.Radiobutton(self.difficulty_frame, text="Easy (1~20)", variable=self.difficulty_var, value="Easy").pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(self.difficulty_frame, text="Normal (1~50)", variable=self.difficulty_var, value="Normal").pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(self.difficulty_frame, text="Hard (1~100)", variable=self.difficulty_var, value="Hard").pack(side=tk.LEFT, padx=5)

        self.start_button = tk.Button(master, text="게임 시작", command=self.start_game)
        self.start_button.pack(pady=5)

        # 숫자 버튼들을 위한 프레임 생성 (초기에는 숨김)
        self.buttons_frame = tk.Frame(master)
        self.buttons_frame.pack(pady=5)
        self.buttons_frame.pack_forget()

        self.number_buttons = []

        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(master, text="점수: 0")
        self.score_label.pack(pady=5)

        self.reset_button = tk.Button(master, text="다시 시작", command=self.reset_game, state=tk.DISABLED)
        self.reset_button.pack(pady=5)

    def start_game(self):
        diff = self.difficulty_var.get()
        if diff == "Easy":
            self.max_number = 20
        elif diff == "Normal":
            self.max_number = 50
        elif diff == "Hard":
            self.max_number = 100
        else:
            self.max_number = 50

        self.difficulty = diff
        self.answer = random.randint(1, self.max_number)
        self.attempts = 0
        self.score = 0
        self.result_label.config(text="")
        self.score_label.config(text="점수: 0")
        self.reset_button.config(state=tk.NORMAL)

        # 기존 버튼 제거
        for btn in self.number_buttons:
            btn.destroy()
        self.number_buttons = []

        # 숫자 버튼 생성
        for i in range(1, self.max_number + 1):
            btn = tk.Button(self.buttons_frame, text=str(i), width=4, command=lambda num=i: self.check_guess(num))
            btn.grid(row=(i-1)//10, column=(i-1)%10, padx=2, pady=2)
            self.number_buttons.append(btn)

        self.buttons_frame.pack(pady=5)
        self.label_intro.config(text=f"난이도: {diff} | 1부터 {self.max_number} 사이의 숫자 중 하나를 맞춰보세요.")
        self.difficulty_frame.pack_forget()
        self.start_button.pack_forget()

    def check_guess(self, guess):
        self.attempts += 1
        if guess < 1 or guess > self.max_number:
            self.result_label.config(text=f"1부터 {self.max_number} 사이의 숫자를 선택해주세요.")
            return
        if guess < self.answer:
            self.result_label.config(text="더 큰 숫자입니다.")
            self.update_score(-1)
        elif guess > self.answer:
            self.result_label.config(text="더 작은 숫자입니다.")
            self.update_score(-1)
        else:
            self.result_label.config(text=f"정답입니다! {self.attempts}번 만에 맞추셨습니다.")
            self.update_score(10)
            messagebox.showinfo("축하합니다!", f"정답입니다! {self.attempts}번 만에 맞추셨습니다.\n최종 점수: {self.score}")
            # 모든 버튼 비활성화
            for btn in self.number_buttons:
                btn.config(state=tk.DISABLED)

    def update_score(self, delta):
        self.score += delta
        if self.score < 0:
            self.score = 0
        self.score_label.config(text=f"점수: {self.score}")

    def reset_game(self):
        # 난이도 선택으로 돌아가기
        self.difficulty_frame.pack(pady=5)
        self.start_button.pack(pady=5)
        self.buttons_frame.pack_forget()
        self.label_intro.config(text="숫자 맞추기 게임에 오신 것을 환영합니다!\n난이도를 선택하세요.")
        self.result_label.config(text="")
        self.score_label.config(text="점수: 0")
        self.reset_button.config(state=tk.DISABLED)
        for btn in self.number_buttons:
            btn.destroy()
        self.number_buttons = []

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGameGUI(root)
    root.mainloop()

