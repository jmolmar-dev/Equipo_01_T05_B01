# 3.7 Organización del Contenido en MyST

## 3.7.1 Secciones y Encabezados
La organización básica del contenido en MyST se realiza mediante encabezados. Estos se generan con el uso de almohadillas `#`, con un número creciente para indicar la jerarquía.

````{admonition} Ejemplo de Encabezados Jerárquicos
```markdown
# Título Principal
## Subtítulo 1
### Subtítulo 1.1
#### Subtítulo 1.1.1
```
````

Esto permite estructurar claramente el contenido en niveles.

---

## 3.7.2 Separadores de Temas
Los separadores `---` ayudan a dividir secciones visualmente, indicando cambios de tema o contenido.

```{admonition} Ejemplo de Separador
Este es el contenido antes del separador.

---

Este es el contenido después del separador.
```

Esto se escribe como:
````{admonition} Markdown
```
Este es el contenido antes del separador.

---

Este es el contenido después del separador.
```
````

---

## 3.7.3 Archivos Incluidos
Para incluir contenido de otros archivos dentro de un documento, utiliza la directiva `include`.

`````{admonition} Ejemplo de Inclusión de Archivo
````
```{include} ../path/to/otro_documento.md
:relative-docs: docs/
:relative-images:
```
````
`````

Esto inserta el contenido del archivo especificado directamente en la posición del documento actual.

---

## 3.7.4 Índices y Tablas de Contenido
Puedes generar automáticamente un índice o tabla de contenido utilizando la directiva `toctree`.

`````{admonition} Ejemplo de Tabla de Contenidos
````
```{toctree}
:maxdepth: 2
:hidden:

seccion1
seccion2
subdirectorio/seccion3
```
````
`````

Esto genera una tabla de contenido basada en los archivos especificados.

---

## 3.7.5 Etiquetas y Referencias
Organiza contenido utilizando etiquetas personalizadas para referenciar secciones específicas. Usa la directiva `(identificador)=` para asignar una etiqueta.

````{admonition} Ejemplo de Etiqueta y Referencia
```markdown
(etiqueta-seccion)=
# Título de la Sección

Contenido de la sección etiquetada.

Consulta la sección {ref}`etiqueta-seccion` para más información.
```
````




