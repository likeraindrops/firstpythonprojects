import random
adventurelist = ["get eggs, chocolate, honey, and mango sauce from TJoe's",
                 "watch a single episode/lecture of a data science course",
                 "organize and wipe down desk",
                 "neat stuff"]
print("""
Type 'help' for a list of prompts!""")
def adventurepicker():
    help = {
        "keyword: " : "description",
        "  help: ": "You're here!",
        "  list: ": "This is the current list of adventures and neat stuff",
        "  add: ": "add to the neat list",
        "  pick: ": "let python pick the next neat adventure!"
    }
    def adadd():
        newadd = (input("""What else?
"""))
        if newadd == "done":
            return
        else:
            adventurelist.append(newadd)
        return (adadd())
    def adpick():
        try:
            index = int(random.randint(0, len(adventurelist) - 1))
            upnext = """
The next adventure is going to be: 

            ✩ {}!
"""
            print(upnext.format(adventurelist[index]))
            def completioncheck():
                task = input("""Has this been completed? :) ('yes', 'no', or 'not yet')
""")
                if task == "yes":
                    print("""
            Congrats!

Would you like to update the entry, wipe it from the list, or leave it?""")
                    listwiper()
                elif task == "no" or task == "not yet":
                    encouragement()
                else:
                    print("Oops!")
                    completioncheck()
            def listwiper():
                listwipe = (input(
"""('update' or 'wipe' or 'leave')
"""))
                if listwipe == "leave":
                    print("""
        It'll be shuffled back in!""")
                elif listwipe == "wipe":
                   adventurelist.pop(index)
                   print("""
        All done! Walk slowly, never backwards. Keep at it!""")
                elif listwipe == "update":
                    adventurelist[index] = input("""
What's the update to '""" + adventurelist[index] + """'?
""")
                    print("""
        Got it!""")
                else:
                    return listwiper()
            def encouragement():
                #print("randomized words of encouragement!")
                print("""What about further delineation of the goal? Start with the tiniest step.
Perhaps shower and put on clean clothes.
Open the browser window and do an internet search.
Gather some information.
Give it two minutes!
Check in with yourself.

Has enough progress been made to shuffle it back in?
""")
                listwiper()
            completioncheck()
        except ValueError:
            print("The list is empty! Add some adventures!")
        return

    fork = input("""
What would you like to do?
""")
    if fork == "add":
        firstitem = (input("""
What's being added? 
        Try to use all relevant specifics, like location and quantity.
            Eg, get x, y, and z from specific store
            or the specific tutorial or lesson episode that's up next
                (inc subject, source, and format)
        (type 'done' when the list is ready!)
"""))
        if firstitem == "done":
            return adventurepicker()
        else:
            adventurelist.append(firstitem)
            adadd()
        return adventurepicker()
    elif fork == "pick":
        adpick()
        return adventurepicker()
    elif fork == "list":
        print("")
        for things in adventurelist:
            print("✩", things)
    else:
        print("""
Oh, no! Try these keywords instead!""")
        for terms, defs in help.items():
            print (terms, defs)
    return adventurepicker()

adventurepicker()