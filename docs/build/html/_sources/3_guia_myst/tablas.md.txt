# 3.4 Tablas en MyST

## 3.4.1 Tablas Básicas
Las tablas en MyST se pueden crear usando la sintaxis básica de Markdown.

```{admonition} Ejemplo de Tabla Básica
| Columna 1 | Columna 2 | Columna 3 |
|-----------|-----------|-----------|
| Fila 1    | Valor 1   | Valor 2   |
| Fila 2    | Valor 3   | Valor 4   |
```

Esto se logra con:
````{admonition} Markdown
```
| Columna 1 | Columna 2 | Columna 3 |
|-----------|-----------|-----------|
| Fila 1    | Valor 1   | Valor 2   |
| Fila 2    | Valor 3   | Valor 4   |
```
````

---

## 3.4.2 Tablas Mejoradas con MyST
Puedes mejorar tus tablas utilizando directivas de MyST para agregar alineaciones, anchos y estilos avanzados.

````{admonition} Ejemplo de Tabla Mejorada
```{list-table}
---
header-rows: 1
---
* - Cabecera 1
  - Cabecera 2
  - Cabecera 3
* - Fila 1, Col 1
  - Fila 1, Col 2
  - Fila 1, Col 3
* - Fila 2, Col 1
  - Fila 2, Col 2
  - Fila 2, Col 3
```
````

Esto se logra con:
````{admonition} Markdown
```
```{list-table}
---
header-rows: 1
---
* - Cabecera 1
  - Cabecera 2
  - Cabecera 3
* - Fila 1, Col 1
  - Fila 1, Col 2
  - Fila 1, Col 3
* - Fila 2, Col 1
  - Fila 2, Col 2
  - Fila 2, Col 3
```
````

---

## 3.4.3 Tablas con Ancho Personalizado
Puedes ajustar el ancho de las columnas para que se adapten mejor al contenido.

````{admonition} Ejemplo de Ancho Personalizado
```{list-table}
---
header-rows: 1
widths: 20 30 50
---
* - Columna Estrecha
  - Columna Mediana
  - Columna Ancha
* - Corto
  - Texto de longitud media
  - Este texto es más largo para demostrar el ancho personalizado
```
````

Esto se logra con:
````{admonition} Markdown
```
```{list-table}
---
header-rows: 1
widths: 20 30 50
---
* - Columna Estrecha
  - Columna Mediana
  - Columna Ancha
* - Corto
  - Texto de longitud media
  - Este texto es más largo para demostrar el ancho personalizado
```
````

---

## 3.4.4 Combinar Celdas en Tablas
No es posible combinar celdas directamente con la sintaxis de Markdown o MyST, pero puedes usar HTML dentro de MyST si necesitas esta funcionalidad.

````{admonition} Ejemplo de Tabla con Celdas Combinadas
```{raw} html
<table>
  <tr>
    <th>Cabecera 1</th>
    <th>Cabecera 2</th>
    <th>Cabecera 3</th>
  </tr>
  <tr>
    <td rowspan="2">Celda combinada</td>
    <td>Fila 1, Col 2</td>
    <td>Fila 1, Col 3</td>
  </tr>
  <tr>
    <td>Fila 2, Col 2</td>
    <td>Fila 2, Col 3</td>
  </tr>
</table>
```
````

Esto se logra con:
````{admonition} Markdown
```
```{raw} html
<table>
  <tr>
    <th>Cabecera 1</th>
    <th>Cabecera 2</th>
    <th>Cabecera 3</th>
  </tr>
  <tr>
    <td rowspan="2">Celda combinada</td>
    <td>Fila 1, Col 2</td>
    <td>Fila 1, Col 3</td>
  </tr>
  <tr>
    <td>Fila 2, Col 2</td>
    <td>Fila 2, Col 3</td>
  </tr>
</table>
```
````


