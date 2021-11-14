from random import randint
from time import time
import matplotlib.pyplot as plt
import numpy as np

class Board() :
    def __init__ (self, x_player=3 , o_player=3):
        self.board =  [' ' for i in range(10)]
        self.x_player = int(x_player)
        self.o_player = int(o_player)
        self.statistics = {'P1_TYPE' : x_player, 'P2_TYPE' : o_player , 'Round': "Player, Time, Postion"}
        self.winner = 0

    def  __str__ (self):
        return (f'   |   | \n {self.board[1]} | {self.board[2]} | {self.board[3]}\n   |   | \n-----------\n   |   | \n {self.board[4]} | {self.board[5]} | {self.board[6]}\n   |   | \n-----------\n   |   | \n {self.board[7]} | {self.board[8]} | {self.board[9]}\n   |   | ')

    def add_letter(self,board,letter,postion):
        board[postion] = letter

    def check_free(self,board,postion):
        return board[postion] == ' '      

    def check_winner(self,board,letter):
        return((board[1] == board[2] == board[3] == letter) 
        or (board[4] == board[5] == board[6] == letter)
        or (board[7] == board[8] == board[9] == letter)
        or (board[1] == board[4] == board[7] == letter)
        or (board[2] == board[5] == board[8] == letter)
        or (board[3] == board[6] == board[9] == letter)
        or (board[1] == board[5] == board[9] == letter)
        or (board[3] == board[5] == board[7] == letter))

    def generate_free_postions(self,board):
        return  [x for x , letter in enumerate(board) if letter == ' ' and x != 0]

    def random_move(self,board,letter ):
        start_time = time()
        while True :
            postion = randint(1,9)
            if self.check_free(board, postion) :
                self.add_letter(board,letter, postion)
                break 
        end_time = time()
        ex_time = end_time - start_time
        return (None,ex_time,postion)

    def minmax_move(self,board,letter):
        start_time = time()
        freepostions = self.generate_free_postions(board)
        if self.check_winner(board,"X"):
            end_time = time()
            ex_time = end_time - start_time
            return (1,ex_time,None)
        elif self.check_winner(board,"O"):
            end_time = time()
            ex_time = end_time - start_time
            return (-1,ex_time,None)
        elif not(freepostions):
            end_time = time()
            ex_time = end_time - start_time
            return (0,ex_time,None)
        if letter == "X":
            max_v = -2 
            for i in freepostions :
                new_board = board[:]
                new_board[i] = letter
                v = self.minmax_move(new_board,"O")
                if max_v < v[0]:
                    postion = i
                    max_v = max(max_v , v[0])
            end_time = time()
            ex_time = end_time - start_time
            return (max_v,ex_time,postion)
        if letter == "O":
            min_v = 2 
            for i in freepostions :
                new_board = board[:]
                new_board[i] = letter
                v = self.minmax_move(new_board,"X")
                if min_v > v[0]:
                    postion = i
                    min_v = min(min_v , v[0] )
            end_time = time()
            ex_time = end_time - start_time
            return (min_v,ex_time, postion)

    def alpha_beta_move(self,board,letter,alpha = -2 , beta = 2):
        start_time = time()
        freepostions = self.generate_free_postions(board)
        if self.check_winner(board,"X"):
            end_time = time()
            ex_time = end_time - start_time
            return (1,ex_time,None)
        elif self.check_winner(board,"O"):
            end_time = time()
            ex_time = end_time - start_time
            return (-1,ex_time,None)
        elif not(freepostions):
            end_time = time()
            ex_time = end_time - start_time
            return (0,ex_time,None)
        if letter == "X":
            max_v = -2 
            for i in freepostions :
                new_board = board[:]
                new_board[i] = letter
                v = self.alpha_beta_move(new_board,"O",alpha,beta)
                if max_v < v[0]:
                    postion = i
                    max_v = max(max_v , v[0])
                alpha = max(max_v , alpha)
                if beta <= alpha:
                    break
            end_time = time()
            ex_time = end_time - start_time
            return (max_v,ex_time,postion)
        if letter == "O":
            min_v = 2 
            for i in freepostions :
                new_board = board[:]
                new_board[i] = letter
                v = self.alpha_beta_move(new_board,"X",alpha,beta)
                if min_v > v[0]:
                    postion = i
                    min_v = min(min_v , v[0] )
                beta = min(min_v, beta)
                if beta <= alpha:
                    break
            end_time = time()
            ex_time = end_time - start_time
            return (min_v,ex_time, postion)

    def human_move(self,board,letter):
        start_time = time()
        while True :
            postion = input("Select the postion you want to place an 'X' in (1-9): ")
            try :
                postion = int(postion)
                if postion >= 1 and postion <=9 :
                    if self.check_free(board,postion):
                        self.add_letter(board,letter,postion)
                        break
                    else :
                        print("Sorry, the postion is already used :3")
                else :
                    print("Please, Select a postion with the range -_-")
            except:
                print(" Please, enter a valid postion -_-")
        end_time = time()
        ex_time = end_time - start_time
        return (None,ex_time,postion) 

    def rest(self):
        self.board =  [' ' for _ in range(10)]

    def add_statistics(self, round ,Value, time, postion):
        if round%2 == 1 :
            self.statistics[round]= ('P1', Value, time, postion)
        else :
            self.statistics[round]= ('P2', Value, time, postion)


    def play(self):
        print(""""
                              __                    __        __   __        __
 /         /    /            /  | /                /  |      /    /  | /|/| /   
(     ___ (___     ___      (___|(  ___           (___|     ( __ (___|( / |(___ 
|   )|___)|       |___      |    | |   )\   )     |   )     |   )|   )|   )|    
|__/ |__  |__      __/      |    | |__/| \_/      |  /      |__/ |  / |  / |__  
                                          /                                     
                                ─────▄██▀▀▀▀▀▀▀▀▀▀▀▀▀██▄─────
                                ────███───────────────███────
                                ───███─────────────────███───
                                ──███───▄▀▀▄─────▄▀▀▄───███──
                                ─████─▄▀────▀▄─▄▀────▀▄─████─
                                ─████──▄████─────████▄──█████
                                █████─██▓▓▓██───██▓▓▓██─█████
                                █████─██▓█▓██───██▓█▓██─█████
                                █████─██▓▓▓█▀─▄─▀█▓▓▓██─█████
                                ████▀──▀▀▀▀▀─▄█▄─▀▀▀▀▀──▀████
                                ███─▄▀▀▀▄────███────▄▀▀▀▄─███
                                ███──▄▀▄─█──█████──█─▄▀▄──███
                                ███─█──█─█──█████──█─█──█─███
                                ███─█─▀──█─▄█████▄─█──▀─█─███
                                ███▄─▀▀▀▀──█─▀█▀─█──▀▀▀▀─▄███
                                ████─────────────────────████
                                ─███───▀█████████████▀───████
                                ─███───────█─────█───────████
                                ─████─────█───────█─────█████
                                ───███▄──█────█────█──▄█████─
                                ─────▀█████▄▄███▄▄█████▀─────
                                ──────────█▄─────▄█──────────
                                ──────────▄█─────█▄──────────
                        __                   __                 __                               
 /  | / /    /        |/  | / / /           /|  /              /  |                     /        
(   |  (___ (___      |___|  ( (           ( | (___  ___      (___|      ___  ___  ___ (___      
| / )| |    |   )     |   )| | | \   )       | |   )|___)     |    |   )|   )|   )|___)|         
|/|/ | |__  |  /      |__/ | | |  \_/        | |  / |__       |    |__/ |__/ |__/ |__  |__       
                                   /                                    |    |                   
            """)
        turn = ("X",self.x_player)
        wait = ("O",self.o_player)
        round = 0
        while not(self.winner):
            if not(self.generate_free_postions(self.board)):
                break
            round+=1
            print(self)
            if turn[1] == 0 :
                self.add_statistics(round,*self.human_move(self.board,turn[0]))
            elif turn[1] ==1 :
                self.add_statistics(round,*self.random_move(self.board,turn[0]))
            elif turn[1] == 2:
                k = self.minmax_move(self.board,turn[0])
                self.add_letter(self.board,turn[0],k[-1])
                self.add_statistics(round,*k)
            elif turn[1] == 3:
                k = self.alpha_beta_move(self.board,turn[0])
                self.add_letter(self.board,turn[0],k[-1])
                self.add_statistics(round,*k)
            if self.check_winner(self.board,"X"):
                self.winner = 1
            if self.check_winner(self.board,"O"):
                self.winner = -1
            turn ,wait = wait, turn
            print(self)
        if self.winner == 1:
            print("X won the game !")
            self.statistics['Winner'] = "P1"
        elif self.winner ==-1 :
            print("O won the game !")
            self.statistics['Winner'] = "P2"
        else:
            print("Draw")
            self.statistics['Winner'] = "Draw"

def main():
    x = Board(3,3)
    x.play()
    ab = x.statistics
    y = Board(2,2)
    y.play()
    mn = y.statistics
    print(ab)
    print(mn)
    labels = ["Round"+str(i) for i in ab.keys() if type(i) == int]
    print(labels)
    mn_time = [i[2] for i in mn.values() if type(i) == tuple]
    ab_time =[i[2] for i in ab.values() if type(i) == tuple]
    print(mn_time)
    print(ab_time)
    for i in range(len(mn_time)):
        print(((mn_time[i] - ab_time[i])/mn_time[i]*100) ) if mn_time[i] != 0 else print(1) 
main()