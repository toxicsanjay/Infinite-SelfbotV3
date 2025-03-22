import sys
import getpass
import discord
import requests
import asyncio
import time
import threading
import json
import os
import sys
import random
import pyjokes
from dhooks import Webhook
from discord.ext import commands, tasks
from googletrans import Translator, LANGUAGES

print("""

   _____ _______ ____  _____  __  __    _____ ______ _      ______ ____   ____ _______  __      ______  
  / ____|__   __/ __ \|  __ \|  \/  |  / ____|  ____| |    |  ____|  _ \ / __ \__   __| \ \    / /___ \ 
 | (___    | | | |  | | |__) | \  / | | (___ | |__  | |    | |__  | |_) | |  | | | |     \ \  / /  __) |
  \___ \   | | | |  | |  _  /| |\/| |  \___ \|  __| | |    |  __| |  _ <| |  | | | |      \ \/ /  |__ < 
  ____) |  | | | |__| | | \ \| |  | |  ____) | |____| |____| |    | |_) | |__| | | |       \  /   ___) |
 |_____/   |_|  \____/|_|  \_\_|  |_| |_____/|______|______|_|    |____/ \____/  |_|        \/   |____/ 

                                    Developer: notherxenon & ToxicSanjay
                                            Github: rifatgamingop                                                                   

""")

token = getpass.getpass("Give Your ID Token: ")
message = input("What do you want to spam?: ")
reason = input("Give the reasons to put on audits: ")

client = commands.Bot(command_prefix=">", self_bot=True)

@client.event
async def on_ready():
    print("Storm SelfBot Is Online")
    print("------------------------")
    print("Prefix is >")

client.help_command = None
client.remove_command("help")

# Help message for each category
general_help = """**# General Commands**
- `>help`           : Get a list of available commands
- `>ping`           : Check selfbot response time
- `>restart`        : Restart the selfbot
- `>about`          : Information about the selfbot
- `>math`           : Perform basic math operations
"""

server_help = """**# Server Commands**
- `>serverinfo`     : View server information
- `>servericon`     : Display server icon
- `>membercount`    : View the total number of members in the server
- `>renameserver`   : Rename the server
- `>renamechannels` : Rename channels in the server
- `>renameroles`    : Rename roles in the server
- `>copyserver`     : Duplicate the server's settings
- `>prune`          : Remove inactive members
- `>nickall`        : Change the nickname of all members
"""

user_help = """**# User Commands**
- `>userinfo`       : View information about a user
- `>afk`            : Set yourself as AFK (Away From Keyboard)
- `>dm`             : Send a direct message to a user
- `>dmall`          : Send a direct message to all members
"""

fun_help = """**# Fun Commands**
- `>joke`           : Get a random joke
- `>meme`           : Fetch a random meme
- `>hug`            : Hug another user
- `>slap`           : Slap another user
- `>kiss`           : Kiss another user
"""

packing_help = """**# Packing Commands**
- `>spam`           : Spam on the server with your provided amount
- `>react`          : Auto add reaction to all your message
- `>stopreact`      : Stop the auto reaction
- `>autoreply`      : Set up auto-replies for someone
- `>stopreply`      : Stop auto-replies
- `>gc`             : Start group name changing
- `>stopgc`         : Stop group name changing
"""

status_help = """**# Status Commands**
- `>listen`         : Set a "Listening to" status
- `>play`           : Set a "Playing" status
- `>stream`         : Set a "Streaming" status
- `>removestatus`   : Remove your current status
"""

utility_help = """**# Utility Commands**
- `>hook`           : Send a message via webhook
- `>encode`         : Encode a message or string
- `>decode`         : Decode a message or string
- `>translate`      : Translate text to another language
- `>purge`          : Purge a number of messages
- `>snipe`          : View the last deleted message
- `>ipinfo`         : Get information about an IP address
"""

crypto_help = """**# Crypto Commands**
- `>ltc_balance`    : Check your Litecoin (LTC) balance
"""

nuking_help = """**# Nuking Commands**
- `>wizz`           : Fully nuke server
- `>ban_everyone`   : Ban all members in the server
- `>massban`        : Ban multiple members at once
"""

# Create a dictionary to store the help texts
help_texts = {
    "general": general_help,
    "server": server_help,
    "user": user_help,
    "fun": fun_help,
    "packing": packing_help,
    "status": status_help,
    "utility": utility_help,
    "crypto": crypto_help,
    "nuking": nuking_help
}

# Help command to show the main categories
@client.command()
async def help(ctx, category=None):
    if category is None:
        # Show all categories
        help_message = """**# Storm Selfbot V3 Help Menu**
- `>help general`  : Show general commands
- `>help server`   : Show server commands
- `>help user`     : Show user commands
- `>help fun`      : Show fun commands
- `>help packing`  : Show packing commands
- `>help status`   : Show status commands
- `>help utility`  : Show utility commands
- `>help crypto`   : Show crypto commands
- `>help nuking`   : Show nuking commands
"""
        await ctx.send(help_message)
    else:
        # Show the help for a specific category
        category = category.lower()
        if category in help_texts:
            await ctx.send(help_texts[category])
        else:
            await ctx.send(f"Sorry, I couldn't find any help for `{category}`. Try `>help` for a list of categories.")



@client.command()
async def hook(ctx, user: discord.Member, *, message):
    if not ctx.author.guild_permissions.manage_webhooks:
        print("You do not have permissions to manage webhooks in that server.")
        await ctx.message.delete()
        return

    await ctx.message.delete()
    
    channel = ctx.channel
    avatar_url = user.avatar_url
    bytes_of_avatar = bytes(requests.get(avatar_url).content)
    webhook = await channel.create_webhook(name=f"{user.display_name}", avatar=bytes_of_avatar)
    print(user.display_name)
    webhook_url = webhook.url 
    WebhookObject = Webhook(webhook_url)
    WebhookObject.send(message)
    WebhookObject.delete()
    
def ssspam(webhook_url):
    while spams:
        data = {'content': message}
        try:
            response = requests.post(webhook_url, json=data)
            if response.status_code == 204:
                continue
            elif response.status_code == 429:  # Rate limit error
                retry_after = response.json().get('retry_after', 1) / 1000
                print(f"Rate limited. Retrying in {retry_after} seconds.")
                time.sleep(retry_after)
            else:
                print(f"Unexpected status code {response.status_code}: {response.text}")
                delay = random.randint(30, 60)
                time.sleep(delay)
        except Exception as e:
            print(f"Error in ssspam: {e}")
            delay = random.randint(30, 60)
            time.sleep(delay)

@client.command()
async def wizz(ctx):
    try:
        # Delete existing channels and roles
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()
            except Exception as e:
                print(f"Error deleting channel: {e}")

        # Edit guild
        try:
            await ctx.guild.edit(
                name='Server Got Nuked',
                description='Nuked Using Storm Selfbot',
                reason=reason,
                icon=None,
                banner=None
            )
        except Exception as e:
            print(f"Error editing guild: {e}")

        # Create 5 text channels
        channels = []
        for i in range(5):
            try:
                channel = await ctx.guild.create_text_channel(name='nuked by storm selfbot')
                channels.append(channel)
                await asyncio.sleep(1)  # Delay to prevent hitting rate limits
            except Exception as e:
                print(f"Error creating channel: {e}")

        # Create webhooks and start spamming
        global spams
        spams = True

        for channel in channels:
            try:
                webhook_name = 'Raped By Xenon & ToxicSanjay'  # Use a name that does not contain "discord"
                webhook = await channel.create_webhook(name=webhook_name)
                threading.Thread(target=ssspam, args=(webhook.url,)).start()
                await asyncio.sleep(1)  # Delay to prevent hitting rate limits
            except Exception as e:
                print(f"Webhook Error {e}")

    except Exception as e:
        print(f"Error in wizz command: {e}")

def get_ltc_balance(address):
    """Retrieve the LTC balance for a given address from BlockCypher API."""
    url = f'https://api.blockcypher.com/v1/ltc/main/addrs/{address}/balance'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        balance = data['final_balance'] / 1_000_000  # Convert satoshis to LTC
        return f"{balance:.8f}"  # Return balance with 8 decimal places
    except requests.RequestException as e:
        return f"Error retrieving balance: {e}"

@client.command()
async def ltc_balance(ctx, address):
    """View LTC balance from a given address."""
    balance = get_ltc_balance(address)
    await ctx.send(f"LTC balance for address {address}: {balance} LTC")

@client.command()
async def serverinfo(ctx):
    """Get information about the server."""
    guild = ctx.guild
    name = guild.name
    id = guild.id
    member_count = guild.member_count
    owner = guild.owner
    created_at = guild.created_at.strftime('%Y-%m-%d %H:%M:%S')
    await ctx.send(f"Server Name: {name}\nServer ID: {id}\nMembers: {member_count}\nOwner: {owner}\nCreated At: {created_at}")

@client.command()
async def userinfo(ctx, member: discord.Member = None):
    """Get information about a user."""
    member = member or ctx.author
    name = member.name
    id = member.id
    joined_at = member.joined_at.strftime('%Y-%m-%d %H:%M:%S')
    roles = [role.name for role in member.roles]
    await ctx.send(f"User Name: {name}\nUser ID: {id}\nJoined At: {joined_at}\nRoles: {', '.join(roles)}")

@client.command()
async def servericon(ctx):
    """Get the server's icon URL."""
    guild = ctx.guild
    icon_url = guild.icon.url
    await ctx.send(f"Server Icon URL: {icon_url}")

@client.command()
async def afk(ctx, *, reason="No reason provided"):
    """Set an advanced AFK status."""
    # Store the AFK status in a database or an in-memory structure if needed
    await ctx.send(f"{ctx.author.name} is now AFK: {reason}")
    
@client.command()
async def nickall(ctx, nickname):
     await ctx.reply("Starting Nicknaming all members in the server .")
     gey = 0
     for user in list(ctx.guild.members):
        try:
            await user.edit(nick=nickname)
            gey+=1
        except:
            pass
     try:await ctx.reply(f"Successfully changed nickname of {gey} members .")
     except:await ctx.send(f"Successfully changed nickname of {gey} members .")
     
@client.command()
async def copyserver(ctx, target_guild_id: int):
    # Delete old channels and roles in the target server
    target_guild = client.get_guild(target_guild_id)
    if not target_guild:
        await ctx.send("Target guild not found.")
        return

    # Delete all channels
    for channel in target_guild.channels:
        try:
            await channel.delete()
        except Exception as e:
            print(f"Error deleting channel: {e}")

    # Delete all roles
    for role in reversed(target_guild.roles):
        try:
            await role.delete()
        except Exception as e:
            print(f"Error deleting role: {e}")

    # Copy categories, channels, and roles
    for category in ctx.guild.categories:
        new_category = await target_guild.create_category(category.name)
        for channel in category.channels:
            if isinstance(channel, discord.VoiceChannel):
                await new_category.create_voice_channel(channel.name)
            elif isinstance(channel, discord.TextChannel):
                await new_category.create_text_channel(channel.name)

    for role in sorted(ctx.guild.roles, key=lambda r: r.position):
        if role.name != "@everyone":
            await target_guild.create_role(name=role.name, permissions=role.permissions, color=role.color, hoist=role.hoist, mentionable=role.mentionable)

    # Copy guild settings
    try:
        await target_guild.edit(name=f"backup-{ctx.guild.name}", icon=ctx.guild.icon)
    except Exception as e:
        print(f"Error editing guild: {e}")

    await ctx.send(f"Server copied to {target_guild.name}.")
    
def encode_message(message):
    return ''.join(chr(ord(c) + 3) for c in message)

def decode_message(message):
    return ''.join(chr(ord(c) - 3) for c in message)

@client.command()
async def encode(ctx, *, message: str):
    encoded = encode_message(message)
    await ctx.send(f"Encoded Message: {encoded}")

@client.command()
async def decode(ctx, *, message: str):
    decoded = decode_message(message)
    await ctx.send(f"Decoded Message: {decoded}")
     
@client.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)

@client.command()
async def listen(ctx, *, message):
    await ctx.message.delete()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=message))

@client.command()
async def play(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(name=message)
    await client.change_presence(activity=game)

@client.command()
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(name=message, url='https://twitch.tv/notrifat')
    await client.change_presence(activity=stream)

@client.command()
async def removestatus(ctx):
    await ctx.message.delete()
    await client.change_presence(activity=None, status=discord.Status.dnd)

@client.command()
async def dm(ctx, *, message: str):
    await ctx.message.delete()
    h = 0
    for user in list(ctx.guild.members):
        try:
            await user.send(message)
            h += 1
        except Exception as e:
            print(e)
    try:
        await ctx.reply(f"Successfully dmed {h} members in {ctx.guild.name}")
    except:
        await ctx.send(f"Successfully dmed {h} members in {ctx.guild.name}")


@client.command()
async def ping(ctx):
    latency = round(client.latency * 1000)
    await ctx.send(f"Ping: {latency}ms")

@client.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(f'{message}\n')

@client.command()
async def prune(ctx, days: int = 1, rc: int = 0, *, reason: str = reason):
    await ctx.message.delete()
    roles = [role for role in ctx.guild.roles if len(role.members) > 0]
    hm = await ctx.guild.prune_members(days=days, roles=roles, reason=reason)
    await ctx.send(f"Successfully Pruned {hm} Members")

@client.command(aliases=['mc'])
async def membercount(ctx):
    member_count = ctx.guild.member_count
    await ctx.send(f"```This server has {member_count} Members.```")

@client.command(name='banall', aliases=["be", "baneveryone"])
async def ban_everyone(ctx):
    for m in ctx.guild.members:
        try:
            await m.ban(reason=reason)
            print(f"Banned {m}")
        except discord.Forbidden:
            print(f"I don't have the necessary permissions to ban {m}")
        except discord.HTTPException as e:
            print(f"An error occurred while banning {m}: {e}")

@client.command()
async def dmall(ctx, *, message):
    for user in client.user.friends:
        try:
            await user.send(message)
            print(f"Messaged: {user.name}")
        except:
            print(f"Couldn't message: {user.name}")

@client.command(aliases=['rs'])
async def renameserver(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)

@client.command(aliases=['rc'])
async def renamechannels(ctx, *, name):
    for channel in ctx.guild.channels:
        await channel.edit(name=name)

@client.command(aliases=['rr'])
async def renameroles(ctx, *, name):
    for role in ctx.guild.roles:
        await role.edit(name=name)


@client.command()
async def massban(ctx):
    """Ban all members in the server."""
    # Ensure the bot has the necessary permissions
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("You need administrator permissions to use this command.")
        return

    # Check if the bot has the 'Ban Members' permission
    if not ctx.guild.me.guild_permissions.ban_members:
        await ctx.send("I don't have permission to ban members in this server.")
        return

    # List to keep track of banned users
    banned_users = []
    
    # Attempt to ban each member
    for member in list(ctx.guild.members):
        if member == ctx.guild.me:
            continue  # Skip the bot itself
        try:
            await member.ban(reason="Mass ban command executed.")
            banned_users.append(member)
            await asyncio.sleep(1)  # To avoid rate limits
        except discord.Forbidden:
            await ctx.send(f"I don't have permission to ban {member.mention}.")
        except discord.HTTPException as e:
            await ctx.send(f"An error occurred while banning {member.mention}: {e}")

    # Send a summary of banned users
    await ctx.send(f"Successfully banned {len(banned_users)} members.")

@client.command()
async def about(ctx):
    about_message = (
        "**Storm Selfbot V3**\n"
        "-----------------------------\n"
        "The ultimate selfbot for advanced Discord users.\n"
        "Features:\n"
        "- Best nuking commands to nuke fast.\n"
        "- Advanced automation tools.\n"
        "- Crypto and stock management.\n"
        "- Moderation utilities.\n"
        "- Fun and productivity tools.\n"
        "- Lightning-fast performance.\n"
        "\n"
        "Developer: notherxenon & toxicsajay [Retired Dev: sh4dow.runz]\n"
        "Version: 3.0\n"
        "GitHub: [Click Here](https://github.com/rifatgamingop)\n"
        "\n"
        "Disclaimer: Use responsibly and comply with Discord's ToS."
    )
    await ctx.send(about_message)

@client.command()
async def joke(ctx):
    joke = pyjokes.get_joke()
    await ctx.send(f"Here's a joke for you: {joke}")

@client.command()
async def meme(ctx):
    # Fetch a random meme from the Meme API
    response = requests.get("https://meme-api.com/gimme")
    if response.status_code == 200:
        data = response.json()
        meme_url = data.get("url")
        meme_title = data.get("title")
        
        if meme_url:
            # Send the meme in the channel
            await ctx.send(f"**{meme_title}**\n{meme_url}")
        else:
            await ctx.send("Couldn't fetch a meme right now. Please try again later.")
    else:
        await ctx.send("Error fetching meme. Please try again later.")



# List of predefined hug GIF URLs
hug_gifs = [
    "https://images-ext-1.discordapp.net/external/K6PI2Xh0O1dtAHrxtn0migKbiP7oE-DsNRWTwRGtDW8/https/cdn.weeb.sh/images/rkIK_u7Pb.gif?width=550&height=291",
    "https://images-ext-1.discordapp.net/external/3wXDLr7wXxXe0SXGMsZAAKR68yQDiuFn9y5d4ww1UlI/https/cdn.weeb.sh/images/BJ0UovdUM.gif?width=550&height=284",
    "https://images-ext-1.discordapp.net/external/TZn6hcfd6jIPMoUafGI1Tk682OM5021sHwdHV_uHdpU/https/cdn.weeb.sh/images/ryg2dd7wW.gif?width=550&height=275",
    "https://images-ext-1.discordapp.net/external/J8VQeuIX02yM134dAShL7Q4a5g_lySbtIgWsnB2tqNM/https/cdn.weeb.sh/images/S1OAduQwZ.gif?width=550&height=309"
]

@client.command()
async def hug(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("You need to mention someone to hug!")
        return
    
    # Randomly select a hug GIF
    gif1_url = random.choice(hug_gifs)
    
    # Send a message with the GIF
    await ctx.send(f"{ctx.author.display_name} hugs {member.display_name}! 🤗\n{gif1_url}")

# List of predefined slap GIF URLs
slap_gifs = [
    "https://images-ext-1.discordapp.net/external/6LbijnPllcNx9YUNhVTtCW6WB1GczwKg40ykCoP0LRQ/https/cdn.weeb.sh/images/rJvR71KPb.gif?width=449&height=330",
    "https://images-ext-1.discordapp.net/external/RkuVbGqqfdQnvvz5G6kccEkN3qQkWStkPDU8ghc1GL8/https/cdn.weeb.sh/images/H16aQJFvb.gif?width=687&height=385",
    "https://images-ext-1.discordapp.net/external/IQnl-SE1tZ75MUQTE0A2Q8o9FCGsF99DjY-r0yiIDKc/https/cdn.weeb.sh/images/HyPjmytDW.gif?width=445&height=338"
]

@client.command()
async def slap(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("You need to mention someone to slap!")
        return
    
    # Randomly select a slap GIF
    gif2_url = random.choice(slap_gifs)
    
    # Send a message with the GIF
    await ctx.send(f"{ctx.author.display_name} slaps {member.display_name}! 😠\n{gif2_url}")

kiss_gifts = [
    "https://images-ext-1.discordapp.net/external/aVabAKVgnUMWWH-0yGVe6v3H_QISdNSiRov8pXKGxt8/https/cdn.weeb.sh/images/r1H42advb.gif?width=581&height=327",
    "https://images-ext-1.discordapp.net/external/f8CBPFmC073A6t2gGusaZ1QCw0FQZZCv0DW-2tXLa6Q/https/cdn.weeb.sh/images/H1a42auvb.gif?width=687&height=429",
    "https://images-ext-1.discordapp.net/external/3MV0SEwyPKGDzEJcy5d_ve_Tz8V6hnJP8ur-uSC1gIk/https/cdn.weeb.sh/images/HJkxXNtjZ.gif?width=550&height=309"
]

@client.command()
async def kiss(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("You need to mention someone to kiss!")
        return
    
    gif3_url = random.choice(kiss_gifs)

    await ctx.send(f"{ctx.author.display_name} kisses {member.display_name}! 🤗\n{gif3_url}")

@client.command()
async def math(ctx, num1: float, operation: str, num2: float):
    """
    A simple calculator command that takes two numbers and an operation.
    Usage example: !calc 5 + 3
    """
    # Define result variable
    result = None
    
    # Perform calculation based on the operation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            await ctx.send("Error: Cannot divide by zero.")
            return
    else:
        await ctx.send("Error: Invalid operation. Use +, -, *, or /.")
        return
    
    # Send the result to the channel
    await ctx.send(f"The result of {num1} {operation} {num2} is: {result}")

auto_react = False
reaction_emoji = None

@client.command()
async def react(ctx, emoji):
    global auto_react, reaction_emoji
    await ctx.message.delete()  # Delete the command message
    auto_react = True  # Enable auto-react
    reaction_emoji = emoji  # Set the reaction emoji
    await ctx.send(f"Auto-react is now ON with {emoji}!", delete_after=5)  # Optional: delete message after 5 seconds

@client.command()
async def stopreact(ctx):
    global auto_react
    await ctx.message.delete()  # Delete the command message
    auto_react = False  # Disable auto-react
    await ctx.send("Auto-react is now OFF!", delete_after=5)  # Optional: delete message after 5 seconds

# Event listener to react to all messages when auto-reaction is enabled

auto_reply = False
opponent = None

@client.command()
async def autoreply(ctx, user: discord.User):
    global auto_reply, opponent
    await ctx.message.delete()  # Delete the command message
    auto_reply = True  # Enable auto-reply
    opponent = user  # Set the opponent
    await ctx.send(f"Auto-reply is now ON for {user.mention}!", delete_after=5)

@client.command()
async def stopreply(ctx):
    global auto_reply, opponent
    await ctx.message.delete()  # Delete the command message
    auto_reply = False  # Disable auto-reply
    opponent = None  # Clear the opponent
    await ctx.send("Auto-reply is now OFF!", delete_after=5)

# Event listener to auto-reply to messages from the opponent
@client.event
async def on_message(message):
    global auto_reply, opponent, auto_react, reaction_emoji
    
    # Auto-reply functionality
    if auto_reply and opponent and message.author == opponent and not message.author.bot:
        # Example auto-replies
        replies = [
            "hey yo u ugly grangky dork ass nigga",
            "ur looking so shit",
            "ong ur lifeless ur a discord crusader alfronzo",
            "alexander fucked ur momma with japanese katana"
        ]
        
        # Send a random auto-reply from the list
        import random
        reply = random.choice(replies)
        await message.channel.send(reply)
    
    # Auto-react functionality
    if auto_react and reaction_emoji and message.author == client.user:
        try:
            await message.add_reaction(reaction_emoji)
        except discord.errors.InvalidArgument:
            print(f"Invalid emoji: {reaction_emoji}")
    
    await client.process_commands(message)

# Global variables to manage the loop and group ID
gc_loop_running = False
gc_group = None

@client.command()
async def gc(ctx, group_id: int):
    global gc_loop_running, gc_group
    await ctx.message.delete()  # Delete the command message
    
    # Find the group by ID (group DMs are found in private channels)
    group = client.get_channel(group_id)
    if not isinstance(group, discord.GroupChannel):
        await ctx.send(f"Invalid Group ID: {group_id}. Please provide a valid group DM ID.", delete_after=5)
        return
    
    gc_group = group
    gc_loop_running = True  # Set the loop to start

    await ctx.send(f"Started changing the group name for Group ID: {group_id}", delete_after=5)
    
    # Start the loop task to change the group name
    change_group_name.start()

@tasks.loop(seconds=1)  # Change the group name every 10 seconds (adjust as needed)
async def change_group_name():
    global gc_loop_running, gc_group
    if gc_group and gc_loop_running:
        # List of sample group names to loop through
        names = [
            "Nigga",
            "Get",
            "Fucked",
            "Up",
            "We",
            "Rule",
            "You"
        ]
        for name in names:
            if not gc_loop_running:
                break  # Exit loop if stop command is issued
            try:
                await gc_group.edit(name=name)  # Change the group name
                print(f"Changed group name to: {name}")
                await asyncio.sleep(1)  # Wait for 10 seconds before changing again
            except discord.Forbidden:
                print(f"Permission denied to change group name for {gc_group.name}")
                break

@client.command()
async def stopgc(ctx):
    global gc_loop_running
    await ctx.message.delete()  # Delete the command message
    gc_loop_running = False  # Stop the loop
    change_group_name.stop()  # Stop the loop task
    await ctx.send("Stopped changing the group name.", delete_after=5)

@client.command()
async def ipinfo(ctx, ip_address: str):
    try:
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        data = response.json()
        
        if response.status_code == 200:
            ip_info = (
                f"**IP Address:** {data.get('ip')}\n"
                f"**Hostname:** {data.get('hostname')}\n"
                f"**City:** {data.get('city')}\n"
                f"**Region:** {data.get('region')}\n"
                f"**Country:** {data.get('country')}\n"
                f"**Location:** {data.get('loc')}\n"
                f"**Organization:** {data.get('org')}\n"
            )
            await ctx.send(ip_info)
        else:
            await ctx.send("Could not fetch IP information. Please check the IP address and try again.")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

@client.command()
async def restart(ctx):
    """
    Command to restart the bot.
    """
    await ctx.send("Bot is restarting...")  # Informing the user that the bot will restart.
    
    # Command to restart the bot (it works if you run the bot from the command line).
    os.execv(sys.executable, ['python'] + sys.argv)

@client.command()
async def checkpromo(ctx, promo_link: str):
    """
    Command to check if the promo link is valid.
    """
    # Check if the promo link matches a URL pattern (simple regex)
    if re.match(r'https?://[^\s]+', promo_link):
        await ctx.send(f"The promo link {promo_link} is valid!")
    else:
        await ctx.send(f"The promo link {promo_link} is invalid. Please check the link and try again.")

@client.command()
async def translate(ctx, target_lang, *, text):
    """
    Command to translate text into any supported language.
    """
    # Initialize the Translator
    translator = Translator()

    try:
        # Translate the text
        translation = translator.translate(text, dest=target_lang)

        # Check if the target language is valid
        if target_lang not in LANGUAGES:
            await ctx.send("Invalid language code. Please provide a valid language code.")
            return
        
        # Send the translated text
        await ctx.send(f"Original: {text}\nTranslated ({LANGUAGES[target_lang]}): {translation.text}")
    
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

sniped_messages = {}

@client.event
async def on_message_delete(message):
    # Store the deleted message details in the sniped_messages dictionary
    sniped_messages[message.channel.id] = {
        "content": message.content,
        "author": str(message.author),
        "time": message.created_at.strftime("%Y-%m-%d %H:%M:%S"),
    }

@client.command()
async def snipe(ctx):
    channel_id = ctx.channel.id
    if channel_id in sniped_messages:
        msg = sniped_messages[channel_id]
        await ctx.send(
            f"**Author:** {msg['author']}\n**Time:** {msg['time']}\n**Message:** {msg['content']}"
        )
    else:
        await ctx.send("There's nothing to snipe in this channel!")

@client.command()
async def die(ctx):
    for i in range(1, 11):
        await ctx.send(str(i))
        await asyncio.sleep(0.5)  # Adding delay to make it feel more natural
    await ctx.send("Died Lmao")

client.run(token, bot=False)
