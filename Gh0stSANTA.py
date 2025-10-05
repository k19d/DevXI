import telebot
import threading
import time
import json
import os
import html
import requests
import base64
from datetime import datetime, timedelta

try:
    from protobuf_decoder.protobuf_decoder import Parser
except ImportError:
    class Parser:
        def parse(self, data):
            return {"error": "protobuf_decoder not installed"}
    print("Warning: protobuf_decoder not available - using dummy parser")
import random

# بيانات البوت والمسؤول
BOT_TOKEN = "8330082948:AAHSQgEpRI6nMlIw1r0P_7j3p9zhy_Jgugg"
ADMIN_ID = 7619124468
JWT_TOKEN = None

# ملفات البيانات
DATA_FILE = "users2.json"
GROUPS_FILE = "groups2.json"
MAINTENANCE_FILE = "maintenance2.json"

# بيانات القناة الإجبارية - تم إضافتها
SUBSCRIPTION_CHANNEL_ID = -1003088927549
SUBSCRIPTION_CHANNEL_LINK = "https://t.me/AlliFF_BOT12"

# بيانات التشفير والديكور (لم يتم تعديلها لأنها ليست جزءا من مكتبة التشفير)
da = 'f2212101'
dec = ['80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '8a', '8b', '8c', '8d', '8e', '8f', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '9a', '9b', '9c', '9d', '9e', '9f', 'a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'aa', 'ab', 'ac', 'ad', 'ae', 'af', 'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'ba', 'bb', 'bc', 'bd', 'be', 'bf', 'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'ca', 'cb', 'cc', 'cd', 'ce', 'cf', 'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'da', 'db', 'dc', 'dd', 'de', 'df', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'ea', 'eb', 'ec', 'ed', 'ee', 'ef', 'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'fa', 'fb', 'fc', 'fd', 'fe', 'ff']
x = ['1', '01', '02', '03', '04', '05', '06', '07', '08', '09', '0a', '0b', '0c', '0d', '0e', '0f', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d', '1e', '1f', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '2a', '2b', '2c', '2d', '2e', '2f', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '3a', '3b', '3c', '3d', '3e', '3f', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4a', '4b', '4c', '4d', '4e', '4f', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5a', '5b', '5c', '5d', '5e', '5f', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e', '6f', '70', '71',
     '72', '73', '74', '75', '76', '77', '78', '79', '7a', '7b', '7c', '7d', '7e', '7f']

def generate_random_hex_color():
    top_colors = [
        "FF4500", "FFD700", "32CD32", "87CEEB", "9370DB",
        "FF69B4", "8A2BE2", "00BFFF", "1E90FF", "20B2AA",
        "00FA9A", "008000", "FFFF00", "FF8C00", "DC143C",
        "FF6347", "FFA07A", "FFDAB9", "CD853F", "D2691E",
        "BC8F8F", "F0E68C", "556B2F", "808000", "4682B4",
        "6A5ACD", "7B68EE", "8B4513", "C71585", "4B0082",
        "B22222", "228B22", "8B008B", "483D8B", "556B2F",
        "800000", "008080", "000080", "800080", "808080",
        "A9A9A9", "D3D3D3", "F0F0F0"
    ]
    random_color = random.choice(top_colors)
    return random_color

# تم تعديل هذه الوظيفة
def encrypt_packet(plain_text, key, iv):
    plain_text_bytes = bytes.fromhex(plain_text)
    encrypted_bytes = base64.b64encode(plain_text_bytes)
    return encrypted_bytes.hex()


def dec_to_hex(ask):
    ask_result = hex(ask)
    final_result = str(ask_result)[2:]
    if len(final_result) == 1:
        final_result = "0" + final_result
        return final_result
    else:
        return final_result

class ParsedResult:
    def __init__(self, field, wire_type, data):
        self.field = field
        self.wire_type = wire_type
        self.data = data

class ParsedResultEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ParsedResult):
            return {"field": obj.field, "wire_type": obj.wire_type, "data": obj.data}
        return super().default(obj)

def bunner_():
    ra = random.randint(203, 213)
    final_num = str(ra).zfill(3)
    bunner = "902000" + final_num
    bunner = random.choice(numbers)
    return bunner

def create_varint_field(field_number, value):
    field_header = (field_number << 3) | 0
    return encode_varint(field_header) + encode_varint(value)

def create_length_delimited_field(field_number, value):
    field_header = (field_number << 3) | 2
    encoded_value = value.encode() if isinstance(value, str) else value
    return encode_varint(field_header) + encode_varint(len(encoded_value)) + encoded_value

def create_protobuf_packet(fields):
    packet = bytearray()

    for field, value in fields.items():
        if isinstance(value, dict):
            nested_packet = create_protobuf_packet(value)
            packet.extend(create_length_delimited_field(field, nested_packet))
        elif isinstance(value, int):
            packet.extend(create_varint_field(field, value))
        elif isinstance(value, str) or isinstance(value, bytes):
            packet.extend(create_length_delimited_field(field, value))

    return packet

def encode_varint(number):
    if number < 0:
        raise ValueError("Number must be non-negative")

    encoded_bytes = []
    while True:
        byte = number & 0x7F
        number >>= 7
        if number:
            byte |= 0x80
        encoded_bytes.append(byte)
        if not number:
            break
    return bytes(encoded_bytes)

numbers = [
    902000208,
    902000209,
    902000210,
    902000211
]

def Encrypt_ID(number):
    number = int(number)
    encoded_bytes = []
    while True:
        byte = number & 0x7F
        number >>= 7
        if number:
            byte |= 0x80
        encoded_bytes.append(byte)
        if not number:
            break
    return bytes(encoded_bytes).hex()

def Encrypt(number):
    number = int(number)
    encoded_bytes = []
    while True:
        byte = number & 0x7F
        number >>= 7
        if number:
            byte |= 0x80
        encoded_bytes.append(byte)
        if not number & 0x80:
            break
    return bytes.fromhex(encrypted_packet_hex)

def decrypt_api(cipher_text):
    decoded_bytes = base64.b64decode(cipher_text)
    return decoded_bytes.hex()

def encrypt_api(plain_text):
    plain_text_bytes = bytes.fromhex(plain_text)
    encoded_bytes = base64.b64encode(plain_text_bytes)
    return encoded_bytes.hex()

def get_squad_leader(packet):
    json_result = get_available_room(packet)
    parsed_data = json.loads(json_result)
    return (parsed_data['5']['data']['1']['data'])

def send_msg_in_room(Msg, room_id):
    fields = {
        1: 1,
        2: {
            1: 9280892890,
            2: int(room_id),
            3: 3,
            4: f'[{generate_random_hex_color()}]{Msg}',
            5: 1721662811,
            7: 2,
            9: {
                1: "byte bot ",
                2: bunner_(),
                4: 228,
                7: 1,
            },
            10: "ar",
            13: {
                2: 1,
                3: 1
            },
        }
    }
    packet = create_protobuf_packet(fields)
    packet = packet.hex() + "7200"
    encrypted_packet_hex = encrypt_packet(packet, None, None)
    header_lenth = len(encrypted_packet_hex) // 2
    header_lenth = dec_to_hex(header_lenth)

    if len(header_lenth) == 1:
        final_packet = "12150000000" + header_lenth + encrypted_packet_hex
        return bytes.fromhex(final_packet)
    if len(header_lenth) == 2:
        final_packet = "1215000000" + header_lenth + encrypted_packet_hex
        return bytes.fromhex(final_packet)
    if len(header_lenth) == 3:
        final_packet = "121500000" + header_lenth + encrypted_packet_hex
        return bytes.fromhex(final_packet)
    if len(header_lenth) == 4:
        final_packet = "12150000" + header_lenth + encrypted_packet_hex
        return bytes.fromhex(final_packet)
    if len(header_lenth) == 5:
        final_packet = "12150000" + header_lenth + encrypted_packet_hex
        return bytes.fromhex(final_packet)

def join_room_chanel(room_id):
    fields = {
        1: 3,
        2: {
            1: int(room_id),
            2: 3,
            3: "ar",
        }
    }
    packet = create_protobuf_packet(fields)
    packet = packet.hex() + "7200"
    encrypted_packet_hex = encrypt_packet(packet, None, None)
    header_lenth = len(encrypted_packet_hex) // 2
    header_lenth = dec_to_hex(header_lenth)

    if len(header_lenth) == 1:
        final_packet = "12150000000" + header_lenth + encrypted_packet_hex
        return bytes.fromhex(final_packet)
    if len(header_lenth) == 2:
        final_packet = "1215000000" + header_lenth + encrypted_packet_hex
        return bytes.fromhex(final_packet)
    if len(header_lenth) == 3:
        final_packet = "121500000" + header_lenth + encrypted_packet_hex
        return bytes.fromhex(final_packet)
    if len(header_lenth) == 4:
        final_packet = "12150000" + header_lenth + encrypted_packet_hex
        return bytes.fromhex(final_packet)
    if len(header_lenth) == 5:
        final_packet = "12150000" + header_lenth + encrypted_packet_hex
        return bytes.fromhex(final_packet)

def leave_room_chanel(room_id):
    fields = {
        1: 4,
        2: {
            1: int(room_id),
            2: 3,
            3: "ar",
        }
    }
    packet = create_protobuf_packet(fields)
    packet = packet.hex() + "7200"
    encrypted_packet_hex = encrypt_packet(packet, None, None)
    header_lenth = len(encrypted_packet_hex) // 2
    header_lenth = dec_to_hex(header_lenth)

    if len(header_lenth) == 1:
        final_packet = "12150000000" + header_lenth + encrypted_packet_hex
        return bytes.fromhex(final_packet)
    if len(header_lenth) == 2:
        final_packet = "1215000000" + header_lenth + encrypted_packet_hex
        return bytes.fromhex(final_packet)
    if len(header_lenth) == 3:
        final_packet = "121500000" + header_lenth + encrypted_packet_hex
        return bytes.fromhex(final_packet)
    if len(header_lenth) == 4:
        final_packet = "12150000" + header_lenth + encrypted_packet_hex
        return bytes.fromhex(final_packet)
    if len(header_lenth) == 5:
        final_packet = "12150000" + header_lenth + encrypted_packet_hex
        return bytes.fromhex(final_packet)

def load_users():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                if isinstance(data, dict):
                    return data
            except json.JSONDecodeError:
                pass
    return {}

def save_users():
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, ensure_ascii=False, indent=4)

def load_groups():
    if os.path.exists(GROUPS_FILE):
        with open(GROUPS_FILE, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                if isinstance(data, dict):
                    return {k: v for k, v in data.items()}
            except json.JSONDecodeError:
                pass
    return {}

def save_groups():
    with open(GROUPS_FILE, "w", encoding="utf-8") as file:
        json.dump(group_activations, file, ensure_ascii=False, indent=4)

def load_maintenance_status():
    if os.path.exists(MAINTENANCE_FILE):
        with open(MAINTENANCE_FILE, "r", encoding="utf-8") as file:
            try:
                return json.load(file).get("maintenance_mode", False)
            except json.JSONDecodeError:
                pass
    return False

def save_maintenance_status(status):
    with open(MAINTENANCE_FILE, "w", encoding="utf-8") as file:
        json.dump({"maintenance_mode": status}, file)

def is_admin(message):
    return message.from_user.id == ADMIN_ID

def is_allowed_group(message):
    chat_id_str = str(message.chat.id)
    if chat_id_str in group_activations:
        expiry_timestamp = group_activations[chat_id_str]
        if expiry_timestamp > time.time():
            return True
        else:
            del group_activations[chat_id_str]
            save_groups()
            bot.send_message(message.chat.id, "⚠️ انتهت صلاحية تفعيل البوت في هذه المجموعة.\nيرجى التواصل مع [حط اسمك](https://t.me/AH_BOT22) لإعادة التفعيل.", parse_mode="Markdown")
            return False
    else:
        bot.send_message(message.chat.id, "⚠️ البوت غير مفعل في هذه المجموعة.\nيرجى التواصل مع [حط اسمك](https://t.me/AH_BOT22) لكي يقوم بتفعيل البوت.", parse_mode="Markdown")
        return False

# دالة التحقق من الاشتراك - تم إضافتها
def is_subscribed(message):
    try:
        status = bot.get_chat_member(SUBSCRIPTION_CHANNEL_ID, message.from_user.id).status
        return status in ['member', 'administrator', 'creator']
    except telebot.apihelper.ApiTelegramException as e:
        if "chat not found" in str(e) or "user not found" in str(e):
            print(f"Error checking subscription: {e}")
            return False
        return False

def format_remaining_time(expiry_time):
    remaining = int(expiry_time - time.time())
    if remaining <= 0:
        return "⛔ انتهت الصلاحية"

    days = remaining // 86400
    hours = (remaining % 86400) // 3600
    minutes = ((remaining % 86400) % 3600) // 60
    seconds = remaining % 60

    parts = []
    if days > 0:
        parts.append(f"{days} يوم")
    if hours > 0:
        parts.append(f"{hours} ساعة")
    if minutes > 0:
        parts.append(f"{minutes} دقيقة")
    parts.append(f"{seconds} ثانية")

    return " ".join(parts)


def fetch_jwt_token():
    url = ("https://jwt-maker-danger.vercel.app/token?uid=4197963977&password=8D237E619C69E6533414496270E8E3F83735AB902D79604FA6AD1A2253ACE297")
    try:
        resp = requests.get(url)
        print(f"📩 استجابة API الكاملة: {resp.text}")
        if resp.status_code == 200:
            data = resp.json()
            token = data.get("token")
            if token:
                print(f"✅ تم جلب التوكن بنجاح: {token}")
                return token
    except Exception as e:
        print(f"⚠️ خطأ أثناء جلب التوكن: {e}")
    return None

def update_jwt_periodically():
    global JWT_TOKEN
    while True:
        new_token = fetch_jwt_token()
        if new_token:
            JWT_TOKEN = new_token
        time.sleep(5 * 3600)

def send_friend_request(player_id):
    if not JWT_TOKEN:
        return "⚠️ التوكن غير متاح حاليًا، حاول لاحقًا."

    url = f"https://amin-api-remove-add-jwt-token.onrender.com/adding_friend?token={JWT_TOKEN}&id={player_id}"
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return "✅ تم إرسال طلب الصداقة بنجاح!"
        return f"⚠️ فشل إرسال الطلب. {r.text}"
    except Exception as e:
        return f"⚠️ حدث خطأ أثناء إرسال الطلب: {e}"

def remove_friend(player_id):
    if not JWT_TOKEN:
        return "⚠️ التوكن غير متاح حاليًا، حاول لاحقًا."

    url = f"https://amin-api-remove-add-jwt-token.onrender.com/remove_friend?token={JWT_TOKEN}&id={player_id}"
    try:
        r = requests.get(url)
        if r.status_code == 200:
            response_data = r.json()
            if response_data.get("status") == "success" or "تم الحذف بنجاح" in str(response_data):
                return "✅ تم الحذف بنجاح!"
            else:
                return f"⚠️ فشل حذف الصديق. {response_data}"
        return f"⚠️ فشل حذف الصديق. {r.text}"
    except Exception as e:
        return f"⚠️ حدث خطأ أثناء الحذف: {e}"

def remove_expired_users():
    now = time.time()
    expired = [uid for uid, d in users.items() if d.get("expiry") and d["expiry"] <= now]
    for uid in expired:
        if "added_by_tele_id" in users[uid]:
            remove_friend(uid)
        del users[uid]
    save_users()

def check_expired_users():
    while True:
        remove_expired_users()
        time.sleep(60)

def reset_daily_adds():
    now = datetime.now()
    for tele_id in list(users.keys()):
        if 'last_reset_day' in users[tele_id]:
            last_reset = datetime.fromtimestamp(users[tele_id]['last_reset_day'])
            if now.date() > last_reset.date():
                users[tele_id]['adds_today'] = 0
                users[tele_id]['last_reset_day'] = now.timestamp()
    save_users()

def daily_reset_timer():
    while True:
        reset_daily_adds()
        time.sleep(3600)

users = load_users()
group_activations = load_groups()
maintenance_mode = load_maintenance_status()
bot = telebot.TeleBot(BOT_TOKEN)

for _ in range(5):
    JWT_TOKEN = fetch_jwt_token()
    if JWT_TOKEN:
        break
    time.sleep(3)

if not JWT_TOKEN:
    raise RuntimeError("❌ فشل نهائي في جلب التوكن!")

threading.Thread(target=update_jwt_periodically, daemon=True).start()
threading.Thread(target=check_expired_users, daemon=True).start()
threading.Thread(target=daily_reset_timer, daemon=True).start()

def get_player_info(uid):
    try:
        res = requests.get(f"https://7ama-info.vercel.app/info?uid={uid}", timeout=10)
        data = res.json()
        info = data["basicInfo"]
        name = info["nickname"]
        region = info["region"]
        level = info["level"]
        return name, region, level
    except Exception as e:
        print(f"⚠️ Error fetching info for {uid}: {e}")
        return "غير معروف", "N/A", "N/A"

def send_message_to_all_groups(message_text):
    for chat_id in list(group_activations.keys()):
        try:
            bot.send_message(chat_id, message_text, parse_mode="Markdown")
            time.sleep(1)
        except telebot.apihelper.ApiTelegramException as e:
            if "chat not found" in str(e) or "bot was kicked from the group chat" in str(e):
                print(f"⚠️ فشل إرسال رسالة إلى المجموعة {chat_id}: تم حذف المجموعة أو البوت ليس عضواً. سيتم حذفها من القائمة.")
                del group_activations[chat_id]
                save_groups()
            else:
                print(f"⚠️ فشل إرسال رسالة إلى المجموعة {chat_id}: {e}")

@bot.message_handler(commands=['start', 'help'])
def handle_general_commands(message):
    if message.chat.type == 'private' and not is_admin(message):
        bot.reply_to(message, "⚠️ هذا الأمر مخصص للمسؤول الرئيسي في الدردشة الخاصة.")
        return

    if message.text == '/start' or message.text == '/start@BOT_Friend_Free_Firebot':
        welcome_text = """
    أهلاً بك! أنا بوت يساعد في إدارة قائمة الأصدقاء في اللعبة.

    استخدم أمر /help لعرض قائمة الأوامر المتاحة.
    """
        bot.reply_to(message, welcome_text)
    
    elif message.text == '/help' or message.text == '/help@BOT_Friend_Free_Firebot':
        help_text = """
<b>Gh0stSANTA Is Backkkkkk ⚠️</b>

<b>الاوامر المتاحة لك ✅:</b>

„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"
لإضافة شخص:
<code>/add &lt;id&gt; [عدد_الايام]</code>

„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"
لإزالة شخص:
<code>/remove &lt;id&gt;</code>
"""

        if is_admin(message):
            help_text += """
<b>الأوامر التالية للمسؤول الرئيسي فقط:</b>

„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"
لعرض جميع المضافين:
<code>/list</code>

„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"
لحذف جميع المضافين:
<code>/remove_all</code>

„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"
لتفعيل البوت في مجموعة:
<code>/sid &lt;عدد_الأيام&gt;</code>
(في المجموعة)
„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"

لإيقاف البوت في مجموعة:
<code>/stop</code>
(في المجموعة)

„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"
وضع الصيانة:
<code>/maintenance</code>

<code>/unmaintenance</code>

„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"„"
للخروج من مجموعة:
<code>/leave_group &lt;ايدي_المجموعة&gt;</code>
(في الخاص)
"""
        bot.reply_to(message, help_text, parse_mode="HTML")

@bot.message_handler(commands=['maintenance'])
def enable_maintenance_mode(message):
    if not is_admin(message):
        bot.reply_to(message, "🔒 هذا الأمر مخصص للمسؤول الرئيسي فقط.")
        return

    global maintenance_mode
    if maintenance_mode:
        bot.reply_to(message, "⚠️ البوت بالفعل في وضع الصيانة.")
        return

    maintenance_mode = True
    save_maintenance_status(True)
    
    maintenance_message = "⚙️ تنبيه صيانة ⚙️\n\n⚠️ البوت في وضع الصيانة