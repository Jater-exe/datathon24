import json
import pathlib
import uuid
from participant import load_participants
import participant

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
    
#pre: edats de dos usuaris
#post: retorna true si les edats son semblants, per tant adients per formar grup
def compare_age(user1_age,user2_age):
    age1 = user1_age
    age2 = user2_age
    if age1 > 25 and age2 > 25:
        return True
    elif age1 > 21 and age2 > 21:
        return abs(age1 - age2) <= 4
    else:
        return abs(age1 - age2) <= 3
    
#pre: any actual d'estudis d'un usuari
#post: retorna true si els dos usuaris es troben en cursos pròxims
def compare_years_study(user1_study, user2_study):
    years_of_study_1 = user1_study
    years_of_study_2 = user2_study

    if years_of_study_1 == years_of_study_2:
        return True
    else:
        if years_of_study_1 == "1st Year" and (years_of_study_2 != "3rd Year" or years_of_study_2 != "4th Year"):
            return True
        elif years_of_study_2 == "1st Year" and (years_of_study_1 != "3rd Year" or years_of_study_1 != "4th Year"):
            return True
        elif years_of_study_1 == "2nd Year" and years_of_study_2 != "4th Year":
            return True
        elif years_of_study_2 == "2nd Year" and years_of_study_1 != "4th Year":
            return True
        elif years_of_study_1 == "3rd Year" and years_of_study_2 != "1st Year":
            return True
        elif years_of_study_2 == "3rd Year" and years_of_study_1 != "1st Year":
            return True
        elif years_of_study_1 == "4th Year" and (years_of_study_2 != "1st Year" and years_of_study_2 != "2nd Year"):
            return True
        elif years_of_study_2 == "4th Year" and (years_of_study_1 != "1st Year" and years_of_study_1 != "2nd Year"):
            return True
        elif years_of_study_1 == "PhD" and years_of_study_2 == "Master's":
            return True
        elif years_of_study_1 == "Master's" and years_of_study_2 == "PhD":
            return True
        else:
            return False




    
    
#COSTA___^^^^

def compareUsers(user1, user2):
    

compareUsers(participants[x], participants[y])