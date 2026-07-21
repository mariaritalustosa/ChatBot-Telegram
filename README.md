# PyChat — Telegram Bot + OpenRouter AI

O **PyChat** é um bot de Telegram simples e funcional desenvolvido em Python. Ele utiliza a biblioteca `pyTelegramBotAPI` para interagir no Telegram e integra-se à API do **OpenRouter** (utilizando o modelo `openai/gpt-oss-20b:free`) para responder dúvidas e bater papo com os usuários em tempo real.

---

## Tecnologias Utilizadas

- **[Python](https://www.python.org/)**
- **[OpenRouter API](https://openrouter.ai/)** 

---

## Pré-requisitos

1. **Python 3** instalado.
2. Token do bot do Telegram gerado via [@BotFather](https://t.me/BotFather).
3. Chave de API (*API key*) gerada na plataforma do [OpenRouter](https://openrouter.ai/).

---

## Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/mariaritalustosa/ChatBot-Telegram.git
cd chatbot
```

### 2. Criar e ativar o ambiente virtual
```bash
# Linux / macOS:
python3 -m venv venv
source venv/bin/activate

# Windows:
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar as dependências
```bash
pip install pyTelegramBotAPI python-dotenv requests
```

### 4. Configurar as variáveis de ambiente
Crie um arquivo chamado .env na raiz do seu projeto contendo suas chaves:
```bash
token_telegram=seu_token_bot_father
key_open_router=sua_key_open_router
```

### 5. Executar o bot
```bash
python chatbot.py
```
