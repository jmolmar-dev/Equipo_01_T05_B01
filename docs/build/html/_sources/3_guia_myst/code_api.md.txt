# 3.5 Códigos Fuente y APIs en MyST

## 3.5.1 Bloques de Código
Para mostrar bloques de código en MyST, puedes usar la sintaxis estándar de Markdown con tres acentos graves ````` o usar directivas enriquecidas para mayor control.

````{admonition} Ejemplo de Bloque de Código Básico
```python
# Este es un bloque de código básico en Python
print("Hola, mundo!")
```
````

Esto se logra con:
````{admonition} Markdown
```
```python
# Este es un bloque de código básico en Python
print("Hola, mundo!")
```
````

---

## 3.5.2 Bloques de Código con Directivas
Las directivas de MyST permiten personalizar aún más los bloques de código, añadiendo títulos, líneas resaltadas, etc.

````{admonition} Ejemplo de Bloque de Código con Directivas
```{code-block} python
---
name: Ejemplo de Código Python
linenos: true
emphasize-lines: 2
---
# Código Python con configuración personalizada
x = 10
print(f"El valor de x es {x}")
```
````

Esto se logra con:
````{admonition} Markdown
```
```{code-block} python
---
name: Ejemplo de Código Python
linenos: true
emphasize-lines: 2
---
# Código Python con configuración personalizada
x = 10
print(f"El valor de x es {x}")
```
````

---

## 3.5.3 Incrustar APIs en Documentos
Puedes incluir documentaciones de APIs directamente en tus documentos usando la directiva `automodule` o `autoclass` de Sphinx.

````{admonition} Markdown
```
```{automodule} mi_modulo.ejemplo
---
members: true
undoc-members: true
show-inheritance: true
---
```
````

---

## 3.5.4 Resaltar Fragmentos de Código
Puedes resaltar fragmentos específicos dentro del texto utilizando bloques en línea.

```{admonition} Ejemplo de Código en Línea
Este es un ejemplo de `código en línea` dentro de un párrafo.
```

Esto se logra con:
````{admonition} Markdown
```
Este es un ejemplo de `código en línea` dentro de un párrafo.
```
````

---

## 3.5.5 Adjuntar Archivos de Código
Para incluir archivos de código externos en tu documentación, utiliza la directiva `literalinclude`.

````{admonition} Ejemplo de Inclusión de Archivo
```{literalinclude} ../../../src/operaciones.py
---
language: python
linenos: true
emphasize-lines: 3
---
```
````

Esto se logra con:
````{admonition} Markdown
```
```{literalinclude} ../../../src/operaciones.py
---
language: python
linenos: true
emphasize-lines: 3
---
```
````

---

## 3.5.6 Notas sobre la Configuración
Al usar directivas como `automodule` o `literalinclude`, asegúrate de que las rutas de los archivos sean correctas y de que la configuración de Sphinx permita el uso de estas directivas. Esto puede requerir ajustes en `conf.py` como:

```python
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]
```



