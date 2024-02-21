# Guía de inicio

## backend 
1. Introducción

Este archivo README te guiará a través de la configuración de tu entorno Python y la instalación de los requisitos necesarios para ejecutar un proyecto. Se asume que tienes conocimientos básicos de Python y manejo de línea de comandos.
2. Entorno Python

2.1. Opciones:

    Virtualenv: Crea un entorno virtual aislado para el proyecto, recomendado para mayor control y evitar conflictos con otras instalaciones de Python.
 
2.2. Recomendación:

Para la mayoría de proyectos, se recomienda usar virtualenv.

2.3. Instalación de virtualenv:

`pip install virtualenv`

2.4. Creación de un entorno virtual:

`virtualenv venv`

2.5. Activación del entorno virtual:

`source venv/bin/activate`

2.6. Desactivación del entorno virtual:

deactivate

3. Instalación de Requerimientos

3.1. Archivo requirements.txt:

Este archivo contiene una lista de las bibliotecas y dependencias necesarias para ejecutar el proyecto.

3.2. Instalación de paquetes:

`pip install -r requirements.txt`

3.3. Actualización de paquetes:

`pip install -r requirements.txt --upgrade`

4. Verificación

Para verificar que la configuración se ha realizado correctamente, puedes ejecutar el comando:

`python -m pip list`

Este comando mostrará una lista de las bibliotecas instaladas en tu entorno Python.

## frontend

Al momento de clonar el repositorio se debe ejecutar en la carpeta del frontend
`npm install` 
