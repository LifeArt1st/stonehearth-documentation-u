from pyparsing import Word, alphas, Optional, Combine, ZeroOrMore, Group, quotedString, delimitedList, Suppress, alphanums, ParseResults, removeQuotes

import io
import os
from pathlib import PurePath

CONSOLE_OUTPUT = True

encoding = "utf-8"
types = {"true": "Boolean", "false": "Boolean"}

def convertType(s, l, t):
    if t[0] in types:
        return types[t[0]]

def parse_events_from_text(text):
    variable = Word(alphanums + "-_.:()")

    # Entity on which the event will be triggered
    obj = variable.setResultsName("object")

    # Name of the event
    name = (quotedString + Optional(Suppress("..") + variable)).setResultsName("name")

    # Parameter List of the event
    paramName = variable.setResultsName("name")
    paramType = variable.setResultsName("type").setParseAction(convertType)
    param = Group(paramName + Suppress("=") + paramType).setResultsName("parameter")
    paramList = Group(Optional(Suppress("{") + ZeroOrMore(delimitedList(param)) + Suppress("}"))).setResultsName("parameters")

    parameter = obj | name | paramList

    # Function Start
    trigger = "radiant.events.trigger"
    async = Optional("_async")

    # Function Call
    functionOpening = Combine(trigger + async + "(").setResultsName("functionOpening")
    functionCall = ZeroOrMore(Group(functionOpening + delimitedList(parameter) + Suppress(")")))

    resultsList = functionCall.searchString(text)

    results = []
    
    for resultsL in resultsList:
        if len(resultsL) != 0:
            if resultsL not in results:
                results.append(resultsL)

    return results

def make_string_from_params(params):
    return ", ".join(["{0}: {1}".format(param["name"], param["type"]) for param in params])
        

def make_string_from_events(events):
    events_string = []
    for event in events:
        object_ = event["object"]
        name_str = event.get("name")
        if name_str != None:
            name_str = event.get("name")[0].translate(str.maketrans({"'":"`", '"':"`"}))
            name_var = "+ <{0}>".format(event.get("name")[1]) if len(event.get("name")) > 1 else ""
        name = "`{0}` {1}".format(name_str, name_var) if event.get("name") != None else None
        params = event.get("parameters")
        if params != None:
            params = make_string_from_params(params) 
        async = "✔" if "trigger_async" in event["functionOpening"] else "✖"
        string = "{0} | {1} | {2} | {3}".format(object_, name, params, async)
        
        events_string.append(string)

    return events_string

def parse_events_from_file(filename, outputfile):
    with open(filename, "r") as fn:
        events = parse_events_from_text(fn.read())
        with io.open(outputfile, "w", encoding = encoding) as fo:
            for l_event in events:
                print(type(l_event))
                if isinstance(l_event, ParseResults):
                    # found something
                    print("##### "+filename, file = fo)
                    print("Object | Name | Arguments | Async", file = fo)
                    print("------ | ---- | --------- | -----", file = fo)
                    for event in make_string_from_events(l_event):
                        print("Test")
                        print(event, file = fo)

def _get_lua_file_count(root):
    count = 0
    for path, subdirs, files in os.walk(root):
        for name in files:
            file = PurePath(path, name)
            # only read if its a lua file
            if file.suffix == ".lua":
                count += 1
    return count

def parse_events_from_files(root, outputfile):
    with io.open(outputfile, "w", encoding = encoding) as fo:
        # found something
        print("## " + root + " - events", file = fo)
        print("*I can't promise that these are all events.*\n", file = fo)
        print("Arguments are read as follows -> `<name>: <type>`. While the type is just the variable which was assigned to the name.\n", file = fo)
        print("Object | Name | Arguments | Async | file", file = fo)
        print("------ | ---- | --------- | ----- | ----", file = fo)
        openedFiles = 0
        eventCount = 0
        filesToParse = _get_lua_file_count(root)
        for path, subdirs, files in os.walk(root):
            for name in files:
                file = PurePath(path, name)
                # only read if its a lua file
                if file.suffix == ".lua":
                    # open file to read
                    with io.open(str(file), "r") as fn:
                        openedFiles += 1
                        # get events
                        events_results = parse_events_from_text(fn.read())
                        for event_result in events_results:
                            # convert events into a string
                            # print them out
                            for event in make_string_from_events(event_result):
                                eventCount += 1
                                print(event + " | " + str(file), file = fo)
                        consoleString = "searching... [{0}/{1}] -> {2}".format(openedFiles, filesToParse, eventCount)
                        if CONSOLE_OUTPUT: print(consoleString, end="\r", flush = True)
        print("###### A total of **{0}** events found while parsing **{1}** files.".format(eventCount, openedFiles), file = fo)
        if CONSOLE_OUTPUT: print("\nDone!")

if __name__ == "__main__":
    parse_events_from_files("./stonehearth/", "stonehearth_events.markdown")
