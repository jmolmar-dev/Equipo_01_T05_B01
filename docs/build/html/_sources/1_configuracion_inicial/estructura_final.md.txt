# 1.10 Explicación de la Estructura Final del Proyecto:

**RESUMEN ESTRUCTURA INICIAL**:

| **Componente**             | **Explicación**                                                                                                                                         |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| **/build**               | Directorio donde se irán almacenando los archivos que genere posteriormente **Sphinx**, que se distinguirán en función del formato de salida dentro de distintos subdirectorios: **HTML, PDF, ...** |
| **/source**             | Directorio principal donde se almacenarán los archivos fuente de la documentación, en este caso, serán en formato **Markdown**, así como el archivo de configuración principal del proyecto, en **Código Python**, respectivamente. |
| **/_static**           | Subcarpeta dentro de **source** donde se incluirán recursos estáticos, tales como imágenes o archivos de CSS, entre otros.                         |
| **/_templates**          | Carpeta destinada a archivos que personalicen nuestras plantillas HTML para generar la documentación.                                              |
| **conf.py**              | Es el archivo de configuración principal de nuestro proyecto: recoge parámetros como el nombre del mismo o las extensiones que tiene habilitada, así como el tema que se va a emplear, entre otros. **(Será explicado más detalladamente en el siguiente apartado)**. |
| **index.rst**            | Archivo donde se inicializará la documentación. Será el punto de partida para generar un índice y reconducir al usuario a los distintos apartados que desee consultar, los cuales serán desarrollados en otros archivos **Markdown** aparte. Cabe destacar que debe ser renombrado de **.rst** a **.md**. |
| **make.bat**             | Script de **Windows** que nos permitirá ejecutar ciertos comandos de construcción de forma posterior, con los que generaremos la documentación en los distintos formatos. |
| **Makefile**            | Archivo empleado dentro de los **sistemas Unix (Linux/Mac)** para construir la documentación. Cumple la misma función que el **make.bat** en otros sistemas operativos. |


A la estructura inicial vista en el apartado anterior, con todos los cambios que se han ido realizando punto, deberíamos incluirle los siguientes directorios/archivos:

**1. Subdirectorios /1_configuracion_inicial, 2_comandos, 3_guia_myst:**

Estos subdirectorios son los que almacenarán todo el contenido en formato **Markdown**, con el cual hemos ido explicando y documentando todos los apartados y lo vamos a seguir haciendo hasta la finalización. Cabe destacar que cada uno de ellos posee su propio archivo **index.md**, con el objetivo de tener un índice y un direccionamiento más detallado dentro de la documentación.

----------

**2. Subdirectorios dentro del directorio /build:**

Al generar nuestra documentación, se nos generarán dos directorios dentro del mismo: 

- En el caso de generar **HTML**, serán doctrees y html respectivamente.

- Si generamos **PDF**, se sustituirá el de html por **latex**.

----------

**3. Directorio src:**

Directorio donde durante nuestro proyecto hemos tenido que almacenar el código **Python**, con el que hemos generado la documentación con el formato docstring de Google posteriormente, lo cual ya se ha explicado de forma previa.


