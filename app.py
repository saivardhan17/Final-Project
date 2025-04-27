# app.py

import streamlit as st
from review_summarizer import summarizer_workflow
from chatbot_generator import chatbot_workflow

from sentiment_analyzer import sentiment_workflow
from marketing_copy_generator import marketing_workflow

st.set_page_config(page_title="AutoCommerce Suite", layout="wide")

st.title(" AutoCommerce Suite")
st.sidebar.title("Select a Feature")

option = st.sidebar.selectbox(
    "Choose a functionality:",
    (
        "Chatbot Generator from FAQ",
        "Product Review Summarizer",
        "Customer Sentiment Analyzer",
        "Marketing Copy Generator"
    )
)

if option == "Chatbot Generator from FAQ":
    chatbot_workflow()
elif option == "Product Review Summarizer":
    summarizer_workflow()
elif option == "Customer Sentiment Analyzer":
    sentiment_workflow()
elif option == "Marketing Copy Generator":
    marketing_workflow()
import discord
from discord.ext import commands

# --------------- SETUP ---------------

# Your bot token
TOKEN = 'MTM2NjA0MTE3MDI0NTA1ODU3Mg.GRcj2j.x2eiX-aRasZqoPiaGhoCwSOE5ermkhotVCXch8'

# Set up intents (important to read message content)
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


# Example Q&A pairs
qa_pairs = {
    "Hi": "Hello! How can I help you today?",
    "who are you": "I am your friendly Discord bot!",
    "help": "Sure, what do you need help with?",
    "bye": "Goodbye! Have a great day!",
    "what is AI": "AI stands for Artificial Intelligence. It refers to the ability of computer systems to perform tasks that typically require human intelligence, such as learning, problem-solving, and decision-making. In simpler terms, AI is about making machines think and act like humans."
}

# --------------- EVENTS ---------------

# Event when bot is ready
@bot.event
async def on_ready():
    print(f' Bot is online! Logged in as: {bot.user}')

# Event when a message is sent
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    print(f'📩 Message received: {message.content} from {message.author}')

    msg_content = message.content.lower().strip()  # strip extra spaces

    for question, answer in qa_pairs.items():
        if question in msg_content:
            print(f'💬 Sending response: {answer}')
            await message.channel.send(answer)
            break  # important: don't send multiple replies
    
    await bot.process_commands(message)


# --------------- COMMANDS ---------------

@bot.command()
async def ping(ctx):
    print(' Ping command triggered')
    await ctx.send('Pong!')

# --------------- RUN BOT ---------------

bot.run(TOKEN)
