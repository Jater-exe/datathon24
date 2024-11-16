#pre: edats de dos usuaris
#post: retorna true si les edats son semblants, per tant adients per formar grup

def compare_age(user1_age, user2_age):
    age1 = user1_age
    age2 = user2_age
    if age1 > 25 and age2 > 25:
        return True
    elif age1 > 21 and age2 > 21:
        return abs(age1 - age2) <= 4
    else:
        return abs(age1 - age2) <= 3