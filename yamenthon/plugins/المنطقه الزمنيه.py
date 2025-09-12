import asyncio
import glob
import os

from . import zedub
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _zedutils
from . import BOTLOG, BOTLOG_CHATID, mention

plugin_category = "الادوات"


config = "./config.py"
var_checker = [
    "APP_ID",
    "PM_LOGGER_GROUP_ID",
    "PRIVATE_CHANNEL_BOT_API_ID",
    "PRIVATE_GROUP_BOT_API_ID",
]
exts = ["jpg", "png", "webp", "webm", "m4a", "mp4", "mp3", "tgs"]


# قاموس الأوقات بالعربي
tz_map = {
    "فلسطين": "Asia/Gaza",            
    "اليمن": "Asia/Aden",
    "العراق": "Asia/Baghdad",
    "السعودية": "Asia/Riyadh",
    "السعوديه": "Asia/Riyadh",
    "سوريا": "Asia/Damascus",
    "الامارات": "Asia/Dubai",
    "الإمارات": "Asia/Dubai",
    "قطر": "Asia/Qatar",
    "الكويت": "Asia/Kuwait",
    "البحرين": "Asia/Bahrain",
    "سلطنة عمان": "Asia/Muscat",
    "عمان": "Asia/Muscat",
    "الاردن": "Asia/Amman",
    "لبنان": "Asia/Beirut",
    "مصر": "Africa/Cairo",
    "السودان": "Africa/Khartoum",
    "ليبيا": "Africa/Tripoli",
    "الجزائر": "Africa/Algiers",
    "المغرب": "Africa/Casablanca",
    "تونس": "Africa/Tunis",
    "موريتانيا": "Africa/Nouakchott",
    "ايران": "Asia/Tehran",
    "تركيا": "Europe/Istanbul",
    "امريكا": "America/New_York",     
    "روسيا": "Europe/Moscow",
    "ايطاليا": "Europe/Rome",
    "المانيا": "Europe/Berlin",
    "فرنسا": "Europe/Paris",
    "اسبانيا": "Europe/Madrid",
    "بريطانيا": "Europe/London",
    "بلجيكا": "Europe/Brussels",
    "النرويج": "Europe/Oslo",
    "الصين": "Asia/Shanghai",
    "اليابان": "Asia/Tokyo",
    "الهند": "Asia/Kolkata",
    "اندنوسيا": "Asia/Jakarta",
    "ماليزيا": "Asia/Kuala_Lumpur",
}


@zedub.zed_cmd(
    pattern="ضع وقت(?: |$)([\\s\\S]*)",
    command=("وقت", plugin_category),
    info={
        "header": "لتغيير المنطقة الزمنية من داخل تيليجرام.",
        "usage": [
            "{tr}ضع وقت اليمن",
            "{tr}ضع وقت السعودية",
        ],
    },
)
async def variable(event):
    if not os.path.exists(config):
        return await edit_delete(
            event,
            "**- عـذراً .. لايـوجـد هنـالك ملـف كـونفـج 📁🖇**\n\n"
            "**- هـذه الاوامـر خـاصـة فقـط بالمنصبيـن ع السيـرفـر 📟💡**"
        )

    user_input = event.pattern_match.group(1).strip()
    if not user_input:
        return await edit_or_reply(event, "**⌔∮** `.ضع وقت <اسم الدولة>`")

    cat = await edit_or_reply(event, "**⌔∮ جـارِ إعـداد المنطقـة الزمنية ...**")

    # إذا المستخدم كتب دولة بالعربي
    if user_input in tz_map:
        value = f'"{tz_map[user_input]}"'
    else:
        # إذا كتب منطقة زمنية جاهزة
        value = f'"{user_input}"'

    variable = "TZ"

    with open(config, "r") as f:
        configs = f.readlines()

    string = ""
    match = False
    for i in configs:
        if i.strip().startswith(f"{variable} "):
            string += f'{variable} = {value}\n'
            match = True
        else:
            string += i

    if not match:
        string += f'{variable} = {value}\n'

    with open(config, "w") as f1:
        f1.write(string)

    await cat.edit(
        f"**- تم تغيـير المنطقة الزمنية إلى :** `{value}` ✅\n\n"
        "**- يتم الان اعـادة تشغيـل بـوت يمن ثون ...**\n**يستغـرق الامر 5-8 دقيقـه ▬▭ ...**"
    )

    await event.client.reload(cat)
    
#حقوق الاسطوره عاشق الصمت 
#سورس يمنثون 🇾🇪

ASHEQ_ALSAMT_cmd = (
    "𓆩 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗧𝗶𝗺𝗲 **🝢 المنطقة الزمنية** 𓆪\n"
    "**⋆┄─┄─┄─┄─┄─┄─┄─┄⋆**\n"
    "**✧ قائمـة اوامر تغييـر المنطقـة الزمنيـة لـ ضبط الوقت ع يمنثـون حسب توقيت دولتك 🌐:** \n\n"
    "⪼ `.ضع وقت فلسطين` \n"
    "⪼ `.ضع وقت اليمن` \n"
    "⪼ `.ضع وقت العراق` \n"
    "⪼ `.ضع وقت السعودية` \n"
    "⪼ `.ضع وقت سوريا` \n"
    "⪼ `.ضع وقت الامارات` \n"
    "⪼ `.ضع وقت قطر` \n"
    "⪼ `.ضع وقت الكويت` \n"
    "⪼ `.ضع وقت البحرين` \n"
    "⪼ `.ضع وقت سلطنة عمان` \n"
    "⪼ `.ضع وقت الاردن` \n"
    "⪼ `.ضع وقت لبنان` \n"
    "⪼ `.ضع وقت مصر` \n"
    "⪼ `.ضع وقت السودان` \n"
    "⪼ `.ضع وقت ليبيا` \n"
    "⪼ `.ضع وقت الجزائر` \n"
    "⪼ `.ضع وقت المغرب` \n"
    "⪼ `.ضع وقت تونس` \n"
    "⪼ `.ضع وقت موريتانيا` \n"
    "⪼ `.ضع وقت ايران` \n"
    "⪼ `.ضع وقت تركيا` \n"
    "⪼ `.ضع وقت امريكا` \n"
    "⪼ `.ضع وقت روسيا` \n"
    "⪼ `.ضع وقت ايطاليا` \n"
    "⪼ `.ضع وقت المانيا` \n"
    "⪼ `.ضع وقت فرنسا` \n"
    "⪼ `.ضع وقت اسبانيا` \n"
    "⪼ `.ضع وقت بريطانيا` \n"
    "⪼ `.ضع وقت بلجيكا` \n"
    "⪼ `.ضع وقت النرويج` \n"
    "⪼ `.ضع وقت الصين` \n"
    "⪼ `.ضع وقت اليابان` \n"
    "⪼ `.ضع وقت الهند` \n"
    "⪼ `.ضع وقت اندنوسيا` \n"
    "⪼ `.ضع وقت ماليزيا` \n\n"
    "**🛃 اذا لم تجد دولتك .. قم بالبحث عن اقرب دوله لها**\n"
    "𓆩 [𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗩𝗮𝗿𝘀 - قنـاة الفـارات](t.me/YamenThon_vars) 𓆪"
)



@zedub.zed_cmd(pattern="الوقت")
async def cmd(zelzallltm):
    await edit_or_reply(zelzallltm, ASHEQ_ALSAMT_cmd)
