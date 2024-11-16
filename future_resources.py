def compare_exp_level_group(interest):

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