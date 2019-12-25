import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xlsxwriter
import math
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression


df = pd.read_excel('C:\\Users\\Jeff\\Downloads\\2019-spring-match-data-OraclesElixir-2019-05-21.xlsx')
new_df = pd.read_excel('C:\\Users\\Jeff\\Desktop\\LCS.xlsx')

drop_list=["gameid", "url", "split", 'date', 'patchno','player','ban1','ban2','ban3','ban4','ban5', 'firedrakes',
           'waterdrakes', 'earthdrakes','airdrakes', 'champion', 'elementals', 'oppelementals', 'elders','oppelders',
           'visiblewardclearrate','invisiblewardclearrate','heraldtime', 'week', 'game', 'playerid']#'league'
def info_parsing(df):
    df.drop(drop_list, axis=1, inplace=True)
    df.fillna(-9999999, inplace=True)
    #df.loc[df['position']=='Team']
    test= df[df.position.str.match('Team')] #limiting the search to just one thing for now
    league = df.loc[df['league'] == 'LCS'] #not used currently since we want to maximize the amount of data
    Team = test.loc[(test['team']=='Team Liquid')]
    writer = pd.ExcelWriter('C:\\Users\\Jeff\\Desktop\\LCS.xlsx', engine='xlsxwriter')
    Team.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    return df

#League_list=["LCS"] #To be added later for multi leagues
info_parsing(df)
#print(new_df)
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


B_side = lambda row: math.floor((int(row['result']) + int(row['side']==0))/2)
new_df["Blue Side"] = new_df.apply(B_side, axis=1)


R_side = lambda row: math.floor((int(row['result']) + int(row['side']==1))/2)
new_df["Red Side"] = new_df.apply(R_side, axis=1)

FB_side = lambda row: math.floor((int(row['result']) + int(row['fb']==1))/2)
new_df["FB"] = new_df.apply(FB_side, axis=1)

FBlooded_side = lambda row: math.floor((int(row['result']) + int(row['fb']==0))/2)
new_df["FBlooded"] = new_df.apply(FBlooded_side, axis=1)

FD = lambda row: math.floor((int(row['result']) + int(row['fd']==1))/2)
new_df["FD"] = new_df.apply(FD, axis=1)

NoFD = lambda row: math.floor((int(row['result']) + int(row['fd']==0))/2)
new_df["No FD"] = new_df.apply(NoFD, axis=1)


FT = lambda row: math.floor((int(row['result']) + int(row['ft']==1))/2)
new_df["FT"] = new_df.apply(FT, axis=1)

NoFT = lambda row: math.floor((int(row['result']) + int(row['ft']==0))/2)
new_df["NoFT"] = new_df.apply(NoFT, axis=1)

forecast_out = int(math.ceil(0.1*len(new_df)))
PA = (new_df['gdat15']-new_df['gdat10'])*new_df['result']
PB = (new_df['gdat10']-new_df['gdat15'])*new_df['result']

#new_df = new_df[["NoFT","FT","No FD","FD","Blue Side","Red Side",'FB','FBlooded','result','teamtowerkills','opptowerkills']]
forecast_col = 'result'
print(forecast_out)
df['result'] = df[forecast_col].shift(-forecast_out)


X = np.array(new_df.drop(['result'],1))
y = np.array(new_df['result'])
X = preprocessing.scale(X)
y = np.array(new_df['result'])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y,test_size=0.7)
clf = LinearRegression()
clf.fit(X_train,y_train)
accuracy = clf.score(X_test,y_test)

print(accuracy)