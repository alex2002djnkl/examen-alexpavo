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


