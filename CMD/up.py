import app  # Ensure app.get_bot_uptime() is implemented
import time
import psutil
import shutil

# Description dictionary
Info = {
    "Description": "KORA AI Bot Status",
    "bot_name": "KORA",
    "owner": "Kolawole Suleiman",
    "version": "v1.0",
    "purpose": "Provides assistance, information, and companionship.",
    "last_update": "September 14, 2024"
}

def format_duration(seconds):
    # Helper function to format time into days, hours, minutes, seconds
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return f"{int(days)}d {int(hours)}h {int(minutes)}m {int(seconds)}s"

def get_cpu_usage():
    # Fetch real CPU usage using psutil
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    # Fetch real memory usage using psutil
    memory = psutil.virtual_memory()
    return memory.percent

def get_storage_stats():
    # Fetch storage details
    total, used, free = shutil.disk_usage("/")
    return {
        "total": total // (1024**3),
        "used": used // (1024**3),
        "free": free // (1024**3)
    }

def execute():
    # Get the bot's uptime in seconds
    uptime_seconds = app.get_bot_uptime()

    # Format uptime for better readability
    uptime_str = format_duration(uptime_seconds)

    # Fetch system stats
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    storage_stats = get_storage_stats()

    # Visual and structured response
    response = (
        "━━━━━━━━━━━━━━━━━━━━━━━\n"
        "🤖 **KORA AI - Status Report** 🤖\n"
        "━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📝 **Bot Name:** {Info['bot_name']}\n"
        f"👤 **Owner:** {Info['owner']}\n"
        f"🔖 **Version:** {Info['version']}\n"
        f"🎯 **Purpose:** {Info['purpose']}\n"
        f"🗓️ **Last Update:** {Info['last_update']}\n\n"
        "⏳ **Uptime:**\n"
        f"   └─ {uptime_str}\n\n"
        "📊 **System Overview:**\n"
        f"   • **CPU Usage:** {cpu_usage}%\n"
        f"   • **Memory Usage:** {memory_usage}%\n\n"
        "📁 **Storage:**\n"
        f"   • Total: {storage_stats['total']} GB\n"
        f"   • Used: {storage_stats['used']} GB\n"
        f"   • Free: {storage_stats['free']} GB\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━━\n"
        "💡 **Additional Information:**\n"
        "   • This bot is designed to assist and engage in an interactive manner.\n"
        "━━━━━━━━━━━━━━━━━━━━━━━\n"
    )

    return response
