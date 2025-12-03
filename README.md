# 🤖 Meu Chatbot com Gemini

Este é um projeto que desenvolvi para explorar o universo de **Agentes de IA** e **Python**. A ideia aqui foi criar um chatbot funcional que roda direto no terminal, conectado à API do Google Gemini.

Focada em boas práticas, a estrutura do projeto já usa **Poetry** para não virar bagunça com dependências e variáveis de ambiente para segurança.

## 🛠 O que usei aqui?

* **Python 3.13+**: Linguagem base.
* **Google Generative AI (Gemini 2.5 Flash)**
* **Poetry**: Para gerenciar os pacotes e ambientes virtuais.
* **Python-dotenv**: Pra esconder a API Key e não subir senha no GitHub.

## 🚀 Como rodar na sua máquina

Se você quiser testar ou usar como base, segue o passo a passo:

### 1. Clone o repositório
```bash
git clone [https://github.com/SEU-USUARIO/ai-agents.git](https://github.com/SEU-USUARIO/ai-agents.git)
cd ai-agents
```
### 2. Instale as dependências
Como estou usando o Poetry, ele resolve tudo com um comando só:
```bash
poetry install
```
### 3. A parte da Segurança (API Key) 🔐
Eu não deixei minha chave exposta no código (assim como você não deve fazer).

Crie um arquivo chamado .env na raiz do projeto (olha o .gitignore pra ver que ele é ignorado pelo Git).

Cole sua chave do Google AI Studio lá dentro assim:
```bash
GENAI_API_KEY="SUA_CHAVE_AQUI"
```

## 🎮 Botando pra rodar
Para iniciar o chat, é só rodar o comando abaixo. O script vai carregar as variáveis e iniciar o loop de conversa:
```bash
poetry run python app.py
```
Se quiser sair, é só digitar "sair" ou "exit".

## Utilitário Extra
Também deixei um script chamado teste_modelos.py. Fiz ele para listar quais versões do Gemini minha conta tem acesso, caso precise trocar o modelo no futuro:
```bash
poetry run python teste_modelos.py
```

Desenvolvido por José Cruz 👨‍💻 Estudando Engenharia de Software e explorando IA.
