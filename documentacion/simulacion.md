[[Volver al inicio](../README.md)]

# Simulación

Se realizo simulación de los registros usando el siguiente prompt:

## Prompt

```
<contexto>
    Una compañia realiza auditorías de campo en cadenas de supermercados.
    Como parte del proceso se registran fotografías por cada categoría
    auditada, juntos con dos fotos obligatorias de inicio y fin de la
    auditoría.
</contexto>

<detalles>
    <tablas>
        <tabla-clientes>
            <detalles>
                Debe tener el ID y el nombre del cliente
            </detalles>
            <cantidad-registros>
                7
            </cantidad-registros>
        </tabla-clientes>

        <tabla-categorias>
            <detalles>
                Debe tener el ID y el nombre de la categoría
            </detalles>
            <cantidad-registros>
                12
            </cantidad-registros>
        </tabla-categorias>

        <tabla-cliente-categorias>
            <detalles>
                Indica que categoría audita cada cliente
            </detalles>

        </tabla-cliente-categorias>

        <tabla-auditorias>
            <detalles>
                Debe tener el ID, la fecha, el nombre del auditor
                responsable, cliente al que pertenece el auditor
            </detalles>
            <cantidad-registros>
                21
            </cantidad-registros>
        </tabla-auditorias>

        <tabla-fotos>
            <detalles>
                Registro de fotos subidas por auditoría y categoría
            </detalles>
            <cantidad-registros>
                21
            </cantidad-registros>
        </tabla-fotos>
    </tablas>

    <ejemplos>
        <ejemplo-1>
            El cliente 'Cruz Verde' audita 3 categorías, por lo tanto, se esperan mínimo 5 fotos (3 categorías + 2 de control).
        </ejemplo-1>

        <ejemplo-2>
            El cliente 'Embonor' audita 5 categorías, se esperan mínimo 7 fotos.
        </ejemplo-2>
    </ejemplos>

    <formato1>
        Genera la información en formato json, listo para ser consumido en MongoDB.
    </formato1>

    <formato2>
        Genera la información de forma tabular, de forma que sea sencillo entender la información.
    </formato2>    

    <consideraciones>
        <consideracion-1>
            Una auditoría con menos fotos que el mínimo esperado según el cliente se considera un caso de alerta.
        </consideracion-1>

        <consideracion-2>
            En la generación del conjunto de datos, el 14% de las auditorías deben contar con menos fotos del mínimo esperado.
        </consideracion-2>
    </consideraciones>

</detalles>

<tarea>
    Genera una base de datos simulada de acuerdo al contexto y los detalles.
</tarea>
```
## Resultado

### Formato registro y consideraciones
Se obtiene 21 registros con el siguiente formato:
```json
  {
    "auditoria_id": "Audit_001",
    "fecha": "2023-11-01T08:30:00Z",
    "auditor": "Carlos Ruiz",
    "cliente": { "id": "C01", "nombre": "Cruz Verde" },
    "configuracion": { "categorias": ["CAT04", "CAT09", "CAT11"], "min_fotos": 5 },
    "fotos_registro": [                                            ^----- Atributo para eliminar
      { "tipo": "control", "nombre": "inicio" },
      { "tipo": "categoria", "id": "CAT04" },   <------ Atributo para cambiar tipo
      { "tipo": "categoria", "id": "CAT09" },   <------ Atributo para cambiar tipo
      { "tipo": "categoria", "id": "CAT11" },   <------ Atributo para cambiar tipo
      { "tipo": "control", "nombre": "fin" }
    ],
    "conteo_total": 5,          <------ Atributo para eliminar
    "estado_alerta": false      <------ Atributo para eliminar
  }
```
Se eliminan los atributos indicados para obtener estos datos mediante el procesamiento de los datos:
```json
  {
    "auditoria_id": "Audit_001",
    "fecha": "2023-11-01T08:30:00Z",
    "auditor": "Carlos Ruiz",
    "cliente": { "id": "C01", "nombre": "Cruz Verde" },
    "configuracion": { "categorias": ["CAT04", "CAT09", "CAT11"]},
    "fotos_registro": [                                           
      { "tipo": "control", "nombre": "inicio" },
      { "tipo": "categoria", "id": "CAT04" },   <------ Atributo para cambiar tipo
      { "tipo": "categoria", "id": "CAT09" },   <------ Atributo para cambiar tipo
      { "tipo": "categoria", "id": "CAT11" },   <------ Atributo para cambiar tipo
      { "tipo": "control", "nombre": "fin" }
    ],
  }
```
Por otro lado, además de los registros en formato `JSON`, entrega varias tablas, una de estas es la tabla categorías:

### Tabla categorías

Se genera la siguiente tabla:

|  ID  |  Nombre de la categoría  |
|:--:|:----------------------:|
|CAT01| Lácteos|
|CAT02| Bebidas|
|CAT03| Snacks|
|CAT04| Limpieza|
|CAT05| Mascotas|
|CAT06| Carnes|
|CAT07| Panadería|
|CAT08| Congelados|
|CAT09| Cuidado Personal|
|CAT10| Frutas y Verduras|
|CAT11| Enlatados|
|CAT12| Vinos y Licores|

La cual es considerada unicamente para cambiar el nombre a los atributos indicados.

Considerando lo explicado anteriormente, el atributo `categorias` no tiene sentido que se encuentre anidado en el atributo `configuracion`, por tanto, el atributo `configuracion` es eliminado, y la el atributo `categorias` pasa a ser un atributo anidado del atributo `cliente`.

El formato de los registros queda como sigue:

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

Los valores eliminados serán obtenidos mediante el procesamiento de datos, y la tabla de tabla será obtenida al igual que el resto de tablas mediante el análisis de los registros.

## Almacenamiento en MongoDB

Estos registros son almacenados en una base de datos con el mobre `dyn`, en la colección `registros`. El script que ejecuta el proceso de almacenamiento puede ser consultado [aquí](../script_mongodb/registros.mongodb). Este es ejecutado desde VSCode con una extensión propia de MongoDB.