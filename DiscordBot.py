import discord

client = discord.Client()


@client.event
async def on_message(message):
    id = client.get_guild(Client_ID)

    if message.author == client.user:
        return

    elif message.content == "!ilechlopa":
        await message.channel.send(f"""```Tyle chłopa jest na serwie: 
{id.member_count}```""")

    elif message.content.find("!60") != -1:
        await message.channel.send(f"""{message.author.mention} To 60, {message.author.mention} :right_fist: :left_fist: policja.""")

    elif message.content.find("!es") != -1:
        await message.channel.send(f"""{message.author.mention} es :sunglasses: :call_me:""")

    elif message.content.find("!sieema") != -1:
        if str(message.channel) == 'sieema':
            await message.channel.send(f"""{message.author.mention} Sieema! :wave:""")

    elif message.content.find("!help") != -1:
        await message.channel.send("""```
Komendy tego bota to:
!ilechlopa - pokazuje ile osób jest na serwerze
!60 - wzywa od 60
!es - pisze es
!sieema - działa tylko w kanale sieema, pisze sieema```""")

client.run("BOT_TOKEN")
