import json
import pathlib
import uuid
from participant import load_participants

data_path = "data/datathon_participants.json"
participants = load_participants(data_path)

#PRE: dues llistes de llenguatges
#POST: llista dels idiomes coincidents
def compare_languages(list)
    
def compare_aviailability()

#JAUME__^^^^
 
def compare_prefered_role()
    
def compare_programming_skills()
    
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