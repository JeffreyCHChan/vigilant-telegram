import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xlsxwriter

df = pd.read_excel('C:\\Users\\Jeff\\Downloads\\2019-spring-match-data-OraclesElixir-2019-05-21.xlsx')
new_df = pd.read_excel('C:\\Users\\Jeff\\Desktop\\LCS.xlsx')
drop_list=["gameid", "url", "split", 'date', 'patchno','player','ban1','ban2','ban3','ban4','ban5']
def info_parsing(df):
    df.drop(drop_list, axis=1, inplace=True)
    league_reduced = df.loc[df['league'] == 'LCS']
    player_id=league_reduced.drop(columns="playerid")
    pos_team= player_id[player_id['position']=='Team'].index
    player_id.drop(pos_team, inplace=True)
    writer = pd.ExcelWriter('C:\\Users\\Jeff\\Desktop\\LCS.xlsx', engine='xlsxwriter')
    player_id.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    return df
League_list=["LCS"] #To be added later for multi leagues
info_parsing(df)
'''Next is making a string values a int value'''
def handle_non_numerical_data(new_df):
    columns = new_df.columns.values

    for column in columns:
        text_digit_vals = {}

        def convert_to_int(val):
            return text_digit_vals[val]

        if new_df[column].dtype != np.int64 and df[column].dtype != np.float64:
            column_contents = new_df[column].values.tolist()
            unique_elements = set(column_contents)
            x = 0
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    text_digit_vals[unique] = x
                    x += 1
            new_df[column] = list(map(convert_to_int, new_df[column]))
    return new_df
handle_non_numerical_data(new_df)
print(new_df.iloc[:10,:10])