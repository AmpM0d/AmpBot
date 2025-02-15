"""Helper script to run a select combination of bots"""

# Import necessary modules
from .bot_config import bots
from . import bot_config as bc
from .wikisite import site
import time

# Run a select list of bots
def runbots(botlist):
    pre_dependencies=[]
    post_dependencies=[]
    for i in botlist:
        if "pre_deps" in i:
            for j in i["pre_deps"]:
                if not j in pre_dependencies: 
                    pre_dependencies.append(j)
        if "post_deps" in i:
            for j in i["post_deps"]:
                if not j in post_dependencies: 
                    post_dependencies.append(j)
    runtimevars={"site":site}
    while 1:
        iterationvars={}
        # Run an iteration of each specified bot and then wait
        for i in pre_dependencies:
            i(runtimevars,iterationvars)
        for i in botlist:
            print("Running 1 iteration of",i["prettyname"])
            i["function"](runtimevars,iterationvars)
        for i in post_dependencies:
            i(runtimevars,iterationvars)
        time.sleep(600)

# Main function, argument parser logic
def main(argv):
    # If no arguments, run all bots.
    if len(argv)==1:
        botstorun=bots.values()
    else:
        # Otherwise run the chosen bots
        botstorun=[]
        for item in argv[1:]:
            botstorun.append(bots[item])
    runbots(botstorun)

if __name__=="__main__":
    # If this script is being run as main, do the stuff.
    import sys
    main(sys.argv)