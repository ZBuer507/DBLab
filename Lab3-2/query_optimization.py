'''
SELECT [ ENAME = ’Mary’ & DNAME = ’Research’ ] ( EMPLOYEE JOIN DEPARTMENT )
PROJECTION [ BDATE ] ( SELECT [ ENAME = ’John’ & DNAME = ’Research’ ] ( EMPLOYEE JOIN DEPARTMENT ) )
SELECT [ ESSN = ’01’ ] ( PROJECTION [ ESSN , PNAME ] ( WORKS_ON JOIN PROJECT ) )
PROJECTION [ ENAME ] ( SELECT [ SALARY < 3000 ] ( EMPLOYEE JOIN SELECT [ PNO = ’P1’ ] ( WORKS_ON JOIN PROJECT ) ) )
PROJECTION [ DNAME , SALARY ] ( AVG [ SALARY ] ( SELECT [ DNAME = ’Research’ ] ( EMPLOYEE JOIN DEPARTMENT ) ) )
'''

class action:
    def __init__(self, name, parameter, children):
        self.name = name
        self.parameter = parameter
        if(children != None):
            for i in range(len(children)):
                children[i].parent = self
        self.children = children
        self.parent = None
    
    def print(self):
        global indentation
        global actionList
        if self not in actionList:
            actionList.append(self)
        print("\t"*indentation,end="")
        print(self.name, self.parameter)
        if(self.children != []):
            indentation += 1
            for child in self.children:
                print("\t"*indentation,end="")
                child.print()
            indentation -= 1
            

def ana_notjoin(list):
    # print(list)
    name = list[0]
    list = list[1:]
    index = 0
    while True:
        try:
            if list[index] != "]":
                index += 1
            else:
                break
        except:
            print(name + " Error")
    parameter = list[1:index]
    list = list[index + 1:]
    #print(list)
    children = analyze(list[1:-1])
    return [action(name, parameter, children)]

def ana_join(list):
    # print(list)
    index = 0
    ac1 = None
    ac2 = None
    while True:
        try:
            if list[index] != "JOIN":
                index += 1
            else:
                break
        except:
            print("Join Error")
    list1 = list[0:index]
    list2 = list[index + 1:]
    # print(list1)
    # print(list2)
    if len(list1) == 1:
        ac1 = [action(list1[0], [], [])]
    else:
        ac1 = analyze(list2)
    if len(list2) == 1:
        ac2 = [action(list2[0], [], [])]
    else:
        ac2 = analyze(list2)
    return [action("JOIN", [], ac1 + ac2)]

def analyze(list):
    # print(list)
    if list[0] in keyword[0:-1]:
        # print(list[0])
        return ana_notjoin(list)
    elif keyword[3] in list:
        # print(keyword[3])
        return ana_join(list)
    return []

def find(name, node):
    if node.name in items:
        if name in items[node.name]:
            return False
        else:
            return True
    else:
        conti = True
        for child in node.children:
            conti = find(name, child)
            if not conti:
                break
        return conti

def opti(join):
    global actionList
    parent = join.parent
    n = 4
    if parent == None:
        return False
    if parent.name == "PROJECTION":
        n = 2
    if len(parent.parameter) < n:
        search = True
        while search:
            i = 0
            for item in join.children:
                search = find(parent.parameter[0], item)
                if not search:
                    print(parent.parameter[0])
                    break
                if search:
                    i += 1
            if i == len(join.children):
                return False
        join.parent = parent.parent
        if parent.parent != None:
            parent.parent.children.remove(parent)
            parent.parent.children.append(join)
        child = join.children[i]
        child.parent = parent
        join.children[i] = parent
        parent.parent = join
        parent.children.append(child)
        parent.children.remove(join)
    else:
        search = True
        while search:
            i = 0
            for item in join.children:
                search = find(parent.parameter[0], item)
                if not search:
                    print(parent.parameter[0])
                    break
                if search:
                    i += 1
            if i == len(join.children):
                return False
        #list = []
        list = parent.parameter[:n - 1]
        parent.parameter = parent.parameter[n:]
        new = action(parent.name, list, [join.children[i]])
        child = join.children[i]
        child.parent = new
        join.children[i] = new
        new.parent = join
        
    

global indentation
indentation = 0
keyword = ["SELECT", "PROJECTION", "AVG", "JOIN"]
items = {"EMPLOYEE":("ENAME", "SALARY"), "DEPARTMENT":("DNAME", "BDATE"), "WORKS_ON":("ESSN"), "PROJECT":("PNO", "PNAME")}
global actionList
actionList = []


if __name__ == "__main__":
    str = input("Input(from note above):")
    list = str.split(" ")
    head = analyze(list)
    head[0].print()
    conti = 0
    while conti < 5:
        for item in actionList:
            if item.name == "JOIN" and item.parent != None and item.parent.name != "JOIN":
                opti(item)
        conti += 1
    for item in actionList:
        if item.parent == None:
            item.print()
            break
    