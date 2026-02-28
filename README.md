# Modelado de datos y simulación generada

*Para las instrucciones de como ejecutar el proceso click [aquí](./documentacion/instrucciones.md).*

Diseñar un flujo de validación automatizado utilizando Python, que verifique si las auditorías cumplen con el número mínimo de fotos esperadas según el cliente auditado y las categorías asociadas. El resultado debe mostrarse en un dashboard y además generarse un archivo Excel con las alertas encontradas y enviarse por correo automáticamente desde el notebook.

## Simulación generada

Se realiza una simulación de 21 registros de auditorias usando [google gemini](https://gemini.google.com/). Estos son almacenados en formato `JSON` en [MongoDB](https://www.mongodb.com/), una base de datos NoSQL y de código abierto.

El formato del registro es el siguiente:

```json
{
    "auditoria_id": "Audit_001",
    "fecha": "2023-11-01T08:30:00Z",
    "auditor": "Carlos Ruiz",
    "cliente": { 
        "id": "C01", 
        "nombre": "Cruz Verde", 
        "categorias": [
            "CAT04", 
            "CAT09", 
            "CAT11"
            ] },
    "fotos_registro": [
      { "tipo": "control", "nombre": "inicio" },
      { "tipo": "limpieza", "id": "CAT04" },
      { "tipo": "cuidado personal", "id": "CAT09" },
      { "tipo": "enlatados", "id": "CAT09" },
      { "tipo": "control", "nombre": "fin" }
    ],
  }
```
Todos los detalles pueden ser consultados [aquí](documentacion/simulacion.md).

## Generación de tablas

Después de que la información es almacenada en **MongoDB**, construimos los pipelines para obtener las tablas, los cuales son ejecutados desde Python mediante la librería `pymongo`, dando como resultado las siguientes tablas:

- clientes
- auditoria
- categoria
- cliente categoria
- foto cargada
- fotos requeridas por cliente
- fotos registradas por auditoria
- resumen

El procesamiento de los registros se realiza por medio de pipelines con `pymongo`, librería de Python para interactuar con la base de datos MongoDB. Estos pipelines pueden ser consultados [aquí](./config/pipelines.yaml).

## Generación de tablas

Las tablas son exportadas a un archivo de Excel en la carpeta `data`.
