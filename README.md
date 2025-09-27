# Análisis de Patrones en Archivos de Texto (TFG)

Este proyecto de **Trabajo de Fin de Grado (TFG)** se centra en el **análisis de patrones** en **archivos de texto**, utilizando **feeds RSS** para obtener y procesar información. El propósito es identificar patrones y tendencias en los datos proporcionados por estos archivos.

## Descripción del Proyecto

El objetivo de este proyecto es analizar los contenidos de archivos RSS y extraer las etiquetas `title` y `description`, almacenar estos campos de interés en una base de datos, para posteriormente extraer estos datos mediante una API, y, por último, detectar las referencias al concepto mencionado usando y comparando el rendimiento de distintos LLMs, intentando hacer reproducible el escenario en un equipo con recursos limitados.

## Tecnologías y Herramientas Utilizadas

- **Python**: Lenguaje principal utilizado para el procesamiento y análisis de los datos.
- **VS Code**: Entorno de desarrollo utilizado para programar y gestionar el proyecto.
- **GitHub**: Control de versiones y almacenamiento de código.
- **MongoDB**: BBDD para almacenar etiquetas de interés de los RSS.
- **Docker**: Implementacion y gestión de códigos en contenedores.
- **Flask**: Microframework de Python usado para la creación de la API.
- **Ollama**: Plataforma que permite la ejecución de LLMs en local.

## Estructura del Repositorio

- **tfg_python/** → Contiene los scripts de procesamiento de los feeds RSS.  
- **tfg_api/** → Implementación de la API REST con Flask, que permite acceder a los datos almacenados.  
- **tfg_mongo/** → Archivos relacionados con la configuración y conexión a la base de datos MongoDB.  
- **progreso_codigos/** → Carpeta de trabajo con iteraciones y pruebas realizadas durante el desarrollo.  

- **docker-compose.yml** → Orquesta los contenedores (tfg_api, tfg_mongo y tfg_python) para facilitar la ejecución del proyecto.  
- **procesar3_0.py** → Script principal para lanzar el procesamiento de los datos por un modelo específico de Ollama.  
- **resultados.txt** → Ficheros con ejemplos de salida obtenida en distintas ejecuciones con distintos modelos.  
- **rss_manual.json** → Ejemplo de archivo RSS utilizado como muestra para pruebas.

## Ejecución del Proyecto

Asegúrate de tener **Docker** y **Docker Compose** instalados.  
En la raíz del proyecto, ejecuta:

```bash
docker-compose up --build
```
Una vez montado el escenario, tendríamos que ejecutar el script de cada contenedor, y ya estaría funcionando.
IMPORTANTE: El script de recoleccion de datos (tfg_python), tiene dos modos de ejecución:

1. **[Bajo demanda]**  
   ```bash
   python3 data10_0.py
   ```

2. **[Modo periódico]**  
   ```bash
   python3 data10_0.py --duracion 'TIEMPO EN MINUTOS' --intervalo 'INTERVALO EN MINUTOS'
   ```