from logging import exception
import lightbulb
import hikari
import random as rand
import math

bot = lightbulb.BotApp(
    token='', 
    default_enabled_guilds=()
)

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('Bot is now online.')

@bot.command
@lightbulb.command('rules', 'Literally 1984')
@lightbulb.implements(lightbulb.SlashCommand)
async def rules(ctx):
    await ctx.respond("Please **DO NOT** announce to the server when you are going to masturbate. This has been a reoccurring issue, and I\'m not sure why some people have such under developed social skills that they think that a server full of mostly male strangers would need to know that. No one is going to be impressed and give you a high five (especially considering where that hand has been). I don't want to add this to the rules, since it would be embarrassing for new users to see that we have a problem with this, but it is going to be enforced as a rule from now on. \n\nIf it occurs, you will be warned, then additional occurrences will be dealt with at the discretion of modstaff. Thanks.")

@bot.command
@lightbulb.command('utilities','General utilities commands')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group(ctx):
    pass

@my_group.child
@lightbulb.command('heyguys', 'Hey guys')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def heyguys(ctx):
    await ctx.respond('Hey guys')

@my_group.child
@lightbulb.option('picked', 'Rock, paper, or scissors', type=str)
@lightbulb.command('simplerps', 'Rock, paper, scissors to decide who takes OF (lmao)')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def simplerps(ctx):
    if ctx.options.picked == 'rock':
        await ctx.respond(':rock:')
    elif ctx.options.picked == 'paper':
        await ctx.respond(':newspaper:')
    elif ctx.options.picked == 'scissors':
        await ctx.respond(':scissors:')
    else:
        await ctx.respond('Input invalid.')

@bot.command
@lightbulb.command('pricoutils','Priconne utilities')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group1(ctx):
    pass

@my_group1.child
@bot.command
@lightbulb.option('bosshp', 'Remaining Boss HP', type=int)
@lightbulb.option('higherdmg', 'Higher Damage Hit (Releases First)', type=int)
@lightbulb.option('lowerdmg', 'Lower Damage Hit (Releases Last)', type=int)
@lightbulb.command('oftime', 'Overflow Time calculator for sync hits')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def oftime(ctx):
    await ctx.respond('Your overflow time is ' + str(math.ceil((90 * (1 - (ctx.options.bosshp - ctx.options.higherdmg) / ctx.options.lowerdmg) + 20))) + ' seconds.')

@my_group1.child
@bot.command
@lightbulb.option('currentrarity', 'Current Rarity')
@lightbulb.option('targetrarity', 'Target Rarity')
@lightbulb.option('boughtshards', 'Amount of Shards Already Bought')
@lightbulb.option('currentshards', 'Amount of Current Shards')
@lightbulb.command('amuletcost', 'Divine amulet cost calculator for unit shards')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def amuletcost(ctx):
    await ctx.respond('Syntax error')

@my_group1.child
@bot.command
@lightbulb.option('damage', 'Current Damage')
@lightbulb.option('instances', 'Number of Damage Instances')
@lightbulb.command('logbarrier', '(dev) Log barrier filtered damage calculator for instanced dmg numbers')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def logbarrier(ctx):
    await ctx.respond('Syntax error')

@bot.command
@lightbulb.command('akasha','Genshin utilities')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def akasha(ctx):
    pass

@akasha.child
@bot.command
@lightbulb.option('critrate', 'Crit Rate', type=float)
@lightbulb.option('critdmg', 'Crit DMG', type=float)
@lightbulb.command('cvcalc', 'Calculate artifact CV and rate it (WIP)')
@lightbulb.implements(lightbulb.SlashSubCommand)

async def cvcalc(ctx):
    totalCV = float((ctx.options.critrate * 2.0) + ctx.options.critdmg)
    response = ''
    if (totalCV < 20):
      response = ' (**1/5, It\'s trash!**)'
    elif (totalCV >= 20) and (totalCV < 32):
      response = ' (**2/5, It\'s decent!**)'
    elif (totalCV >= 32) and (totalCV < 36):
      response = ' (**3/5, It\'s good!)'
    elif (totalCV >= 36) and (totalCV < 45):
      response = ' (**4/5, It\'s insane!**)'
    elif (totalCV >= 45) and (totalCV < 55):
      response = ' (**5/5, It\'s literally rigged! Fuck you!**)'
    elif (totalCV >= 55):
      response = ' (**That artifact literally cannot exist!**)'
    await ctx.respond('Your Artifact\'s CV is ' + str(totalCV) + str(response))

@akasha.child
@bot.command
@lightbulb.option('choice','4star or 5star', type=str)
@lightbulb.command('tierlist','Character strength tierlist (Last Updated: Patch 3.4)')
@lightbulb.implements(lightbulb.SlashSubCommand)

async def tierlist(ctx):
  message = ''
  if (ctx.options.choice == '4star'):
    message = '**Take with a grain of salt. Last updated 12/18/2022** https://media.discordapp.net/attachments/1038426042462904401/1053884602294480996/4stars_tierlist_34.png?width=600&height=669'
  elif (ctx.options.choice == '5star'):
    message = '**Take with a grain of salt. Last updated 12/18/2022** https://media.discordapp.net/attachments/1038426042462904401/1053884602613244005/5stars_tierlist_34.png?width=575&height=670' 
  else:
    message = 'Invalid input!'
  await ctx.respond(str(message))

@akasha.child
@bot.command
@lightbulb.command('niloupost', 'Posts a random Nilou image')
@lightbulb.implements(lightbulb.SlashSubCommand)

async def niloupost(ctx):
  post = rand.randint(1,10)
  if (post == 1):
    image = 'https://twitter.com/chenyileiFCC/status/1604215016810430464'
  elif (post == 2):
    image = 'https://twitter.com/Tatonxry/status/1602994900751962114'
  elif (post == 3):
    image = 'https://twitter.com/hyura3/status/1602984204484100097'
  elif (post == 4):
    image = 'https://twitter.com/Toi1et_Paper/status/1601162290992058368'
  elif (post == 5):
    image = 'https://twitter.com/AON__oo/status/1601833158508363777'
  elif (post == 6):
    image = 'https://twitter.com/SprygonL/status/1601199674395791360'
  elif (post == 7):
    image = 'https://twitter.com/sssong_aa/status/1600493247310475264'
  elif (post == 8):
    image = 'https://twitter.com/Yu_Hydra0319/status/1599049434859732992'
  elif (post == 9):
    image = 'https://twitter.com/ReReReRe_mon/status/1598693851127947264'
  elif (post == 10):
    image = 'https://twitter.com/Sco_ttie/status/1598936731398852610'
  await ctx.respond(str(image))

bot.run()
