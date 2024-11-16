#PRE: dues variables int, del curs actual dels usuaris 1 i 2
#POST: booleà que retorna la compatibilitat

def compare_years_study(years_of_study_1, years_of_study_2):
    if years_of_study_1 == years_of_study_2:
        return True
    else:
        if years_of_study_1 == "1st Year" and years_of_study_2 == "2nd Year":
            return True
        elif years_of_study_1 == "2nd Year" and (years_of_study_2 == "1st Year" or years_of_study_2 == "3rd Year"):
            return True
        elif years_of_study_1 == "3rd Year" and (years_of_study_2 == "2nd Year" or years_of_study_2 == "4th Year"):
            return True
        elif years_of_study_1 == "4th Year" and years_of_study_2 == "3rd Year":
            return True
        elif (years_of_study_1 == "Master's" or years_of_study_1 == "PhD") and (years_of_study_2 == "Master's" or years_of_study_2 == "PhD"):
            return True
        else:
            return False