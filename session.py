import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define your token (replace 'YOUR_BOT_TOKEN' with your actual bot token)
TOKEN = '6670342404:AAHwMhGtlwGdl7ys4vcF_w03jviSgO7EYxM'

# Define command callback functions
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Generate Program", callback_data='generate')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Welcome to the Program Generator Bot!\nPress the button to generate a program session.", reply_markup=reply_markup)

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == 'generate':
        session = generate_program_session()  # Replace this with your program session generation logic
        query.edit_message_text(text="Generated Program Session:\n" + session)

def generate_program_session():
    # Replace this with your program session generation logic
    session = "Sample program session:\n- Morning: Jogging\n- Afternoon: Coding\n- Evening: Reading"
    return session

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Define command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    
    # Define callback query handler
    dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
