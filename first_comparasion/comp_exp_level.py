def compare_exp_level(interest):

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