# ===== Imports ===== #
from dotenv import load_dotenv
from os import getenv

# ===== Get keys ===== #
load_dotenv()
gemini_api_key = getenv( "GEMINI_API_KEY" )


# ===== Initialise Langchain ===== #



# ========== #
print( gemini_api_key )


