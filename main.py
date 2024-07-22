import html
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from config import TELEGRAM_TOKEN, OWNER_ID

def start(update: Update, context: CallbackContext):
    user = update.effective_user
    mention = f"<a href='tg://user?id={user.id}'>{html.escape(user.first_name)}</a>"
    update.message.reply_html(f'𝐇𝐞𝐥𝐥𝐨 {mention}! 👋 𝐈'𝐦 𝐲𝐨𝐮𝐫 𝗘𝗱𝗶𝘁 𝗚𝘂𝗮𝗿𝗱𝗶𝗮𝗻 𝗕𝗼𝘁, 𝐡𝐞𝐫𝐞 𝐭𝐨 𝐦𝐚𝐢𝐧𝐭𝐚𝐢𝐧 𝐚 𝐬𝐞𝐜𝐮𝐫𝐞 𝐞𝐧𝐯𝐢𝐫𝐨𝐧𝐦𝐞𝐧𝐭 𝐟𝐨𝐫 𝐨𝐮𝐫 𝐝𝐢𝐬𝐜𝐮𝐬𝐬𝐢𝐨𝐧𝐬.

🚫 𝗘𝗱𝗶𝘁𝗲𝗱 𝗠𝗲𝘀𝘀𝗮𝗴𝗲 𝗗𝗲𝗹𝗲𝘁𝗶𝗼𝗻: 𝗜'𝗹𝗹 𝗿𝗲𝗺𝗼𝘃𝗲 𝗲𝗱𝗶𝘁𝗲𝗱 𝗺𝗲𝘀𝘀𝗮𝗴𝗲𝘀 𝘁𝗼 𝗺𝗮𝗶𝗻𝘁𝗮𝗶𝗻 𝘁𝗿𝗮𝗻𝘀𝗽𝗮𝗿𝗲𝗻𝗰𝘆.

📣 𝗡𝗼𝘁𝗶𝗳𝗶𝗰𝗮𝘁𝗶𝗼𝗻𝘀: 𝗬𝗼𝘂'𝗹𝗹 𝗯𝗲 𝗶𝗻𝗳𝗼𝗿𝗺𝗲𝗱 𝗲𝗮𝗰𝘁𝗶𝗺𝗲 𝘁𝗶𝗺𝗲 𝗮 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝗶𝘀 𝗱𝗲𝗹𝗲𝘁𝗲𝗱.

🌟 𝗚𝗲𝘁 𝗦𝘁𝗮𝗿𝘁𝗲𝗱:
𝟏. 𝐀𝐝𝐝 𝐦𝐞 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐠𝐫𝐨𝐮𝐩.
𝟐. 𝐈'𝐥𝐥 𝐬𝐭𝐚𝐫𝐭 𝐩𝐫𝐨𝐭𝐞𝐜𝐭𝐢𝐧𝐠 𝐢𝐧𝐬𝐭𝐚𝐧𝐭𝐥𝐲.

➡️ 𝐂𝐥𝐢𝐜𝐤 𝐨𝐧 𝗔𝗱𝗱 𝗠𝗲 𝗧𝗼 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽 𝐭𝐨 𝐚𝐝𝐝 𝐦𝐞 𝐚𝐧𝐝 𝐤𝐞𝐞𝐩 𝐨𝐮𝐫 𝐠𝐫𝐨𝐮𝐩 𝐬𝐚𝐟𝐞!

𝐈𝐌 𝐌𝐀𝐃𝐄 𝐁𝐘 @TeamXApex
𝐂𝐑𝐄𝐀𝐓𝐎𝐑 𝐎𝐅 𝐌𝐘 𝐂𝐎𝐃𝐄 𝐈𝐒 @AKIRA_ISHIKKI')

def check_edit(update: Update, context: CallbackContext):
    bot: Bot = context.bot

    # Check if the update is an edited message
    if update.edited_message:
        edited_message = update.edited_message
        
        # Get the chat ID and message ID
        chat_id = edited_message.chat_id
        message_id = edited_message.message_id
        
        # Get the user who edited the message
        user_id = edited_message.from_user.id
        
        # Create the mention for the user
        user_mention = f"<a href='tg://user?id={user_id}'>{html.escape(edited_message.from_user.first_name)}</a>"
        
        # Delete the message if the editor is not the owner
        if user_id != OWNER_ID:
            bot.delete_message(chat_id=chat_id, message_id=message_id)
            
            # Send a message notifying about the deletion
            bot.send_message(chat_id=chat_id, text=f"{user_mention} 𝗷𝘂𝘀𝘁 𝗲𝗱𝗶𝘁 𝗮 𝗺𝗲𝘀𝘀𝗮𝗴𝗲. 𝗜 𝗱𝗲𝗹𝗲𝘁𝗲 𝗵𝗶𝘀 𝗲𝗱𝗶𝘁𝗲𝗱 𝗺𝗲𝘀𝘀𝗮𝗴𝗲.", parse_mode='HTML')

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Start command handler
    dp.add_handler(CommandHandler("start", start))
    
    # Message edit handler
    dp.add_handler(MessageHandler(Filters.update.edited_message, check_edit))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
