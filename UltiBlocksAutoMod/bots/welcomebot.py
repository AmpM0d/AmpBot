"""
A bot module to welcome new users
"""

# Import necessary modules
import pywikibot

# Define a function to run every iteration of the bot loop
def iteration(runtimevars,iterationvars):
        for e in iterationvars['revisions']:
            print(e)
            iterationvars["didanything"]=True
# If we're being run as the main file, print an error,
# because I don't want to update more entry points than I have to.
if __name__ == "__main__":
     print("Please do not run welcomebot as main. Please instead run it via start.bat or start.sh")
