from redbot.core import commands, Config
from fuzzywuzzy import process
import json
from redbot.core.data_manager import bundled_data_path

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
                    "nightcrawler": "https://lh3.googleusercontent.com/1bEKNK3utJXk9ETIyds2epX9OUSdH2OHVjzv0y6AXOHv0zI2YrtAs6DKai-1svdYGkyUIJGqGW3kw62JJYI=w1366-h626",
                    "kamala khan": "https://lh4.googleusercontent.com/Gvq_ic16FoVAS4l9EjSE239kHDhyrrgw9EBRybh-V9izJOvovCtZ3SV1QPg0q8XHPGUzlLNuqGRZatCsgr4=w1366-h626",
                    "blade": "https://lh3.googleusercontent.com/KRT7jg99wBhYJDsbMzgPl0kezlF1QJV4-6tZm3S14oiSID14K-rpAbVDz8BLd66KafjuD7rjp-u8L3EOPLc=w1366-h626",

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
        
        results = process.extractOne(search, list(all_keys))
        try:
            link = await self.config.current.portraits.get_raw(results[0])
            await ctx.send(link + "\n\nScore: " + str(results[1]))
        except Exception as e:
            await ctx.send("No champs were found or there was an error in the process.")
            print(e)

    @datamine.group()
    async def search(self, ctx):
        pass

    @search.command()
    async def ability(self, ctx, id):
        await ctx.send("Searching for ability... this may take a while...")
        with open(str(bundled_data_path(self)) + "/en/bcg_stat_en.bytes", 'r') as read_file:
            data = json.load(read_file)
        data = data['strings']
        for x in data:
            if x['k'] == id:
                await ctx.send("```" + x['v'] + "```")
                return

    @search.command()
    async def bio(self, ctx, id):
        await ctx.send("Searching for champion bio... this may take a while")
        with open(str(bundled_data_path(self)) + "/en/character_bios_en.bytes", 'r') as read_file:
            data = json.load(read_file)
        data = data['strings']
        name_list = []
        for x in data:
            name_list.append(x['k'][18:])
        
        results = process.extractOne(id, name_list)
        if results[0] != "BLADE":
            result = 'ID_CHARACTER_BIOS_' + results[0]
        else:
            result = "ID_CHARACER_BIOS_" + results[0]
        
        for x in data:
            if x['k'] == result:
                await ctx.send("```" + x['v'] + "```")
                return
        