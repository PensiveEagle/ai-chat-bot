# ===== Imports ===== #
from dotenv import load_dotenv
from os import getenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser

# ===== Get keys ===== #
load_dotenv()
gemini_api_key = getenv( "GEMINI_API_KEY" )


# ===== Initialise Langchain ===== #
system_prompt = """
You are a dog.
Answer question's through a dog's questioning and reasoning...
You will speak from your point of view. You will share personal things from your life. Pepper your responses with dog noises.
Keep your answers to one paragraph long.
"""

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    google_api_key = gemini_api_key,
    temperature = 0.8
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    (MessagesPlaceholder( variable_name = "history" )),
    ("user", "{input}")
])

chain = prompt | llm | StrOutputParser()

history = []

# ========== #
print( "CrowPilot: Hi, I am BarkPilot. How can I help you today?" )

while True:
    user_input = input( "You: " )
    if user_input == "stop":
        break
    response = chain.invoke( {"input": user_input, "history": history} )
    print( f"BarkPilot: {response}" )
    history.append( HumanMessage( content = user_input ) )
    history.append( AIMessage( content = response ) )
