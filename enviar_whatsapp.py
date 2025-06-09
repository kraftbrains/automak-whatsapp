import pywhatkit
import datetime
import time
import random

from numeros import numeros

mensagem = (
    "📣 Advogado(a), você já tem um site profissional?\n\n"
    "Em um mercado cada vez mais competitivo, ter um site próprio é essencial para:\n\n"
    "✅ Construir autoridade e confiança;\n"
    "✅ Ser encontrado no Google por quem busca seus serviços;\n"
    "✅ Passar mais credibilidade que apenas um perfil nas redes sociais;\n"
    "✅ Atender potenciais clientes 24h por dia pelo whatsapp.\n\n"
    "📌 Oferecemos sites profissionais com domínio e hospedagem inclusos.\n\n"
    "Acesse: https://kraftbrains.dev.br/campanhaadvogado\n"
    "Ou responda esta mensagem para saber mais!"
)

emojis = ['😊', '👍', '😉', '👋', '🤝', '🙏']


agora = datetime.datetime.now()
hora = agora.hour
minuto = agora.minute
segundo = agora.second


if segundo > 50:
    minuto += 3
else:
    minuto += 2

for i, numero in enumerate(numeros):

    mensagem_personalizada = f"{mensagem}\n{random.choice(emojis)}"
    send_minute = minuto + i * 2
    send_hour = hora + (send_minute // 60)
    send_minute = send_minute % 60
    pywhatkit.sendwhatmsg(numero, mensagem_personalizada, send_hour, send_minute, wait_time=10, tab_close=True)
    print(f"Mensagem agendada para {numero} às {send_hour:02d}:{send_minute:02d}")
    time.sleep(5)
    if (i + 1) % 10 == 0:
        print("Pausa de segurança para evitar bloqueio...")
        time.sleep(60)

print("Todas as mensagens foram agendadas para envio no WhatsApp Web.")
