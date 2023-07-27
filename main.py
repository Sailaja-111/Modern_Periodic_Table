class colors:
    reset = '\033[0m'
    bold = '\033[01m'
    underline = '\033[04m'
    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'
def all_elements(file_name,element_names):
    for i in range(len(file_name)):
        source = file_name[i]
        with open(source, "r", encoding='utf-8') as f:
            data = f.read()
            print(colors.bold, colors.underline, colors.fg.yellow, "\n\n\n************************************",colors.fg.red, "INFORMATION ABOUT ",element_names[i], colors.fg.yellow,"*********************************************\n\n\n")
            print(colors.reset, colors.bg.black, colors.bold, colors.fg.pink, data)
            f.close()
def search_by_name(file_name,element_names):
    print(colors.bold,colors.bg.black,colors.fg.green,"**********************",colors.fg.pink,"SEARCH BY NAME",colors.fg.green,"***************************\n")
    print(colors.fg.purple,"Enter the name of the element\n")
    element_name=input()
    count=0
    for i in range(len(file_name)):
        if(element_name==element_names[i]):
            count=count+1
            source = file_name[i]
            with open(source, "r", encoding='utf-8') as f:
                data = f.read()
                print(colors.bold, colors.underline, colors.fg.yellow, "\n\n\n************************************", colors.fg.red, "INFORMATION ABOUT ", element_names[i], colors.fg.yellow,"*********************************************\n\n\n")
                print(colors.reset, colors.bg.black, colors.bold, colors.fg.pink, data)
                f.close()
    if(count==0):
        print("ENTER VALID NAME\n")
def search_by_symbol(file_name,element_names,symbol):
    print(colors.bold, colors.bg.black, colors.fg.green, "**********************", colors.fg.pink, "SEARCH BY SYMBOL", colors.fg.green, "***************************\n")
    print(colors.fg.purple, "Enter the symbol of the element\n")
    element_symbol = input()
    count = 0
    for i in range(len(file_name)):
        if (element_symbol == symbol[i]):
            count = count + 1
            source = file_name[i]
            with open(source, "r", encoding='utf-8') as f:
                data = f.read()
                print(colors.bold, colors.underline, colors.fg.yellow, "\n\n\n************************************",colors.fg.red, "INFORMATION ABOUT ", element_names[i], colors.fg.yellow,"*********************************************\n\n\n")
                print(colors.reset, colors.bg.black, colors.bold, colors.fg.pink, data)
                f.close()
    if (count == 0):
        print("ENTER VALID NAME\n")
def search_by_atomic_no(file_name,element_names,atomic_nos):
    print(colors.bold, colors.bg.black, colors.fg.green, "**********************", colors.fg.pink, "SEARCH BY ATOMIC NO",colors.fg.green, "***************************\n")
    print(colors.fg.purple, "Enter the atomic number of the element\n")
    element_no = int(input())
    count = 0
    for i in range(len(file_name)):
        if (element_no == atomic_nos[i]):
            count = count + 1
            source = file_name[i]
            with open(source, "r", encoding='utf-8') as f:
                data = f.read()
                print(colors.bold, colors.underline, colors.fg.yellow, "\n\n\n************************************",colors.fg.red, "INFORMATION ABOUT ", element_names[i], colors.fg.yellow,"*********************************************\n\n\n")
                print(colors.reset, colors.bg.black, colors.bold, colors.fg.pink, data)
                f.close()
    if (count == 0):
        print("ENTER VALID NAME\n")
file_name=["hydrogenn.txt","helium.txt","lithium.txt","berylium.txt","boron.txt","carbon.txt","nitrogen.txt","oxygen.txt","fluorine.txt","neon.txt"]
element_names=["HYDROGEN","HELIUM","LITHIUM","BERYLIUM","BORON","CARBON","NITROGEN","OXYGEN","FLUORINE","NEON"]
symbol=["H","He","Li","Be","B","C","N","O","F","Ne"]
atomic_nos=[1,2,3,4,5,6,7,8,9,10]
while(1):
    print(colors.bold, colors.bg.black, colors.fg.yellow, "****************************************", colors.fg.pink,"WELCOME TO PERIODIC TABLE", colors.fg.yellow, "********************************************")
    print(colors.bg.black, "\n\n\n")
    print(colors.bold, colors.fg.red, "ENTER YOUR CHOICE\n")
    print(colors.fg.cyan, "1.", colors.fg.green, "EXPLORE\n")
    print(colors.fg.cyan, "2.", colors.fg.green, "ADD INFORMATION FOR ELEMENT\n")
    print(colors.fg.cyan, "3.", colors.fg.green, "EXIT\n\n\n")
    choice = int(input())
    if (choice == 1):
        print(colors.bold, colors.fg.yellow, "\n\n\n\n****************************************", colors.fg.pink,
              "TO EXPLORE PERIODIC TABLE", colors.fg.yellow, "********************************************")
        print(colors.bold, colors.fg.red, "\n\n\nENTER THE CORRESPONDING NUMBER\n")
        print(colors.fg.cyan, "1.Search by", colors.bold, "'NAME'")
        print(colors.fg.cyan, "2.Search by", colors.bold, "'SYMBOL'")
        print(colors.fg.cyan, "3.Search by", colors.bold, "'ATOMIC NO'")
        print(colors.fg.cyan, "4.ALL ELEMENTS\n\n\n\n")
        search = int(input())
        if (search == 1):
            search_by_name(file_name,element_names)
        elif (search == 2):
            search_by_symbol(file_name,element_names,symbol)
        elif (search == 3):
            search_by_atomic_no(file_name,element_names,atomic_nos)
        elif (search == 4):
            all_elements(file_name,element_names)
        else:
            print("Enter valid choice")
    elif (choice == 2):
        source = input("enter file name\n")
        file_name.append(source)
        x = input("enter element name:")
        element_names.append(x)
        f = open(source, "w")
        f.write("\t NAME      :")
        f.write(x)
        f.write("\n")
        y = input("enter element no:")
        atomic_nos.append(y)
        f.write("\t ATOMIC NO :")
        f.write(y)
        f.write("\n")
        z = input("enter symbol")
        symbol.append(z)
        f.write("\t SYMBOL     :")
        f.write(z)
        f.write("\n")
        k = input("enter color")
        f.write("\t COLOR : ")
        f.write(k)
        f.write("\n")
        a = input("enter group")
        f.write("\t GROUP : ")
        f.write(a)
        f.write("\n")
        b = input("enter period")
        f.write("\t PERIOD : ")
        f.write(b)
        f.write("\n")
        c = input("enter valency")
        f.write("\t VALENCY : ")
        f.write(c)
        f.write("\n")
        f = open(source, "r")
        data = f.read()
        print(colors.bold, colors.underline, colors.fg.yellow, "\n\n\n************************************",colors.fg.red, "INFORMATION ABOUT", x, colors.fg.yellow,"*********************************************\n\n\n")
        print(colors.reset, colors.bg.black, colors.bold, colors.fg.pink, data)
        f.close()
        count = count + 1
    elif (choice==3):
        break
    else:
        print("ENTER VALID CHOICE")
