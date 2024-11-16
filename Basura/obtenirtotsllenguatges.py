from participant import load_participants

data_path = "data/datathon_participants.json"
participants = load_participants(data_path)

conjunt_final = []

for persona in participants:
    skills_persona = list(persona.programming_skills.keys())

        # Si conjunt_final está vacío, inicialízalo con skills_persona
    for language in skills_persona:
        if language not in conjunt_final:
            conjunt_final.append(language)


print(conjunt_final)

