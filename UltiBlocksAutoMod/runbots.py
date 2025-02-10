"""Helper script to run a select combination of bots"""

# Import necessary modules
from .bots import sandbox, remind
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
        bots=[sandbox,remind]
    else:
        # Otherwise run the chosen bots
        # TODO: I'm going to make a more centralized system for managing multiple bots
        bots=[]
        if "sandboxbot" in argv:
            bots.append(sandbox)
        if "remindbot" in argv:
            bots.append(remind)
    runbots(bots)

if __name__=="__main__":
    # If this script is being run as main, do the stuff.
    import sys
    main(sys.argv)