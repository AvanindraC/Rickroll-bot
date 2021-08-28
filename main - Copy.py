import wikipedia
import discord
from discord.ext import commands
import re, requests, urllib.parse, urllib.request
from googlesearch import search
import random
import praw
from keep_alive import keep_alive
import pyjokes
from tawpy import Tenor
from tawpy import Enum
from datetime import datetime
import pytz
client = discord.Client()
def timezone(one, two):  
    a =  pytz.timezone(one)
    b= pytz.timezone(two)

    datetime_utc = datetime.now(a)
    res1 =  datetime_utc.strftime('%H:%M %Z %z')
    res1 = res1+"\n"
  
    datetime_ist = datetime.now(b)
    res2 = datetime_ist.strftime('%H:%M %Z %z')
    em = discord.Embed(description = res1 + res2, color=discord.Color.from_rgb(0, 255, 255))
    return em
def rickroll():
  vids = [ 'https://user-images.githubusercontent.com/77975448/130755920-2eeef248-8976-4de1-97db-0421b9631bd1.mp4', 'https://user-images.githubusercontent.com/77975448/130755923-d55eac65-d407-4711-8720-f57fd7389e8c.mp4', 'https://user-images.githubusercontent.com/77975448/130756539-4edb3240-0894-45ad-93b2-2f9c57c6b6ff.mp4',
'https://user-images.githubusercontent.com/77975448/130756569-064040f7-17f9-4923-904e-5fc4ee0fd1da.mp4', 'https://user-images.githubusercontent.com/77975448/130760005-b69b2ba2-8294-4d4c-9976-d5eb379ef2df.mp4', 'https://user-images.githubusercontent.com/77975448/130760014-fc1395af-5b0a-4f63-a2cb-84e92d757ab9.mp4', 'https://user-images.githubusercontent.com/77975448/130760022-9346ee5e-6dcb-402c-a56a-e7bb58db9aaf.mp4', 'https://user-images.githubusercontent.com/77975448/130760038-35a6c47f-dd2b-45a5-900d-866178052345.mp4', 'https://user-images.githubusercontent.com/77975448/130760058-063ad085-4c72-4882-8298-f1d2c332581d.mp4', 'https://user-images.githubusercontent.com/77975448/130760072-a094d2f7-35f6-4716-a638-f63f6d5d2289.mp4',
'https://user-images.githubusercontent.com/77975448/130773300-47e0ee11-de3f-4ae7-b209-4eae9d74e19d.mp4', 'https://user-images.githubusercontent.com/77975448/130773303-88765288-4da4-4f67-bad6-afdc6d5135cf.mp4', 
'https://user-images.githubusercontent.com/77975448/130776465-5d766839-2824-4434-ad57-60384dfc9ae0.mp4', 'https://user-images.githubusercontent.com/77975448/130776602-5279e8a5-3ec5-4857-9d07-1bef7249cb14.mp4', 'https://user-images.githubusercontent.com/77975448/130776588-0b8ab582-fabc-48d5-b98a-0f614315bd5e.mp4', 'https://user-images.githubusercontent.com/77975448/130777016-315d09ad-5677-4b4f-a839-8d33ea27e5a9.mp4', 'https://user-images.githubusercontent.com/77975448/130961886-369efc51-7db0-45a1-87b6-5890d7a7530a.mp4','https://user-images.githubusercontent.com/77975448/130755914-6ef3fb40-0c6c-4c41-a16a-659962a35751.mp4','https://user-images.githubusercontent.com/77975448/130760058-063ad085-4c72-4882-8298-f1d2c332581d.mp4', 'https://user-images.githubusercontent.com/77975448/130963376-0bc1f40a-5bcd-459e-a3cd-5d0adc55ae8d.mp4', 'https://user-images.githubusercontent.com/77975448/130963387-926845d7-76a9-4ed7-8ed8-a9b5360788e7.mp4', 'https://user-images.githubusercontent.com/77975448/130963394-930cbe7a-757c-4156-b7b0-b498bb0bd580.mp4']
  vid = random.choice(vids)
  return vid
def gif(self, content):
  


  tenor = Tenor()
  a = tenor.search_for_gifs(query=content)
  url = random.choice(a)
  em = discord.Embed(color=discord.Color.from_rgb(0, 255, 255))
  em.set_image(url=url)
  return em
def joke():
  jk=pyjokes.get_joke(language='en', category= 'neutral')
  return jk
def memes():
  reddit = praw.Reddit(client_id ='', 
                     client_secret = '', 
                     user_agent = '')
  sr = random.choice(['memes', 'dankmemes', 'sciencememes', 'queenmemes', 'linuxmemes', 'IndianDankMemes', 'animememes'])
  submission = reddit.subreddit(sr).random()#top(over_18=False)
  
  
  title = submission.title
  url =  submission.url
  em = discord.Embed(title=title,  color=discord.Color.from_rgb(0, 255, 255))
  em.set_image(url=url)
  return em

async def pa(embeds,ctx):
      message=await ctx.send(embed=embeds[0])
      pag=0
      await message.add_reaction("◀️")
      await message.add_reaction("▶️")
      def check(reaction, user):          
          return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
      while True:
          try:
              reaction, user= await client.wait_for("reaction_add", timeout=360, check=check)
              #await message.remove_reaction(reaction, user)
              if str(reaction.emoji) == "▶️" and pag+1!=len(embeds):
                  pag+=1
                  await message.edit(embed=embeds[pag])
              elif str(reaction.emoji) == "◀️" and pag!=0:
                  pag-=1
                  await message.edit(embed=embeds[pag])
          except asyncio.TimeoutError:
             break

def fact():
  reddit = praw.Reddit(client_id ='', 
                     client_secret = '', 
                     user_agent = '')
  sr = 'interestingasfuck'
  submission = reddit.subreddit(sr).random()#top(over_18=False)
  
  
  title = submission.title
  url =  submission.url
  em = discord.Embed(title=title,  color=discord.Color.from_rgb(0, 255, 255))
  em.set_image(url=url)
  return em
def getlink(song):
    music_name = song
    query_string = urllib.parse.urlencode({"search_query": music_name})
    formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
    search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
    clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
    clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
    return clip2
def google(query):
    last = search(query)
    result=""
    for i in last:
        result+=i+"\n"
    return result
def wikipediaa(query):
    results= wikipedia.summary(query, sentences=5)
    return results
def help():
  em = discord.Embed(title="**Never Gonna Give y'all up**", description=
  '''**Rickroll-bot**\n **Prefix** r%\n **Commands :** \n google (Search google)\n getytlink (Get youtube link of a video)\n wiki (Search wikipedia)\n joke (get a joke)\nmeme (memes from reddit)\n gif (get a gif from a topic)\ninteresting (get something interesting)\n tz (allows you to see the time of two timezones and compare them)\ngtz (Get the your timezone by giving the abreviation of you country. For eg. China = CN, India = IN)''',   color=discord.Color.from_rgb(0, 255, 255))
  em.set_image(url='https://c.tenor.com/rtnshG9YFykAAAAd/rick-astley-rick-roll.gif')
  return em
def help_admin():
  em = discord.Embed(title="**Never Gonna Give y'all up**", description=
  '''**Rickroll-bot**\n **Prefix** r%\n **Commands :** \n google (Search google)\n getytlink (Get youtube link of a video)\n wiki (Search wikipedia)\n joke (get a joke)\nmeme (memes from reddit)\n gif (get a gif from a topic)\nwelcome (gives a link to rickroll)\nsurprise (a nifty little surprise)\npingstrike <person> (pings 10 times. Only to be use in complete emergencies)\ninteresting (get something interesting)\n tz (allows you to see the time of two timezones and compare them)\ngtz (Get the your timezone by giving the abreviation of you country. For eg. China = CN, India = IN)''',   color=discord.Color.from_rgb(0, 255, 255))
  em.set_image(url='https://c.tenor.com/rtnshG9YFykAAAAd/rick-astley-rick-roll.gif')
  return em
def welcome():
  em = discord.Embed(title="**Welcome to our server**", description=
  '''**To gain access to the server, pass this challenge:**
  https://drive.google.com/file/d/102M_T9cf6bW5kpgGJtyGviVAiOpeAkkG/view?usp=sharing
  ''', color=discord.Color.from_rgb(0, 255, 255))
  return em
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('r%hello'):
        await message.channel.send(f'Never gonna give you up {message.author.mention}')
    if message.content.startswith('r%getytlink'):
        message.content = message.content.strip('r%getytlink ')
        await message.channel.send(getlink(message.content))
    if message.content.startswith('r%google'):
        message.content = message.content.strip('r%google ')
        await message.channel.send(google(message.content))
    if message.content.startswith('r%help'):
        await message.channel.send(embed = help())
    if message.content.startswith('r%wiki '):
        message.content = message.content.strip('r%wiki')
        print(message.content)
        await message.channel.send(wikipediaa(message.content))
    if message.content.startswith('r%joke'):
        await message.channel.send(joke())
    if message.content.startswith('r%welcome'):
        await message.channel.send(embed=welcome())
    if message.content.startswith('r%meme'):
      await message.channel.send(embed=memes()) 
    if message.content.startswith('r%gif'):
      message.content = message.content.strip('r%gif ')
      await message.channel.send(embed=gif(self = ' ', content=message.content))
    if message.content.startswith('r%surprise'):
      await message.channel.send("Here's a special video generated by A.I. made for you") 
      await message.channel.send(rickroll()) 
    if message.content.startswith('r%ps'):
        message.content = message.content.strip('r%ps')

        for i in range(1, 11):
          await message.channel.send(message.content)
        
    if message.content.startswith('r%admin_help'):
      await message.channel.send(embed = help_admin())
    if message.content.startswith('r%tz'):
      message.content = message.content.strip('r%tz ')
      print(message.content)
      wun, too = message.content.split(' ')
      print(message.content)
      await message.channel.send(embed = timezone(wun, too))
    if message.content.startswith('r%interesting'):
      await message.channel.send(embed=fact()) 
    if message.content.startswith('r%gtz'):
      message.content = message.content.strip('r%gtz ')
      await message.channel.send(pytz.country_timezones(message.content))
keep_alive()    
client.run('token')
