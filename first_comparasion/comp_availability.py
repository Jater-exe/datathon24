#PRE: dos diccionaris de tipus str:bool
#POST: una llista de strings
def compare_availability(dict1, dict2):
    result = []
    keys = list(dict1.keys())
    i = 0
    while i < len(dict1):
        if dict1[keys[i]] and dict2[keys[i]]:
            result.append(keys[i])
        i += 1
    return result