# run.py
import os
import json
import logging
import aiofiles

from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from utils.db_handler import DBManager

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

admin_id = None

# Database definition
order_definition = {
    'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
    'uid': 'INTEGER',
    'order_items': 'TEXT',
    'order_total': 'REAL',
    'order_paid': 'INTEGER',  # 0 for False, 1 for True
    'client_name': 'TEXT',
    'client_address': 'TEXT',
    'tracking_sent': 'INTEGER',  # 0 for False, 1 for True
    'td_received': 'TEXT',
    'timedate': 'TEXT'
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if admin_id is None:
        admin_setup_msg = "Run /setup to add the first admin. This should be the Owner of the Channel/Group."
        update.message.reply_text(admin_setup_msg)
    
    await update.message.reply_text(
        'Welcome! Click below to open the Mini App:',
        reply_markup=ReplyKeyboardMarkup.from_button(
            KeyboardButton(
                text="STONEDWAY Menu",
                web_app=WebAppInfo(url="http://127.0.0.1:8080/"),
            )
        ),
    )
    
async def load_config():
    async with aiofiles.open('config.json', 'r') as file:
        config_data = await file.read()
        return json.loads(config_data)

async def web_app_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Handle order data received from the web app and enter to DB
    pass

async def get_my_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    await update.message.reply_text(f"Your User ID is: {user_id}")

async def save_admin_id():
    global admin_id
    config['ADMIN_ID'] = admin_id
    async with aiofiles.open('config.json', 'w') as file:
        await file.write(json.dumps(config, indent=4))


def load_admin_id():
    return config.get('ADMIN_ID')

async def get_orders(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global admin_id
    user_id = update.message.from_user.id
    if user_id == admin_id:
        orders = await fetch_orders_from_db()   # Make sure this function is async too
        message = format_orders(orders)         # This can remain synchronous if it's just formatting
        await update.message.reply_text(message)
    else:
        await update.message.reply_text("You are not authorized to view orders.")


async def setup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global admin_id
    setup_password = config['ADMIN_ID']
    user_provided_password = ' '.join(context.args)

    if admin_id is not None:
        await update.message.reply_text("Admin has already been set up.")
        return

    if user_provided_password == setup_password:
        admin_id = update.message.from_user.id
        config['ADMIN_ID'] = str(admin_id)
        await update.message.reply_text(f"Admin ID set to {admin_id}.")
    else:
        await update.message.reply_text("Incorrect setup password. Unauthorized access attempt logged.")


async def main():
    global admin_id
    
    # Database setup
    db_manager = DBManager('backend/telegram_project/db.sqlite3')
    with db_manager.create_connection() as conn:
        db_manager.create_table(conn, 'orders', order_definition)
    
    app = Application.builder().token(config['TELEGRAM_BOT_TOKEN']).build()
    
    admin_id = load_admin_id()

    app.add_handler(CommandHandler('getmyid', get_my_id))
    app.add_handler(CommandHandler('setup', setup))
    app.add_handler(CommandHandler('orders', get_orders))
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, web_app_data))

    await app.run_polling()

if __name__ == '__main__':
    config = asyncio.run(load_config())
    admin_id = load_admin_id()
    asyncio.run(main())
