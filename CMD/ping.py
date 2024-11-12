import time
import psutil
import platform
from datetime import timedelta

def execute():
    # Bot basic information
    bot_name = "KORA"
    owner = "Kolawole Suleiman"
    version = "v1.0"

    # Get runtime and storage details
    uptime = time.time() - psutil.boot_time()
    uptime_str = str(timedelta(seconds=int(uptime)))
    
    # Storage info
    disk_usage = psutil.disk_usage('/')
    total_storage = f"{disk_usage.total / (1024 ** 3):.2f} GB"
    used_storage = f"{disk_usage.used / (1024 ** 3):.2f} GB"
    free_storage = f"{disk_usage.free / (1024 ** 3):.2f} GB"

    # Memory info
    memory = psutil.virtual_memory()
    total_memory = f"{memory.total / (1024 ** 2):.2f} MB"
    used_memory = f"{memory.used / (1024 ** 2):.2f} MB"
    free_memory = f"{memory.available / (1024 ** 2):.2f} MB"

    # System info
    system_info = platform.system() + " " + platform.release()
    python_version = platform.python_version()

    # Formatted response with emojis
    response = (
        f"🤖 **Bot Information** 🤖\n"
        f"**Name**: {bot_name}\n"
        f"**Owner**: {owner}\n"
        f"**Version**: {version}\n\n"
        f"🕒 **Uptime**: {uptime_str}\n\n"
        f"💾 **Storage**\n"
        f"   - Total: {total_storage}\n"
        f"   - Used: {used_storage}\n"
        f"   - Free: {free_storage}\n\n"
        f"📊 **Memory**\n"
        f"   - Total: {total_memory}\n"
        f"   - Used: {used_memory}\n"
        f"   - Free: {free_memory}\n\n"
        f"🖥️ **System**\n"
        f"   - OS: {system_info}\n"
        f"   - Python: {python_version}\n"
    )

    return response
