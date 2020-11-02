import pandas as pd
import json
import random

dataPath = '/Users/sandro.nunes/repos/d3-tests/app/data/challenge_17b_Sandro.csv'
jsonDataPath = '/Users/sandro.nunes/repos/d3-tests/app/data/challenge_17b_Sandro.json'
parameterList = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
bList = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800]
rawData = pd.read_csv(dataPath)
snrList = list(rawData.columns)
xPosList = list(map(lambda x: x*10, list(range(len(snrList)))))

# for parameter, i in zip(parameterList, range(len(parameterList))):
#     rawData.loc[i, 'parameter'] = parameter

jsonData = []

for parameter, parameterIndex in zip(parameterList, range(len(parameterList))):
    for snrValue, snrValueIndex in zip(snrList, range(len(snrList))):
        for bValue in bList:
            jsonData.append({
                'parameter': parameter,
                'snr': snrValue,
                'confidence': rawData.loc[parameterIndex, snrValue] + random.randrange(-5, 5),
                'b': bValue,
                'xPos': xPosList[snrValueIndex] + parameterIndex + 5,
                'constant': 0,
            })

for e in jsonData :
    if (e['b'] == 50 ):
        print(e['xPos'])

with open(jsonDataPath, 'w') as f:
    json.dump(jsonData, f)





