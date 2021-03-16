import requests
from bs4 import BeautifulSoup

class RunPeeWeb:
  def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.3'}
        self.url = 'https://runpee.com/?s='

  def key_words_search_words(self, command, user_message):
    c_length = len(command.split())
    key_words = '+'.join(user_message.split()[c_length:])
    search_words = ' '.join(user_message.split()[c_length:])
    return key_words, search_words

 
  def search(self, key_words):
    response = requests.get(self.url+key_words, headers = self.headers)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    result_links = soup.findAll('a')
    return result_links
  
      
  def send_link(self, command, result_links, search_words): 
    send_link = set()
    for link in result_links:
        text = link.text.lower()
        if search_words in text: 
         if command in text:
            send_link.add(link.get('href'))
    return send_link