import yandex.cloud.compute.v1 as compute_v1
from telegram import Bot, Update
from telegram.ext import CommandHandler, Updater, CallbackContext

def start_vm(update: Update, context: CallbackContext):
    # Get the VM ID from the command arguments
    vm_id = context.args[0]
    
    # Create the Compute API client
    compute_api = compute_v1.ComputeServiceClient(credentials=credentials)
    
    # Start the VM
    op = compute_api.start_instance(vm_id)
    op.result()
    
    # Send a confirmation message to Telegram
    update.message.reply_text(f"VM {vm_id} is starting")

def main():
    # Set up the Telegram bot
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    
    # Add the start_vm command handler
    dp.add_handler(CommandHandler("start_vm", start_vm))
