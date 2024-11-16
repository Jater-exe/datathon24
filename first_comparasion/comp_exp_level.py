#PRE: Dues cadenes que representen els nivells Beginner, Intermediate o Advanced
#POST: Un booleà si coincideixen (amb tolerància)
def compare_exp_level(exp1, exp2):
    if exp1 == "Beginner" and exp2 == "Advanced":
        return False 
    else:
        return True