"""
A bot module to check for users posting the command "/remindme" and leave them a message on their talk page

This module will soon support setting a later time. 
"""

# Import necessary modules
from ast import Return
import pywikibot

wrapper=[]

# Define a function to run every iteration of the bot loop
def getlistrevisions(site):
        # Get the last revision the bot checked
        last = float(pywikibot.Page(site, "User:" + site.username() + "/last_revision").text)
        # Define the recent changes generator
        r = site.recentchanges()
        # Loop through recent changes
        # Initialize an empty variable to eventually hold the latest
        # revision we've checked (for updating last_revision if we need to)
        now=None
        edits=[]
        # Loop until we break (I've found this
        # less messy than specifying a while condition)
        while 1:
            # Get the next revision and its ID
            e = next(r)
            i = e["revid"]
            # The revision ID seems to be zero for things that are not
            # page edits or creations, so we ignore those.
            if i==0: continue
            # Stop if we reach the last revision we've already checked
            if i<=last:
                break
            # Ignore our own edits (removing this probably
            # won't lead to a spam loop, but it could)
            if e["user"]==site.username():
                continue
            # Set the latest revision variable if it hasn't been set
            if now is None:
                now=i
            edits.append(e)

        return edits

def preRunBots(runtimevars,iterationvars):
    site=runtimevars['site']
    iterationvars['didanything']=False
    iterationvars['revisions']=getlistrevisions(site)

def postRunBots(runtimevars,iterationvars):
    site=runtimevars['site']
    if iterationvars['didanything']:
        # Get our last revision page
        page=pywikibot.Page(site, "User:" + site.username() + "/last_revision")
        # Edit and save it
        page.text=str(iterationvars['revisions'][0]["revid"])
        page.save("Bot: updating my latest revision data")

# If we're being run as the main file, print an error,
# because I don't want to update more entry points than I have to.
if __name__ == "__main__":
     print("Please do not run remindbot as main. Please instead run it via start.bat or start.sh")