#PRE: Dues llistes de strings
#POST: Una llista de strings

def compare_challenge(list1, list2):
    result = []
    for challenge1 in list1:
        for challenge2 in list2:
            if challenge1 == challenge2 and challenge1 not in result:
                result.append(challenge1)
    return result

