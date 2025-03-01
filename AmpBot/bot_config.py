"""
Bot definition file for AmpBot
This file is very formulaic. It consists of
necessary imports and definitions for each
bot that is to be run.
"""

# Create empty dictionary to store list of bots
bots={}
# Import any prerequisites
# The requirement system is developed on
# an as-needed basis, so this part of the
# system will rarely get updates if there
# is not a bot that needs them. Also, any
# updates to this system that a bot needs
# will be part of the pull request that
# creates the need for them. 
#
# This essay will likely be moved to documentation
# later in this issue.
from . import foreachrevision as foreach

# Import the per-iteration function from remindmebot
from .bots.remindmebot import iteration as remindmebot
# Create the bot definition
# Remindmebot needs foreachrevision
bots["remindmebot"]={
    "name":"remindmebot",
    "prettyname":"Reminder Bot",
    "description":"A bot that reminds users on their talk pages when they add '/remindme' to a talk page",
    "function":remindmebot,
    "pre_deps":[
        foreach.preRunBots
    ],
    "post_deps":[
        foreach.postRunBots
    ]
}

# Import the sandbox clearing bot's iteration function
from .bots.sandboxbot import iteration as sandboxbot
# Create bot definition
bots["sandboxbot"]={
    "name":"sandboxbot",
    "prettyname":"Sandbox Clearing Bot",
    "description":"A bot that clears the global sandbox if no human has edited it for 4 hours",
    "function":sandboxbot
}

# Import the welcoming bot's iteration function
from .bots.welcomebot import iteration as welcomebot
# Create bot definition
bots["welcomebot"]={
    "name":"welcomebot",
    "prettyname":"Welcoming Bot",
    "description":"A bot that welcomes users after their first edit",
    "function":welcomebot,
    "pre_deps":[
        foreach.preRunBots
    ],
    "post_deps":[
        foreach.postRunBots
    ]
}
