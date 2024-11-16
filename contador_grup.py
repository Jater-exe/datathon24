import json

def constructor_group(group_members, group_size, full_group):
    try:
        # Lee el archivo JSON existente
        with open("data/datathon_groups.json", 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # Si el archivo no existe o está vacío, inicializa con una lista vacía
        data = []

    # Determina el próximo ID
    if data:  # Si ya hay datos en el archivo
        next_id = max(group.get("id", 0) for group in data) + 1
    else:  # Si no hay datos, empieza desde 1
        next_id = 1

    # Añade el nuevo grupo con el ID incremental
    data.append({
        "id": next_id,
        "group_size": group_size,
        "group_members": group_members,
        "full_group": full_group
    })

    # Guarda los datos actualizados en el archivo
    with open("data/datathon_groups.json", 'w') as file:
        json.dump(data, file, indent=4)


# Ejemplo de uso:
constructor_group(["member1", "member2"], 2, False)



#####################################################
import json
import uuid


def constructor_group(group_members, group_size, full_group):

    with open("data/datathon_groups.json", 'r') as file:
        data = json.load(file)

    data.append({"id":uuid.UUID, "group_size":group_size, "group_members":group_members, "full_group": full_group})

    with open("data/datathon_groups.json", 'w') as file:
        json.dump(data, file, indent=4)
