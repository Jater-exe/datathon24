import json
import pathlib
import uuid
from participant import load_participants
import participant
from first_comparasion import compare_languages, compare_availability, compare_prefered_role, compare_programming_skills, compare_age, compare_years_study, compare_datathons, compare_exp_level, compare_challenge, compare_group_size

data_path = "data/datathon_participants.json"
participants = load_participants(data_path)

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