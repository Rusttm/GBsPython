import logging
import configparser
import os
import candygame
import tictacgame
import calcgame
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

from telegram import ForceReply, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler

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
        self.current_user_game = dict()
        self.delete_msg_id = 0
        self.game_dict = dict({'nogame': {'function': self.start, 'help': 'Игра не выбрана', 'command': '/start'},
                               'tictaс': {'function': self.GameTicTac, 'help': 'Введите координату', 'command': '/tictac'},
                               'candy': {'function': self.GameCandy, 'help': 'Сколько конфет возьмете?', 'command': '/candy'},
                               'calc': {'function': self.GameCalc, 'help': 'Введите выражение', 'command': '/calc'}
                               })

        self.commands_dict = dict({'/start': '-перезапуск бота',
                                   '/help': '- помощь',
                                   '/tictac': '-игра в крестики-нолики',
                                   '/candy': '-игра в конфетки',
                                   '/calc': 'решение математического выражения'})
        self.NewBot()


    # Define a few command handlers. These usually take the two arguments update and
# context.

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send a message and restart bot when the command /start is issued."""
        self.current_gamer[update.message.from_user.id] = 'nogame'
        user = update.effective_user
        await update.message.reply_html(
            rf"Hi {user.mention_html()}!",
            reply_markup=ForceReply(selective=True),
        )
        msg = '\n'.join([str(f"{key}: {value}") for key, value in self.commands_dict.items()])
        await update.message.reply_html(f"Основные функции:\n {msg}", reply_markup=ForceReply(selective=True))





    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send a message when the command /help is issued."""

        temp_msg = self.game_dict.get(self.current_gamer[update.message.from_user.id], self.game_dict['nogame'])['help']
        await update.message.delete()
        await update.message.reply_text(f"{temp_msg}")

    async def echo(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Echo the user message."""
        logging.info(msg=f"message from: {update.message.chat.first_name}, text: {update.message.text} ")
        current_user_game = self.current_gamer[update.message.from_user.id]
        if current_user_game != 'nogame':
            print(update.message.text)
            result = self.current_user_game[update.message.from_user.id].UserTurn(update.message.text)
            await update.message.reply_text(result[1])
            if result[0] == 'end':
                self.current_gamer[update.message.from_user.id] = 'nogame'
                await update.message.reply_text("Игра закончена нажмите /start для выхода в главное меню")
                await update.message.reply_text(f"Или нажмите {self.game_dict[current_user_game]['command']} для новой игры")
        else:
            await update.message.reply_text(f"Hi {update.message.from_user.first_name}({update.message.from_user.id}) "
                                        f"and you wrote {update.message.text}")
    async def GameTicTac(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """start tictak game"""
        self.current_gamer[update.message.from_user.id] = 'tictaс'
        self.current_user_game[update.message.from_user.id] = tictacgame.XOgame(user_name=update.message.from_user.id)
        await update.message.reply_text("Игра крестики нолики началась. Поле:")
        field = self.current_user_game[update.message.from_user.id].PrintField()
        await update.message.reply_text(field)
        await update.message.reply_text("Чем Вы будете играть? 'O' или 'X'")

    async def GameCandy(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """start tictak game"""
        self.current_gamer[update.message.from_user.id] = 'candy'
        self.current_user_game[update.message.from_user.id] = candygame.CandyGame(user_name=update.message.from_user.id)
        start_msg = self.current_user_game[update.message.from_user.id].StartMessage()
        await update.message.reply_text(start_msg[1])
        await update.message.reply_text("Сколько \U0001F36C возьмете?")

    async def GameCalc(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """start tictak game"""
        self.current_gamer[update.message.from_user.id] = 'calc'
        self.current_user_game[update.message.from_user.id] = calcgame.CalcGame(user_name=update.message.from_user.id)
        await update.message.reply_text("Введите выражение для вычисления")






    def NewBot(self) -> None:
        """Start the bot."""

        # Create the Application and pass it your bot's token.
        self.application = Application.builder().token(TOKEN).build()

        # on different commands - answer in Telegram
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CommandHandler("help", self.help_command))
        self.application.add_handler(CommandHandler("tictac", self.GameTicTac))
        self.application.add_handler(CommandHandler("calc", self.GameCalc))
        self.application.add_handler(CommandHandler("candy", self.GameCandy))
        self.application.add_handler(CommandHandler("stop", self.start))

        # on non command i.e message - echo the message on Telegram
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.echo))

        # Run the bot until the user presses Ctrl-C
        self.application.run_polling()




if __name__ == "__main__":
    bot_run = JohnBotGB()