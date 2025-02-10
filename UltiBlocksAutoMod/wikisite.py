"""
Defines objects that are shared across the project, so that they can easily be imported. 
"""

# Get our site object, for use by scripts importing this.
import pywikibot
site = pywikibot.Site()
site.login()