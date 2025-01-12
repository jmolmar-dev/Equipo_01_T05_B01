# 3.1 Tipografia MYST: 

## 3.1.1 Encabezados
Los encabezados funcionan de la misma manera que en markdown, usando almohadillas consecutivas.
```{admonition} Ejemplo Encabezados
<span style="font-size: 32px;">Encabezado de nivel 1</span>

<span style="font-size: 28px;">Encabezado de nivel 2</span>

<span style="font-size: 24px;">Encabezado de nivel 3</span>

<span style="font-size: 20px;">Encabezado de nivel 4</span>
```
Lo que sería el resultado de:
````{admonition} Markdown
```
# Encabezado de nivel 1
## Encabezado de nivel 2
### Encabezado de nivel 3
#### Encabezado de nivel 4
```
````

---

## 3.1.2 Parráfos
Un parrafo es una linea de texto separada por una linea en blanco.

```{admonition} Ejemplo Parrafo

Ejemplo Parrafo 1.

Ejemplo Parrafo 2.
```
---
## 3.1.3 Cambios de tema
Un cambio de tema separa dos secciones de temas distintos.

---

Lo que es el resultado de: 
````{admonition} Markdown
```
---
```
````
---
## 3.1.4 Estilos de Texto

```{admonition} Estilos de Texto 
Este es un texto **en negrita**.

Este es un texto *en cursiva*.

Este texto está en {sub}`subíndice`.

Este texto está en {sup}`superíndice`.
```
Lo cual es el resultado de:
````{admonition} Markdown
```
Este es un texto **en negrita**.

Este es un texto *en cursiva*.

Este texto está en {sub}`subíndice`.

Este texto está en {sup}`superíndice`.
```
````
---
## 3.1.5 Salto de linea.
Un salto de linea separa dos lineas sin necesidad de una linea en blanco.
```{admonition} Ejemplo Salto de Linea
Pulgas \
tenía \
el perro.
```

Lo cual es el resultado de:
````{admonition} Markdown
```
Pulgas \
tenía \
el perro.
```
````
---
## 3.1.6 Listas numeradas y no numeradas
```{admonition} Ejemplo Listas Numeradas y No Numeradas
- Lista no numerada empezada por \- 
- Con dos puntos
    * Y una lista anidada empezada por \* 

* Tambien puede hacerse a la inversa
* Con una lista no numerada empezada por \*
    - Y listas anidadas empezadas por \-
* E incluso
    1. Listas numeradas
    2. Anidadas

1. Las listas numeradas
2. Por supuesto
    1. Pueden tener
    2. Listas anidadas
3. Y estar solas
```

Lo cual es el resultado de:
````{admonition} Markdown
```
- Lista no numerada empezada por \- 
- Con dos puntos
    * Y una lista anidada empezada por \* 

* Tambien puede hacerse a la inversa
* Con una lista no numerada empezada por \*
    - Y listas anidadas empezadas por \-
* E incluso
    1. Listas numeradas
    2. Anidadas

1. Las listas numeradas
2. Por supuesto
    1. Pueden tener
    2. Listas anidadas
3. Y estar solas
```
````
---

## 3.1.7 Citas
> Aunque la mona se vista de seda, mona se queda.

Esto es el resultado de:

````{admonition} Markdown
```
> Aunque la mona se vista de seda, mona se queda.
```
````
---
## 3.1.8 Notas de Pie de Página
```{admonition} Ejemplo Notas de Pie de Página
- Esta referencia a nota de pie de página esta numerada manualmente.[^3]
- Mientras que esta está numerada automaticamente.[^myref]
[^myref]: This is an auto-numbered footnote definition.
[^3]: This is a manually-numbered footnote definition.
```

Esto es el resultado de:

````{admonition} Markdown
```
- Esta referencia a nota de pie de página esta numerada manualmente.[^3]
- Mientras que esta está numerada automaticamente.[^myref]
[^myref]: This is an auto-numbered footnote definition.
[^3]: This is a manually-numbered footnote definition.
```
````
