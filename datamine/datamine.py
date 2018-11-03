from redbot.core import commands, Config
from difflib import get_close_matches

BaseCog = getattr(commands, "Cog", object)

class Datamine(BaseCog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=4524586975)

        default_global = {
            "next": {
                "images": [],
                "docs": []
            },
            "current": {
                "portraits": {
                    "nightcrawler": "https://drive.google.com/open?id=1PydQ78Mx8uUvJ2S4noBo4A8T2RCgLKVt",
                    "Kamala Khan": "https://drive.google.com/open?id=1xeeOdtx6ybeOgKshIZvMGRPQ2o8B3kcc",
                    "Blade": "https://drive.google.com/open?id=1-P1X5kSW4RpqtIMZ1ko6euA1Clp-Uihz"
                }
            }
        }

        self.config.register_global(**default_global)

    @commands.group()
    async def datamine(self, ctx):
        pass

    @datamine.command()
    async def next(self, ctx):
        await ctx.send("")

    @datamine.command()
    async def portrait(self, ctx, *, search):
        all_keys = await self.config.current.get_raw('portraits')
        all_keys = all_keys.keys()
        matches = get_close_matches(search, list(all_keys), 1)
        try:
            link = await self.config.current.portraits.get_raw(search)
            await ctx.send(link)
        except Exception as e:
            await ctx.send("No champs were found or there was an error in the process.")
            print(e)