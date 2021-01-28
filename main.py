import discord
from discord.utils import get
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix= "|", description = "bot pour les propositions de jeux en stream", intents=intents)

@bot.event
async def on_ready():
    print("yeet")

@bot.command()
async def propo(ctx, *, message):
    lophim = bot.get_user(350745596010823682) #On récupère l'utilisateur LOPHIM
    await lophim.send(f"L'utilisateur {ctx.author} vous as envoyé la proposition de jeu suivante : \n{message}") #Je lui envoie le message
    await ctx.send("Ta proposition a bien été transmise")

bot.run("ODA0MzkxMjU4MjY4MTA2NzYy.YBLpvA.U1HgTvp7PBzNMqqSNRA6CDzibbI")