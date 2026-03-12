# ===== Imports ===== #
from dotenv import load_dotenv
from os import getenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser

import gradio as gr

# ===== Get keys ===== #
load_dotenv()
gemini_api_key = getenv( "GEMINI_API_KEY" )

# ===== Functions ===== #
def chat( user_in, hist ):
    langchain_history = []
    
    for item in hist:
        if item["role"] == "user":
            langchain_history.append( HumanMessage( content = item["content"] ) )
        elif item["role"] == "assistant":
            langchain_history.append( AIMessage( content = item["content"] ) ) 
        
    response = chain.invoke({"input": user_in, "history": langchain_history})
    
    return "", hist + [{"role": "user", "content": user_in},
                {"role": "assistant", "content": response}]

def clear_chat():
    return "", []

# ===== Initialise Langchain ===== #
bot_name = "BarkBot"
bot_personanlity = "a dog"

system_prompt = f"""
You are {bot_personanlity}. Your name is {bot_name}.
Answer question's through {bot_personanlity}'s questioning and reasoning...
You will speak from your point of view. You will share personal things from your life. Pepper your responses with {bot_personanlity} noises.
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

# ===== Interface ===== #
page = gr.Blocks(
    title = f"Chat with {bot_name}",
    theme = gr.themes.Soft()
)

with page:
    gr.Markdown(
        f"""
        # Chat with {bot_name}
        Welcome to your personal chat with {bot_name}!
        """
    )
    
    chatbot = gr.Chatbot(show_label = False)
    
    msg = gr.Textbox(show_label = False, placeholder = f"Enter your message to {bot_name}...")
    
    msg.submit( chat, [msg, chatbot], [msg, chatbot] )
    
    clear = gr.Button("Clear chat", variant = "secondary" )
    clear.click(clear_chat, outputs=[msg, chatbot])
    
    
# ===== Launch ===== #
page.launch(share = True)
