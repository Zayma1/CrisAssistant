import speech_recognition as sr

def transcrever_audio(arquivo_audio):
    reconhecedor = sr.Recognizer()

    with sr.AudioFile(arquivo_audio) as source:
        audio = reconhecedor.record(source)

        try:
            texto = reconhecedor.recognize_google(audio, language='pt-BR')
            print(f"Transcrição: {texto}")
            return texto
        except sr.UnknownValueError:
            print("Não foi possível entender o áudio.")
            return None
        except sr.RequestError as e:
            print(f"Erro ao se conectar ao serviço de reconhecimento de fala: {e}")
            return None
