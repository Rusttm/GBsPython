import logging
import configparser
import os

try:
    # get data from in file
    conf = configparser.ConfigParser()
    #conf.read('config.ini')
    conf.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
    TOKEN = conf['TOKENS']['telegram']

except IndexError:
    print('Error, cant read .ini file')

from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO,
    filename='bot.log', filemode='a'
)
logger = logging.getLogger(__name__)

class JohnBotGB():
    def __init__(self):
        self.project = False
        self.current_gamer = dict() # 'user_id' : 'tictac', calc or false
        self.delete_msg_id = 0
        self.game_dict = dict({'noname': {'function': self.start, 'help': 'Игра не выбрана'},
                               'tictaс': {'function': self.GameTicTac, 'help': 'Введите координату'},
                               'calc': {'function': self.GameCalc, 'help': 'Введите выражение'}})

        self.commands_dict = dict({'/start': '-перезапуск бота',
                                   '/help': '- помощь',
                                   '/tictac': '-игра в крестики-нолики',
                                   '/calc': 'решение математического выражения'})
        self.NewBot()

    # Define a few command handlers. These usually take the two arguments update and
# context.

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send a message and restart bot when the command /start is issued."""
        self.current_gamer[update.message.from_user.id] = 'noname'
        user = update.effective_user
        await update.message.reply_html(
            rf"Hi {user.mention_html()}!",
            reply_markup=ForceReply(selective=True),
        )
        msg = '\n'.join([str(f"{key}: {value}") for key, value in self.commands_dict.items()])
        await update.message.reply_html(f"Основные функции:\n {msg}", reply_markup=ForceReply(selective=True))


    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send a message when the command /help is issued."""

        temp_msg = self.game_dict.get(self.current_gamer[update.message.from_user.id], self.game_dict['noname'])['help']
        await update.message.delete()
        await update.message.reply_text(f"{temp_msg}")


    async def echo(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Echo the user message."""
        logging.info(msg=f"message from: {update.message.chat.first_name}, text: {update.message.text} ")
        await update.message.reply_text(f"Hi {update.message.from_user.first_name}({update.message.from_user.id}) "
                                        f"and you wrote {update.message.text}")
    async def GameTicTac(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """start tictok game"""
        self.current_gamer[update.message.from_user.id] = 'tictaс'
        await update.message.reply_text("Игра крестики нолики началась -Ваш ход")

        await update.message.reply_text("Игра крестики нолики закончена. Досвидания!")

    async def GameCalc(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """start tictok game"""
        self.current_gamer[update.message.from_user.id] = 'calc'
        await update.message.reply_text("Введите выражение для вычисления")





    def NewBot(self) -> None:
        """Start the bot."""

        # Create the Application and pass it your bot's token.
        application = Application.builder().token(TOKEN).build()

        # on different commands - answer in Telegram
        application.add_handler(CommandHandler("start", self.start))
        application.add_handler(CommandHandler("help", self.help_command))
        application.add_handler(CommandHandler("tictac", self.GameTicTac))
        application.add_handler(CommandHandler("calc", self.GameCalc))
        # on non command i.e message - echo the message on Telegram
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.echo))

        # Run the bot until the user presses Ctrl-C
        application.run_polling()




if __name__ == "__main__":
    bot_run = JohnBotGB()