import pywikibot,datetime,time

def maybebot(site,rev):
    if site.isBot(rev.user):
        return True
    user = rev.user.lower()
    comment = rev.comment.lower()
    return comment.startswith('bot:')

def main():
    # Initialize the site with the custom configuration from user-config.py
    site = pywikibot.Site()  # This uses the custom configuration defined in user-config.py

    # Log in using the credentials from the config file
    site.login()

    while 1:
        # Define the page you want to edit (example: User:YourUsername/sandbox)
        page = pywikibot.Page(site, "UltiBlocks Wiki:Sandbox")  # Change to your page
        # Get the current content of the page
        revisions=page.revisions()
        #print(next(revisions).user,site.username())
        while 1:
            try: rev=next(revisions)
            except StopIteration: break
            if rev.user==site.username():
                print("Last revision was me")
                break
            elif maybebot(site,rev):
                print("Last revision was a bot")
                pass
            else:
                print("Last revision was a human")
                if datetime.datetime.now(datetime.timezone.utc)-rev.timestamp.replace(tzinfo=datetime.timezone.utc)>datetime.timedelta(hours=4):
                    page.text="{{Sandbox top}}\n<!--Edit below this line, please. -->\n"
                    page.save("Bot: Clearing sandbox")
                break
        time.sleep(5)
        # Modify the content
#        new_text = current_text + "\n\nThis is a new edit via PyWikiBot."

        # Save the new content to the page
#        page.text = new_text
#        page.save("Editing the page via PyWikiBot")

if __name__ == "__main__":
    main()
