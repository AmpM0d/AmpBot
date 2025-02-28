"""
A bot module to welcome new users
"""

# Import necessary modules
import pywikibot

# Define a function to run every iteration of the bot loop
def iteration(runtimevars,iterationvars):
        for e in iterationvars['revisions']:
            print(e)
            contribs=pywikibot.User(runtimevars["site"],e["user"]).contributions(len(iterationvars['revisions'])+1)
            if e["revid"]==list(contribs)[-1][1]:
                # Get the user's talk page
                userpage=pywikibot.Page(runtimevars['site'],"User talk:"+e["user"])
                # Add the reminder and save the page. Make sure not to mark it as minor,
                # because then the user won't get notified, which defeats the whole purpose.
                userpage.text+="\n== Welcome to the AmpMod Wiki! ==\n{{User:UltiBlocksAutoMod/Welcome-v1}} ~~~~"
                userpage.save("Bot: welcome",minor=False)
                # Show confirmation that the user has been welcomed
                # (probably not necessary, but is helpful whenever I'm debugging this)
                print("Welcomed",e["user"])
                # Set the flag to update the latest revision checked, and avoid a spam loop.
                iterationvars["didanything"]=True
# If we're being run as the main file, print an error,
# because I don't want to update more entry points than I have to.
if __name__ == "__main__":
     print("Please do not run welcomebot as main. Please instead run it via start.bat or start.sh")
