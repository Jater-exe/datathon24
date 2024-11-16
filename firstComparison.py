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


#pre: entrada d'usuaris dels quals desconeixem la pertinença a un grup
#post: true si s'aconsegueix agrupar l'usuari, false en cas contrari

def assign_user_to_group(user, users_data, groups):
  
    user_interests = set(user['interests'])
    
    # Try to assign the user to an existing group
    for group in groups:
        # Check if any user in the current group shares an interest with the new user
        for member in group:
            member_interests = set(users_data[member]['interests'])
            if user_interests.intersection(member_interests):
                if len(group) < 2:  # Ensure the group size does not exceed 2
                    group.append(user['name'])
                    return True
    
    # If no suitable group was found, create a new one if possible
    if len(groups) < len(users_data) // 2:
        groups.append([user['name']])
        return True
    
    return False

#pre: dos usuaris de la base de dades
#post: true si els dos usuaris han participat en un nombre semblant de datathons +-1

def have_similar_datathons(user1, user2, datathon_data):
    
    # Obte el nombre de datathons en que ha participat cada usuari 
    datathons_user1 = datathon_data[user1]
    datathons_user2 = datathon_data[user2]
    
    # Comprova que la diferencia maxima de datathon es com a molt 1
    return abs(datathons_user1 - datathons_user2) <= 1    


def group_by_expertise(users_data, team_size=2):

    # Inicialitza diccionaris que agrupen els usuaris per nivell d'expertesa 
    grouped_teams = {
        'beginner': [],
        'intermediate': [],
        'expert': []
    }
    
    # Grups temporals
    temp_groups = {
        'beginner': [],
        'intermediate': [],
        'expert': []
    }
    
    # Itera sobre els usuaris del dataset per assignar-li a cadascu a cada grup temporal 
    for user, expertise in users_data.items():
        if expertise in temp_groups:
            temp_groups[expertise].append(user)
            
            # Si el grup temporal assoleix les 2 persones, crea un grup
            if len(temp_groups[expertise]) == team_size:
                grouped_teams[expertise].append(temp_groups[expertise])
                temp_groups[expertise] = []  # Reset the temporary group for the next team
    
    # Per a usuaris restants en cas que el nombre total no sigui un multiple de 4
    for expertise, remaining_users in temp_groups.items():
        if remaining_users:
            grouped_teams[expertise].append(remaining_users)
    
    return grouped_teams


def group_by_challenge_interests(users_data):

    grouped_pairs = []
    ungrouped_users = []
    used_users = set()

    # Itera per el dataset per trobar parelles 
    for i, user1 in enumerate(users_data):
        if user1['name'] in used_users:
            continue
        
        # Intentar trobar coincidencia per user1
        found_pair = False
        for j, user2 in enumerate(users_data):
            if i == j or user2['name'] in used_users:
                continue
            
            # Comprova que hi hagi alguna coincidencia als interessos
            if set(user1['interests']).intersection(set(user2['interests'])):
                grouped_pairs.append([user1['name'], user2['name']])
                used_users.add(user1['name'])
                used_users.add(user2['name'])
                found_pair = True
                break
        
        # Si no es troba parella, marcar l'usuari com a sense grup 
        if not found_pair:
            ungrouped_users.append(user1['name'])

    return grouped_pairs, ungrouped_users

#COSTA___^^^^

def compareUsers(user1, user2):
    

compareUsers(participants[x], participants[y])