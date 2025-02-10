"""
Bot module to clear the sandbox after no humans have edited it for 4 hours
"""

# Importing necessary modules
import pywikibot,datetime

# Function to detect if a revision was made by a bot (we probably don't need this, but whatever)
# TODO: move this to a common library
def maybebot(site,rev):
    # If the user is flagged as a bot, then duh, they're a bot.
    if site.isBot(rev.user):
        return True
    # I'm requesting all bots, before they run unsupervised,
    # add "Bot:" to the start of their edit summaries.
    # This helps ensure that no bots get into feedback loops with each other.
    comment = rev.comment.lower()
    return comment.startswith('bot:')

# Function to run one iteration of this bot
# Originally written by ChatGPT as a basic script to edit a page once. I built from there.
def iteration(site):
        # Define the page you want to clear after inactivity
        page = pywikibot.Page(site, "UltiBlocks Wiki:Sandbox")
        # Get the revisions of the page
        revisions=page.revisions()
        while 1:
            # Get the next revision. If there is not one, you're done.
            try: rev=next(revisions)
            except StopIteration: break
            # If the last revision was me, nothing needs to be done.
            if rev.user==site.username():
                break
            # If the last revision was another bot,
            # ignore it to avoid potential feedback loops
            elif maybebot(site,rev):
                pass
            # If the last revision was a human, check how long ago it was.
            else:
                # I use Unix timestamps for as much as I can, because it's
                # simply a number of seconds. This uses datetimes and timedeltas,
                # but I will probably change that.
                if datetime.datetime.now(datetime.timezone.utc)-rev.timestamp.replace(tzinfo=datetime.timezone.utc)>datetime.timedelta(hours=4):
                    # If more then 4 hours have passed since the last human edit, reset the sandbox to it's default content
                    page.text="{{Sandbox top}}\n<!--Edit below this line, please. -->\n"
                    page.save("Bot: Clearing sandbox")
                # Once we've found the last human edit, we're done.
                break

# If we're being run as the main file, print an error,
# because I don't want to update more entry points than I have to.
if __name__ == "__main__":
     print("Please do not run sandboxbot as main. Please instead run it via start.bat or start.sh")