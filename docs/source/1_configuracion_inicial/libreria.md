# 1.2 Instalación y Funcionamiento de las Librerías necesarias:

Para la realización de este proyecto de documentación, hemos necesitado las siguientes librerías:

| **Librería**              | **Descripción**                                                                                                                                                                                                 |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Sphinx**                | Herramienta para generar documentación en formatos como HTML o PDF. Soporta archivos en reStructuredText o Markdown, y es ideal para la documentación de proyectos de software.                                |
| **Sphinx-rtd-theme**      | Permite aplicar el tema Read the Docs en Sphinx, proporcionando un diseño limpio y profesional. Es utilizado como estándar en la documentación.                                                                |
| **MyST-Parser**           | Extiende a Sphinx para procesar archivos Markdown, además de reStructuredText, ofreciendo mayor flexibilidad a los usuarios.                                                                                   |
| **Sphinxcontrib-napoleon**| Extensión que facilita la integración de docstrings escritos en los estilos de Google o Numpy. Convierte estos formatos automáticamente al adecuado para el framework.                                          |

Para la instalación, se ha efectuado el siguiente comando: 

```bash
pip install sphinx sphinx-rtd-theme myst-parser sphinxcontrib-napoleon 
```

Cabe destacar que debemos de tener el **Entorno Virtual** activado en el momento de instalar dichas Librerías. Una vez se hayan instalado, el siguiente paso será plasmarlo dentro de un archivo de requisitos, _**requirements.txt**_, con el objetivo de que cualquiera pueda emplearlo en el futuro para poder realizar el mismo proyecto. Para eso se crea el archivo de texto plano en la raíz del proyecto, y posteriormente ejecutamos: 

```bash
pip freeze > requirements.txt
```