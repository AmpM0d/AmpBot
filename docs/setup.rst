Setting up UltiBlocksAutoMod
============================

Prerequisites
&&&&&&&&&&&&&
* Git should be installed on your system
* You should have a recent version of Python 3.

 * The project doesn't use any super fancy Python features, so you can probably use a wide range of versions.

* You should have knowledge of the command line on your system, as well as (ideally) Python knowledge. 
* If you're contributing to the documentation, make sure you know ReST.

Setup
&&&&&

Cloning the repository
----------------------
Cloning and entering the repository should be as simple as two commands, which work on any system.

| ``git clone https://github.com/AmpM0d/UltiBlocksAutoMod``
| ``cd UltiBlocksAutoMod``

Installing other requirements
-----------------------------

Once you are in the project directory, you should then set up your environment by running the ``install.bat`` script (Windows) or ``install.sh`` (Linux). We do not currently have a separate script for contributing to documentation, so you currently must install the bot libraries as well. This will be changed eventually.

If the setup script prompts you for usernames and passwords which you don't have, leave them blank, as you will not use them. If you are testing or contributing to the actual source code, you should have gotten permission from an admin on the Wiki, created a Wiki account, gotten its permissions set to bot, and obtained a bot password.

Start contributing!
&&&&&&&&&&&&&&&&&&&
Now, it's time to start developing!

Contributing to documentation
-----------------------------

If you are contributing to the developer documentation, you will want to start the autobuild server to see your changes in real time. You'll want to open a command line to the ``.venv/Scripts`` or ``.venv/bin`` directory (Windows or Linux respectively) and run this command:

``sphinx-autobuild ../../docs ../../docs/_build``

Leave this process running, and split screen your browser with your code editor. Open the browser to `<http://localhost:8000>`_
.

When you make changes, simply save them, and the documentation will rebuild.
