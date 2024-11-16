#PRE: dues llistes de llenguatges
#POST: llista dels idiomes coincidents
def compare_languages(list1, list2):
    result = []
    for language1 in list1:
        for language2 in list2:
            if (language1 == language2 and language1 not in result):
                result.append(language1)
    return result 