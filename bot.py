import asyncio

import disnake
from disnake.ext import commands



bot = commands.Bot(command_prefix="?", help_command=None, intents=disnake.Intents.all())


@bot.event
async def on_ready():
    await bot.change_presence(status=disnake.Status.dnd, activity=disnake.Game("Пиздуй от сюда."))


@bot.event
async def on_message(message):
    await bot.process_commands(message)

    msg = message.content.lower()
    censored_words = [ "https://media.discordapp.net/attachments/1203029622292221952/1204520585980420106/20220422_103153.gif", "https://media.discordapp.net/attachments/1203029622292221952/1204520585980420106/20220422_103153.gif?ex=674d6c76&is=674c1af6&hm=4836661cc45b3298e5e87c91b84c4bd41abf413952d7b4ee1a0f95956b4b07fd&", "https://media.discordapp.net/attachments/974002682291433502/974030430191886346/1737324307.gif?ex=6595b587&is=65834087&hm=054cff6b7ed53ab78481f5d975d585e7cb1038324f6610198a750f3495df8343&","https://media.discordapp.net/attachments/974002682291433502/974030430191886346/1737324307.gif?ex=674d61c7&is=674c1047&hm=bdc4bdc4e42666e1e95d86b6ec389e40d4b42d626358128dc1593ec5671c4ef8&"
    
    
    
    
    
    
    
    
    
    
    
    
    
    ]

    for bad_content in msg.split():
        if bad_content in censored_words:
            await message.delete()
            await message.channel.send(f"{message.author.mention}, Ах ты тварь!", delete_after=1) 
    


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1310234425014878228)
    role = disnake.utils.get(member.guild.roles, id=1153355360963411988)

    await member.add_roles(role)


@bot.event
async def on_command_error(ctx, error):
    print(error)

    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author}, Пашёл нахуй от сюда!")
    elif isinstance(error, commands.UserInputError):
        await ctx.send(embed=disnake.Embed(
            description=f"Правильное использование команды: `{ctx.prefix}{ctx.command.name}` ({ctx.command.brief})\nExample: {ctx.prefix}{ctx.command.usage}"
        ))


@bot.command(name="очистить", aliases=["clear", "cls"], brief="Очистить чат от сообщений, по умолчанию 10.", usage="clear <amount=10>")
@commands.has_permissions(administrator=True, manage_messages=True)
async def clear(ctx, amount: int=10):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"Было удалено {amount + 1} сообщений.", delete_after=3)


@bot.command(name="кик", aliases=["kick", "kick-member"], brief="Выгнать пользователя с сервера", usage="kick <@user> <reason=None>")
@commands.has_permissions(administrator=True, kick_members=True)
async def kick(ctx, member: disnake.Member, *, reason=None):
    await ctx.message.delete()

    await ctx.send(f"Участник {member.mention}, был выгнан с сервера!", delete_after=3)
    await member.kick(reason=reason)


@bot.command(name="бан", aliases=["ban", "ban-member"], brief="Забанить пользователя на сервере", usage="ban <@user> <reason=None>")
@commands.has_permissions(administrator=True, ban_members=True)
async def ban(ctx, member: disnake.Member, *, reason=None):
    await ctx.message.delete()

    await ctx.send(f"Участник {member.mention}, был забанен на сервере.")
    await member.ban(reason=reason)


@bot.command(name="разбанить", aliases=["unban", "unban-member"], brief="Разбанить пользователя на сервере", usage="unban <user_id>")
@commands.has_permissions(administrator=True, ban_members=True)
async def unban(ctx, user_id: int):
    user = await bot.fetch_user(user_id)
    await ctx.guild.unban(user)

    await ctx.send("Участник разбанен")



@bot.command()
async def help(ctx):
    embed = disnake.Embed(
        title="Навигация по командам",
        description="Здесь ты сможешь найти доступные команды и их описание"
    )
    commands_list = ["clear", "kick", "ban", "unban"]
    descriptions_for_commands = ["Очистить чат", "Кикнуть пользователя", "Забанить пользователя", "Разбанить пользователя"]

    for command_name, description_command in zip(commands_list, descriptions_for_commands):
        embed.add_field(
            name=command_name,
            value=description_command,
            inline=False # Будет выводиться в столбик, если True - в строчку
        )

    await ctx.send(embed=embed)


bot.run("MTMxMjQ2OTYxNzY2NjU1NTk2NQ.GOLyrG.6kf33_lXBIQU-2LKZOcrL_uz4zH5qd3mu_svMs")