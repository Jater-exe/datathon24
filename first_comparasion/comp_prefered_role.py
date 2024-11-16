#PRE: dues cadenes seleccionades entre Literal["Analysis", "Visualization", "Development", "Design", "Don't know", "Don't care"]
#POST: un dels usuaris no li importa la seva funcio o dos coincideixen
def compare_prefered_role(preferedrole1: str, preferedrole2: str):

    if(preferedrole1=="Don't know" or preferedrole2=="Don't know" or preferedrole1=="Don't care" or preferedrole2=="Don't care"):
        return "One user doesn't care"
    elif(preferedrole1==preferedrole2): 
        return "Coincideixen en rol"
    else:
        return "No coincideixen en rol"