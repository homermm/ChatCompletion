import os
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

# Configuramos la aplicación FastAPI
app = FastAPI()

# Configuramos la API Key de OpenAI
openai_api_key = os.getenv("OPENAI_API_KEY")  # Clave de la API de OpenAI en variable de entorno

client = OpenAI(api_key=openai_api_key)

# Clase para recibir los datos en la solicitud
class ChatRequest(BaseModel):
    prompt: str
    contexto: str

@app.post("/chat-completion/")
async def chat_completion(request: ChatRequest):
    prompt = request.prompt
    contexto = request.contexto

    # Combinamos el contexto y el prompt
    full_prompt = f"{contexto}\n\n{prompt}"

    try:
        # Realizamos la llamada a la API con el cliente OpenAI
        response = client.responses.create(
            model="gpt-4o-mini",
            instructions="You are a helpful assistant.",  # Se puede poner un contexto general
            input=full_prompt  # El prompt combinado (contexto + pregunta)
        )

        # Extraemos y devolvemos la respuesta generada
        respuesta = response.output_text.strip()
        return {"respuesta": respuesta}

    except Exception as e:
        return {"error": str(e)}