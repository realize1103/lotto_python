import telepot


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        else:
            cls._instances[cls].__init__(*args, **kwargs)

        return cls._instances[cls]


class Alert_api(metaclass=Singleton):
    def __init__(self):
        super().__init__()
        self.botToken = "257517385:AAFt5b9CX8kmq5G2Q0VAi69KUszsYmD1UL4"
        self.chatID = "57736053"
        self.bot = telepot.Bot(self.botToken)

    def send_message(self, msg):
        print(str(msg))
        self.bot.sendMessage(self.chatID, msg)

    def send_file(self,document_file):
        self.bot.sendDocument(self.chatID, document_file)
