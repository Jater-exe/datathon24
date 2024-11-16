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
    
def compare_age()

def compare_years_study()
    
#COSTA___^^^^

def compareUsers(user1, user2):
    

compareUsers(participants[x], participants[y])