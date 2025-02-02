# 3.9 Roles y Directivas en MyST

## 3.9.1 ¿Qué son los Roles y las Directivas?
Los roles son marcadores en línea que agregan formato o funcionalidad, mientras que las directivas son bloques más grandes para incluir contenido dinámico o personalizado.

---

## 3.9.2 Ejemplo de Roles

### Rol: **doc**
Permite crear enlaces a otros documentos en tu proyecto.

```
Consulta la documentación en {doc}`seccion1`.
```

Renderiza como:
> Consulta la documentación en [Sección 1](https://mi-documentacion.com/seccion1).

---

### Rol: **ref**
Crea referencias a etiquetas definidas previamente.

```
Consulta más detalles en {ref}`etiqueta-seccion`.
```

Renderiza como:
> Consulta más detalles en [Título de la Sección](https://mi-documentacion.com/seccion#etiqueta-seccion).

---

### Rol: **numref**
Permite referencias numeradas a figuras, tablas o secciones.

```
Consulta la figura {numref}`figura-1`.
```

---

## 3.9.3 Ejemplo de Directivas

### Directiva: **figure**
Incluye una figura con su título y descripción.

```
```{figure} ../images/imagen.png
:alt: Una descripción de la imagen
:width: 50%

Título de la Figura
```
```

---

### Directiva: **`note`**
Destaca contenido importante como una nota.

```
```{note}
Recuerda actualizar la guía periódicamente.
```
```

Renderiza como:  
> **Nota**: Recuerda actualizar la guía periódicamente.

---

### Directiva: **`warning`**
Muestra un mensaje de advertencia.

```
```{warning}
Este proceso puede sobrescribir archivos existentes.
```
```

Renderiza como:  
> \textwarning **Advertencia**: Este proceso puede sobrescribir archivos existentes.

---

El uso de roles y directivas en MyST mejora la claridad y navegación del contenido.
