from discord.ext import commands as Arasaka

class ping(Arasaka.Cog):
    def __init__(self,Arasaka):
        self.Arasaka = Arasaka

    @Arasaka.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.Arasaka.latency * 1000)}ms')

def setup(Arasaka):
    Arasaka.add_cog(ping(Arasaka))