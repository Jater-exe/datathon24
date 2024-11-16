import json
import pathlib
import uuid
from participant import load_participants
import participant
from first_comparasion import compare_languages, compare_availability, compare_prefered_role, compare_programming_skills, compare_age, compare_years_study, compare_datathons, compare_exp_level, compare_challenge, compare_group_size

data_path = "data/datathon_participants.json"
participants = load_participants(data_path)

def index(user1, user2):

    #Calcul percentatge challenges

    challenges = compare_challenge(user1.interest_in_challenges, user2.interest_in_challenges)

    challenges_index = len(challenges) #Quants reptes coincideixen

    #Calcul percentatge languages
    languages = compare_languages(user1.preferred_languages, user2.preferred_languages)
    
    if(len(languages)>=1):
        languages_index = 100
    else:
        languages_index = 0

    #Calcul percentatge disponibilitat
    disp = compare_availability(user1.availability, user2.availability)
    disp_index = len(disp) * 20

    #Calcul percentatge rol

    rol = compare_prefered_role(user1.preferred_role, user2.preferred_role)

    if(rol=="One user doesn't care"):
        rol_index = 80
    elif(rol=="No coincideixen en rol"):
        rol_index = 100
    else:
        rol_index = 0

    #Calcul percentatge exp_level

    exp_level = compare_exp_level(user1.experience_level, user2.experience_level)

    if(exp_level):
        exp_level_index = 100
    else:
        exp_level_index = 0

    #Calcul percentatge anys estudiats

    anys_estudiats = compare_years_study(user1.year_of_study, user2.year_of_study)

    if(anys_estudiats):
        anys_estudiats_index=100
    else:
        anys_estudiats_index=0

    #Calcul percentatge mesura equip

    group_size = compare_group_size(user1.preferred_team_size, user2.preferred_team_size)

    if(group_size == "Coincideixen en grup"):
        group_size_index = 100
    elif(group_size == "Diferencia de 1"):
        group_size_index = 60
    elif(group_size == "Diferencia de 2"):
        group_size_index = 30
    elif(group_size == "Una persona vol anar sola"):
        group_size_index = 0

    #Calcul percentatge hackatons previes

    number_hackatons = compare_datathons(user1.hackathons_done, user2.hackathons_done)
    
    if(number_hackatons):
        number_hackatons_index = 100
    else:
        number_hackatons_index = 0

    #Calcul percentatge edat

    edat = compare_age(user1.age, user2.age)

    if(edat):
        edat_index = 100
    else:
        edat_index = 0

    important = challenges_index*0.25 + languages_index*0.17 + disp_index*0.15 + rol_index*0.13
    intermig = exp_level_index*0.10 + anys_estudiats_index*0.10
    baix = group_size_index*0.04 + number_hackatons_index*0.03 + edat_index*0.03

    quoeficient = important + intermig + baix

    return quoeficient

#PRE: Dos usuaris
#POST: Totes les dades coincidents
def compareUsers(user1, user2):
    result = {}
    coin_challenges = challenges(user1.challenges, user2.challenges)
    coin_languages = compare_availability(user1.preferred_languages, user2.preferred_languages)
    coin_availability = compare_availability(user1.availability, user2.availability)
    coin_role = compare_prefered_role(user1.preferred_role, user2.preferred_role)
    coin_exp_level = compare_exp_level(user1.experience_level, user2.experience_level)
    coin_skills = compare_programming_skills(user1.programming_skills, user2.programming_skills)
    coin_studies = compare_years_study(user1.year_of_study, user2.year_of_study)
    coin_team_size = compare_team_size(user1.preferred_team_size, user2.preferred_team_size)
    coin_prev_hack = compare_prev_hack(user1.hackatons_done, user2.hackatons_done)
    coin_age = compare_age(user1.age, user2.age)
    result["challenges"] = coin_challenges
    result["languages"] = coin_languages
    result["availability"] = coin_availability
    result["role"] = coin_role
    result["experience_level"] = coin_exp_level
    result["skills"] = coin_skills
    result["studies"] = coin_studies
    result["team_size"] = coin_team_size
    result["previous_hackathons"] = coin_prev_hack
    result["age"] = coin_age

    return result

#compareUsers(participants[x], participants[y])