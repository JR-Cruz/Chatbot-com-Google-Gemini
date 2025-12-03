import google.generativeai as genai
import os
import sys
from dotenv import load_dotenv

def configurar_modelo():
    load_dotenv()
    api_key = os.getenv("GENAI_API_KEY")

    if not api_key:
        print("Erro: Variável GENAI_API_KEY não encontrada no arquivo .env")
        return None

    print("Chave de API carregada com sucesso.")
    genai.configure(api_key=api_key)

    return genai.GenerativeModel('models/gemini-2.5-flash')

def rodar_chat(model):
    chat = model.start_chat(history=[])
    print("\n--- Chat Iniciado (Digite 'sair' para encerrar) ---")

    while True:
        try:
            texto_usuario = input("\nVocê: ")
            
            if texto_usuario.strip().lower() in ["sair", "exit"]:
                print("Encerrando o chat...")
                break
            
            if not texto_usuario.strip():
                continue

            response = chat.send_message(texto_usuario)
            print(f"Bot: {response.text}")

        except Exception as e:
            print(f"Ocorreu um erro na comunicação: {e}")

def main():
    modelo = configurar_modelo()
    
    if modelo:
        rodar_chat(modelo)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()