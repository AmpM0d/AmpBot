"""
A bot module to edit lots of pages
"""

# Import necessary modules
import re
import time
import pywikibot,json

def allpages(site):
    for namespace in site.namespaces:
        if namespace>=0 and namespace!=2 and namespace!=8:
            for page in site.allpages(namespace = namespace):
                yield (page.title())
def pwbread(site,file):
    return pywikibot.Page(site,file).text
def pwbappend(site,file):
    p=pywikibot.Page(site,file)
    def inner(v,save=False,summ="Bot: misc action"):
        p.text+=v
        if save:
            print(p.text)
            p.save(summ)
    return inner

# Define a function to run every iteration of the bot loop
def iteration(runtimevars,iterationvars):
    backlog=pwbread(runtimevars["site"],"User:"+runtimevars["site"].user()+"/MassEditBacklog")
    botbacklog=pwbappend(runtimevars["site"],"User:"+runtimevars["site"].user()+"/MassEditInternalBacklog")
    for i in backlog.strip().split("\n"):
        for j in allpages(runtimevars["site"]):
            try: botbacklog("\n"+json.dumps([j,*json.loads(i)]))
            except json.decoder.JSONDecodeError: pass
    botbacklog("",save=True,summ="Bot: Updating my internal backlog")
    bl=pywikibot.Page(runtimevars["site"],"User:"+runtimevars["site"].user()+"/MassEditBacklog")
    bl.text=""
    bl.save("Bot: Updating backlog")
    bkl=pwbread(runtimevars['site'],"User:"+runtimevars["site"].user()+"/MassEditInternalBacklog").split("\n")
    process,old=bkl[:200],bkl[200:]
    for i in process:
        try: i=json.loads(i)
        except json.decoder.JSONDecodeError: continue
        page=pywikibot.Page(runtimevars['site'],i[0])
        ot=page.text
        page.text=re.sub(i[1],i[2],page.text)
        if ot!=page.text:
            page.save("Bot: Mass edit")
            time.sleep(10)
        time.sleep(0.5)
        print(i[0])
    p=pywikibot.Page(runtimevars['site'],"User:"+runtimevars["site"].user()+"/MassEditInternalBacklog")
    p.text="\n".join(old)
    p.save("Bot: updating my mass edit data")
# If we're being run as the main file, print an error,
# because I don't want to update more entry points than I have to.
if __name__ == "__main__":
     print("Please do not run masseditregex as main. Please instead run it via start.bat or start.sh")
