import os
import google.generativeai as genai
import importlib
from dotenv import load_dotenv
import logging
from io import BytesIO

# Load environment variables
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API Key not found. Please check your .env file.")

# Configure Google Generative AI
genai.configure(api_key=api_key)

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

system_instruction = """
*System Name:* KORA AI Assistance by Kolawole Suleiman...
"""

# Handle general text messages
def handle_text_message(user_message):
    """
    Processes regular text messages from the user.
    
    :param user_message: The message text from the user.
    :return: AI-generated response.
    """
    try:
        logger.info("Processing text message: %s", user_message)

        # Start a chat with the model
        chat = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config={
                "temperature": 0.3,
                "top_p": 0.95,
                "top_k": 64,
                "max_output_tokens": 8192,
            }
        ).start_chat(history=[])

        # Generate a response to the user's message
        response = chat.send_message(f"{system_instruction}\n\nHuman: {user_message}")
        return response.text

    except Exception as e:
        logger.error("Error processing text message: %s", str(e))
        return "Sorry, I encountered an error processing your message."

# Handle text commands
def handle_text_command(command_name):
    try:
        # Get the path to the CMD directory
        cmd_folder = "CMD"
        
        # List all the .py files in the CMD directory
        for filename in os.listdir(cmd_folder):
            if filename.endswith(".py"):  # Check if file ends with .py
                module_name = filename[:-3]  # Remove the .py extension
                try:
                    # Dynamically import the module
                    cmd_module = importlib.import_module(f"{cmd_folder}.{module_name}")
                    logger.info(f"Module {module_name} loaded successfully.")
                    
                    # Call the execute function from the module
                    return cmd_module.execute()
                except Exception as e:
                    logger.error(f"Error loading module {module_name}: {e}")
                    continue
        
        return "No commands found in CMD directory."

    except Exception as e:
        logger.error(f"Error handling text command: {str(e)}")
        return "An error occurred while processing the command."

# Handle attachments (e.g., direct images)
def handle_attachment(attachment_data, attachment_type="image"):
    """
    Processes attachments sent by the user.
    
    :param attachment_data: Raw data of the attachment (e.g., image bytes).
    :param attachment_type: Type of the attachment (default is 'image').
    :return: AI-generated response or a message about the attachment.
    """
    if attachment_type == "image":
        logger.info("Direct image received for processing.")
        
        try:
            # Use another API like Google Vision API for image processing (if supported)
            # If you still want to process images using generative AI, make sure the model supports it

            response = "Image received, but processing with generative AI may not be supported."

            logger.info("Image processed successfully.")
            return response

        except Exception as e:
            logger.error("Failed to process image: %s", str(e))
            return "Error processing the image."
    
    logger.info("Unsupported attachment type: %s", attachment_type)
    return "Unsupported attachment type."
