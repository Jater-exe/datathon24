import json

with open('datathon_participants.json', 'r') as file:
    data = json.load(file)

for obj in data:
    obj['group_size'] = 1
    obj['group_UID'] = "none"
    obj['group_name'] = "none"
with open('datathon_participants.json', 'w') as file:
    json.dump(data, file, indent=4)