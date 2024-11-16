def compare_group_size(group1, group2):
    if(group1==group2):
        return "Coincideixen en grup"
    elif(abs(group1-group2)==1):
        return "Diferencia de 1"
    elif(abs(group1-group2)==2):
        return "Diferencia de 2"
    elif(abs(group1-group2)==3 or abs(group1-group2)==4):
        return "Una persona vol anar sola"
