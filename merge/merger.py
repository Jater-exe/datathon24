from participant import load_participants

#PRE: Dos grups prèviament definits
#POST: Una llista de paràmetres per a constructor_group

data_path = "data/datathon_participants.json"
participants = load_participants(data_path)

def find_member(UUID):
    counter = 0
    for element in participants:
        if element.id == UUID:
            return counter
        counter += 1

def update_groups(group1, group2):
    #size group1
    group1.group_size += group2.group_size
    #members group1
    for member in group2.group_members:
        group1.group_members.append(member)
    #users group1
    for user in group1.group_members:
        UUID = user
        user_position = find_member(UUID)
        participants[user_position].group_size = group1.group_size
        if participants[user_position].preferred_team_size == group1.group_size:
            group1.full_group = True
    #users group2
    for user in group2.group_members:
        UUID = user
        user_position = find_member(UUID)
        participants[user_position].group_size = group1.group_size
        participants[user_position].group_UID = group1.id

        

def merge(group1, group2):
    user_position1 = find_member(group1.group_members[0])
    preferred_members1 = participants[user_position1].preferred_team_size
    actual_members1 = len(group1.group_members)

    user_position2 = find_member(group2.group_members[0])
    preferred_members2 = participants[user_position2].preferred_team_size
    actual_members2 = len(group2.group_members)
    if preferred_members1 == preferred_members2 and (actual_members1 + actual_members2 <= preferred_members1):
        update_groups(group1, group2)