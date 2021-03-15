import discord
import os
import search_runpee
from dotenv import load_dotenv

# Use python-dotenv pakcage to get variables stored in .env file of your project
load_dotenv()

client = discord.Client()
no_result_message = 'Sorry, we can\'t find what you are searching for. We may not have written anything about it yet, but you can subscribe to our news letter for updates of our newest content --> https://runpee.com/about-runpee/runpee-movie-newsletter/'


@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message): 
  if message.author == client.user:
      return  
  # lower case message
  message_content = message.content.lower()  

  # instantiate RunPeeWeb class from search_runpee.py
  runpee_web = search_runpee.RunPeeWeb()
  
  if message.content.startswith(f'$hello'):
    await message.channel.send('Hello there! I\'m the bad robot you fart face.')
  
  if f'$search' in message_content:

    key_words, search_words = runpee_web.key_words_search_words('$search', message_content)
    result_links = runpee_web.search(key_words)
    links = send_link(' ', result_links, search_words)
    if len(links) > 0:
      for link in links:
       await message.channel.send(link)
    else:
      await message.channel.send(no_result_message)

    
def send_link(command, result_links, search_words):
  send_link = set()
  for link in result_links:
      text = link.text.lower()
      if search_words in text: 
        if command in text:
          send_link.add(link.get('href'))
  return send_link

# print(os.getenv('TOKEN'))
print('TOKEN' in os.environ)

client.run(os.getenv('TOKEN'))
