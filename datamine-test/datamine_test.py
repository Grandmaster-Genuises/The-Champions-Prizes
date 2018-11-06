from redbot.core import commands, checks
import pygsheets

class Datamine_test:
    def __init__(self, bot):
        self.bot = bot
        self.gc = pygsheets.authorize(service_file='creds/pygsheetsTest-0131bfa081ca.json')

    @checks.is_owner()
    @commands.command()
    async def test(self, ctx):
        sh = self.gc.open('me new ssheet')
        wks = sh.sheet1
        wks.update_cell('A1', "Testing")
        await ctx.send("Edited")