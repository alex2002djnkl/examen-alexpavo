# =============================================================================
# Nom:      ??????
# Descripció: ??????
# ===== Dades d'entrada =====
# @param:   ?????? de tipus ??????
#       ??????
# ===== Dades a tornar  =====
# @return:  ?????? de tipus ??????
#       ??????


# Aquesta linea defineix la funcio amb els parametres demanarCaracter y missatgeError    
def llegirUnCaracter(demanarCaracter,missatgeError):

     # demanarCaracter es igual a str    
    demanarCaracter = str
     # missatge de error es igual a Error   
    missatgeError = "Error"
     # demana que entris un caracter
    print("Entra un caracter siusplau:")
     # si demanarCaracter es igual a str print Molt Bona Paraula!
    if demanarCaracter == str:

        print ("Molt bona paraula!")
    # si no, Error
    
    else:
       
       print (missatgeError)
# =============================================================================
    


# =============================================================================
# Nom:      ??????
# Descripció: ??????
# ===== Dades d'entrada =====
# @param:   ?????? de tipus ??????
#       ??????
# ===== Dades a tornar  =====
# @return:  ?????? de tipus ??????
#       ??????

# definim la funció, amb parametre demanar nom y missatge error 
def llegirDecimal(demanarNombre, missatgeError):

    # missatge es igual a float 
    missatgeError = float 
    # fem un bucle per a que nombre decimal que es float retorni el numero decimal, hi ha un except per a posibles errors
    while True:
        try:
            nombredecimal = float(input(demanarNombre))
            return nombredecimal
        except ValueError:
            print(missatgeError)

# Exemple per utiliztar


demanar = "Introdueix un nombre decimal: "
error = "Error. Si us plau, introdueix un nombre decimal vàlid."
decimal = llegirDecimal(demanar, error)
print(f"Has introduït el nombre decimal: {decimal}")








