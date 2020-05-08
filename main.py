import secret
import discord
import requests
import random
import json


class bot(discord.Client):
    def __init__(self, *args, **kwargs):
        self.timer = 0
        self.suspend = False
        self.repl = False
        self.voiceMap = {}
        self.voiceQ = {}
        super().__init__(*args, **kwargs)

        

client = bot()
client.pfix = '!'





Secret = secret.secretInformation(secret.role_required, secret.role_needed, secret.assign_role_on_join, secret.discord_bot_token, secret.API_key)


@client.event
async def on_ready():
    print('Bot owner:\n' + str(client.user.id))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}



@client.event
async def on_member_join(member):
    print(str(secret.role_required))
    print(str(secret.server_name))
    print(str(secret.role_needed))
    
    if secret.assign_role_on_join == True:
        print(secret.server_name)
        server = discord.utils.get(client.guilds, name=secret.server_name)
                                    
        role = discord.utils.get(server.roles, name=secret.role_needed)
                                    
        await member.add_roles(role)
        
       





@client.event
async def on_message(message):

    def lookup(num):
        url = "https://f-sm-jorquera-phone-insights-v1.p.rapidapi.com/parse"

        payload = "{\"phone_number\": \"" + num + "\"}"
        headers = {
            'x-rapidapi-host': "f-sm-jorquera-phone-insights-v1.p.rapidapi.com",
            'x-rapidapi-key': Secret.getApiKey(),
            'content-type': "application/json",
            'accept': "application/json"
            }

        response = requests.request("POST", url, data=payload, headers=headers)

        if "Missing or invalid default region." in response.text:
            return "False"
        else:
            return response.text
                
        
    
    if message.content.lower().startswith(client.pfix + "lookup"):
        roleFound = False
        if Secret.roleWanted == True:
            
            
            for role in message.author.roles:
                if str(role) == Secret.roleNeeded:
                    roleFound = True
                    
            if roleFound:
                                
                embed = discord.Embed(
                    title = 'Phone Insights',
                    colour=discord.Colour.from_rgb(90,37,37)
                )
            
                #embed.set_footer(text='Thank you for playing Cursed Clouds!')
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/688973831548829750/707432691770851378/f.webp')
                embed.add_field(value="Processing Your Request", name="Thank you for using the bot.")
                
                
                await message.channel.send(embed=embed)


                messageContent = message.content.replace(" ", "")
                phoneNum = messageContent.replace("!lookup", "")

                

                res = lookup(phoneNum)

                if res == "False":
                    embed = discord.Embed(
                    title = 'Phone Insights',
                    colour=discord.Colour.from_rgb(90,37,37)
                    )
            
                    
                    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/688973831548829750/707432691770851378/f.webp')
                    embed.add_field(value="Error: Please enter the country code before the phone number", name="Thank you for using the bot.")
                    
                    
                    await message.channel.send(embed=embed)


                    messageContent = message.content.replace(" ", "")
                    phoneNum = messageContent.replace("!lookup", "")
                else:
                    res = res.replace("\'\'", "\'None\'")
                    resDict = json.loads(res)
                    

                    embed = discord.Embed(
                    title = 'Results',
                    colour=discord.Colour.from_rgb(90,37,37)
                    )


                    

                    
                   
                    embed.add_field(name="Country Code", value=resDict["country_code"])
                    embed.add_field(name="Country", value=resDict["country_code_iso"], inline=False)
                    
                    if resDict["location"] == '':
                        embed.add_field(name="Location", value="None", inline=False)
                    else:
                        embed.add_field(name="Location", value=resDict["location"], inline=False)

                    if resDict["location_latitude"] == '':
                        embed.add_field(name="Latitude", value="None", inline=False)
                    else:
                        embed.add_field(name="Latitude", value=resDict["location_latitude"], inline=False)
                        
                    if resDict["location_longitude"] == '':
                        embed.add_field(name="Longitude", value="None", inline=False)
                    else:
                        embed.add_field(name="Longitude", value=resDict["location_longitude"], inline=False)


                    if resDict["number_type"] == '':
                        embed.add_field(name="Number Type", value="None", inline=False)
                    else:
                        embed.add_field(name="Number Type", value=resDict["number_type"], inline=False)


                    if resDict['is_valid_number'] == '':
                        embed.add_field(name="Is Valid Number", value="None", inline=False)
                    else:
                        embed.add_field(name="Is Valid Number", value=resDict["is_valid_number"], inline=False)

                    if resDict['carrier'] == '':
                        embed.add_field(name="Carrier", value="None", inline=False)
                    else:
                        embed.add_field(name="Carrier", value=resDict["carrier"], inline=False)

                    
                    
                 
                
                    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/688973831548829750/707432691770851378/f.webp')
                    
                    await message.channel.send(embed=embed)
                    

                

                
            else:
                embed = discord.Embed(
                title = 'Phone Insights',
                colour=discord.Colour.from_rgb(90,37,37)
                )
            
                    
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/688973831548829750/707432691770851378/f.webp')
                embed.add_field(value="Error: You Do Not Have Premission To Use The Bot", name="Thank you for using the bot.")
                    
                    
                await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(
            title = 'Phone Insights',
            colour=discord.Colour.from_rgb(90,37,37)
            )
            
                #embed.set_footer(text='Thank you for playing Cursed Clouds!')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/688973831548829750/707432691770851378/f.webp')
            embed.add_field(value="Processing Your Request", name="Thank you for using the bot.")
                
                
            await message.channel.send(embed=embed)


            messageContent = message.content.replace(" ", "")
            phoneNum = messageContent.replace("!lookup", "")

                

            res = lookup(phoneNum)

            if res == "False":
                embed = discord.Embed(
                title = 'Phone Insights',
                colour=discord.Colour.from_rgb(90,37,37)
                )
            
                    
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/688973831548829750/707432691770851378/f.webp')
                embed.add_field(value="Error: Please enter the country code before the phone number", name="Thank you for using the bot.")
                    
                    
                await message.channel.send(embed=embed)


                messageContent = message.content.replace(" ", "")
                phoneNum = messageContent.replace("!lookup", "")
            else:
                res = res.replace("\'\'", "\'None\'")
                resDict = json.loads(res)
                    

                embed = discord.Embed(
                title = 'Results',
                colour=discord.Colour.from_rgb(90,37,37)
                )


                    

                    
                   
                embed.add_field(name="Country Code", value=resDict["country_code"])
                embed.add_field(name="Country", value=resDict["country_code_iso"], inline=False)
                    
                if resDict["location"] == '':
                    embed.add_field(name="Location", value="None", inline=False)
                else:
                    embed.add_field(name="Location", value=resDict["location"], inline=False)

                if resDict["location_latitude"] == '':
                    embed.add_field(name="Latitude", value="None", inline=False)
                else:
                    embed.add_field(name="Latitude", value=resDict["location_latitude"], inline=False)
                        
                if resDict["location_longitude"] == '':
                    embed.add_field(name="Longitude", value="None", inline=False)
                else:
                    embed.add_field(name="Longitude", value=resDict["location_longitude"], inline=False)


                if resDict["number_type"] == '':
                    embed.add_field(name="Number Type", value="None", inline=False)
                else:
                    embed.add_field(name="Number Type", value=resDict["number_type"], inline=False)


                if resDict['is_valid_number'] == '':
                    embed.add_field(name="Is Valid Number", value="None", inline=False)
                else:
                    embed.add_field(name="Is Valid Number", value=resDict["is_valid_number"], inline=False)

                if resDict['carrier'] == '':
                    embed.add_field(name="Carrier", value="None", inline=False)
                else:
                    embed.add_field(name="Carrier", value=resDict["carrier"], inline=False)

                    
                    
                 
                
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/688973831548829750/707432691770851378/f.webp')
                    
                await message.channel.send(embed=embed)
                    

                

            
    
   
client.run(Secret.getDiscordToken())
