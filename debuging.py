from participant import load_participants
from rich import print
import first_comparasion as f1
from merge import find_member, merge, update_groups, constructor_group, load_groups

data_path = "data/datathon_participants.json"
participants = load_participants(data_path)

data_path = "data/datathon_groups.json"
grups = load_groups(data_path)


grup_solo1 = grups[3]
grup_solo2 = grups[4]

merge(grup_solo1, grup_solo2)
