# README - Task Tracker
Roadmap.sh: Easy - https://roadmap.sh/projects/task-tracker

## Descripción

**Task Tracker** es una aplicación de línea de comandos sencilla para gestionar tareas desde la terminal. Permite crear, actualizar, eliminar y listar tareas, así como marcar el progreso (pendiente, en progreso o completada).
El proyecto utiliza un archivo `tasks.json` para almacenar los datos localmente sin necesidad de bases de datos externas.

Este proyecto fue desarrollado con el objetivo de practicar:

* Uso de argumentos en CLI.
* Manejo de archivos y persistencia en formato JSON.
* CRUD básico en aplicaciones de consola.
* Buenas prácticas de programación en Python sin librerías externas.


## Características

* **Agregar tareas** con un identificador único.
* **Actualizar** descripciones de tareas.
* **Eliminar** tareas por su ID.
* **Marcar** tareas como *todo*, *in-progress* o *done*.
* **Listar** todas las tareas o filtrarlas por estado.
* **Persistencia automática** en un archivo `tasks.json`.
* **Timestamps** de creación y última actualización.

## Estructura del proyecto

```
task-tracker/
│
├── task-cli.py      # Script principal para ejecutar comandos
├── tasks.json       # Archivo de almacenamiento (se crea al usar la app)
└── README.md        # Documentación del proyecto
```

## Requisitos previos

* Python 3.x instalado en tu sistema.
* Terminal o consola para ejecutar el programa.

## Instalación y uso

1. Clonar el repositorio:

```bash
git clone https://github.com/ovasquezn/roadmap_task_tracker
cd task-tracker
```

2. Dar permisos de ejecución al script:

```bash
chmod +x task-cli.py
```

3. Usar los comandos disponibles:

### Agregar una tarea

```bash
./task-cli.py add "Comprar leche"
```

> Salida: `Task added successfully (ID: 1)`

### Actualizar una tarea

```bash
./task-cli.py update 1 "Comprar pan y leche"
```

### Eliminar una tarea

```bash
./task-cli.py delete 1
```

### Marcar como en progreso

```bash
./task-cli.py mark-in-progress 2
```

### Marcar como completada

```bash
./task-cli.py mark-done 2
```

### Listar todas las tareas

```bash
./task-cli.py list
```

### Listar tareas por estado

```bash
./task-cli.py list todo
./task-cli.py list in-progress
./task-cli.py list done
```

## Ejemplo de `tasks.json`

```json
[
    {
        "id": 1,
        "description": "Comprar leche",
        "status": "todo",
        "createdAt": "2025-07-30 22:31:10",
        "updatedAt": "2025-07-30 22:31:20"
    }
]
```

## Manejo de errores

* Si intentas actualizar, eliminar o marcar una tarea inexistente, el sistema muestra un mensaje de error.
* Si el archivo `tasks.json` está corrupto, se inicializa automáticamente.
