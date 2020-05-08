#     _______________________________________________________
#    /\                                                      \
#(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)
#    \/''''''''''''''''''''''''''''''''''''''''''''''''''''''/
#    (                                                      (
#     )                                                      )
#    (         Edit thelines of code under this for         (
#     )              Configuration Options                  )
#    )                                                       )
#    (                                                      (
#    /\''''''''''''''''''''''''''''''''''''''''''''''''''''''\    
#(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)
#    \/______________________________________________________/


#This is your discord server name as it appears on discord
server_name = "Discord Server Name"

#If you want to require your users to have a discord role set to True
role_required = True

#If they need a role, this is the role that you want them to have to have
role_needed = "User"

#If you want the bot to auto assign the role to users, set this to True
assign_role_on_join = True


#This is the token for the bot you can find here
#https://discord.com/developers/applications
discord_bot_token = ""

#You can register for a free API key here
#https://rapidapi.com/f.sm.jorquera/api/phone-insights
API_key = ""



#     _______________________________________________________
#    /\                                                      \
#(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)
#    \/''''''''''''''''''''''''''''''''''''''''''''''''''''''/
#    (                                                      (
#     )                                                      )
#    (            Dont touch anything under this            (
#     )           Unless You Know What Your Doing           )
#    )                                                       )
#    (                                                      (
#    /\''''''''''''''''''''''''''''''''''''''''''''''''''''''\    
#(O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)
#    \/______________________________________________________/



class secretInformation():
    def __init__(self, roleWanted, roleNeeded, assignRole, discordToken, api):
        self.roleWanted = roleWanted
        self.roleNeeded = roleNeeded
        self.assignRole = assignRole
        self.__discordToken = discordToken
        self.__api = api

    def getApiKey(self):
        return self.__api

    def getDiscordToken(self):
        return self.__discordToken

    
        






