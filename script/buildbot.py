import os
import sys
import telebot

# Đọc biến môi trường
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHATID")
DEVICE = os.environ.get("DEVICE", "Unknown Device")
KPM = os.environ.get("KPM", "N/A")
lz4kd = os.environ.get("LZ4KD", "Off")
BBR = os.environ.get("BBR", "Off")
KSU_VAR = os.environ.get("KSU_VAR", "KSU")
kernelversion = os.environ.get("KERNEL_VERSION", "0.0.0")
ksuver = os.environ.get("KSUVER", "v0.0")

# Template tin nhắn
MSG_TEMPLATE = """
<b>New Build Published!</b>
#{device}
<pre>Kernel Info
kernelver: {kernelversion}
KSU_VAR: {KSU_VAR}
KsuVersion: {Ksuver}
KPM: {kpm}
Lz4kd: {lz4kd}
Lz4&zstd: {lz4_zstd}
BBR: {BBR}
</pre>
Cảm ơn vì đã đến ❤️
Please Join Our Group! tg @vieosoneplus
""".strip()

def check_lz4_zstd():
    return "On" if lz4kd == "Off" else "Off"

def get_caption():
    caption = MSG_TEMPLATE.format(
        device=DEVICE,
        kernelversion=kernelversion,
        Ksuver=ksuver,
        KSU_VAR=KSU_VAR,
        kpm=KPM,
        lz4kd=lz4kd,
        lz4_zstd=check_lz4_zstd(),
        BBR=BBR,
    )
    return caption if len(caption) <= 1024 else f"{DEVICE} - {kernelversion}"


def upload_zip_files():
    bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")
    files = sys.argv[1:]
    for file_path in files:
        file_name = os.path.basename(file_path)
        if not os.path.exists(file_path):
            print(f"[-] File not found: {file_path}")
            continue
        with open(file_path, "rb") as file:
            bot.send_document(CHAT_ID, file, caption=get_caption())
            print(f"Uploaded: {file_name}")

if __name__ == "__main__":
    upload_zip_files()
