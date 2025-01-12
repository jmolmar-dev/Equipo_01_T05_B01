# 3.6 Cross-References en MyST

## 3.6.1 Enlaces Internos Básicos
Puedes crear enlaces internos en tu documento MyST utilizando la sintaxis estándar de Markdown o referencias explícitas con etiquetas.

````{admonition} Ejemplo de Enlace Interno
Puedes saltar a la sección [3.6.2 Enlaces con Títulos](#3.6.2 Enlaces-con-titulos).
````

Esto se logra con:
````{admonition} Markdown
```markdown
Puedes saltar a la sección [3.6.2 Enlaces con Títulos](#enlaces-con-titulos).
```
````

---

## 3.6.2 Enlaces con Títulos
Los encabezados en MyST automáticamente generan identificadores que pueden ser referenciados mediante `#` seguido del identificador. Si el encabezado tiene caracteres especiales, estos se reemplazan automáticamente (por ejemplo, espacios por guiones).

````{admonition} Ejemplo de Referencia a un Encabezado
Consulta la sección [3.6.1 Enlaces Internos Básicos](#3.6.1 Enlaces-internos-basicos) para más detalles.
````

Esto se logra con:
````{admonition} Markdown
```markdown
Consulta la sección [3.6.1 Enlaces Internos Básicos](#enlaces-internos-basicos) para más detalles.
```
````

---

## 3.6.3 Etiquetas Personalizadas
Puedes agregar etiquetas personalizadas a las secciones o elementos usando la directiva `{ref}`. Esto permite crear nombres amigables para las referencias.

````{admonition} Ejemplo de Etiqueta Personalizada
:class: note
```markdown
(seccion-personalizada)=
# Título de la Sección

Contenido de la sección con una etiqueta personalizada.
```

Y puedes referenciarla con:
```
:ref:`Consulta esta sección personalizada <seccion-personalizada>` para obtener más información.
```
````

---

## 3.6.4 Referencias Cruzadas a Figuras, Tablas y Código
Puedes referenciar figuras, tablas y bloques de código usando etiquetas y la directiva `:ref:`.

````{admonition} Ejemplo de Referencia Cruzada
:class: note
```{figure} ../_static/fun-fish.webp
---
name: figura-divertida
---
Este es un pez divertido.
```

Luego, puedes referenciar la figura con:
```
Mira la figura en {ref}`figura-divertida` para más detalles.
```
````

Esto se logra asignando una etiqueta en la figura y referenciándola.

---

## 3.6.5 Referencias Externas
Para enlazar a recursos externos, simplemente usa la sintaxis estándar de Markdown.

````{admonition} Ejemplo de Enlace Externo
Visita [la documentación de MyST](https://myst-parser.readthedocs.io/) para más información.
````

Esto se logra con:
````{admonition} Markdown
```markdown
Visita [la documentación de MyST](https://myst-parser.readthedocs.io/) para más información.
```
````

---

Con estas herramientas, puedes estructurar tus documentos MyST con enlaces internos, referencias cruzadas y etiquetas personalizadas, mejorando la navegación y claridad de tus contenidos.
