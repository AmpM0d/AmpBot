import getpass
uname=input("Username?")
botpwduname=input("Bot password username?")
botpwd=getpass.getpass("Bot password: ")
c=f"""family = 'ultiblocks'
mylang = 'en'
usernames['ultiblocks']['en'] = '{uname}'
password_file = "user-password.py"
put_throttle=0"""
p=f"""('{uname}', BotPassword('{botpwduname}', '{botpwd}'))"""