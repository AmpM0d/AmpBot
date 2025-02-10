"""Configuration generator to set up the bot passwords 
Used when setting up the repository, to generate the files that need to exist, but can't be committed for security reasons"""

# Import module to securely input passwords
import getpass
# Prompt for bot username and bot password data
uname=input("Username?")
botpwduname=input("Bot password username?")
botpwd=getpass.getpass("Bot password: ")
# Generate the configuration files
c=f"""family = 'ultiblocks'
mylang = 'en'
usernames['ultiblocks']['en'] = '{uname}'
password_file = "user-password.py"
put_throttle=0"""
p=f"""('{uname}', BotPassword('{botpwduname}', '{botpwd}'))"""
# Todo in a later commit: actually write the files