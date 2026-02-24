# ===== Imports ===== #
from dotenv import load_dotenv
from os import getenv

# ===== Get keys ===== #
load_dotenv()
gemini_api_key = getenv( "GEMINI_API_KEY" )


# ===== Initialise Langchain ===== #



# ========== #
print( "Hi, I am Albert. How can I halp you today?" )

while True:
    user_input = input( "You: " )
    if user_input == "stop":
        break
    print( f"Cool thank for sharing '{user_input}'")
