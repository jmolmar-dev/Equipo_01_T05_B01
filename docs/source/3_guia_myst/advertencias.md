# 3.2 Admonitions en MyST

## 3.2.1 ¿Qué son los Admonitions?
Los admonitions en MyST son bloques de contenido destacados que puedes usar para resaltar información importante, advertencias, ejemplos, o cualquier tipo de contenido que quieras destacar. MyST soporta varios tipos de admonitions predefinidos y personalizables.

```{admonition} Ejemplo de Admonition Básico
Este es un admonition básico sin tipo específico.
```

Esto se logra con:
````{admonition} Markdown
```
```{admonition} Ejemplo de Admonition Básico
Este es un admonition básico sin tipo específico.
```
````

---

## 3.2.2 Admonitions Predefinidos
MyST incluye admonitions predefinidos como `note`, `warning`, `tip`, y más.

````{admonition} Ejemplo de Admonitions Predefinidos
```{note}
Este es un admonition de tipo "note".
```

```{warning}
Este es un admonition de tipo "warning".
```

```{tip}
Este es un admonition de tipo "tip".
```
````

Esto se logra con:
`````{admonition} Markdown
````
```{note}
Este es un admonition de tipo "note".
```

```{warning}
Este es un admonition de tipo "warning".
```

```{tip}
Este es un admonition de tipo "tip".
```
````
`````

---

## 3.2.3 Admonitions con Títulos Personalizados
Puedes agregar un título personalizado a un admonition para especificar su propósito.

````{admonition} Ejemplo con Título Personalizado

```{admonition} Recuerda Esto
Este es un admonition con un título personalizado.
```
````

Esto se logra con:
````{admonition} Markdown
```
```{admonition} Recuerda Esto
Este es un admonition con un título personalizado.
```
````

---

## 3.2.4 Admonitions con Código Formateado
Puedes incluir bloques de código dentro de un admonition para combinar explicaciones con ejemplos.

`````{admonition} Ejemplo Admonition con Código
````{warning}
### Importante
Cuidado con los índices fuera de rango en Python:

```python
lista = [1, 2, 3]
print(lista[3])  # Esto genera un IndexError
```
````
`````

Esto se logra con:
`````{admonition} Markdown
```
````{warning}
### Importante
Cuidado con los índices fuera de rango en Python:

```python
lista = [1, 2, 3]
print(lista[3])  # Esto genera un IndexError
```

`````

---

## 3.2.5 Personalización Avanzada
Puedes personalizar la apariencia de los admonitions con estilos adicionales usando etiquetas HTML o CSS dentro de ellos.

````{admonition} Ejemplo de Personalización
```{tip}
<span style="color: green; font-weight: bold;">Este es un admonition personalizado con texto verde y negrita.</span>
```
````

Esto se logra con:
````{admonition} Markdown
```
```{tip}
<span style="color: green; font-weight: bold;">Este es un admonition personalizado con texto verde y negrita.</span>
```
````




