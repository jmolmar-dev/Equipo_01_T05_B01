# 3.3 Imágenes y Figuras en MyST

## 3.3.1 Imágenes Básicas
Para insertar imágenes básicas en MyST, utiliza la sintaxis de Markdown estándar con `![]()`.

```{admonition} Ejemplo de Imagen Básica
![Descripción de la imagen]( ../_static/fun-fish.png "Fun Fish is Fun")
```

Esto se logra con:
````{admonition} Markdown
```
![Descripción de la imagen](../_static/fun-fish.png "Fun Fish is Fun")
```
````

---

## 3.3.2 Figuras con MyST
Las figuras en MyST son bloques enriquecidos que permiten agregar leyendas y configuraciones adicionales a las imágenes.

````{admonition} Ejemplo de Figura con Leyenda
```{figure} ../_static/fun-fish.png
---
align: center
name: pescado-divertido
---
Este es un ejemplo de figura con una leyenda centrada.
```
````

Esto se logra con:
````{admonition} Markdown
```
```{figure} ../_static/fun-fish.png
---
align: center
name: pescado-divertido
---
Este es un ejemplo de figura con una leyenda centrada.
```
````

---

## 3.3.3 Ajustes de Alineación
Puedes controlar la alineación de las imágenes o figuras usando el parámetro `align`.

````{admonition} Ejemplo de Alineación
```{figure} ../_static/fun-fish.png
---
align: left
---
Figura alineada a la izquierda.
```
```{figure} ../_static/fun-fish.png
---
align: right
---
Figura alineada a la derecha.
```
```{figure} ../_static/fun-fish.png
---
align: center
---
Figura centrada.
```



````

Esto se logra con:
`````{admonition} Markdown
````
```{figure} ../_static/fun-fish.png
---
align: left
---
Figura alineada a la izquierda.
```
```{figure} ../_static/fun-fish.png
---
align: right
---
Figura alineada a la derecha.
```
```{figure} ../_static/fun-fish.png
---
align: center
---
Figura centrada.
```


````
`````

---

## 3.3.4 Escalado de Imágenes
Puedes ajustar el tamaño de las imágenes con el parámetro `width`.

````{admonition} Ejemplo de Escalado
```{figure} ../_static/fun-fish.png
---
width: 50%
---
Figura con un ancho del 50%.
```

```{figure} ../_static/fun-fish.png
---
width: 200px
---
Figura con un ancho de 200px.
```
````

Esto se logra con:
`````{admonition} Markdown
````
```{figure} ../_static/fun-fish.png
---
width: 50%
---
Figura con un ancho del 50%.
```

```{figure} ../_static/fun-fish.png
---
width: 200px
---
Figura con un ancho de 200px.
````
`````

---

## 3.3.5 Referencias a Figuras
Puedes asignar un nombre a las figuras con el parámetro `name` y luego referenciarlas en el texto.

````{admonition} Ejemplo de Referencias a Figuras
```{figure} ../_static/fun-fish.png
---
name: fun-fish
---
Figura con nombre para referencia.
```
````

Como se muestra en {ref}`fun-fish`, puedes referenciar figuras en tu documento.


Esto se logra con:
`````{admonition} Markdown
````
```{figure} ../_static/fun-fish.png
---
name: fun-fish
---
Figura con nombre para referencia.
```

Como se muestra en {ref}`fun-fish`, puedes referenciar figuras en tu documento.
````
`````



