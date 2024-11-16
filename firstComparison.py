import json
import pathlib
import uuid
from participant import load_participants
import participant

data_path = "data/datathon_participants.json"
participants = load_participants(data_path)

#PRE: dues llistes de llenguatges
#POST: llista dels idiomes coincidents
def compare_languages(list)
    
def compare_aviailability()

#JAUME__^^^^
 
#PRE: dues cadenes seleccionades entre Literal["Analysis", "Visualization", "Development", "Design", "Don't know", "Don't care"]
#POST: un dels usuaris no li importa la seva funcio o dos coincideixen
def compare_prefered_role(preferedrole1: str, preferedrole2: str):

    if(preferedrole1=="Don't know" or preferedrole2=="Don't know" or preferedrole1=="Don't care" or preferedrole1=="Don't care"):
        return "One user doesn't care"

    if(preferedrole1==preferedrole2): 
        return "Coincideixen en rol"
    
def compare_programming_skills(dict1, dict2):

    conjunt_user1 = set(dict1.keys()) #Guardem unicament claus del diccionari de user1 (es a dir, nomes els llenguatges q sap) 
    conjunt_user2 = set(dict2.keys()) #Rt

    shared_languages = conjunt_user1 & conjunt_user2
    unique_languages1 = conjunt_user1 - shared_languages
    unique_languages2 = conjunt_user2 - shared_languages

    list_result = [shared_languages, unique_languages1, unique_languages2]

    return list_result




    
#FORGAS___^^^^
    
def compare_age()

def compare_years_study()
    
#COSTA___^^^^

def compareUsers(user1, user2):
    

compareUsers(participants[x], participants[y])