import json
#PRE: Dos grups prèviament definits
#POST: Una llista de paràmetres per a constructor_group

def find_member(UUID, participants):
    counter = 0
    for element in participants:
        if element.id == UUID:
            return counter
        counter += 1

def grup_to_dict(grup):
    return {
        "id": grup.id,
        "group_size": grup.group_size,
        "group_members": grup.group_members,
        "full_group": grup.full_group,
        "group_name": grup.group_name
    }
def participant_to_dict(participant):
    return {
        "id": participant.id,
        "name": participant.name,
        "email": participant.email,
        "age": participant.age,
        "year_of_study": participant.year_of_study,
        "shirt_size": participant.shirt_size,
        "university": participant.university,
        "dietary_restrictions": participant.dietary_restrictions,
        "interests": participant.interests,
        "preferred_role": participant.preferred_role,
        "experience_level": participant.experience_level,
        "hackathons_done": participant.hackathons_done,
        "objective": participant.objective,
        "introduction": participant.introduction,
        "technical_project": participant.technical_project,
        "future_excitement": participant.future_excitement,
        "fun_fact": participant.fun_fact,
        "preferred_languages": participant.preferred_languages,
        "friend_registration": participant.friend_registration,
        "preferred_team_size": participant.preferred_team_size,
        "availability": participant.availability,
        "programming_skills": participant.programming_skills,
        "interest_in_challenges": participant.interest_in_challenges,
        "group_size": participant.group_size,
        "group_UID": participant.group_UID,
        "group_name": participant.group_name
    }


def update_groups(group1, group2, participants, groups):
    #size group1
    group1.group_size += group2.group_size
    #members group1
    for member in group2.group_members:
        group1.group_members.append(member)
    #users group1
    for user in group1.group_members:
        UUID = user
        user_position = find_member(UUID, participants)
        participants[user_position].group_size = group1.group_size
        participants[user_position].group_UID = group1.id
        if participants[user_position].preferred_team_size == group1.group_size:
            group1.full_group = True
    #users group2
    for user in group2.group_members:
        UUID = user
        user_position = find_member(UUID, participants)
        participants[user_position].group_size = group1.group_size
        participants[user_position].group_UID = group1.id
    #guardar progrés
    groups_dict = []
    for element in groups:
        groups_dict.append(grup_to_dict(element))
    groups_dict.append(grup_to_dict(group1))
    groups_dict.append(grup_to_dict(group2))
    with open("data/datathon_groups.json", 'w') as file:
            json.dump(groups_dict, file, indent=4)
    participants_dict = []
    for person in participants:
        participants_dict.append(participant_to_dict(person))
    for user in group1.group_members:
        user_position = find_member(user, participants)
        participants_dict.append(participant_to_dict(participants[user_position]))
    with open("data/datathon_participants.json", 'w') as file:
        json.dump(participants_dict, file, indent=4)

        

def merge(group1, group2, participants, groups):
    user_position1 = find_member(group1.group_members[0], participants)
    preferred_members1 = participants[user_position1].preferred_team_size
    actual_members1 = len(group1.group_members)

    user_position2 = find_member(group2.group_members[0], participants)
    preferred_members2 = participants[user_position2].preferred_team_size
    actual_members2 = len(group2.group_members)
    if preferred_members1 == preferred_members2 and (actual_members1 + actual_members2 <= preferred_members1):
        update_groups(group1, group2, participants, groups)