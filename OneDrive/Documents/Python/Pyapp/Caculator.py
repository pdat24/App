import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning
import math

class Solving_sqrt(object):

    def only_one_normal_sqrt(self, string):
        self.numbers_after_sqrt_sign = ""
        self.result_after_sqrt = ""
        self.the_remain_value_after_sqrt = ""
        self.the_value_will_be_returned = ""
        self.the_left_value_of_sqrt_sign = string[:string.index('√')]
        for i in range(string.index('√')+1, len(string)):
            if string[i].isdigit() or string[i] == '.' :
                self.numbers_after_sqrt_sign+=string[i]
            else:
                self.the_remain_value_after_sqrt = string[i:]
                break
        self.result_after_sqrt = str(math.sqrt(float(self.numbers_after_sqrt_sign)))
        self.the_value_will_be_returned = self.the_left_value_of_sqrt_sign + self.result_after_sqrt + self.the_remain_value_after_sqrt
        return self.the_value_will_be_returned

    def only_one_normal_sqrt_and_have_curly_brace(self, string):
        self.numbers_after_sqrt_sign = ""
        self.result_after_sqrt = ""
        self.the_remain_value_after_sqrt = ""
        self.the_value_will_be_returned = ""
        self.the_left_value_of_sqrt_sign = string[:string.index('√')]
        for i in range(string.index('√')+2, len(string)) if string[string.index('√')+1] == '(' else ... :
            if (string[i]) != ')':
                self.numbers_after_sqrt_sign += string[i]
            else:
                self.result_after_sqrt = str(math.sqrt(eval(self.numbers_after_sqrt_sign, {'π':math.pi, 'e':math.e})))
                self.the_remain_value_after_sqrt = string[i+1:]
                break
        self.the_value_will_be_returned = self.the_left_value_of_sqrt_sign + self.result_after_sqrt + self.the_remain_value_after_sqrt
        return self.the_value_will_be_returned

    def finally_treat_sqrt_step(self, string):
        self.string_index = 0
        while ('√' in string):
            if (string[self.string_index] == '√') and (string[self.string_index+1] != '('):
                string = self.only_one_normal_sqrt(string)
            elif (string[self.string_index] == '√') and (string[self.string_index+1] == '('):
                string = self.only_one_normal_sqrt_and_have_curly_brace(string)
            self.string_index+=1
        return string

class EnterExpression(ttk.Frame, Solving_sqrt):
    expression_will_be_evaluted = ""
    Ans = 0
    def __init__(self):
        super(EnterExpression, self).__init__()
        self.expression_is_computed = False
        self.radix_system = 'D'
        self.screen_after_expression_is_deleted = tk.Canvas(self, width = 296, height = 120, bg = 'gray')
        self.screen_after_expression_is_deleted.grid(row = 0, column = 0, columnspan = 6, pady = 10)
        self.bit = tk.Label(self, text = f'{self.radix_system}', bg = 'gray', font = "courier 11")
        self.bit.grid(column = 0, row = 0, columnspan = 6, sticky = 'ne', padx = 10, pady = 12)

        self.add_sign     = ttk.Button(self, text = "+", command = lambda: self.showscreen('+'), width = 5)
        self.hyphen_sign  = ttk.Button(self, text = "-", command = lambda: self.showscreen('-'), width = 5)
        self.mutiply_sign = ttk.Button(self, text = "x", command = lambda: self.showscreen('x'), width = 5)
        self.divide_sign  = ttk.Button(self, text = "/", command = lambda: self.showscreen('/'), width = 5)
        self.clear_sign   = ttk.Button(self, text = "C", command = lambda: self.showscreen('C'), width = 5)
        self.delete_sign  = ttk.Button(self, text = "<<<", command = lambda: self.showscreen('<<<'), width = 5)

        self.add_sign.grid      (row = 1, column = 0, pady = 5, sticky = 'w', ipady = 5, ipadx = 1)
        self.hyphen_sign.grid   (row = 1, column = 1, pady = 5, sticky = 'w', ipady = 5, ipadx = 1)
        self.mutiply_sign.grid  (row = 1, column = 2, pady = 5, sticky = 'w', ipady = 5, ipadx = 1)
        self.divide_sign.grid   (row = 1, column = 3, pady = 5, sticky = 'w', ipady = 5, ipadx = 1)
        self.delete_sign.grid   (row = 1, column = 4, pady = 5, sticky = 'w', ipady = 5, ipadx = 1)
        self.clear_sign.grid    (row = 1, column = 5, pady = 5, sticky = 'w', ipady = 5, ipadx = 1)

        self.zero       = ttk.Button(self, text = "0", command = lambda: self.showscreen(0), width = 5)
        self.one        = ttk.Button(self, text = "1", command = lambda: self.showscreen(1), width = 5)
        self.two        = ttk.Button(self, text = "2", command = lambda: self.showscreen(2), width = 5)
        self.three      = ttk.Button(self, text = "3", command = lambda: self.showscreen(3), width = 5)
        self.four       = ttk.Button(self, text = "4", command = lambda: self.showscreen(4), width = 5)
        self.five       = ttk.Button(self, text = "5", command = lambda: self.showscreen(5), width = 5)
        self.six        = ttk.Button(self, text = "6", command = lambda: self.showscreen(6), width = 5)
        self.seven      = ttk.Button(self, text = "7", command = lambda: self.showscreen(7), width = 5)
        self.eight      = ttk.Button(self, text = "8", command = lambda: self.showscreen(8), width = 5)
        self.nine       = ttk.Button(self, text = "9", command = lambda: self.showscreen(9), width = 5)    
        self.dot        = ttk.Button(self, text = ".", command = lambda: self.showscreen('.'), width = 5)
        self.ans        = ttk.Button(self, text = "Ans", command = lambda: self.showscreen("Ans"), width = 5)
        self.opening_curly_brace  = ttk.Button(self, text = "(", command = lambda: self.showscreen('('), width = 5)
        self.closing_curly_brace  = ttk.Button(self, text = ")", command = lambda: self.showscreen(')'), width = 5)
        self.pi         = ttk.Button(self, text = "π", command = lambda: self.showscreen('π'), width = 5)
        self.e          = ttk.Button(self, text = "e", command = lambda: self.showscreen('e'), width = 5)
        self.pow        = ttk.Button(self, text = "^", command = lambda: self.showscreen('^'), width = 5)
        self.sqrt       = ttk.Button(self, text = "√", command = lambda: self.showscreen('√'), width = 5)
        self.equal_sign = ttk.Button(self, text = "=", command = lambda: self.showscreen('='), width = 10)
        self.Dec        = ttk.Button(self, text = "Dec", command = lambda: self.showscreen("Dec"), width = 5)
        self.Bin        = ttk.Button(self, text = "Bin", command = lambda: self.showscreen("Bin"), width = 5)
        self.Oct        = ttk.Button(self, text = "Oct", command = lambda: self.showscreen("Oct"), width = 5)
        self.Hex        = ttk.Button(self, text = "Hex", command = lambda: self.showscreen("Hex"), width = 5)

        self.zero.grid      (row = 2, column = 0, pady = 5, sticky = 'w', ipady = 5, ipadx = 1)
        self.one.grid       (row = 2, column = 1, pady = 5, sticky = 'w', ipady = 5, ipadx = 1)
        self.two.grid       (row = 2, column = 2, pady = 5, sticky = 'w', ipady = 5, ipadx = 1)
        self.three.grid     (row = 2, column = 3, pady = 5, sticky = 'w', ipady = 5, ipadx = 1)
        self.four.grid      (row = 2, column = 4, pady = 5, sticky = 'w', ipady = 5, ipadx = 1)
        self.five.grid      (row = 2, column = 5, pady = 5, sticky = 'w', ipady = 5, ipadx = 1)
        self.six.grid       (row = 3, column = 0, pady = 5, sticky = 'w', ipady = 5, ipadx = 1)
        self.seven.grid     (row = 3, column = 1, pady = 5, sticky = 'w', ipady = 5, ipadx = 1)
        self.eight.grid     (row = 3, column = 2, pady = 5, sticky = 'w', ipady = 5, ipadx = 1)
        self.nine.grid      (row = 3, column = 3, pady = 5, sticky = 'w', ipady = 5, ipadx = 1)
        self.dot.grid       (row = 3, column = 4, pady = 5, sticky = 'w', ipady = 5, ipadx = 1)
        self.opening_curly_brace.grid (row = 4, column = 0, pady = 5, sticky = 'w', ipady = 5, ipadx = 1)
        self.closing_curly_brace.grid (row = 4, column = 1, pady = 5, sticky = 'w', ipady = 5, ipadx = 1)
        self.pi.grid        (row = 4, column = 2, pady = 5, sticky = 'w', ipady = 5, ipadx = 1)
        self.e.grid         (row = 4, column = 3, pady = 5, sticky = 'w', ipady = 5, ipadx = 1)
        self.pow.grid       (row = 4, column = 4, pady = 5, sticky = 'w', ipady = 5, ipadx = 1)
        self.sqrt.grid      (row = 4, column = 5, pady = 5, sticky = 'w', ipady = 5, ipadx = 1)
        self.ans.grid       (row = 3, column = 5, pady = 5, sticky = 'w', ipady = 5, ipadx = 1)
        self.equal_sign.grid(row = 5, column = 4, columnspan = 2, pady = 5, sticky = 'w', ipady = 5, ipadx = 11)
        self.Dec.grid       (row = 5, column = 0, pady = 5, sticky = 'w', ipady = 5, ipadx = 1)
        self.Bin.grid       (row = 5, column = 1, pady = 5, sticky = 'w', ipady = 5, ipadx = 1)
        self.Oct.grid       (row = 5, column = 2, pady = 5, sticky = 'w', ipady = 5, ipadx = 1)
        self.Hex.grid       (row = 5, column = 3, pady = 5, sticky = 'w', ipady = 5, ipadx = 1)
        self.grid()

    def showscreen(self, input_data):
        self.operators_can_be_used_after_computed ='+-^x/'
        self.FRESHER = 'πe√.Ans()'
        self.omit_access_operator = None

        if   input_data == 'Hex': self.radix_system = 'H'
        elif input_data == 'Dec': self.radix_system = 'D'
        elif input_data == 'Bin': self.radix_system = 'B'
        elif input_data == 'Oct': self.radix_system = 'O'

        elif (input_data == "Ans") and (self.radix_system != 'D'):
            ...

        elif input_data == "C":
            self.expression_will_be_evaluted  = ""
            self.screen_after_expression_is_deleted = tk.Canvas(self, width = 296, height = 120, bg = 'gray')
            self.screen_after_expression_is_deleted.grid(row = 0, column = 0, columnspan = 6, pady = 10)
            self.bit_mode = tk.Label(self, text = f"{self.radix_system}", bg = 'gray', font = "courier 11")
            self.bit_mode.grid(column = 0, row = 0, columnspan = 6, sticky = 'ne', padx = 10, pady = 12)

        elif input_data == "<<<":
            if self.expression_is_computed == False:
                try:
                    if self.expression_will_be_evaluted.endswith("Ans"):
                        self.expression_will_be_evaluted =  self.expression_will_be_evaluted.rstrip("Ans")
                    else:
                        self.expression_will_be_evaluted  = self.expression_will_be_evaluted [:len(self.expression_will_be_evaluted )-1]
                    self.screen_after_expression_is_deleted = tk.Canvas(self, width = 296, height = 120, bg = 'gray')
                    self.screen_after_expression_is_deleted.grid(row = 0, column = 0, columnspan = 6, pady = 10)
                    self.bit_mode = tk.Label(self, text = f"{self.radix_system}", bg = 'gray', font = "courier 11")
                    self.bit_mode.grid(column = 0, row = 0, columnspan = 6, sticky = 'ne', padx = 10, pady = 12)
                    self.expression_will_be_displayed = tk.Label(self, text = f"{self.expression_will_be_evaluted}", font = "tkDefaeultFont 13", bg = "gray")
                except: ...

        elif input_data == "=":
            self.expression_is_computed = True
            try:
                if "**" not in self.expression_will_be_evaluted:
                    self.expression_will_be_evaluted = self.expression_will_be_evaluted.replace('^', '**')
                    if self.expression_will_be_evaluted.startswith('0x') == False:
                        self.expression_will_be_evaluted = self.expression_will_be_evaluted.replace('x', '*')
                    self.expression_will_be_evaluted = self.finally_treat_sqrt_step(self.expression_will_be_evaluted)

                    if self.radix_system == "H":
                        self.expression_will_be_evaluted = str(hex(round(eval(self.expression_will_be_evaluted, {'π':math.pi, 'e':math.e, "Ans": self.Ans}))))
                    elif self.radix_system == "B":
                        self.expression_will_be_evaluted = str(bin(round(eval(self.expression_will_be_evaluted, {'π':math.pi, 'e':math.e, "Ans": self.Ans}))))
                    elif self.radix_system == "O":
                        self.expression_will_be_evaluted = str(oct(round(eval(self.expression_will_be_evaluted, {'π':math.pi, 'e':math.e, "Ans": self.Ans}))))
                    else:
                        self.expression_will_be_evaluted = str(eval(self.expression_will_be_evaluted, {'π':math.pi, 'e':math.e, "Ans": self.Ans}))

                    if len(self.expression_will_be_evaluted) >= 27:
                        self.expression_will_be_evaluted = float(self.expression_will_be_evaluted)
                        
                    if self.radix_system != 'D':
                        self.screen_after_expression_is_deleted = tk.Canvas(self, width = 296, height = 120, bg = 'gray')
                        self.expression_will_be_displayed = tk.Label(self, text = f"{eval(self.expression_will_be_evaluted)}", font = "tkDefaeultFont 13", bg = "gray")
                        self.screen_after_expression_is_deleted.grid(row = 0, column = 0, columnspan = 6, pady = 10)
                    
                    self.result = tk.Label(self, text = f"= {self.expression_will_be_evaluted}", font = "tkDefaeultFont 13", bg = "gray")
                    self.result.grid(row =0 , column = 0, columnspan = 6, pady = 15, padx = 10, sticky = "sw")
                    self.Ans = float(eval(self.expression_will_be_evaluted))
                else:
                    showwarning (
                        title = "Warning!",
                        message = "Systax warning! '**' "
                    )          
            except Exception as bug:
                if self.expression_will_be_evaluted  == "":
                    ...
                else:
                    showerror (
                        title = "Systax Error",
                        message = "Incorrect expression!"
                    )
        else: 
            if self.expression_is_computed and (str(input_data) in self.operators_can_be_used_after_computed):
                self.screen_after_expression_is_deleted = tk.Canvas(self, width = 296, height = 120, bg = 'gray')
                self.screen_after_expression_is_deleted.grid(row = 0, column = 0, columnspan = 6, pady = 10)

            elif self.expression_is_computed and (str(input_data).isdigit() or input_data in self.FRESHER):
                self.screen_after_expression_is_deleted = tk.Canvas(self, width = 296, height = 120, bg = 'gray')
                self.screen_after_expression_is_deleted.grid(row = 0, column = 0, columnspan = 6, pady = 10)
                self.expression_will_be_evaluted = ""

            self.expression_is_computed = False

            if (len(self.expression_will_be_evaluted) %29 == 0) and (len(self.expression_will_be_evaluted)!=0):
                self.expression_will_be_evaluted  += f"{str(input_data)}\n"
            else:
                if (self.radix_system == 'D') or (str(input_data).isdigit()):
                    self.expression_will_be_evaluted  += str(input_data)
            self.expression_will_be_displayed = tk.Label(self, text = f"{self.expression_will_be_evaluted }", font = "tkDefaeultFont 13", bg = "gray")
        try:
            self.expression_will_be_displayed.grid(row = 0, column = 0, columnspan = 6, pady = 30, padx =10, sticky = "nw")
        except: ...
        try:
            self.bit_mode = tk.Label(self, text = f"{self.radix_system}", bg = 'gray', font = "courier 11")
            self.bit_mode.grid(column = 0, row = 0, columnspan = 6, sticky = 'ne', padx = 10, pady = 12)
        except Exception as e:
            ...
class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()
        self.geometry("300x400")
        self.resizable(False, False)
        self.title("Caculater")
        self.style = ttk.Style()
        self.style.theme_use('clam')
if __name__ == '__main__':
    app = App()
    EnterExpression()
    app.mainloop()