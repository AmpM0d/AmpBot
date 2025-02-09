from .bots import sandbox, remind
from .wikisite import site
import time

def runbots(botlist):
    while 1:
        for i in botlist:
            i(site)
        time.sleep(5)

def main(argv):
    if len(argv)==1:
        bots=[sandbox,remind]
    else:
        bots=[]
        if "sandboxbot" in argv:
            bots.append(sandbox)
        if "remindbot" in argv:
            bots.append(remind)
    runbots(bots)

if __name__=="__main__":
    import sys
    main(sys.argv)