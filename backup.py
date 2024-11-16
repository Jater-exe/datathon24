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
    elif(preferedrole1==preferedrole2): 
        return "Coincideixen en rol"
    else:
        return "No coincideixen en rol"
    
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
def compare_age(user1_age, user2_age):
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



def compareUsers(user1, user2):



def index(user1, user2, challenges, languages, disp, rol, exp_level, studied_years, team_size, hackatons_prev, edat):

    #Calcul percentatge challenges

    #Calcul percentatge languages
    languages = compare_languages(user1.preferred_languages, user2.preferred_languages)
    
    if(len(languages)>1):
        languages_index = 100
    elif(len(languages)==1):
        languages_index = 50
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



    #Calcul percentatge anys estudiats

    anys_estudiats = compare_years_study(user1.year_of_study, user2.year_of_study)

    if(anys_estudiats):
        anys_estudiats_index=100
    else:
        anys_estudiats_index=0

    #Calcul percentatge mesura equip

    #Calcul percentatge hackatons previes

    #Calcul percentatge edat

    edat = compare_age(user1.age, user2.age)

    if(edat):
        edat_index = 100
    else:
        edat_index = 0

    




    


compareUsers(participants[x], participants[y])