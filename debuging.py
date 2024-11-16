from participant import load_participants
from rich import print
import first_comparasion as f1

data_path = "data/datathon_participants.json"
participants = load_participants(data_path)

max = 0
above70 = 0
above50 = 0
above30 = 0
above0 = 0



for i in range(0,325):
    for j in range(0,325):
        actual = f1.quoeficient(participants[i], participants[j])

        if(actual > max):
            max = actual
            UUID1 = participants[i].id
            UUID2 = participants[j].id


        if(actual > 70):
            above70 += 1
        if(actual > 50 and actual < 70):
            above50 += 1
        if(actual > 30 and actual < 50):
            above30 += 1
        if(actual < 30):
            above0 += 1

print(max, "sobre 70:", above70, "entre 50 i 70:", above50, "entre 30 i 50", above30, "inferior:", above0, UUID1, UUID2)