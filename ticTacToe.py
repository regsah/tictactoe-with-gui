import tkinter as tk
import tkinter.messagebox
import os
import sys


class TicTacToe:

    player=0

    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()

        master.iconphoto(True, tk.PhotoImage(file='icon.png'))

        self.create_menu(master, frame)
        self.game_board(master, frame, size=3)

    def create_menu(self, master, frame):

        menu = tk.Menu(master)
        master.config(menu=menu)

        size_menu = tk.Menu(menu)
        menu.add_cascade(label="size",menu=size_menu)
        size_menu.add_command(label="3x3", command=lambda: self.game_board(master, frame, size=3))
        size_menu.add_command(label="4x4", command=lambda: self.game_board(master, frame, size=4))


    def game_board(self, master, frame, size):

        gamelist = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]

        self.destroy_widgets(frame)

        self.set_grid(master, frame, 3)

        button1 = tk.Button(frame, command=lambda: self.game_move(gamelist=gamelist, button=button1, frame=frame))
        button2 = tk.Button(frame, command=lambda: self.game_move(gamelist=gamelist, button=button2, frame=frame))
        button3 = tk.Button(frame, command=lambda: self.game_move(gamelist=gamelist, button=button3, frame=frame))
        button4 = tk.Button(frame, command=lambda: self.game_move(gamelist=gamelist, button=button4, frame=frame))
        button5 = tk.Button(frame, command=lambda: self.game_move(gamelist=gamelist, button=button5, frame=frame))
        button6 = tk.Button(frame, command=lambda: self.game_move(gamelist=gamelist, button=button6, frame=frame))
        button7 = tk.Button(frame, command=lambda: self.game_move(gamelist=gamelist, button=button7, frame=frame))
        button8 = tk.Button(frame, command=lambda: self.game_move(gamelist=gamelist, button=button8, frame=frame))
        button9 = tk.Button(frame, command=lambda: self.game_move(gamelist=gamelist, button=button9, frame=frame))

        button1.grid(column=0, row=0, sticky='nsew')
        button2.grid(column=0, row=1, sticky='nsew')
        button3.grid(column=0, row=2, sticky='nsew')
        button4.grid(column=1, row=0, sticky='nsew')
        button5.grid(column=1, row=1, sticky='nsew')
        button6.grid(column=1, row=2, sticky='nsew')
        button7.grid(column=2, row=0, sticky='nsew')
        button8.grid(column=2, row=1, sticky='nsew')
        button9.grid(column=2, row=2, sticky='nsew')

        if size == 4:
            gamelist = [[0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]]
            self.set_grid(master, frame, 4)

            button10 = tk.Button(frame, command=lambda: self.game_move(gamelist=gamelist, button=button10, frame=frame))
            button11 = tk.Button(frame, command=lambda: self.game_move(gamelist=gamelist, button=button11, frame=frame))
            button12 = tk.Button(frame, command=lambda: self.game_move(gamelist=gamelist, button=button12, frame=frame))
            button13 = tk.Button(frame, command=lambda: self.game_move(gamelist=gamelist, button=button13, frame=frame))
            button14 = tk.Button(frame, command=lambda: self.game_move(gamelist=gamelist, button=button14, frame=frame))
            button15 = tk.Button(frame, command=lambda: self.game_move(gamelist=gamelist, button=button15, frame=frame))
            button16 = tk.Button(frame, command=lambda: self.game_move(gamelist=gamelist, button=button16, frame=frame))


            button10.grid(column=3, row=0, sticky='nsew')
            button11.grid(column=3, row=1, sticky='nsew')
            button12.grid(column=3, row=2, sticky='nsew')
            button13.grid(column=0, row=3, sticky='nsew')
            button14.grid(column=1, row=3, sticky='nsew')
            button15.grid(column=2, row=3, sticky='nsew')
            button16.grid(column=3, row=3, sticky='nsew')

    def set_grid(self, master, frame, size):

        frame.columnconfigure(size-1, minsize=100)
        frame.rowconfigure(size-1, minsize=100)

        master.geometry(f"{size*100}x{size*100}")

        col_count, row_count = frame.grid_size()

        for col in range(col_count):
            frame.grid_columnconfigure(col, minsize=100)
        for row in range(row_count):
            frame.grid_rowconfigure(row, minsize=100)

    def destroy_widgets(self, frame):
        for widgets in frame.winfo_children():
            widgets.destroy

    def game_move(self, gamelist, button, frame):
        info = button.grid_info()
        x_position = info["column"]
        y_position = info["row"]

        if button.cget('bg') == 'SystemButtonFace':
            gamelist[y_position][x_position] = self.player + 1
            if self.player == 0:
                button.configure(bg="blue")
            elif self.player == 1:
                button.configure(bg="#ffb300")

            if self.win_check(gamelist):
                self.win_colors(frame)
                self.restart_box(type='victory')
            elif self.tie_check(gamelist):
                self.restart_box(type="tie")

            self.player = ((self.player + 1) % 2)



    def tie_check(self, gamelist):

        full_rows = 0
        for row in range(len(gamelist)):
            if gamelist[row].count(0) == 0:
                full_rows += 1

        if full_rows == len(gamelist):
            return True
        else:
            return False


    def win_check(self, gamelist):
        win_list = []

        def win_condition(win_list):
            if win_list.count(win_list[0]) == len(win_list) and win_list[0] != 0:
                return True
            else:
                return False

        #horizontal
        for row in gamelist:
            if win_condition(row):
                return True

        #vertical
        for col in range(len(gamelist)):
            win_list = []
            for row in gamelist:
                win_list.append(row[col])
            if win_condition(win_list):
                return True

        #diagonal
        win_list = []
        for i in range(len(gamelist)):
            win_list.append(gamelist[i][i])
        if win_condition(win_list):
            return True

        win_list = []
        for row, col in enumerate(reversed(range(len(gamelist)))):
            win_list.append(gamelist[row][col])
        if win_condition(win_list):
            return True


    def win_colors(self, frame):

        color_check = True
        wait_time = 200
        for i in range(1000):
            if color_check:
                frame.after(wait_time, lambda: self.change_button_color(frame, "green"))
                color_check = False
            else:
                frame.after(wait_time, lambda: self.change_button_color(frame, "red"))
                color_check = True
            wait_time += 200

    def change_button_color(self, frame, color):
        for button in frame.winfo_children():
            button.configure(bg=color)

    def restart_box(self,type):
        if type == 'tie':
            ask = tkinter.messagebox.askyesno(title='Tie!', message='Tie! Do you want to play again?')
        elif type == 'victory':
            ask = tkinter.messagebox.askyesno(title='Victory!', message=f'Player {self.player + 1} won! Do you want to play again?')


        if ask:
            python = sys.executable
            os.execl(python, python, *sys.argv)
        else:
            quit()



root = tk.Tk()
app = TicTacToe(root)
root.title("TicTacToe")
root.resizable(width=False, height=False)
root.mainloop()