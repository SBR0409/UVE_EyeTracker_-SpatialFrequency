import pickle
import json


# open the pickle file
with open('AllData.pickle', 'rb') as handle:
    AllData = pickle.load(handle)

# print the data
print(len(AllData[0]["P1"]["LSF"]))
print(len(AllData[0]["P1"]["BSF"]))
print(len(AllData[0]["P1"]["HSF"]))
print(len(AllData[1]["P1"]["LSF"]))
print(len(AllData[1]["P1"]["BSF"]))
print(len(AllData[1]["P1"]["HSF"]))
print(len(AllData[2]["P1"]["LSF"]))
print(len(AllData[2]["P1"]["BSF"]))
print(len(AllData[2]["P1"]["HSF"]))
print(len(AllData[3]["P1"]["LSF"]))
print(len(AllData[3]["P1"]["BSF"]))
print(len(AllData[3]["P1"]["HSF"]))


# comnver to json

with open('AllData.json', 'w') as handle:
    json.dump(AllData, handle)
