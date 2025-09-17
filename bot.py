import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv  # Đọc biến môi trường

# Load biến môi trường từ file .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Bật log (để kiểm soát lỗi)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Lệnh /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Xin chào Boss 🐺, AlphaMind Bot đã sẵn sàng phục vụ!")

# Lệnh /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Các lệnh hiện có:\n/start - Khởi động bot\n/help - Xem trợ giúp")

def main():
    # Kết nối bot với Telegram bằng token trong .env
    app = Application.builder().token(TOKEN).build()

    # Thêm lệnh
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # Chạy bot
    app.run_polling()

if __name__ == "__main__":
    main()
