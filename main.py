'''
This script was created by Derick Stevens to practice visualization and data cleaning.
Thank you to axsddlr for providing this awesome API that made the creation of this tool much easier.

In this section I will detail player strength calculations
'''

import requests
import json
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def get_na_players():
    url = 'https://vlrggapi.herokuapp.com/stats/na'
    api = requests.get(url)
    players = api.json()

    return players


def list_players(players):
    p = players.get('data')
    p = p['segments']
    return p


player_stats = list_players(get_na_players())
player_df = pd.DataFrame(player_stats)
# player_df = player_df['average_combat_score'].astype(str).astype(float).nlargest(50)
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)


# team group
def get_org(df):
    df.groupby(['org', 'player'])
    return df


player_by_org = get_org(player_df)
#player_by_org.get_group('C9W')
print(player_by_org)

'''
fig, ply_scatter = plt.subplots()
ply_scatter.scatter(x=sorted(player_df['average_combat_score']), y=sorted(player_df['kill_deaths']), c="DarkBlue")
ply_scatter.set_xlabel('ACS')
ply_scatter.set_ylabel('KDR')

# annotate points in axis
for idx, row in player_df.iterrows():
    ply_scatter.annotate(row['player'], (row['average_combat_score'], row['kill_deaths']) )
# force matplotlib to draw the graph

xti = [round(int(float(x))) for x in player_df['average_combat_score']]
yti = [float(x) for x in player_df['kill_deaths']]


plt.gcf().set_size_inches((25.6, 14.4))
loc = matplotlib.ticker.LinearLocator(numticks=5)
loc2 = matplotlib.ticker.LinearLocator(numticks=5)
plt.gca().xaxis.set_major_locator(loc)
plt.gca().yaxis.set_major_locator(loc2)

plt.show()
'''

