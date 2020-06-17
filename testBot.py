from discord.ext import commands
import sqlite3
from sqlite3 import Error
from os import path

description = '''A bot for testing purposes only.

Have fun!'''

# Specify extensions that are loaded on startup
startup_extensions = ['commands', 'generalEvents', 'createEmbed']

bot = commands.Bot(command_prefix='~', description=description)

@bot.event
async def on_ready():
    print('We have logged in as {}, {}'.format(bot.user.name, bot.user.id))

    con = create_database_connection('active_messages.sqlite')
    c = con.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS active_messages(message_id NUMERIC PRIMARY KEY, message_content type NOT NULL)')
    c.execute('SELECT message_id FROM active_messages')
    con.commit()
    con.close()

def create_database_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as e:
        print(f"The error '{e}' occurred while connecting to a database")

    return connection

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    token_file = open('token.txt', 'r')
    TOKEN = token_file.read()
    token_file.close()
    bot.run(TOKEN)