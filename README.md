# Activitat 1

## Establiment de Middlewares

En aquesta activitat, hem configurat els middlewares necessaris per a la nostra aplicació.

![Establiment de Middlewares](image-1.png)

## Adaptació de l'AlumneModel

Hem adaptat l'`AlumneModel` a la consulta actual, que ara inclou el camp `DescAula` i elimina les identificacions (`id`) de l'aula i de l'alumne.

![Adaptació de l'AlumneModel](image-2.png)

## Codi JavaScript

A continuació, presentem la versió actualitzada del codi JavaScript:

![Codi JavaScript](image-3.png)

## Resultat Final

El resultat final de la implementació es mostra a continuació:

![Resultat Final](image.png)

---

# Activitat 2

## Modificació Principal

Aquesta activitat inclou una modificació significativa en la funcionalitat, on hem afegit les opcions `orderby`, `contain`, `skip` i `limit`.

![Modificació Principal](image-4.png)

## Exemples d'Execució

Aquí tenim alguns exemples d'execució de les noves funcionalitats:

![Exemples d'Execució](image-5.png)

## Resposta

Les respostes que retornem són les següents:

![Resposta](image-6.png)

**Nota:** Tots els camps són opcionals. Si el nom no existeix, el sistema ho gestionarà adequadament:

![Gestió d'Errors](image-7.png)

---

# Activitat 3

## Crida a alumnesCSV

Hem implementat la funcionalitat `alumnesCSV`, que ens permet gestionar la importació de dades des d'un fitxer CSV.

![Crida a alumnesCSV](image-8.png)

## Separació de Dades

Les dades del fitxer CSV es separen per comes (`,`):

![Separació de Dades](image-9.png)

## Eliminació de la Primera Línia

Eliminem la primera línia del CSV, que és un comentari:

![Eliminació de la Primera Línia](image-10.png)

## Codi

El codi per a la gestió de la importació es mostra a continuació:

![Codi de Gestió](image-11.png)

## Afegint el CSV

Finalment, afegim les dades del CSV a la base de dades:

![Afegint el CSV](image-12.png)

## Resultat Final

La implementació acaba amb els següents resultats:

![Resultat Final](image-13.png)
