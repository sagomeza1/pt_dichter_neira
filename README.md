# Modelado de datos y simulación generada

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


