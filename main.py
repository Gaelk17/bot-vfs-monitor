from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Substitua pelo seu token do BotFather
TOKEN = '7923352480:AAE_27YQCZNEo9ioycZKaHk6Np90zYd_nb0'

# Função para responder ao comando /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Olá! Eu sou o bot de agendamento. Como posso ajudar?')

# Função para responder ao comando /agenda
def agenda(update: Update, context: CallbackContext) -> None:
    comando = ' '.join(context.args)  # Pega os argumentos passados com o comando
    if comando:
        update.message.reply_text(f"Comando recebido: '{comando}'. Vou agendar isso para você!")
    else:
        update.message.reply_text("Por favor, forneça um comando válido de agendamento. Exemplo: '/agenda agendar para França em Julho'.")

# Função principal para rodar o bot
def main():
    # Cria o updater com o seu token
    updater = Updater(TOKEN)

    # Obter o dispatcher para registrar os handlers
    dispatcher = updater.dispatcher

    # Comandos do bot
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("agenda", agenda))

    # Iniciar o bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
