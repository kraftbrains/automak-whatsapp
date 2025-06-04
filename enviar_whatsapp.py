import pywhatkit
import datetime
import time

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

# Define o horário inicial para envio (1 minuto à frente do horário atual)
agora = datetime.datetime.now()
hora = agora.hour
minuto = agora.minute + 1

for i, numero in enumerate(numeros):
    # Agenda cada mensagem com 1 minuto de diferença
    send_minute = minuto + i
    send_hour = hora + (send_minute // 60)
    send_minute = send_minute % 60
    pywhatkit.sendwhatmsg(numero, mensagem, send_hour, send_minute, wait_time=10, tab_close=True)
    print(f"Mensagem agendada para {numero} às {send_hour:02d}:{send_minute:02d}")
    time.sleep(5)  # Pequeno intervalo para evitar sobreposição

print("Todas as mensagens foram agendadas para envio no WhatsApp Web.")
