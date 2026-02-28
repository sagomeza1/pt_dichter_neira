[[Volver al inicio](../README.md)]

# Instrucciones

Previamente se debe: O tener instalado MongoDB y ejecutarse de forma local, o tener el acceso a algún servicio de MongoDB en la nube.

Si tenemos acceso a un servicio en la nube, la `uri` debe ser almacenada en `.env` en la carpeta `config` con el siguiente formato:

`URI=<TU URI DE MONGO AQUI>`

Una vez tenemos acceso al servicio de MongoDB, ejecutamos [registros.mongodb](../script_mongodb/registros.mongodb), ya que esto simulara los registros debemos tener.

1. Genere un entorno virtual.
    ```python
    python -m venv venv
    ```
2. Active el `venv`.
    ```python
    source venv/bin/activate
    ```

3. Instale las dependencias necesarias.
    ```python
    pip install -r requirements.txt
    ```
4. Ejecute
    ```python
    python main.py
    ```