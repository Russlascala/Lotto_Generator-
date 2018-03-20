"""
File: quickPick.py 
Author: Russ

Create a program that will generate 5 random numbers between 1 - 50 for a lottery "Quick Pick" 
"""
import random
from tkinter import * 

class QuickPick(Frame):

    def __init__(self):
        """Sets up the window and widgets."""
        Frame.__init__(self)
        self.master.title("Quick Pick")
        self.grid()

        # Label for title
        self._welcome = Label(self, text ="Welcome to the Quick Pick Lottery, click the button below to generate the numbers!", 
        fg = "purple",  font=("Helvetica", 12))
        self._welcome.grid(row = 0, column = 0, ipady=5 )

        # Button
        self._button = Button(self, text='Generate numbers', command = self._getNumbers, fg = "green",  font=("Helvetica", 12))
        self._button.grid(row = 1, column = 0, ipady=5, )

        # Label for generated numbers
        self._numberLabel = Label(self, text = "", fg = "blue",  font=("Helvetica", 12))
        self._numberLabel.grid (row = 2 ,column = 0, ipady=6)
    
    def _getNumbers(self):
        """ gets five randomly generated numbers from 1 - 50 and prints them to the GUI"""

        num1 = str(random.randint(1,50))
        num2 = str(random.randint(1,50))
        num3 = str(random.randint(1,50))
        num4 = str(random.randint(1,50))
        num5 = str(random.randint(1,50))

        # Prints out the numbers
        self._numberLabel["text"] = str(num1 + ", " + num2 + ", " + num3 + ", " + num4 + ", " + num5)
        

        # Styles the button to show its been clicked
        self._button['bg'] = 'yellow'
        self._button['fg'] = 'black'
        self._button['text'] = 'Numbers generated'
        

def main():
    QuickPick().mainloop()

main()