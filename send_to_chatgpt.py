import openai
from transcribe_audio import transcrever_audio

openai.api_key = "KEY OPENAI"

def enviar_prompt(prompt):
    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é CrisAssistant, a assistente virtual do Estudante+. Sua função é auxiliar estudantes e professores com respostas claras e úteis."},
                {"role": "user", "content": prompt}
            ]
        )
        return resposta.choices[0].message['content']
    except Exception as e:
        return f"Ocorreu um erro: {str(e)}"

transcricao = transcrever_audio("audio_message.wav")

if transcricao:
    prompt = f"Esta é a transcrição de um áudio recebido por um estudante ou professor:\n\n{transcricao}\n\nCrisAssistant, por favor, forneça uma resposta útil ou análise com base no conteúdo do áudio."
    resposta = enviar_prompt(prompt)
    print("Resposta da CrisAssistant:")
    print(resposta)
else:
    print("A transcrição do áudio falhou.")
