import discord
from discord.ext import commands, tasks
import random
import asyncio
import json
import os
from itertools import cycle

status = cycle(["Playing .help", "friend RaGhAv has fallen into the river#0730 for support", "helping people in 7 servers"])


@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


#Moves3 = ["R","L","F","B","U","D"]

client = commands.Bot(command_prefix = ".")


global money
money = 0

@client.event
async def on_ready():
    change_status.start()
    print("Bot is ready")

@client.event
async def on_member_join(member):
        role = discord.utils.get(member.guild.roles, name='Cubie')
        await member.add_roles(role)
        print(f"{member} has joined")

@client.event
async def on_member_remove(member):
    print(f"{member} has left")

@client.command(aliases=['sd'])
@commands.has_any_role("Mod")
async def shutdown(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send("Shutting down.")
    await ctx.bot.logout()


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

#@client.command(aliases=['scramble', 's'])
#async def scramble(ctx, *, sType):
  #sType = client.wait_for("For what puzzle would you like to scramble")
  #if (sType == "3x3"):
      #await ctx.send("command works")

@client.command(aliases= ['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

#clear command
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

#kick
@client.command()
@commands.has_permissions(manage_guild=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')

#ban
@client.command()
@commands.has_permissions(manage_guild=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

#unban
@client.command()
@commands.has_permissions(manage_guild=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return



@client.command()
async def mute(ctx, member : discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == "Muted(raghavbot)":
            await member.add_roles(role)
            await ctx.send("{} has muted {}".format(member.mention,ctx.author.mention))
            return

            overwrite = discord.PermissionOverwrite(send_messages=False)
            new_role = await guild.create_role(name="Muted(raghavbot)")

            for guild in guild.text_channels:
                await channel.set_permissions(new_role, overwrite=overwrite)

            await member.add_roles(new_role)
            await ctx.send("{} has muted {}" .format(ctx.author.mention,member.mention))


@client.command()
async def unmute(ctx, member : discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == "Muted(raghavbot)":
            await member.remove_roles(role)
            await ctx.send("{} has muted {}".format(ctx.author.mention,member.mention))


@client.command()
async def ineedfriends(ctx):
    await ctx.send("I will be your friend :)")


@client.command()
async def iamlonely(ctx):
    await ctx.send("Dont worry im here :)")


@client.command()
async def oof(ctx):
    await ctx.send("sorry for the oof")


@client.command()
async def ineedtherapy(ctx):
    await ctx.send("I will be your therapist so tell me whats happening in your life")
    await client.wait_for('message')
    await ctx.send("so how did that make you feel")





@client.command()
async def work(ctx):
    global raghav_coins
    raghav_coins = 0
    jobs = ["You helped code a website for a startup company you recieved raghav coins", "You help out an admin in a server by setting up roles", "You contribute to an open source github repository"]
    await ctx.send('Do you want to work? (y/n)')
    message = await client.wait_for('message', check=lambda message: message.author.id == ctx.author.id)
    await ctx.send(random.choice(jobs))
    if message.content.lower() == 'y':
        raghav_coins += 20
        await ctx.send("You have earnt 20 raghav coins you can check your balance by doing .bal")


@client.command()
async def bal(ctx):
    await ctx.send("You have " + str(raghav_coins) + " Raghav coins")



@client.command()
async def ineedagf(ctx):
    await ctx.send("Ha ha well guess what you will never get one")


client.run("Njc2MjU1MDU2NTIxMTk5NjU2.XnqZEg.jhQ3dRw3pvet8fXdyTF3q97R1z4")
