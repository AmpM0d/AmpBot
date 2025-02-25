UltiBlocksAutoMod structure
===========================

UltiBlocksAutoMod's source code is divided into a few parts: the bots themselves, the code that the bots use/share across multiple bots, the configuration that explains what bots exist, and the infrastructure that interprets the other parts.

You will likely modify the bots themselves, you may modify the configuration or shared libraries if you go further in depth on editing a bot, and you will likely never modify the infrastructure. Here are some key aspects of the directory structure: 

* All of the Python code resides under UltiBlocksAutoMod/UltiBlocksAutoMod.
* The bots themselves are in UltiBlocksAutoMod/UltiBlocksAutoMod/bots
* The configuration file is at UltiBlocksAutoMod/UltiBlocksAutoMod/bot_config.py.


The bots
--------
The bot's code itself is fairly simple. The important parts are: 

* You will almost certainly need to import PyWikiBot, the library that makes this bot run
* You might want to import difflib if you are comparing revisions (as remindmebot does)
* You will most likely have a few helper functions
* Your main bot code resides in a function called ``iteration``. It does not technically have to be called that, but it should to follow with the style.

 * This function takes two arguments: ``runtimevars`` and ``iterationvars``.
 * ``runtimevars`` is a dictionary that is preserved for the entire time the bot is running (but erased if restarted). It can be used to keep track of any data that should be remembered, but it will not be a big deal if it is forgotten.
 * ``iterationvars`` is used by foreachrevision to tell bots which revisions they must check

* Your bot should have this or similar code at the bottom: 

| ``if __name__=="__main__":``
|   ``print("Please run this code using the appropriate shell script for your system")``
This will help users who try to run your code without the dedicated script.

The configuration entry
-----------------------

To be run, every bot must have a valid entry in the configuration file (``bot_config.py``). A valid entry is easiest to create from existing entries, but some important parts are:

* ``name``: The machine-friendly name of the bot. Although it doesn't have to, it should be the same as the name of the Python file.

 * It should be the same as the name of the dictionary key

* ``prettyname``: A human friendly version of the bot's name. This will be displayed in the console.
* ``function``: The Python function that is run each iteration of the bot. This should be your ``iteration`` function, which should be imported directly above the configuration entry. 
* ``pre_deps``: A list of Python functions that must run at some point before each iteration. For example, ``foreachrevision.preRunBots``.
* ``post_deps``: A list of Python functions that must run at some point after each iteration. For example, ``foreachrevision.postRunBots``.
