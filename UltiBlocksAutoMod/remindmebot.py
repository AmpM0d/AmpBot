"""
A bot module to check for users posting the command "/remindme" and leave them a message on their talk page

This module will soon support setting a later time. 
"""

# Import necessary modules
import pywikibot
import difflib

# Define a wrapper around difflib to see what was added.
# This function is ChatGPT generated. I've had no problems
# with it so far, but if there are any, make an issue.
def get_added_content(previous_text, current_text):
    # For some reason, we sometimes get None as our previous_text.
    # In this case, everything on the page is added.
    # This might have some unintended side effects, so if you find any, make an issue.
    if previous_text is None: return current_text
    # Use difflib to find differences between the revisions
    diff = difflib.ndiff(previous_text.splitlines(), current_text.splitlines())
    # Extract the added lines (those with the '+' prefix)
    added_lines = [line[2:] for line in diff if line.startswith('+ ')]
    return '\n'.join(added_lines)

# Define a function to run every iteration of the bot loop
def iteration(site):
        # Get the last revision the bot checked
        # TODO: Make this and related code part of a common library
        last = float(pywikibot.Page(site, "User:" + site.username() + "/last_revision").text)
        # Define the recent changes generator
        r = site.recentchanges()
        # Set a variable to determine whether the
        # bot has done anything worthy of updating last_revision
        didanythingmeaningful=False
        # Loop through recent changes
        # Initialize an empty variable to eventually hold the latest
        # revision we've checked (for updating last_revision if we need to)
        now=None
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
            # Filter to only revisions on talk pages (odd numbered namespaces)
            if e["ns"] % 2 == 1 or "__NEWSECTIONLINK__" in page.text:
                # Get the page associated with the revision
                page = pywikibot.Page(site, e["title"])
                # Check if this edit was page creation. If so, the whole page
                # is added content.
                if e["old_revid"]==0:
                    try: added_content = page.getOldVersion(oldid=i)
                    except: 
                        # Just ignore strange edge cases
                        continue
                else:
                    try:
                        current_text = page.getOldVersion(oldid=i)
                        previous_text = page.getOldVersion(oldid=e["old_revid"])
                    except:
                        # Again, ignore edge cases
                        continue
                    if current_text is None or previous_text is None:
                        # Guess what? Ignoring edge cases!
                        continue
                    # Get the added content using the diff function
                    added_content = get_added_content(previous_text, current_text)
                # Regardless of how added content was determined, check for the command.
                if "/remindme" in added_content:
                    # Get the user's talk page
                    userpage=pywikibot.Page(site,"User talk:"+e["user"])
                    # Add the reminder and save the page. Make sure not to mark it as minor,
                    # because then the user won't get notified, which defeats the whole purpose.
                    userpage.text+="\n== Reminder from /{{nothing}}remindme ==\n{{User:UltiBlocksAutoMod/Notification-v1}} ~~~~"
                    userpage.save("Bot: reminder",minor=False)
                    # Show confirmation that the user has been reminded
                    # (probably not necessary, but is helpful whenever I'm debugging this)
                    print("Reminded",e["user"])
                    # Set the flag to update the latest revision checked, and avoid a spam loop.
                    didanythingmeaningful=True
        # If we made any edits...
        if didanythingmeaningful:
            # Get our last revision page
            page=pywikibot.Page(site, "User:" + site.username() + "/last_revision")
            # Edit and save it
            page.text=str(now)
            page.save("Bot: updating my latest revision data")

# If we're being run as the main file, print an error,
# because I don't want to update more entry points than I have to.
if __name__ == "__main__":
     print("Please do not run remindbot as main. Please instead run it via start.bat or start.sh")