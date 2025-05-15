# Análisis de Patrones en Archivos de Texto (TFG)

Este proyecto de **Trabajo de Fin de Grado (TFG)** se centra en el **análisis de patrones** en **archivos de texto**, utilizando **feeds RSS** para obtener y procesar información. El propósito es identificar patrones y tendencias en los datos proporcionados por estos archivos.

## Descripción del Proyecto

El objetivo de este proyecto es analizar los contenidos de archivos RSS y extraer las etiquetas `title` y `description`, para analizar el significado de ciertas palabras o expresiones.

## Pasos Realizados hasta el Momento

Hasta ahora, se han realizado los siguientes pasos:

1. **Exploración de Feeds RSS**: Comprensión del formato y estructura de los archivos RSS.
2. **Recopilación de URLs**: Se han recopilado las URLs de 6 RSS de los periódicos más importantes de España, para obtener de forma rápida un dataset extenso.
3. **Extracción de información de RSS**: Uso de Python para leer y extraer **títulos** y **descripciones** de los artículos de diversos feeds RSS.
4. **Documentación**: Elaboración de documentación básica sobre el proyecto.
5. **Scripts**: Los scripts de los que hablaré a continuación representan de forma sencilla, explicada y paso a paso cómo se han ido consiguiendo los objetivos del proyecto.

   - `data.py`: Este script fue el primero, usado simplemente para obtener el contenido de las etiquetas "Title" y "Description" del RSS de un solo periódico.
   - `data2_0.py`: Este fue el segundo script, obtiene las mismas etiquetas, pero ahora no solo de un periódico. Lo obtiene de una lista concreta de un archivo .txt.
   - `data3_0.py`: Este es el tercer script, el cual hace lo mismo que los anteriores (Reutilizando codigo) y hemos añadido que los RSS se descarguen en formato .xml y se guarden en local en las rutas proporcionadas.
   - `data4_0.py`: Este es el cuarto script, hace exactamente lo mismo que el tercero solo que descargo los RSS en formato .csv. Formato necesario para subir los ficheros a la BBDD (MongoDB).
   - `mongo_collections.py`: Este script se encarga de generar automaticamente las colecciones y las carpetas de la BBDD (MongoDB), y se añaden los ficheros.

## Tecnologías y Herramientas Utilizadas

- **Python**: Lenguaje principal utilizado para el procesamiento y análisis de los datos.
- **VS Code**: Entorno de desarrollo utilizado para programar y gestionar el proyecto.
- **GitHub**: Control de versiones y almacenamiento de código.
- **MongoDB**: BBDD para almacenar etiquetas de interés de los RSS.




