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
    
def compare_programming_skills(dict1, dict2, preferedrole1, preferedrole2):

    conjunt_user1 = set(dict1.keys()) #Guardem unicament claus del diccionari de user1 (es a dir, nomes els llenguatges q sap) 
    conjunt_user2 = set(dict2.keys()) #Rt

    shared_languages = conjunt_user1 & conjunt_user2
    unique_languages1 = conjunt_user1 - shared_languages
    unique_languages2 = conjunt_user2 - shared_languages

    # Analysis
    analysis_skills = ["Data Analysis", "Machine Learning", "TensorFlow", "PyTorch", "Natural Language Processing", "Computer Vision", "SQL", "PostgreSQL", "MongoDB", "AWS/Azure/GCP", "IoT", "Blockchain", "Rust", "Python", "Java", "C", "C++", "Go", "Data", "nlp"]

    # Visualization
    visualization_skills = ["Data Visualization", "Figma", "HTML/CSS", "JavaScript", "React", "TypeScript", "GitHub", "css"]

    # Development
    development_skills = ["Flask", "React Native", "iOS Development", "Android Development", "Flutter", "Docker", "Git", "JavaScript", "TypeScript", "Rust", "C", "C++", "Java", "Go", "PostgreSQL", "MongoDB", "python", "react", "android", "ios", "java script"]

    # Design
    design_skills = ["UI/UX Design", "Figma", "Design", "HTML/CSS", "JavaScript", "React", "Flutter", "UI/UX", "ioI/UX", "design"]

    #MITJANA EN FUNCIO DEL ROL
    # Función para calcular la media según el rol
    def calculate_average(dict_skills, role):
        if role == "Analysis":
            relevant_skills = analysis_skills
        elif role == "Visualization":
            relevant_skills = visualization_skills
        elif role == "Development":
            relevant_skills = development_skills
        elif role == "Design":
            relevant_skills = design_skills
        else:  # Para "Don't know" o "Don't care"
            relevant_skills = set(analysis_skills + visualization_skills + development_skills + design_skills)

        # Filtrar habilidades relevantes del participante
        relevant_user_skills = set(dict_skills.keys()) & set(relevant_skills) #Nomes es queden les repetides, pel que nomes es queden les que te cada user

        # Calcular la media
        if relevant_user_skills:  # Si hay habilidades relevantes
            total_level = sum(dict_skills[skill] for skill in relevant_user_skills)
            return total_level / len(relevant_user_skills)
        else:  # Si no hay habilidades relevantes
            return 0

    # Calcular la media para cada participante
    mitjana1 = calculate_average(dict1, preferedrole1)
    mitjana2 = calculate_average(dict2, preferedrole2)

    list_result = [shared_languages, unique_languages1, unique_languages2, mitjana1, mitjana2]



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
def compare_years_study(years_of_study_1, years_of_study_2):
    if years_of_study_1 == years_of_study_2:
        return True
    else:
        if years_of_study_1 == "1st Year" and years_of_study_2 == "2nd Year":
            return True
        elif years_of_study_1 == "2nd Year" and (years_of_study_2 == "1st Year" or years_of_study_2 == "3rd Year"):
            return True
        elif years_of_study_1 == "3rd Year" and (years_of_study_2 == "2nd Year" or years_of_study_2 == "4th Year"):
            return True
        elif years_of_study_1 == "4th Year" and years_of_study_2 == "3rd Year":
            return True
        elif (years_of_study_1 == "Master's" or years_of_study_1 == "PhD") and (years_of_study_2 == "Master's" or years_of_study_2 == "PhD"):
            return True
        else:
            return False

#pre: dos usuaris de la base de dades
#post: true si els dos usuaris han participat en un nombre semblant de datathons +-1

def have_similar_datathons(hack1, hack2, datathon_data):
    
    # Obte el nombre de datathons en que ha participat cada usuari 
    datathons_user1 = datathon_data[hack1]
    datathons_user2 = datathon_data[hack2]
    
    # Comprova que la diferencia maxima de datathon es com a molt 1
    return abs(datathons_user1 - datathons_user2) <= 1    

#pre: usuaris de la base de dades
#post: agrupacio d'usuaris per nivell d'expertesa
def group_by_expertise(expertise, team_size=2):

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
    for user, expertise in expertise.items():
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


def group_by_challenge_interests(interest):

    grouped_pairs = []
    ungrouped_users = []
    used_users = set()

    # Itera per el dataset per trobar parelles 
    for i, user1 in enumerate(interest):
        if user1['name'] in used_users:
            continue
        
        # Intentar trobar coincidencia per user1
        found_pair = False
        for j, user2 in enumerate(interest):
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

#PRE: Dos usuaris
#POST: Totes les dades coincidents
def compareUsers(user1, user2):
    result = {}
    coin_challenges = challenges(user1.challenges, user2.challenges)
    coin_languages = compare_availability(user1.preferred_languages, user2.preferred_languages)
    coin_availability = compare_availability(user1.availability, user2.availability)
    coin_role = compare_prefered_role(user1.preferred_role, user2.preferred_role)
    coin_exp_level = compare_exp_lvl(user1.experience_level, user2.experience_level)
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

compareUsers(participants[x], participants[y])