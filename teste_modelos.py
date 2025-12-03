import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GENAI_API_KEY")

if api_key:
    print("Chave de API carregada com sucesso.")
else:
    print("Erro ao carregar a chave de API. Verifique o arquivo .env.")
    
genai.configure(api_key=api_key)

print("Modelos disponíveis para você:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)