# 🤖 Meu Chatbot com Gemini

![Python](https://img.shields.io/badge/python-3.13+-blue.svg)
![Poetry](https://img.shields.io/badge/poetry-package_manager-blueviolet)
![Gemini](https://img.shields.io/badge/Google%20AI-Gemini%20Flash-orange)

Este é um projeto que desenvolvi para explorar o universo de **Agentes de IA** e **Python**. A ideia aqui foi criar um chatbot funcional que roda direto no terminal (CLI), conectado à API do Google Gemini.

Focada em boas práticas, a estrutura do projeto já usa **Poetry** organizando com dependências e variáveis de ambiente para segurança.

## 🛠 O que usei aqui?

* **[Python 3.13+](https://www.python.org/)**: Linguagem base.
* **[Google Generative AI](https://ai.google.dev/)**: Modelo `gemini-2.5-flash`.
* **[Poetry](https://python-poetry.org/)**: Para gerenciar os pacotes e ambientes virtuais.
* **[Python-dotenv](https://pypi.org/project/python-dotenv/)**: Pra esconder a API Key e não subir senha no GitHub.

## 📂 Estrutura do Projeto

```text
ai-agents/
├── app.py             # O código principal do chatbot
├── teste_modelos.py   # Script extra para listar modelos disponíveis
├── pyproject.toml     # Onde o Poetry guarda as configurações
├── .env               # Suas chaves secretas (fica no seu PC, não sobe pro Git)
└── README.md          # Este arquivo que você está lendo
```

## 🚀 Como rodar na sua máquina

Se você quiser testar ou usar como base, segue o passo a passo:

### 1. Clone o repositório
```bash
git clone [https://github.com/SEU-USUARIO/ai-agents.git](https://github.com/SEU-USUARIO/ai-agents.git)
cd ai-agents
```

### 2. Instale as dependências
Como estou usando o Poetry:
```bash
poetry install
```

### 3. A parte da Segurança (API Key) 🔐

Eu não deixei minha chave exposta no código (assim como você não deve fazer).

Crie um arquivo chamado .env na raiz do projeto.

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
##
### Desenvolvido por José Cruz 👨‍💻 Estudando Engenharia de Software e explorando IA.
