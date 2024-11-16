#PRE: Dues cadenes que representen els nivells Beginner, Intermediate o Advanced
#POST: Un booleà si coincideixen (amb tolerància)
def compare_exp_level(exp1, exp2):
    if exp1 == exp2:
        return True
    elif exp1 == "Beginner" and exp2 == "Intermediate":
        return True 
    elif exp1 == "Intermediate" and exp2 == "Beginner":
        return True
    elif exp1 == "Advanced" and exp2 == "Beginner":
        return True
    else:
        return False