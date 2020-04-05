import pandas as pd
from tkinter import filedialog
from tkinter import *
import numpy as np

root2 = Tk()
root2.filename = filedialog.askopenfilename(initialdir = "\Documents\GitHub\\vigilant-telegram\Data Science\LCS\Positions",
                                            title = "Select parsed file", filetypes =
(("Excel Workbook","*.xlsx"),("all files","*")))
final_df = pd.read_excel(root2.filename)
'''we are going to need many roots so we can do many things'''



def avgGameTime(final_df): #we need to access every team per week per day
    week = final_df.week
    game = final_df.game
    team = final_df.team
    time = final_df.gamelength
    avg_time = list(zip(week,game,team,time))
    for i in len(avg_time):
        
    print(avg_time)








avgGameTime(final_df)