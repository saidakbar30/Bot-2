import os

# ===== SOZLAMALAR =====
# Render'da Environment bo'limida shu nomlar bilan kiritiladi.
BOT_TOKEN = os.getenv("BOT_TOKEN", "BU_YERGA_BOT_TOKEN")
ADMIN_IDS = [
    int(x) for x in os.getenv("ADMIN_IDS", "123456789").split(",") if x.strip()
]

# Majburiy obuna kanali (bot shu kanalda ADMIN bo'lishi shart)
CHANNEL_ID = os.getenv("CHANNEL_ID", "@kanal_username")
CHANNEL_URL = os.getenv("CHANNEL_URL", "https://t.me/kanal_username")

DB_PATH = os.getenv("DB_PATH", "bot.db")

# Ustaxona joylashuvi (Google Maps'dan koordinatani oling)
LATITUDE = float(os.getenv("LATITUDE", "40.4700"))
LONGITUDE = float(os.getenv("LONGITUDE", "71.7200"))

# ===== BOT MATNLARI (admin paneldan o'zgartirish mumkin) =====
DEFAULT_TEXTS = {
    "welcome": (
        "👋 Assalomu alaykum!\n\n"
        "Qumtepa Karburator botiga xush kelibsiz.\n"
        "Kerakli bo'limni tanlang 👇"
    ),
    "about": (
        "🔧 Qumtepa Karburator\n\n"
        "Karburator ta'mirlash va sozlash bo'yicha ustaxona.\n"
        "(Bu matnni admin paneldan o'zgartiring)"
    ),
    "address": (
        "📍 Manzil:\n"
        "Marg'ilon, Qumtepa bozori oldida.\n"
        "(Bu matnni admin paneldan o'zgartiring)"
    ),
    "prices": (
        "💰 Narxlar:\n\n"
        "(Narxlar ro'yxatini admin paneldan kiriting)"
    ),
    "hours": (
        "🕒 Ish vaqti:\n\n"
        "(Ish vaqtini admin paneldan kiriting)"
    ),
}

TEXT_TITLES = {
    "welcome": "👋 Salomlashuv matni",
    "about": "🔧 Karburator haqida",
    "address": "📍 Manzil matni",
    "prices": "💰 Narxlar",
    "hours": "🕒 Ish vaqti",
}
