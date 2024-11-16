import json
import uuid
import grup


def constructor_group(group_members, group_size, full_group):

    with open("datathon_groups.json", 'r') as file:
        data = json.load(file)

    data.append({"id":uuid.UUID, "group_size":group_size, "group_members":group_members, "full_group": full_group})

    with open("datathon_groups.json", 'w') as file:
        json.dump(data, file, indent=4)
