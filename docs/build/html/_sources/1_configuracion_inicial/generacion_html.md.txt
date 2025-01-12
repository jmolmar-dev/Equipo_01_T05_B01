# 1.8. Generación de HTML a partir de la documentación
 
Una vez tengamos todo listo para generar nuestra documentación, será momento de efectuar el siguiente comando por consola: 

```bash
    sphinx-build -b html . ../build/html 
```

Donde: 

| **Parámetro/Parte**      | **Descripción**                                                                                         |
|--------------------------|---------------------------------------------------------------------------------------------------------|
| **sphinx-build**         | Herramienta de Sphinx con la cual generaremos la documentación.                                         |
| **-b**                   | Indicador para especificar el formato en el cual se generará la documentación.                          |
| **html**                 | Formato respectivo en el que vamos a generar la documentación.                                          |
| **.**                    | Directorio actual donde nos encontramos. En este caso, se ejecuta desde la carpeta source.              |
| **../build/html**        | Ruta hacia el directorio donde queremos que se guarden los archivos resultantes.                        |

----------

Una vez efectuado el comando, se nos generará nuestra documentación en HTML respectivamente, dentro del subdirectorio **html** ubicado en **/build**. Aunque se nos generán varios archivos, realmente nos centraremos en el _**index.html**_, el cual si lo visualizamos podemos observar como ya contendría el índice principal con el cual podemos acceder a nuestra documentación:

![Mi_imagen](../_static/indice.png)


