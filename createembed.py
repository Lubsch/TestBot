from discord.ext import commands
import sqlite3
from testBot import create_database_connection

class CreateEmbed(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def createembed(self, ctx):
        '''Creates an embed, basically a fancy message (not yet working)'''

        await ctx.send('ti: title \n de: description \n ur: url \n co: color (hex) \n ic: icon \n an: author name \n al: author link \n ai: author info \n fi: field \n fo: footer \n ch: channel')

        msg = await self.bot.wait_for('message')

        title, description, url, color, icon, author_name, author_link, author_info, fields, footer, channels = []

        for line in msg.content:
            start = line[:2] if len(line) > 3 else None
            content = line[3:].strip()

            if start == 'ti' and len(title) == 0:
                title.append(content)
            
            elif start == 'de' and len(description) == 0:
                description.append(content)
            
            elif start == 'ur' and len(url) == 0:
                url.append(content)
            
            elif start == 'co' and len(color) == 0:
                color.append(content)
            
            elif start == 'ic' and len(icon) == 0:
                icon.append(content)
            
            elif start == 'an' and len(author_name) == 0:
                author_name.append(content)
            
            elif start == 'al' and len(author_link) == 0:
                author_link.append(content)
            
            elif start == 'ai' and len(author_info) == 0:
                author_info.append(content)
            
            elif start == 'fi':
                fields.append(content)
            
            elif start == 'fo' and len(footer) == 0:
                footer.append(content)
            
            elif start == 'ch':
                channels.append(content)



def setup(bot):
    bot.add_cog(CreateEmbed(bot))