from participant import load_participants
from rich import print
import first_comparasion as f1
from merge import find_member, merge, update_groups, constructor_group, load_groups
import json

data_path_part = "data/datathon_participants.json"
participants = load_participants(data_path_part)

data_path_group = "data/datathon_groups.json"

# Intentar llegir les dades dels grups de manera segura
try:
    with open(data_path_group, 'r') as file:
        grups = json.load(file)
except (json.JSONDecodeError, FileNotFoundError):
    grups = []  # Si el fitxer és buit o no existeix, crear una llista buida

# Realitzar les operacions necessàries
grup_solo1 = grups[0] if len(grups) > 0 else None
grup_solo2 = grups[1] if len(grups) > 1 else None

if grup_solo1 and grup_solo2:
    merge(grup_solo1, grup_solo2, participants)

# Comprovar l'estat de les dades abans de guardar-les
print("Grups abans de guardar:", grups)
print("Participants abans de guardar:", participants)

# Guardar les dades al fitxer JSON només si no estan buides
if grups:
    with open(data_path_group, 'w') as file:
        json.dump(grups, file, indent=4)
else:
    print("Warning: No groups to save.")

if participants:
    with open(data_path_part, 'w') as file:
        json.dump(participants, file, indent=4)
else:
    print("Warning: No participants to save.")