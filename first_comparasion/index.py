from first_comparasion import compare_languages, compare_availability, compare_prefered_role, compare_programming_skills, compare_age, compare_years_study, compare_datathons, compare_exp_level, compare_challenge, compare_group_size

def quoeficient(user1, user2):

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
