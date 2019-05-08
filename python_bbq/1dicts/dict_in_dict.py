import pprint
import pandas as pd
import os
import csv


people = {}

people['Ford'] = {'Name':'Ford Perfect', 'Gender':'Male', 'Occupation':'Researcher', 'Home Planet':'Betelguese Seven'}

people['Arthur'] = {'Name':'Arthur Dent', 'Gender':'Male', 'Occupation':'Sanwich Maker', 'Home Planet':'Earth'}

people['Tricia'] = {'Name':'Tricia McMillan', 'Gender':'Female', 'Occupation':'Mathematician', 'Home Planet':'Earth'}

people['Marvin'] = {'Name':'Marvin', 'Gender':'Unknown', 'Occupation':'Paranoid Android', 'Home Planet':'Unknown'}

# pprint.pprint(people)

# print(people)

#data = pd.read_csv('data_dict.csv', delimiter=';')
#print(data)


f = os.path.join(os.path.dirname(__file__), 'data_dict.csv')
with open(f, "r")as file:
    k = []
    mainDict = {}
    for line in file:
        l = line.strip().split(";")
        if l[0] == 'Name':
            k = l
            continue
        vn = l[0].split(" ")[0]
        mainDict[vn] = {k[i]: l[i] for i in range(len(k))}


    pprint.pprint(mainDict)


