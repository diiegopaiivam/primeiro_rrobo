import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

#função para ouuvir e reconhecer a fala startando o microfone
def start_microfone():
    #Instanciando o microfone
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Vamos conversar?:")
        audio = microfone.listen(source)
    try: 
        frase = microfone.recognize_google(audio, language='pt-BR')
        arquivo = open("plano_aula.txt", "a")
        arquivo.write(frase)
        
    except sr.UnkownValueError:
        print("Não entendi") 

    return frase

#Funcao responsavel por reproduzir a frase dita pelo usuario
def cria_audio(audio):

    audio_final = "você falou" + audio
    tts = gTTS(audio_final,lang='pt-br')

    #Salva o arquivo de audio em mp3
    tts.save('audio.mp3')

    #Executa o audio
    playsound('audio.mp3')

frase = start_microfone()
cria_audio(frase)