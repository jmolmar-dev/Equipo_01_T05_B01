# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Proyecto Tema 5 Equipo 01'
copyright = '2025, Juan Molero Marin'
author = 'Juan Molero Marin'
release = '1'


# Importamos módulos para configurar rutas y extensiones
import os  # Módulo para gestionar rutas del sistema operativo
import sys  # Módulo para modificar el path de búsqueda de Python
import sphinx_rtd_theme  # Tema para mejorar el diseño visual de la documentación

# Configurar la ruta al directorio raíz del proyecto
# os.path.abspath('../') obtiene la ruta absoluta del directorio superior al actual
# sys.path.insert(0, ...) añade esta ruta al inicio de sys.path, que es donde Python busca los módulos
sys.path.insert(0, os.path.abspath('../../'))


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',  # Genera documentación automáticamente desde docstrings
    'sphinx.ext.napoleon',  # Interpreta docstrings en formatos Google y NumPy
    'sphinx.ext.viewcode',  # Agrega enlaces al código fuente en la documentación generada
    'sphinx_rtd_theme',  # Tema visual basado en Read the Docs
    'myst_parser',
    'sphinx.ext.autodoc'
]


latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'fontpkg': r'\usepackage{times}',
    'preamble': r'\usepackage{fancyhdr}',  # Puedes añadir o quitar paquetes aquí
    'figure_align': 'htbp',  # Esto ayuda a que las imágenes se alineen correctamente
    'maketitle': r'\maketitle\newpage',  # Esto puede ayudar a evitar la página en blanco
    'secnumdepth': 0,  # Desactiva la numeración de secciones y subsecciones
    'tableofcontents': '',  # Deja el índice sin numeración
    'preamble': r'''
        \setcounter{secnumdepth}{0}  % Esto elimina la numeración de las secciones
    ''',  # Reconfigura la numeración de secciones para desactivarla
}


latex_documents = [
    ('index', 'proyecto_tema_5_boletin_1.tex', 'Proyecto Tema 5 Boletín 1', 'Autor', 'manual'),
]


# Configuración para soportar múltiples tipos de archivos fuente
source_suffix = {
    '.rst': 'restructuredtext',  # Archivos en formato reStructuredText
    '.md': 'markdown',  # Archivos en formato Markdown
}


templates_path = ['_templates']
exclude_patterns = ['_backup', 'deployment']

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


