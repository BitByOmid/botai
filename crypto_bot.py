import os
import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CommandHandler, ContextTypes
from image_processor import process_image
from technical_analysis import analyze_technical
from fundamental_analysis import analyze_fundamental

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Send me a cryptocurrency chart image for analysis')

async def analyze_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        file = await update.message.photo[-1].get_file()
        await file.download_to_drive('chart.jpg')
        
        # Process image
        crypto_name = process_image('chart.jpg')
        
        # Perform analyses
        fundamental = analyze_fundamental(crypto_name)
        technical = analyze_technical()
        
        # Prepare response
        response = (
            f"1. Name: {fundamental['name']}\n"
            f"2. Category: {fundamental['category']}\n"
            f"3. Current Price: {fundamental['current_price']}\n"
            f"4. Entry Points: {technical['entry_points']}\n"
            f"5. Short-term Target: {technical['short_term']}\n"
            f"6. Medium-term Target: {technical['medium_term']}\n"
            f"7. Long-term Target: {technical['long_term']}"
        )
        
        await update.message.reply_text(response)
        
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")

if __name__ == '__main__':
    application = Application.builder().token(os.getenv('8078650534:AAHtxiQLxJkQBWb8K0wE3C-TONR2xiqc6cc')).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.PHOTO, analyze_image))
    application.run_polling()