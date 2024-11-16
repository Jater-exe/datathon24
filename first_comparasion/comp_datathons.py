#pre: dos usuaris de la base de dades
#post: true si els dos usuaris han participat en un nombre semblant de datathons +-1

def compare_datathons(hack1, hack2):
    
    # Comprova que la diferencia maxima de datathon es com a molt 1
    return abs(hack1 - hack2) <= 1    
