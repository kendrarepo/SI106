import json

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

def get_str(prompt= "Please paste a json formatted string followed by a blank line"):
    # allow the user to enter a multiline string
    print prompt
    text = ""
    stopword = ""
    while True:
        line = raw_input()
        if line.strip() == stopword:
            return text
        text += "%s\n" % line
    
prompt_str = """Enter a single character command.
\t(q)uit
\t(t)ype: print the type of the current data
\t(k)eys: print the keys of the current dictionary
\t(l)en: print the length of the list or number of keys in the dictionary
\t(p)retty_print: print the entire data
\t(f)irst: switch to working with the first element of the list
\t(g)et: get the value associated with some key in the dictionary
\t(o)ut: go back to the enclosing data
"""
def analyze(json_obj_or_str = None):
    if not json_obj_or_str:
        json_obj_or_str = get_str()
    print type(json_obj_or_str)
    if type(json_obj_or_str) == type('') or type(json_obj_or_str) == type(u''):
        try:
            print "here"
            data = json.loads(json_obj_or_str)
        except:
            return "Unable to interpret your string as json", []
    else:
        # it was already a python object, not a json string
        data = json_obj_or_str
    nesting_level = 1
    commands = ["data1 = your_data_object"]
    data_stack = []
    expr = "your_data_object"
    while (True):
        print
        print "working with:", expr
        cmd = raw_input(prompt_str)
        if (cmd == 'q'):
            return (expr, commands)
        elif (cmd == 't'):
            print type(data)
        elif (cmd == 'l'):
            try:
                print len(data)
            except:
                print "It's not a string or a list or a dictionary; can't take its length"
        elif (cmd == 'p'):
            print pretty(data)
        elif (cmd == 'k'):
            try:
                print data.keys()
            except:
                print "Can't print the keys. Perhaps it's not a dictionary?"
        elif (cmd == 'f'):            
            try:
                last_data = data
                data = data[0]
                nesting_level += 1
                commands.append("data%d = data%d[0]" % (nesting_level, nesting_level-1))
                print "\tnesting level %d" % nesting_level
                data_stack.append((expr, last_data))
                expr = expr + "[0]"
            except:
                print "Couldn't extract the first element. Not a list or string, or no elements."
        elif (cmd == 'g'):
            try:
                last_data = data
                key = raw_input("\tKey whose value is to be extracted from the dictionary\n\t")
                data = data[key]
                nesting_level += 1
                commands.append("data%d = data%d['%s']" % (nesting_level, nesting_level-1, key))
                
                data_stack.append((expr, last_data))
                expr = "%s['%s']" % (expr, key)
                print "\tnesting level %d" % nesting_level
            except:
                print "Couldn't extract %s. Either it's not a dictionary or that key isn't in the dictionary" % key
        elif (cmd == 'o'):
            try:
                expr, data = data_stack[-1]
                data_stack = data_stack[:-1]
                commands = commands[:-1]
            except:
                print "already at outermost nested data object"
        else:
            print "Command not recognized"
            
                
if __name__ == '__main__':            
    expr, commands = analyze()
    for c in commands:
        print c
        
    print expr
