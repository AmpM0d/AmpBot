import copy
import json
import os,sys,shutil
os.chdir(os.path.dirname(sys.argv[0])+"/..")
if os.path.exists("windows"):
    shutil.rmtree("windows")
if os.path.exists("linux"):
    shutil.rmtree("linux")
os.mkdir("windows")
os.mkdir("linux")
from .bot_config import bots
def get_text(old,name,prettyname):
    return old.replace("{{name}}",name).replace("{{prettyname}}",prettyname)
launch_tpl=json.load(open("templates/launch.json.tpl"))
basic_launch=launch_tpl["configurations"][0]
for i in bots.values():
    n=copy.deepcopy(basic_launch)
    n["name"]=i["prettyname"]+" only"
    n["args"].append(i["name"])
    launch_tpl["configurations"].append(n)
json.dump(launch_tpl,open(".vscode/launch.json","w"))

for name in bots:
    data=bots[name]
    win_tmp=open("templates/bot_win.bat.tpl").read()
    new=get_text(win_tmp,data["name"],data["prettyname"])
    open("windows/"+data["name"]+".bat","w").write(new)
    linux_tmp=open("templates/bot_linux.sh.tpl").read()
    new=get_text(linux_tmp,data["name"],data["prettyname"])
    open("linux/"+data["name"]+".sh","w").write(new)