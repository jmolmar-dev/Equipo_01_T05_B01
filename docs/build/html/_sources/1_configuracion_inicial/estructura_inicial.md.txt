# 1.4 Explicación de la Estructura inicial del proyecto:

Al ejecutar el comando explicado dentro del apartado anterior, y seguir el proceso de construcción en función de las especificaciones explicadas, se nos formará la siguiente estructura de proyecto **(en nuestro caso justo en el directorio docs al ejecutar el comando del apartado anterior desde allí)**: 

**1. /build:** Directorio donde se irán almacenando los archivos que genere posteriormente **Sphinx**, que se distinguirán en función del formato de salida dentro de distintos subdirectorios: **HMTL,PDF, ...**

----------

**2. /source:** Directorio principal donde se almacenarán los archivos fuente de la documentación, en este caso, serán en formato **Markdown**, así como el archivo de configuración principal del proyecto, en **Código Python**, respectivamente.

----------

**3. /_static:** Subcarpeta dentro de **source** donde se incluirán recursos estáticos, tales como imágenes o archivos de CSS, entre otros.

----------

**4. /_templates:** Carpeta destinada a archivos que personalicen nuestras plantillas HTML para generar la documentación.

----------

**5. conf.py:** Es el archivo de configuración principal de nuestro proyecto: recoge parámetros como el nombre del mismo o las extensiones que tiene habilitada, así como el tema que se va a emplear, entre otros **(Será explicado más detalladamente en el siguiente apartado)**. 

----------

**6.index.rst:** Archivo donde se inicializará la documentación. Será el punto de partida para generar un índice y reconducir al usuario a los distintos apartados que desee consultar, los cuales serán desarrollados en otros archivos **Markdown** aparte. Cabe destacar que debe se ser renombrado de **.rst** a **.md**.

----------

**7. make.bat:** Script de **Windows** que nos permitirá ejecutar ciertos comandos de construcción de forma posterior, con los que generaremos la documentación en los distintos formatos.

----------

**8. Makefile:** Archivo empleado dentro de los **sistemas Unix (Linux/Mac)** para construir la documentación. Cumple la misma función que el **make.bat** en otros sistemas operativos




