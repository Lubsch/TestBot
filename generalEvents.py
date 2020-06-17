from discord.ext import commands
from discord import utils
import sqlite3
from testBot import create_database_connection

class generalEvents(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.accepted_roles = ['MatheLk1', 'MatheGk3', 'KunstGk1', 'VolleyballSp1']

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, reaction_data):
        con = create_database_connection('active_messages.sqlite')
        c = con.cursor()
        c.execute('SELECT message_id FROM active_messages')
        active_messages_ids = c.fetchall()
        active_messages_ids = [row[0] for row in active_messages_ids]
        con.close()

        if reaction_data.message_id in active_messages_ids and not reaction_data.member.bot and utils.get(reaction_data.member.guild.roles, name='RLG') in reaction_data.member.roles and reaction_data.emoji.name in self.accepted_roles:
            await reaction_data.member.add_roles(utils.get(reaction_data.member.guild.roles, name=reaction_data.emoji.name))
    
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, reaction_data):
        con = create_database_connection('active_messages.sqlite')
        c = con.cursor()
        c.execute('SELECT message_id FROM active_messages')
        active_messages_ids = c.fetchall()
        active_messages_ids = [row[0] for row in active_messages_ids]
        con.close()

        current_guild = utils.get(self.bot.guilds, id=reaction_data.guild_id)
        user = utils.get(current_guild.members, id=reaction_data.user_id)

        if reaction_data.message_id in active_messages_ids and not user.bot and utils.get(current_guild.roles, name='RLG') in user.roles and reaction_data.emoji.name in self.accepted_roles:
            await user.remove_roles(utils.get(current_guild.roles, name=reaction_data.emoji.name))

def setup(bot):
    bot.add_cog(generalEvents(bot))