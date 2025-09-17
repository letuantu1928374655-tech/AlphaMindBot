import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Token bot mà Boss lấy từ BotFather
TOKEN = "PASTE_TOKEN_CỦA_BOSS_VÀO_ĐÂY"

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
    # Kết nối bot với Telegram
    app = Application.builder().token(TOKEN).build()

    # Thêm lệnh
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # Chạy bot
    app.run_polling()

if __name__ == "__main__":
    main()
