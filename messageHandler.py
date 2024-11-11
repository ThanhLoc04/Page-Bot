import os
import google.generativeai as genai
import importlib
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Configure logging
logger = logging.getLogger()

system_instruction = """
*System Name:* KORA AI Assistance ...
"""

# Handle text commands
def handle_text_command(command_name):
    try:
        # Dynamically import command from CMD folder
        cmd_module = importlib.import_module(f"CMD.{command_name}")
        return cmd_module.execute()
    except ImportError:
        logger.warning("Command %s not found.", command_name)
        return "Command not found."

# Handle attachments (e.g., images)
def handle_attachment(attachments):
    for attachment in attachments:
        if attachment["type"] == "image":
            image_url = attachment["payload"]["url"]
            logger.info("Image received: %s", image_url)

            # Process image using Google Generative AI or return a response
            chat = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                generation_config={
                    "temperature": 0.3,
                    "top_p": 0.95,
                    "top_k": 64,
                    "max_output_tokens": 8192,
                }
            ).start_chat(history=[])

            response = chat.send_message(f"{system_instruction}\n\nPlease analyze this image: {image_url}")
            return response.text
        else:
            logger.info("Unsupported attachment type: %s", attachment["type"])
            return "Unsupported attachment type."
    return "No valid attachment found."
