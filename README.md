# examen-alexpavo

# Examen, divendres, 23 de febrer de 2024

### MP03: Programació - UF02: Disseny modular
### 2n examen 2a avaluació

## Primera part

Teniu **fins les 15:50** per escollir quins dels següents enunciats escollireu per desenvolupar durant la segona part de l'examen.

No cal que desenvolupeu res, es tracta **només** de valorar quins enunciats fareu. La idea és que com que ja sabeu que se us demana a cada cas, ja podeu intuir que és el que fareu per desenvolupar cada funció, amb els coneixements que teniu.

## Taula de puntuacions

|Nom de la funció|Puntuació<br>Codi|Puntuació<br>Comentaris|Puntuació<br>TOTAL|
|----|:----:|:----:|:----:|
|[**`llegirUnCaracter`**](#funció-llegiruncaracter)|`0,50` punts|`0,50` punts|**`1,0` punt**|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**`demanaSiONo`**](#funció-demanaSiONo)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;depèn de **`llegirUnCaracter`**|`0,50` punts|`0,50` punts|**`1,0` punt**|
|&nbsp;|&nbsp;|&nbsp;|&nbsp;|
|[**`llegirDecimal`**](#funció-llegirDecimal)|`0,50` punt|`0,50` punts|**`1,0` punt**|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**`llegirDecimalPositiu`**](#funció-llegirDecimalPositiu)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;depèn de **`llegirDecimal`**|`0,50` punts|`0,50` punts|**`1,0` punt**|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**`llegirDecimalInterval`**](#funció-llegirDecimalInterval)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;depèn de **`llegirDecimal`**|`0,50` punts|`0,50` punts|**`1,0` punt**|
|&nbsp;|&nbsp;|&nbsp;|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**`llegirVectorDEnters`**](#funció-llegirVectorDEnters)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;depèn de **`llegirEnterPositiu`**<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;facilitada pel professor|`0,50` punt|`0,50` punts|**`1,0` punt**|
|&nbsp;|&nbsp;|&nbsp;|
|[**`mostraVectorEnFila`**](#funció-mostraVectorAmbSeparador)|`1,00` punt|`0,50` punts|**`1,5` punts**|
|[**`mostraVectorAmbSeparador`**](#funció-mostraVectorAmbSeparador)|`1,00` punt|`0,50` punts|**`1,5` punts**|
|[**`Programa principal`**](#programa-principal)<br>per provar TOT el que has fet!|`0,75` punts|`0,25` punts|**`1,0` punt**|

[Funcions facilitades pel professor](#funcions-facilitades-pel-professor)

# EJERCICIS EXAMEN

## Intentaré fer-ho tot.

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
<hr>

## Funció **`llegirUnCaracter`**

Funció per llegir un sol caràcter.

1. La funció mostrarà el text rebut a la variable **`demanarCaracter`**, per demanar a l'usuari que entri un sol caràcter.

1. En el cas en que l'usuari entri alguna cosa que no sigui **només un caràcter**, es mostrarà el text d'**Error**, rebut a la variable **`missatgeError`**.

### Detalls de la funció

|Nom de la funció|Paràmetres rebuts|Paràmetres a retornar|
|----|----|----|
|**`llegirUnCaracter`**|**`demanarCaracter`** de tipus **cadena**<br>**`missatgeError`** de tipus **cadena**|Un **únic caràcter** entrat per l'usuari.|

<hr>

## Funció **`llegirDecimal`**

Funció per llegir un nombre **decimal** entrat per l'usuari.

1. Es mostrarà el text rebut a la variable **`demanarNombre`**, per demanar a l'usuari que entri un decimal.

1. I es mostrarà un text d'**Error**, rebut a la variable **`missatgeError`**, pel cas en que l'usuari entri alguna cosa que no sigui un decimal.

### Detalls de la funció

|Nom de la funció|Paràmetres rebuts|Paràmetres a retornar|
|----|----|----|
|**`llegirDecimal`**|**`demanarNombre`** de tipus **cadena**<br>**`missatgeError`** de tipus **cadena**|Nombre **decimal** entrat per l'usuari.|

<hr>

## Funció **`llegirDecimalPositiu`**

Funció per llegir un nombre **decimal** entrat per l'usuari.

1. Es mostrarà el text rebut a la variable **`demanarNombre`**, per demanar a l'usuari que entri un decimal.

1. Es mostrarà un text d'**Error**, rebut a la variable **`errorNoDecimal`**, pel cas en que l'usuari entri alguna cosa que **no sigui un decimal**.

1. I també, es mostrarà un text d'**Error**, rebut a la variable **`errorNoPositiu`**, pel cas en que l'usuari entri un **decimal que no sigui positiu**.

### Detalls de la funció

|Nom de la funció|Paràmetres rebuts|Paràmetres a retornar|
|----|----|----|
|**`llegirDecimalPositiu`**|**`demanarNombre`** de tipus **cadena**<br>**`errorNoDecimal`** de tipus **cadena**<br>**`errorNoPositiu`** de tipus **cadena**|Nombre **decimal** entrat per l'usuari.|

> ### **NOTA**:  Cal fer servir la funció **`llegirDecimal`**

<hr>

## Funció **`llegirDecimalInterval`**

Funció per llegir un nombre **decimal** entrat per l'usuari i que es troba dins d'un interval de valors limitats per un valor inferior i un valor superior que es rebran com a paràmetres **`limitInferior`** i **`limitSuperior`**, respectivament.

1. Es mostrarà el text rebut a la variable **`demanarNombre`**, per demanar a l'usuari que entri el decimal dins de l'interval.

1. Es mostrarà un text d'**Error**, rebut a la variable **`errorNoDecimal`**, pel cas en que l'usuari entri alguna cosa que **no sigui un decimal**.

1. I també, es mostrarà un text d'**Error**, rebut a la variable **`errorForaInterval`**, pel cas en que l'usuari entri un **decimal que no estigui dins de l'interval** de valors limitats pel valor inferior i pel valor superior. 

1. El valor entrat pot ser igual a qualsevol dels dos limits rebuts.

### Detalls de la funció

|Nom de la funció|Paràmetres rebuts|Paràmetres a retornar|
|----|----|----|
|**`llegirDecimalInterval`**|**`demanarNombre`** de tipus **cadena**<br>**`errorNoDecimal`** de tipus **cadena**<br>**`errorForaInterval`** de tipus **cadena**<br>**`limitInferior`** de tipus **enter**<br>**`limitSuperior`** de tipus **enter**|Nombre **decimal** entrat per l'usuari<br>que es troba dins de l'interval.<br>El valor entrat pot ser igual a limit rebut.|

> ### **NOTA**:  Cal fer servir la funció **`llegirDecimal`**

<hr>

## Funció **`demanaSiONo`**

### Detalls de la funció

Funció que demana a l'usuari que entri un caràcter que només pot ser **`s`** o **`S`** o **`n`** o **`N`**.

1. Es mostrarà el text rebut a la variable **`perDemanarSiONo`**, per demanar a l'usuari que entri un caràcter.

1. Es mostrarà un text d'**Error**, rebut a la variable **`errorNoDecimal`**, pel cas en que l'usuari entri alguna cosa que **no sigui** **`s`** o **`S`** o **`n`** o **`N`**.

|Nom de la funció|Paràmetres rebuts|Paràmetres a retornar|
|----|----|----|
|**`demanaSiONo`**|**`perDemanarSiONo`** de tipus **cadena**<br>**`missatgeError`** de tipus **cadena**|Caràcter entrat per l'usuari i<br>que només pot ser **`s`** o **`S`** o **`n`** o **`N`**.|

> ### **NOTA**:  Cal fer servir la funció **`llegirUnCaracter`**

<hr>

## Funció **`llegirVectorDEnters`**

### Detalls de la funció

Funció que demanarà a l'usuari els enters per omplir un vector d'enters. La mida del vector la rebrà amb el paràmetre **`midaVector`**. Farà servir la funció feta a classe i que proporcionarà el professor **`llegirEnterPositiu`**.

|Nom de la funció|Paràmetres rebuts|Paràmetres a retornar|
|----|----|----|
|**`llegirVectorDEnters`**|**`midaVector`** de tipus **enter**<br>**`demanaElement`** de tipus **cadena**|El vector que conté tots els elements demanats a l'usuari.|

> ### **NOTA**:  Cal fer servir la funció **`llegirEnterPositiu`**

<hr>

## Funció **`mostraVectorEnFila`**

### Detalls de la funció

Funció per mostrar per pantalla el vector rebut en una única línia i separat pel caràcter rebut com **`caracterSeparador`**.

|Nom de la funció|Paràmetres rebuts|Paràmetres a retornar|
|----|----|----|
|**`mostraVectorEnFila`**|**`vectorAMostrar`** de tipus **vector**|**Res**|

<hr>

## Funció **`mostraVectorAmbSeparador`**

### Detalls de la funció

Funció per mostrar per pantalla el vector rebut en una única línia i separat pel caràcter rebut com **`caracterSeparador`**.

|Nom de la funció|Paràmetres rebuts|Paràmetres a retornar|
|----|----|----|
|**`mostraVectorAmbSeparador`**|**`vectorAMostrar`** de tipus **vector**<br>**`caracterSeparador`** de tipus **cadena**|**Res**|

<hr>

## Funció **`estaEnElVector`**

### Detalls de la funció

Funció que rep un nombre i un vector de números, i comprova si el número és o no al vector.

|Nom de la funció|Paràmetres rebuts|Paràmetres a retornar|Puntuació|
|----|----|----|----|
|**`estaEnElVector`**|**`nombreRebut`** de tipus **enter**<br>**`vectorRebut`** de tipus **vector**|Retorna un valor lògic (booleà **`True`** o **`False`**)<br>en funció de si el número rebut està dins del vector o no.<br>Retorna **`True`** si el número **està** al vector.<br>Retorna **`False`** si el número **NO està** al vector.|**`0,50` punts**|

<br>
<hr>

## **Programa principal**

Programa per provar totes les funcions que heu fet durant l'examen.


# Funcions facilitades pel professor

## Funció **`llegirEnter`**

### Detalls de la funció

Funció per llegir un nombre **enter** entrat per l'usuari.

1. Es mostrarà el text rebut a la variable **`demanarEnterPositiu`**, per demanar a l'usuari que entri un **enter positiu**.

1. Es mostrarà un text d'**Error**, rebut a la variable **`errorNoEnter`**, en el cas en que l'usuari entri alguna cosa que **no sigui un enter**.

1. I també, es mostrarà un text d'**Error**, rebut a la variable **`errorNoPositiu`**, en el cas en que l'usuari entri un **enter que no sigui positiu**.

|Nom de la funció|Paràmetres rebuts|Paràmetres a retornar|
|----|----|----|
|**`llegirEnterPositiu`**|**`demanarEnterPositiu`** de tipus **cadena**<br>**`demanaElement`** de tipus **cadena**|Enter positiu entrat per l'usuari.|

## Funció **`llegirEnterPositiu`**

### Detalls de la funció

Funció per llegir un nombre **enter positiu** entrat per l'usuari.

1. Es mostrarà el text rebut a la variable **`demanarEnterPositiu`**, per demanar a l'usuari que entri un **enter positiu**.

1. Es mostrarà un text d'**Error**, rebut a la variable **`errorNoEnter`**, en el cas en que l'usuari entri alguna cosa que **no és un enter**.

1. I també, es mostrarà un text d'**Error**, rebut a la variable **`errorNoPositiu`**, en el cas en que l'usuari entri un **enter que no és positiu**.

|Nom de la funció|Paràmetres rebuts|Paràmetres a retornar|
|----|----|----|
|**`llegirEnterPositiu`**|**`demanarEnterPositiu`** de tipus **cadena**<br>**`demanaElement`** de tipus **cadena**|Enter positiu entrat per l'usuari.|




# Examen, divendres, 23 de febrer de 2024

### MP03: Programació - UF02: Disseny modular
### 2n examen 2a avaluació

## Segona part

Teniu **1** hora i **30 minuts** per desenvolupar les funcions escollides a la primera part.

## Taula de puntuacions

|Nom de la funció|Puntuació<br>Codi|Puntuació<br>Comentaris|Puntuació<br>TOTAL|
|----|:----:|:----:|:----:|
|[**`llegirUnCaracter`**](#funció-llegiruncaracter)|`0,50` punts|`0,50` punts|**`1,0` punt**|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**`demanaSiONo`**](#funció-demanaSiONo)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;depèn de **`llegirUnCaracter`**|`0,50` punts|`0,50` punts|**`1,0` punt**|
|&nbsp;|&nbsp;|&nbsp;|&nbsp;|
|[**`llegirDecimal`**](#funció-llegirDecimal)|`0,50` punt|`0,50` punts|**`1,0` punt**|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**`llegirDecimalPositiu`**](#funció-llegirDecimalPositiu)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;depèn de **`llegirDecimal`**|`0,50` punts|`0,50` punts|**`1,0` punt**|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**`llegirDecimalInterval`**](#funció-llegirDecimalInterval)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;depèn de **`llegirDecimal`**|`0,50` punts|`0,50` punts|**`1,0` punt**|
|&nbsp;|&nbsp;|&nbsp;|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**`llegirVectorDEnters`**](#funció-llegirVectorDEnters)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;depèn de **`llegirEnterPositiu`**<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;facilitada pel professor|`0,50` punt|`0,50` punts|**`1,0` punt**|
|&nbsp;|&nbsp;|&nbsp;|
|[**`mostraVectorEnFila`**](#funció-mostraVectorAmbSeparador)|`1,00` punt|`0,50` punts|**`1,5` punts**|
|[**`mostraVectorAmbSeparador`**](#funció-mostraVectorAmbSeparador)|`1,00` punt|`0,50` punts|**`1,5` punts**|
|**Programa principal**<br>per provar TOT el que has fet!|`0,75` punts|`0,25` punts|**`1,0` punt**|

[Funcions facilitades pel professor](#funcions-facilitades-pel-professor)

<hr>

## Funció **`llegirUnCaracter`**

Funció per llegir un sol caràcter.

1. La funció mostrarà el text rebut a la variable **`demanarCaracter`**, per demanar a l'usuari que entri un sol caràcter.

1. En el cas en que l'usuari entri alguna cosa que no sigui **només un caràcter**, es mostrarà el text d'**Error**, rebut a la variable **`missatgeError`**.

### Detalls de la funció

|Nom de la funció|Paràmetres rebuts|Paràmetres a retornar|
|----|----|----|
|**`llegirUnCaracter`**|**`demanarCaracter`** de tipus **cadena**<br>**`missatgeError`** de tipus **cadena**|Un **únic caràcter** entrat per l'usuari.|

```python
# =============================================================================
# Nom:      ??????
# Descripció: ??????
# ===== Dades d'entrada =====
# @param:   ?????? de tipus ??????
#       ??????
# ===== Dades a tornar  =====
# @return:  ?????? de tipus ??????
#       ??????
def demanarCaracter(demanarCaracter,missatgeError):
# Definició de variables
# Inicialització de variables
    print(f"Encara no s'ha desenvolupat aquesta funció!")
# =============================================================================
```

<hr>

## Funció **`llegirDecimal`**

Funció per llegir un nombre **decimal** entrat per l'usuari.

1. Es mostrarà el text rebut a la variable **`demanarNombre`**, per demanar a l'usuari que entri un decimal.

1. I es mostrarà un text d'**Error**, rebut a la variable **`missatgeError`**, pel cas en que l'usuari entri alguna cosa que no sigui un decimal.

### Detalls de la funció

|Nom de la funció|Paràmetres rebuts|Paràmetres a retornar|
|----|----|----|
|**`llegirDecimal`**|**`demanarNombre`** de tipus **cadena**<br>**`missatgeError`** de tipus **cadena**|Nombre **decimal** entrat per l'usuari.|

```python
# =============================================================================
# Nom:      ??????
# Descripció: ??????
# ===== Dades d'entrada =====
# @param:   ?????? de tipus ??????
#       ??????
# ===== Dades a tornar  =====
# @return:  ?????? de tipus ??????
#       ??????
def llegirDecimal(demanarNombre,missatgeError):
# Definició de variables
# Inicialització de variables
    print(f"Encara no s'ha desenvolupat aquesta funció!")
# =============================================================================
```

<hr>

## Funció **`llegirDecimalPositiu`**

Funció per llegir un nombre **decimal** entrat per l'usuari.

1. Es mostrarà el text rebut a la variable **`demanarNombre`**, per demanar a l'usuari que entri un decimal.

1. Es mostrarà un text d'**Error**, rebut a la variable **`errorNoDecimal`**, pel cas en que l'usuari entri alguna cosa que **no sigui un decimal**.

1. I també, es mostrarà un text d'**Error**, rebut a la variable **`errorNoPositiu`**, pel cas en que l'usuari entri un **decimal que no sigui positiu**.

### Detalls de la funció

|Nom de la funció|Paràmetres rebuts|Paràmetres a retornar|
|----|----|----|
|**`llegirDecimalPositiu`**|**`demanarNombre`** de tipus **cadena**<br>**`errorNoDecimal`** de tipus **cadena**<br>**`errorNoPositiu`** de tipus **cadena**|Nombre **decimal** entrat per l'usuari.|

> ### **NOTA**:  Cal fer servir la funció **`llegirDecimal`**

```python
# =============================================================================
# Nom:      ??????
# Descripció: ??????
# ===== Dades d'entrada =====
# @param:   ?????? de tipus ??????
#       ??????
# ===== Dades a tornar  =====
# @return:  ?????? de tipus ??????
#       ??????
# 
# NOTA: Fa servir la nostra funció llegirDecimal
#
def llegirDecimalPositiu(demanarNombre,errorNoDecimal,errorNoPositiu):
# Definició de variables
# Inicialització de variables
    print(f"Encara no s'ha desenvolupat aquesta funció!")
# =============================================================================
```

<hr>

## Funció **`llegirDecimalInterval`**

Funció per llegir un nombre **decimal** entrat per l'usuari i que es troba dins d'un interval de valors limitats per un valor inferior i un valor superior que es rebran com a paràmetres **`limitInferior`** i **`limitSuperior`**, respectivament.

1. Es mostrarà el text rebut a la variable **`demanarNombre`**, per demanar a l'usuari que entri el decimal dins de l'interval.

1. Es mostrarà un text d'**Error**, rebut a la variable **`errorNoDecimal`**, pel cas en que l'usuari entri alguna cosa que **no sigui un decimal**.

1. I també, es mostrarà un text d'**Error**, rebut a la variable **`errorForaInterval`**, pel cas en que l'usuari entri un **decimal que no estigui dins de l'interval** de valors limitats pel valor inferior i pel valor superior. 

1. El valor entrat pot ser igual a qualsevol dels dos limits rebuts.

### Detalls de la funció

|Nom de la funció|Paràmetres rebuts|Paràmetres a retornar|
|----|----|----|
|**`llegirDecimalInterval`**|**`demanarNombre`** de tipus **cadena**<br>**`errorNoDecimal`** de tipus **cadena**<br>**`errorForaInterval`** de tipus **cadena**<br>**`limitInferior`** de tipus **enter**<br>**`limitSuperior`** de tipus **enter**|Nombre **decimal** entrat per l'usuari<br>que es troba dins de l'interval.<br>El valor entrat pot ser igual a limit rebut.|

> ### **NOTA**:  Cal fer servir la funció **`llegirDecimal`**

```python
# =============================================================================
# Nom:      ??????
# Descripció: ??????
# ===== Dades d'entrada =====
# @param:   ?????? de tipus ??????
#       ??????
# ===== Dades a tornar  =====
# @return:  ?????? de tipus ??????
#       ??????
# 
# NOTA: Fa servir la nostra funció llegirDecimal
#
def llegirDecimalInterval(demanarNombre,errorNoDecimal,errorForaInterval,limitInferior,limitSuperior):
# Definició de variables
# Inicialització de variables
    print(f"Encara no s'ha desenvolupat aquesta funció!")
# =============================================================================
```

<hr>

## Funció **`demanaSiONo`**

### Detalls de la funció

Funció que demana a l'usuari que entri un caràcter que només pot ser **`s`** o **`S`** o **`n`** o **`N`**.

1. Es mostrarà el text rebut a la variable **`perDemanarSiONo`**, per demanar a l'usuari que entri un caràcter.

1. Es mostrarà un text d'**Error**, rebut a la variable **`errorNoDecimal`**, pel cas en que l'usuari entri alguna cosa que **no sigui** **`s`** o **`S`** o **`n`** o **`N`**.

|Nom de la funció|Paràmetres rebuts|Paràmetres a retornar|
|----|----|----|
|**`demanaSiONo`**|**`perDemanarSiONo`** de tipus **cadena**<br>**`missatgeError`** de tipus **cadena**|Caràcter entrat per l'usuari i<br>que només pot ser **`s`** o **`S`** o **`n`** o **`N`**.|

> ### **NOTA**:  Cal fer servir la funció **`llegirUnCaracter`**

```python
# =============================================================================
# Nom:      ??????
# Descripció: ??????
# ===== Dades d'entrada =====
# @param:   ?????? de tipus ??????
#       ??????
# ===== Dades a tornar  =====
# @return:  ?????? de tipus ??????
#       ??????
# 
# NOTA: Fa servir la nostra funció llegirUnCaracter
#
def perDemanarSiONo(cadDemanarCaracter):
# Definició de variables
# Inicialització de variables
    print(f"Encara no s'ha desenvolupat aquesta funció!")
# =============================================================================
```

<hr>

## Funció **`llegirVectorDEnters`**

### Detalls de la funció

Funció que demanarà a l'usuari els enters per omplir un vector d'enters. La mida del vector la rebrà amb el paràmetre **`midaVector`**. Farà servir la funció feta a classe i que proporcionarà el professor **`llegirEnterPositiu`**.

|Nom de la funció|Paràmetres rebuts|Paràmetres a retornar|
|----|----|----|
|**`llegirVectorDEnters`**|**`midaVector`** de tipus **enter**<br>**`demanaElement`** de tipus **cadena**|El vector que conté tots els elements demanats a l'usuari.|

> ### **NOTA**:  Cal fer servir la funció **`llegirEnterPositiu`**

```python
# =============================================================================
# Nom:      ??????
# Descripció: ??????
# ===== Dades d'entrada =====
# @param:   ?????? de tipus ??????
#       ??????
# ===== Dades a tornar  =====
# @return:  ?????? de tipus ??????
#       ??????
def llegirVector(midaVector,demanaElement):
# Definició de variables
# Inicialització de variables
    print(f"Encara no s'ha desenvolupat aquesta funció!")
# =============================================================================
```

<hr>

## Funció **`mostraVectorEnFila`**

### Detalls de la funció

Funció per mostrar per pantalla el vector rebut en una única línia i separat pel caràcter rebut com **`caracterSeparador`**.

|Nom de la funció|Paràmetres rebuts|Paràmetres a retornar|
|----|----|----|
|**`mostraVectorEnFila`**|**`vectorAMostrar`** de tipus **vector**|**Res**|


```python
# =============================================================================
# Nom:      ??????
# Descripció: ??????
# ===== Dades d'entrada =====
# @param:   ?????? de tipus ??????
#       ??????
# ===== Dades a tornar  =====
# @return:  ?????? de tipus ??????
#       ??????
def mostraVectorEnFila(vectorAMostrar):
# Definició de variables
# Inicialització de variables
    print(f"Encara no s'ha desenvolupat aquesta funció!")
# =============================================================================
```

<hr>

## Funció **`mostraVectorAmbSeparador`**

### Detalls de la funció

Funció per mostrar per pantalla el vector rebut en una única línia i separat pel caràcter rebut com **`caracterSeparador`**.

|Nom de la funció|Paràmetres rebuts|Paràmetres a retornar|
|----|----|----|
|**`mostraVectorAmbSeparador`**|**`vectorAMostrar`** de tipus **vector**<br>**`caracterSeparador`** de tipus **cadena**|**Res**|


```python
# =============================================================================
# Nom:      ??????
# Descripció: ??????
# ===== Dades d'entrada =====
# @param:   ?????? de tipus ??????
#       ??????
# ===== Dades a tornar  =====
# @return:  ?????? de tipus ??????
#       ??????
def mostraVectorAmbSeparador(vectorAMostrar,caracterSeparador):
# Definició de variables
# Inicialització de variables
    print(f"Encara no s'ha desenvolupat aquesta funció!")
# =============================================================================
```

<hr>

## Funció **`estaEnElVector`**

### Detalls de la funció

Funció que rep un nombre i un vector de números, i comprova si el número és o no al vector.

|Nom de la funció|Paràmetres rebuts|Paràmetres a retornar|Puntuació|
|----|----|----|----|
|**`estaEnElVector`**|**`nombreRebut`** de tipus **enter**<br>**`vectorRebut`** de tipus **vector**|Retorna un valor lògic (booleà **`True`** o **`False`**)<br>en funció de si el número rebut està dins del vector o no.<br>Retorna **`True`** si el número **està** al vector.<br>Retorna **`False`** si el número **NO està** al vector.|**`0,50` punts**|


```python
# =============================================================================
# Nom:      ??????
# Descripció: ??????
# ===== Dades d'entrada =====
# @param:   ?????? de tipus ??????
#       ??????
# ===== Dades a tornar  =====
# @return:  ?????? de tipus ??????
#       ??????
def estaEnElVector(nombreRebut,vectorRebut):
# Definició de variables
# Inicialització de variables
    print(f"Encara no s'ha desenvolupat aquesta funció!")
# =============================================================================
```

<br>
<hr>

## **Programa principal**

Programa per provar totes les funcions que heu fet durant l'examen.

Cal fer servir el següent tros de codi que us facilito a continuació.


```python
# ===================================================================
# Programa principal (main)
# ===================================================================

# Definició de variables GLOBALS

if __name__ == '__main__':
    # Definició de variables

    # Inicialització de variables
```
# Funcions facilitades pel professor

## Funció **`llegirEnter`**

### Detalls de la funció

Funció per llegir un nombre **enter** entrat per l'usuari.

1. Es mostrarà el text rebut a la variable **`demanarEnterPositiu`**, per demanar a l'usuari que entri un **enter positiu**.

1. Es mostrarà un text d'**Error**, rebut a la variable **`errorNoEnter`**, en el cas en que l'usuari entri alguna cosa que **no sigui un enter**.

1. I també, es mostrarà un text d'**Error**, rebut a la variable **`errorNoPositiu`**, en el cas en que l'usuari entri un **enter que no sigui positiu**.

|Nom de la funció|Paràmetres rebuts|Paràmetres a retornar|
|----|----|----|
|**`llegirEnterPositiu`**|**`demanarEnterPositiu`** de tipus **cadena**<br>**`demanaElement`** de tipus **cadena**|Enter positiu entrat per l'usuari.|

```python
# ============================================================================= 
# Nom:      llegirEnter
# Descripció: Funció per llegir un enter, entrat per l'usuari. 
#       Mostrant el text rebut a (demanarEnter) per demanar a l'usuari
#       que entri un enter. I mostrant un text d'Error, també
#       rebut (errorNoEnter), pel cas en que l'usuari entri alguna
#       cosa que no sigui un enter.
# ===== Dades d'entrada =====
# @param:   demanarEnter de tipus cadena
#       Text a mostrar per demanar un enter a l'usuari!
# @param:   errorNoEnter de tipus cadena
#       Text a mostrar per quan l'usuari entra un que no sigui un enter.
# @param:   errorNoPositiu de tipus cadena
#       Text a mostrar per quan l'usuari entra un enter que no és positiu.
# ===== Dades a tornar  =====
# @return: enterLlegit de tipus enter
#       Enter entrat per l'usuari.
def llegirEnter(demanarEnter,errorNoEnter):
    # Definició de variables
    enterLlegit = int()
    # Inicialització de variables
    enterLlegit = 0
    while (True):
        try:
            print(demanarEnter, end="")
            enterLlegit = int(input())
            return enterLlegit
        except:
            print(errorNoEnter)
# =============================================================================
```

## Funció **`llegirEnterPositiu`**

### Detalls de la funció

Funció per llegir un nombre **enter positiu** entrat per l'usuari.

1. Es mostrarà el text rebut a la variable **`demanarEnterPositiu`**, per demanar a l'usuari que entri un **enter positiu**.

1. Es mostrarà un text d'**Error**, rebut a la variable **`errorNoEnter`**, en el cas en que l'usuari entri alguna cosa que **no és un enter**.

1. I també, es mostrarà un text d'**Error**, rebut a la variable **`errorNoPositiu`**, en el cas en que l'usuari entri un **enter que no és positiu**.

|Nom de la funció|Paràmetres rebuts|Paràmetres a retornar|
|----|----|----|
|**`llegirEnterPositiu`**|**`demanarEnterPositiu`** de tipus **cadena**<br>**`demanaElement`** de tipus **cadena**|Enter positiu entrat per l'usuari.|

```python
# =============================================================================
# Nom:      llegirEnterPositiu
# Descripció: Funció per llegir un enter positiu, entrat per l'usuari.
#       Es mostrarà el text rebut a la variable demanarEnterPositiu, 
#       per demanar a l'usuari que entri un enter positiu.
#       Es mostrarà un text d'Error, rebut a la variable errorNoEnter,
#       en el cas en que l'usuari entri alguna cosa que no sigui un enter.
#       Es mostrarà un text d'Error, rebut a la variable errorNoPositiu
#       en el cas en que l'usuari entri un enter que no sigui positiu.
# ===== Dades d'entrada =====
# @param:   demanarEnterPositiu de tipus cadena
#       Text a mostrar per demanar un enter a l'usuari!
# @param:   errorNoEnter de tipus cadena
#       Text a mostrar per quan l'usuari entri res que no sigui un enter.
# @param:   errorNoPositiu de tipus cadena
#       Text a mostrar per quan l'usuari entri un enter que no és positiu.
# ===== Dades a tornar  =====
# @return: enterPositiu de tipus enter
#       Enter positiu entrat per l'usuari.
# 
# NOTA: Fa servir la nostra funció llegirEnter
#   
def llegirEnterPositiu(demanarEnterPositiu,\
                       errorNoEnter,\
                       errorNoPositiu):
    # Definició de variables
    enterLlegit = int()
    # Inicialització de variables
    enterLlegit = 0
    while (True):
        enterLlegit = llegirEnter(demanarEnterPositiu,errorNoEnter)
        if (enterLlegit >= 0):
            return enterLlegit
        else:
            print(errorNoPositiu)
# =============================================================================
```


