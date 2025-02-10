"""
This file defines the Wiki URL for the UltiBlocks Wiki.
"""
from pywikibot import family


class Family(family.Family):  # noqa: D101
    # Wiki name
    name = 'ultiblocks'
    # Wiki languages (only English)
    langs = {
        'en': 'ultiblocks.miraheze.org',
    }

    # Path for the API
    def scriptpath(self, code):
        return {
            'en': '/w',
        }[code]

    # Which protocol (http or https) to use
    def protocol(self, code):
        return {
            'en': 'https',
        }[code]
