import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xlsxwriter

file = pd.read_excel('C:\\Users\\Jeff\\Downloads\\2019-spring-match-data-OraclesElixir-2019-05-21.xlsx')
print("test")
def info_parsing(file):
    file.drop(["gameid", "url", "split", 'date', 'patchno','player'], axis=1, inplace=True)
    league_reduced = file.loc[file['league'] == 'LCS']
    player_id=league_reduced.drop(columns="playerid")
    pos_team= player_id[player_id['position']=='Team'].index
    player_id.drop(pos_team, inplace=True)
    writer = pd.ExcelWriter('C:\\Users\\Jeff\\Desktop\\LCS.xlsx', engine='xlsxwriter')
    player_id.to_excel(writer, sheet_name='Sheet1')
    writer.save()
League_list=["LCS"] #To be added later for multi leagues
print("Test2")
info_parsing(file)
'''Next is making a string values a int value'''
