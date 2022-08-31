import os
import openai
from dotenv import load_dotenv 
load_dotenv()

openai.api_key = os.getenv(
"OPENAI_API_KEY")

start_sequence = "\nBot:"
restart_sequence = "\n\nUser:"
session_prompt = "Bot is a GPT-3 chatbot who runs on the OpenAI api.\n\n###\nUser: How many pounds are in a kilogram?\nBot: This again? There are 2.2 pounds in a kilogram. Please make a note of this.\n###\nUser: What do you think about economics and the division of labour? Bot On division of labor: It is not immediately intuitive that specializing rather than generalizing would increase productivity, but because humans are innovators those that specialize also innovate their craft and leverage insight to increase their production."

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
      model="text-ada-001"
      prompt=prompt_text,
      temperature=0.8,
      max_tokens=250,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.3,
      stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
