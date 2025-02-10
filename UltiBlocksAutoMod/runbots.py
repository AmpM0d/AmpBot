"""Helper script to run a select combination of bots"""

# Import necessary modules
from .bot_config import bots
from .wikisite import site
import time

# Run a select list of bots
def runbots(botlist):
    while 1:
        # Run an iteration of each specified bot and then wait
        for i in botlist:
            i(site)
        time.sleep(5)

# Main function, argument parser logic
def main(argv):
    # If no arguments, run all bots.
    if len(argv)==1:
        botstorun=[bots[i]["function"] for i in bots]
    else:
        # Otherwise run the chosen bots
        # TODO: I'm going to make a more centralized system for managing multiple bots
        botstorun=[]
        for item in sys.argv[1:]:
            botstorun.append(bots[item])
    runbots(botstorun)

if __name__=="__main__":
    # If this script is being run as main, do the stuff.
    import sys
    main(sys.argv)