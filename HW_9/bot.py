from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import tg_token


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{update.effective_user.first_name}, Вас приветствует многофункциональный бот.'
                                    f'\n/conv Переводит числа в двоичное представление.'
                                    f'\n/code Кодирует Ваше сообщение RLE алгоритмом.'
                                    f'\n/nf Создаст для Вас список чисел негафибоначчи.'
                                    f'\n/help Для вызова справки.')


async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f'\n/conv Переводит числа в двоичное представление.'
        f'\n/code Кодирует Ваше сообщение RLE алгоритмом.'
        f'\n/nf Создаст для Вас список чисел негафибоначчи.'
        f'\nВам необходимо ввести интересующую Вас команду, обязательно используя " / "'
        f', после ввода команды, требуется ввести данные которые Вы хотите преобразовать.'
        f'Если же Вы ошибетесь в написании команды, ничего не случится.')


async def binary(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    num = update.message.text.split()
    x = int(num[1])
    show = x
    y = ''
    while x > 0:
        y = str(x % 2) + y
        x //= 2
    print(y)
    await update.message.reply_text(f'{show} в двоичной системе равно {y}')


async def coding(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = update.message.text
    data = data.replace('/code ', '')
    print(data)
    code = ''
    previous_symbol = ''
    count = 1
    if not data:
        return ''
    for current_sumbol in data:
        if current_sumbol != previous_symbol:
            if previous_symbol:
                code += str(count) + previous_symbol
            count = 1
            previous_symbol = current_sumbol
        else:
            if count == 9:
                code += str(count) + previous_symbol
                count = 1
            count += 1
    code += str(count) + previous_symbol
    await update.message.reply_text(f'Ваше выражение после шифрования: {code}')
    code = coding(data)
    print(code)


async def fib(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    input_num = update.message.text.split()
    n = int(input_num[1])
    fibo_nums = []

    a, b = 0, 1
    for i in range(n + 1):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    print(fibo_nums)
    await update.message.reply_text(f'Список чисел негафибоначчи: {fibo_nums}')


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Извините, я не знаю такую команду. "
                                                                          "Если вы опечатались - введите команду снова,"
                                                                          "либо воспользуйтесь командой /help")


if __name__ == '__main__':
    app = ApplicationBuilder().token(tg_token.token).build()
    app.add_handler(CommandHandler("start", hello))
    app.add_handler(CommandHandler("help", info))
    app.add_handler(CommandHandler("conv", binary))
    app.add_handler(CommandHandler("code", coding))
    app.add_handler(CommandHandler("nf", fib))
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    app.add_handler(unknown_handler)
    app.run_polling()