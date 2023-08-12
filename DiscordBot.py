import discord

client = discord.Client()


@client.event
async def on_message(message):
    id = client.get_guild(788820213239513109)

    if message.author == client.user:
        return

    elif message.content.find("!JD?") != -1:
        await message.channel.send("```Jebać Disa Kurwe Zwisa Orka Skyrwysyna Syna Diabła```")

    elif message.content == "!ilechlopa":
        await message.channel.send(f"""```Tyle chłopa jest na serwie: 
{id.member_count}```""")

    elif message.content.find("!60") != -1:
        await message.channel.send("Mateusz To 60, Mateusz :right_fist: :left_fist: policja.")

    elif message.content.find("!es") != -1:
        await message.channel.send(f"""{message.author.mention} es :sunglasses: :call_me:""")

    elif message.content.find("!sieema") != -1:
        if str(message.channel) == 'sieema':
            await message.channel.send(f"""{message.author.mention} Sieema! :wave:""")

    elif message.content.find("!help") != -1:
        await message.channel.send("""```
Komendy tego bota to:
!JD? - wyzywa disa orka
!ilechlopa - pokazuje ile osób jest na serwerze
!60 - wzywa Mateusza D. od 60 i konfidentów
!es - pisze es
!sieema - działa tylko w kanale sieema, pisze sieema```""")


client.run("Nzg4ODI0NjIzMjIzMjc1NTUy.X9pILQ.2NFYTRvLgmxXVS4uQ14-v5k-a4c")
