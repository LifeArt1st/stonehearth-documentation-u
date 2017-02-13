import re
import os
import io
from pathlib import PurePath

encoding = "utf-8"

reg_events = re.compile(r"radiant\.events\.trigger.*\([\w\W]*?\)")
reg_args = re.compile(r"\w+(?= =)")

def extract_events_from_text(string):
    formattedEvents = []
    
    events = set(re.findall(reg_events, string))
    for event in events:
        items = event.split(',')
        async = "✔" if "trigger_async" in event else "✖"

        if len(items) > 3:
            # rejoin arguments
            arguments = ",".join(items[2:])
            # remove {}
            arguments = arguments[1:len(arguments)-2]
            # remove equations
            arguments = ", ".join(re.findall(reg_args, arguments))
        elif len(items) == 3:
            # remove bracket from argument
            arguments = items[2][:len(items[2])-1]
        else:
            # remove bracket from name if there arent any arguments
            items[1] = items[1][:len(items[1])-1]
            arguments = None

        # remove '...' from name
        items[1] = items[1][2:len(items[1])-1]
        # construct output string
        outputStr = "{0} | {1} | {2} | {3}".format(items[1], arguments, "Empty", async)
        formattedEvents.append(outputStr)

    return formattedEvents

def get_all_events(root, output):
    output = root[2:len(root)-1] + "_" + output
    with io.open(output, "w", encoding = encoding) as outputfile:
        for path, subdirs, files in os.walk(root):
            for name in files:
                file = PurePath(path, name)
                # only read if its a lua file
                if file.suffix == ".lua":
                    # open found lua file for read 
                    with io.open(str(file), "r") as f:
                        # get events from text
                        events = extract_events_from_text(f.read())
                        # only print header if events was find
                        if events != []:
                            print("##### "+str(file), file = outputfile)
                            print("Event Name | Arguments | Triggered | Async", file = outputfile)
                            print("---------- | --------- | --------- | -----", file = outputfile)
                            for event in events:
                                print(event, file = outputfile)

# For just one file you can use this call
# 
#f = open("test.lua", "r")
#print(extract_events_from_text(f.read()) == set())


get_all_events("./radiant/", "events.markdown")
        
