from .bots import sandbox, remind
from .wikisite import site
import time

def main():
    while 1:
        for i in [sandbox,remind]:
            i(site)
        time.sleep(5)