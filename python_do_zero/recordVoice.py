# Antes de executar o arquivo para gerar o gravador devemos instalar as bibliotecas locais
# pip install souddevice | pip install scipy
# Executando o comando acima.
import sounddevice
from scipy.io.wavfile import write

# Define o tempo de gravação
fs = 44100
second = int(input("Quantos segundos deseja gravar? "))

print("\nGravando............\n")

# Captura a gravação de
record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channel=2)
sounddevice.wait()

# Salva arquivo de gravação
write("gravacao.wav", fs, record_voice)

print("Gravação finalizada!")
