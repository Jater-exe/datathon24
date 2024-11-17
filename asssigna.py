import json
from participant import load_participants
from merge.grup import load_groups 
from merge.constructor_grup import constructor_group
from merge.merger import participant_to_dict, grup_to_dict




data_load_part = load_participants('data/datathon_participants.json')
data_load_group = load_groups('data/datathon_groups.json')

with open('data/datathon_participants.json', 'r') as file:
    data_part = json.load(file)
with open('data/datathon_groups.json', 'r') as file:
    data_groups = json.load(file)





for obj in data_load_part:
    if obj.preferred_team_size > 1:
        new_group = constructor_group([obj.id], 1, False)
    else:
        new_group = constructor_group([obj.id], 1, True)
    data_load_group.append(new_group)
    obj.group_size = new_group.group_size
    obj.group_UID = new_group.id
    obj.group_name = new_group.group_name

final_part = participant_to_dict(data_load_part)
final_group = grup_to_dict(data_groups)

with open('datathon_participants.json', 'w') as file:
    json.dump(final_part, file, indent=4)
with open('datathon_groups.json', 'w') as file:
    json.dump(final_group, file, indent=4) 