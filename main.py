from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Substitua pelo seu token do BotFather
TOKEN = '7923352480:AAE_27YQCZNEo9ioycZKaHk6Np90zYd_nb0'

# Função para responder ao comando /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Olá! Eu sou o bot de agendamento. Como posso ajudar?')

# Função para responder ao comando /agenda
async def agenda(update: Update, context: CallbackContext) -> None:
    comando = ' '.join(context.args)  # Pega os argumentos passados com o comando
    if comando:
        await update.message.reply_text(f"Comando recebido: '{comando}'. Vou agendar isso para você!")
    else:
        await update.message.reply_text("Por favor, forneça um comando válido de agendamento. Exemplo: '/agenda agendar para França em Julho'.")

# Função principal para rodar o bot
async def main():
    # Cria o application com o seu token
    application = Application.builder().token(TOKEN).build()

    # Comandos do bot
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("agenda", agenda))

    # Iniciar o bot
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
