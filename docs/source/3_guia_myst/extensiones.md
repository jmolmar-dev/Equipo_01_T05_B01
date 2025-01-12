# 3.8 Extensiones de Sintaxis en MyST

## 3.8.1 Extensiones Opcionales
El parser de MyST incluye varias extensiones opcionales que permiten agregar características avanzadas al contenido. Estas extensiones se pueden habilitar en la configuración de Sphinx mediante la clave `myst_enable_extensions`.

Ejemplo de configuración en `conf.py`:
```python
myst_enable_extensions = [
    "dollarmath",
    "tasklist",
    "fieldlist"
]
```

A continuación, se explican tres extensiones con ejemplos:

---

## 3.8.2 Matemáticas con **dollarmath**
Permite escribir expresiones matemáticas en línea usando `$` para ecuaciones simples o `$$` para ecuaciones en bloques.

````{admonition} Ejemplo de Matemáticas con Dollarmath
```markdown
El área de un círculo es $A = \pi r^2$.

$$
E = mc^2
$$
```
````

Se renderizará como:
- En línea: \( A = \pi r^2 \)  
- Bloque:  
\[
E = mc^2
\]

---

## 3.8.3 Listas de Tareas con **tasklist**
Esta extensión permite agregar listas de tareas con casillas marcables en Markdown.

````{admonition} Ejemplo de Lista de Tareas
```markdown
- [ ] Tarea pendiente
- [x] Tarea completada
- [ ] Otra tarea
```
````

Se renderizará como:
- [ ] Tarea pendiente  
- [x] Tarea completada  
- [ ] Otra tarea  

---

## 3.8.4 Listas de Campos con **fieldlist**
Esta extensión se utiliza para estructurar definiciones con pares clave-valor en formato limpio.

````{admonition} Ejemplo de Lista de Campos
```markdown
:autor: John Doe
:versión: 1.0
:fecha: 12-01-2025
```
````

Renderiza el contenido como una tabla de definiciones:
- **autor**: John Doe  
- **versión**: 1.0  
- **fecha**: 12-01-2025  

---

Habilitar estas extensiones puede enriquecer la presentación y funcionalidad del contenido de tu guía.