import copy
import json
import os,sys
os.chdir(os.path.dirname(sys.argv[0])+"/..")
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