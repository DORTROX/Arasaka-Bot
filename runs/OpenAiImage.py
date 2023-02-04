import os, openai
from dotenv import load_dotenv, find_dotenv
from discord.ext import commands as Arasaka

load_dotenv(find_dotenv())
openai.api_key = os.getenv("openaikey")

class Art(Arasaka.Cog):
    def __init__(self,Arasaka):
        self.Arasaka = Arasaka

        
    @Arasaka.command()
    async def Gart(self,ctx,*,args):
        await ctx.send("Creating an image....")
        a = [[str(args),"Epic cinematic brilliant stunning intricate meticulously detailed dramatic atmospheric maximalist digital matte painting"],[str(args),"detailed matte painting, deep color, fantastical, intricate detail, splash screen, complementary colors, fantasy concept art, 8k resolution trending on Artstation Unreal Engine 5"],[str(args),"head and shoulders portrait, 8k resolution concept art portrait by Greg Rutkowski, Artgerm, WLOP, Alphonse Mucha dynamic lighting hyperdetailed intricately detailed Splash art trending on Artstation triadic colors Unreal Engine 5 volumetric lighting"],[str(args),"Studio Ghibli, Anime Key Visual, by Makoto Shinkai, Deep Color, Intricate, 8k resolution concept art, Natural Lighting, Beautiful Composition"],[str(args),"a masterpiece, 8k resolution, dark fantasy concept art, by Greg Rutkowski, dynamic lighting, hyperdetailed, intricately detailed, Splash screen art, trending on Artstation, deep color, Unreal Engine, volumetric lighting, Alphonse Mucha, Jordan Grimmer, purple and yellow complementary colours"]]
        random_integer = random.randint(0, len(a) - 1)

        selected_item = a[random_integer]
        response = openai.Image.create(
                prompt=str(selected_item),
                n=1,
                size="1024x1024"
            )
        image_url = response['data'][0]['url']
        await ctx.send(image_url)

def setup(Arasaka):
    Arasaka.add_cog(Art(Arasaka))
import random

random_integers = [random.randint(1, 51) for i in range(10)]

print(random_integers)