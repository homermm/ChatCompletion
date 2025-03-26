# Servicio de Chat con OpenAI y FastAPI

Este proyecto implementa un servicio web utilizando FastAPI que permite interactuar con el modelo de lenguaje `gpt-4o-mini` de OpenAI. Recibe un prompt y un contexto, los combina y envía la solicitud a la API de OpenAI para obtener una respuesta.

## Instalación

Para ejecutar este servicio, necesitas tener instalado Python y pip. Sigue estos pasos:

1.  **Clona el repositorio:** Si tienes el código en un repositorio Git, clónalo a tu máquina local.

2.  **Crea un entorno virtual (recomendado):** Es una buena práctica crear un entorno virtual para aislar las dependencias del proyecto.

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/macOS
    venv\Scripts\activate  # En Windows
    ```

3.  **Instala las dependencias:** Instala las bibliotecas necesarias individualmente. En este caso, las dependencias son `fastapi`, `uvicorn` y la librería de `openai`.

    ```bash
    pip install fastapi uvicorn openai pydantic python-dotenv
    ```

    * `fastapi`: Framework web moderno y de alto rendimiento para construir APIs.
    * `uvicorn`: Servidor ASGI para ejecutar aplicaciones FastAPI.
    * `openai`: Librería oficial de Python para interactuar con la API de OpenAI.
    * `pydantic`: Biblioteca para la validación de datos.
    * `python-dotenv`: Para cargar variables de entorno desde un archivo `.env`.

4.  **Configura la clave de la API de OpenAI:**

    * La aplicación busca la clave de la API de OpenAI en una variable de entorno llamada `OPENAI_API_KEY`. Puedes establecer esta variable directamente en tu sistema operativo o utilizando un archivo `.env`.

        Para crear un archivo `.env`, crea un archivo en el mismo directorio donde se encuentra tu script Python con el siguiente contenido:

        ```
        OPENAI_API_KEY=tu_clave_de_api_de_openai
        ```


## Ejecución

Para ejecutar el servicio FastAPI, utiliza el siguiente comando desde tu terminal, asegurándote de estar en el directorio del proyecto:

```bash
uvicorn main:app --reload
```

Una vez que el servidor se inicie, podrás acceder a la API en la dirección http://127.0.0.1:8000.

## Pruebas

Puedes probar el servicio utilizando Postman realizando una solicitud HTTP POST al endpoint `/chat-completion/`.

**Pasos para la prueba en Postman:**

1.  **Crea una nueva solicitud:** Abre Postman y crea una nueva solicitud HTTP.
2.  **Selecciona el método POST:** Cambia el método de la solicitud a `POST`.
3.  **Ingresa la URL:** Introduce la URL del endpoint: `http://127.0.0.1:8000/chat-completion/` (asegúrate de que el servidor FastAPI esté en ejecución).
4.  **Ve a la pestaña "Body":** Selecciona la opción "raw" y elige el formato "JSON".
5.  **Ingresa el siguiente cuerpo JSON:**

    ```json
    {
      "prompt": "¿Cuál es la capital de Francia?",
      "contexto": "Responde en inglés."
    }
    ```

6.  **Envía la solicitud:** Haz clic en el botón "Send".

**Respuesta esperada (200 OK):**

Si la solicitud es exitosa y la variable de entorno `OPENAI_API_KEY` está configurada correctamente, el servidor debería devolver una respuesta con un código de estado `200 OK` y el siguiente cuerpo JSON:

```json
{
  "respuesta": "The capital of France is Paris."
}
