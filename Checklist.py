list = {"party": {"Priority":["money","decorations"], "Lower":["test"]}
        }
yes_list = ["y", 'yes']
#print(list["party"])
def newList():
    Name = input("Name of new list?")
    priority = input("What are some priority tasks?")
    Lower = input("What are some other tasks?")
    list.update({Name:{"Priority":[priority], "Lower":[Lower]}})
    print("\nList added\n")
    for i in list:
        if i == Name:
            print(i)
    for x in list[Name]:
        print(x)
        print(list[Name][x])


def GetList(list):
    event = input("What event are you planning?").lower()
    for i in list:
        if i == event:
            #print(list[i])
            for x in list[i]:
                print(x)
                print(list[i][x])
        else:
            print("Error, list name %s does not currently exist \nWould you like to create one?" %event)

def main():
    GetList(list)
    check = input("Yes or no").lower()
    if check in yes_list:
        newList()
main()