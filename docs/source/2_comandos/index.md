# 2.Comandos Utilizados de forma detallada en el proyecto

Estos serian los comandos que hemos utilizado dentro del proyecto:

| **Comando** | **Descripción** |
|-------------|----------------|
| **python -m venv .env** | Este comando se ha utilizado en el proyecto para construir el entorno virtual desde la raíz del proyecto. `.env` indica el nombre que se asignará al entorno. |
| **.\.env\Scripts\activate** | Este comando se ha usado para activar el entorno de trabajo. |
| **pip install sphinx sphinx-rtd-theme myst-parser sphinxcontrib-napoleon** | Este comando instala las librerías necesarias para el proyecto: `Sphinx`, `sphinx-rtd-theme`, `MyST-Parser` y `sphinxcontrib-napoleon`. |
| **pip freeze > requirements.txt** | "pip freeze" enumera todas las dependencias instaladas en el entorno virtual o global de Python. El símbolo `>` redirecciona la salida al archivo `requirements.txt`. Así, este comando guarda las dependencias del proyecto para que otros puedan instalar las mismas y ejecutar el proyecto sin problemas. |
| **sphinx-quickstart docs** | Este comando inicializa el proyecto con Sphinx. El parámetro `docs` indica el directorio donde se quiere ejecutar, en este caso, la carpeta `docs`. Durante la ejecución, el comando solicita separar los archivos fuente (`source`) de los generados (`build`). Se eligió la opción `yes`. También solicita el nombre del proyecto (indicado como "Proyecto Tema 5 Equipo 01"), los autores, la versión (1), y el idioma (español). |
| **cd .\docs** | Cambia el directorio actual a la carpeta `docs`, donde se encuentra el archivo `make.bat`. Este paso es necesario antes de ejecutar los siguientes comandos. |
| **.\make.bat clean** | Limpia todos los archivos temporales y resultados previos de la generación de la documentación, eliminando los contenidos de la carpeta `_build`. |
| **.\make.bat html** | Compila los archivos fuente de la documentación para generar la versión HTML, cuyo resultado se guarda en la carpeta `_build/html`. |
| **sphinx-apidoc -o ./docs src** | Genera archivos `.rst` en la carpeta `docs` a partir del código fuente ubicado en la carpeta `src`. Esto automatiza la creación de documentación para módulos y paquetes de Python. |
| **sphinx-build -b html . ../build/html** | Genera la documentación en formato HTML desde los archivos fuente (`.`) y guarda los resultados en el directorio `../build/html`. |
| **.\make.bat latexpdf**   | Ejecuta el script `make.bat` con la opción `latexpdf`, que compila la documentación en formato LaTeX y la convierte en un archivo PDF.                 |




