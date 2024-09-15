# CrisAssistant - Assistente Virtual do Estudante+

CrisAssistant é uma assistente virtual desenvolvida para o sistema **Estudante+**. Ela utiliza **Python** em conjunto com o **Twilio** para interagir via WhatsApp, o **Google Speech Recognition** para transcrever áudios e o **OpenAI GPT-3.5** para fornecer respostas inteligentes a mensagens de texto e áudio.

## Funcionalidades

- Recepção de mensagens via WhatsApp usando a API do Twilio.
- Respostas automáticas para mensagens de texto com base em palavras-chave.
- Recepção e transcrição de áudios via WhatsApp utilizando o Google Speech Recognition.
- Integração com OpenAI GPT-3.5 para gerar respostas personalizadas com base em mensagens e áudios transcritos.

## Tecnologias Utilizadas

- **Python 3.6+**
- **Flask**: Framework web para criar a API.
- **Twilio API**: Para integração com o WhatsApp.
- **Google Speech Recognition**: Para transcrição de áudios.
- **OpenAI GPT-3.5**: Para geração de respostas baseadas em IA.

## Requisitos

- Python 3.6 ou superior.
- Conta no Twilio (com o WhatsApp habilitado).
- Conta na OpenAI para utilizar a API GPT-3.5.
- Google Speech Recognition para transcrever áudios.

## Instalação e Configuração

### 1. Clonar o repositório

Clone este repositório em seu ambiente local:

````bash
git clone https://github.com/seuusuario/CrisAssistant.git

cd CrisAssistant
````

### 2. Instalar as dependências

Instale as dependências listadas no arquivo ``requirements.txt``:

````bash
pip install -r requirements.txt
````

### 3. Configurar as variáveis de ambiente

Crie um arquivo ``config.py`` ou defina suas credenciais diretamente no código:

````bash
account_sid = 'SEU_ACCOUNT_SID'
auth_token = 'SEU_AUTH_TOKEN'
openai.api_key = 'SUA_API_KEY_OPENAI'
````
Ou configure diretamente em ``app.py``:

````bash
account_sid = 'SEU_ACCOUNT_SID'
auth_token = 'SEU_AUTH_TOKEN'
openai.api_key = 'SUA_API_KEY_OPENAI'
````
### 4. Executar o servidor

Inicie o servidor Flask para que ele comece a receber mensagens via WhatsApp:

````bash
python app.py
````

## Como Funciona

### 1. Interação com WhatsApp:

- O código escuta por mensagens via WhatsApp utilizando a API do Twilio.

- Ele processa mensagens de texto e também verifica se arquivos de mídia (áudios) foram enviados.

### 2. Transcrição de Áudios:

- Quando um áudio é enviado, o bot faz o download do arquivo e o transcreve utilizando o Google Speech Recognition.

### 3. Geração de Respostas Inteligentes:

- O texto transcrito é enviado para a OpenAI, que gera uma resposta inteligente e relevante com base no conteúdo.
