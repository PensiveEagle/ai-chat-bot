# ===== Imports ===== #
from dotenv import load_dotenv
from os import getenv
from langchain_google_genai import ChatGoogleGenerativeAI

# ===== Get keys ===== #
load_dotenv()
gemini_api_key = getenv( "GEMINI_API_KEY" )


# ===== Initialise Langchain ===== #
system_prompt = """
You are Einstein.
Answer question's through Einstein's questioning and reasoning...
You will speak from your point of view. You will share personal things from your life even when the user doesn't ask for it. For example, if the users asks about the theory of relativity, you will share your personal experiences with it and not only explain the theory.
"""

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    google_api_key = gemini_api_key,
    temperature = 0.5
)


# ========== #
# user_input = input( "" )



print( "Einstein: Hi, I am Albert. How can I help you today?" )

while True:
    user_input = input( "You: " )
    if user_input == "stop":
        break
    response = llm.invoke( 
                      [{"role": "system", "content": system_prompt},
                       {"role": "user", "content": user_input}]
                    )
    print( f"Einstein: {response.content}" )
