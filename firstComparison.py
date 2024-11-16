import json
import pathlib
import uuid
from participant import load_participants

data_path = "data/datathon_participants.json"
participants = load_participants(data_path)

#PRE: dues llistes de llenguatges
#POST: llista dels idiomes coincidents
def compare_languages(list1, list2):
    result = []
    for language1 in list1:
        for language2 in list2:
            if (language1 == language2 and language1 not in result):
                result.append(language1)
    return result 

#PRE: dos diccionaris de tipus str:bool
#POST: una llista de strings
def compare_availability(dict1, dict2):
    result = []
    keys = list(dict1.keys())
    i = 0
    while i < len(dict1):
        if dict1[keys[i]] and dict2[keys[i]]:
            result.append(keys[i])
        i += 1
    return result

#JAUME__^^^^
 
def compare_prefered_role()
    
def compare_programming_skills()
    
#FORGAS___^^^^
    
def compare_age()

def compare_years_study()
    
#COSTA___^^^^

def compareUsers(user1, user2):
    

compareUsers(participants[x], participants[y])