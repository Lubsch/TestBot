from discord.ext import commands
import sqlite3
from testBot import create_database_connection

class Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def reactionmessage(self, ctx):
        '''Sends a message you can react to'''
        bot_message = await ctx.send('Moin')
        con = create_database_connection('active_messages.sqlite')
        c = con.cursor()
        c.execute('INSERT INTO active_messages(message_id, message_content) VALUES(?, ?)', (bot_message.id, bot_message.content))
        con.commit()
        c.close()

def setup(bot):
    bot.add_cog(Commands(bot))
