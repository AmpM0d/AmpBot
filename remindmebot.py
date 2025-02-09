import pywikibot
import datetime
import time
import difflib
from math import inf

def get_added_content(previous_text, current_text):
    # Use difflib to find differences between the revisions
    if previous_text is None: return current_text
    diff = difflib.ndiff(previous_text.splitlines(), current_text.splitlines())
    # Extract the added lines (those with the '+' prefix)
    added_lines = [line[2:] for line in diff if line.startswith('+ ')]
    return '\n'.join(added_lines)

def main():
    # Initialize the site with the custom configuration from user-config.py
    site = pywikibot.Site()  # This uses the custom configuration defined in user-config.py

    # Log in using the credentials from the config file
    site.login()

    # Get the last revision ID from the user-specific page
    

    while True:
        last = float(pywikibot.Page(site, "User:" + site.username() + "/last_revision").text)
        # Define the recent changes iterator
        r = site.recentchanges()
        didanythingmeaningful=False
        # Loop through recent changes
        now=None
        while 1:
            e = next(r)
            i = e["revid"]
            print(i,last)
            if i==0: continue
            if i<=last:
                print("break")
                break
            if e["user"]==site.username():
                continue
            print(e)
            if now is None:
                now=i
                print(now)
            # Filter for articles in namespaces that are odd (likely user or article spaces)
            if e["ns"] % 2 == 1:
                print("Is talk page.")
                # Get the page related to the revision ID
                page = pywikibot.Page(site, e["title"])
                if e["old_revid"]==0:
                    print("Old revid is zero")
                    try: added_content = page.getOldVersion(oldid=i)
                    except: continue
                else:
                    print("Old revid is not zero")
                    try:
                        current_text = page.getOldVersion(oldid=i)
                        previous_text = page.getOldVersion(oldid=e["old_revid"])
                    except: continue
                    print("We have current and previous")
                    if current_text is None or previous_text is None: continue
                    # Get the added content using the diff function
                    print("Diffing...")
                    added_content = get_added_content(previous_text, current_text)
                if "/remindme" in added_content:
                    userpage=pywikibot.Page(site,"User talk:"+e["user"])
                    userpage.text+="\n\n== Reminder from /{{nothing}}remindme ==\nYou asked for a notification using the /{{nothing}}remindme command. ~~~~"
                    userpage.save("Bot: reminder")
                    print("Reminded",e["user"])
                    didanythingmeaningful=True
                print(f"Added content to {e['title']}:\n{added_content}\n")
        if didanythingmeaningful:
            page=pywikibot.Page(site, "User:" + site.username() + "/last_revision")
            page.text=str(now)
            page.save("Bot: updating my latest revision data")
        # Wait for 5 seconds before checking for new recent changes
        print("Wait 5 seconds...")
        time.sleep(5)
        print("Done waiting.")

if __name__ == "__main__":
    main()
