

class dataobj(object):

    def __init__(self):

        self.team_name = None
        self.time = None
        self.match_type = None
        self.data = dict()

    def add_data(self, input_number_pair: tuple(), input_odds_pair: tuple())->None:
        self.data[input_number_pair] = input_odds_pair






import pandas as pd

filename = dataobj._team_name+'_'+dataobj._time+'_'+dataobj._match_type
data = self.data

dic = {'number_home': [],
       'number_away': [],
       'odds_home': [],
       'odds_away': []}

for i in data:
    dic['number_home'].append(i[0])
    dic['number_away'].append(i[1])
    dic['odds_home'].append(data[i][0])
    dic['odds_away'].append(data[i][1])

df = pd.DataFrame(dic)
df.to_csv(filename, index=False)



