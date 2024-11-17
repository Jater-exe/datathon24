from participant import load_participants
from rich import print
import first_comparasion as f1
from merge import find_member, merge, update_groups, constructor_group, load_groups
import json

data_path_part = "data/datathon_participants.json"
participants = load_participants(data_path_part)

data_path_group = "data/datathon_groups.json"
grups = load_groups(data_path_group)

#constructor_group(["97a555b7-99a5-4a5e-8f47-631d5507e25a", "e3464b47-0c0a-41d7-9750-a21adb889205"], 2, False)
#constructor_group(["14cf6a5f-7e48-49c8-9e59-522fe1178ad8", "359f324b-b3ec-4770-8a60-86493503fee4"], 2, False)


grup_solo1 = grups[0]
grup_solo2 = grups[1]

merge(grup_solo1, grup_solo2, participants)

for element in grups:
    print(element)

with open(data_path_group, 'w') as file:
    json.dump(grups, file, indent=4)

with open(data_path_part, 'w') as file:
    json.dump(participants, file, indent=4)