list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [2,4,6,8,10,12,14,16,18,20]
equals = ["=","=","=","=","=","=","=","=","=","="]
plus = ["+","+","+","+","+","+","+","+","+","+",]
minus = ["-","-","-","-","-","-","-","-","-","-",]
divide = ["/","/","/","/","/","/","/","/","/","/",]
multiply = ["*","*","*","*","*","*","*","*","*","*",]


def addAndDisplayLists(list1, list2):
    zipped_lists = zip(list1, list2)
    plusSum = [x + y for (x, y) in zipped_lists]
    pluslist = [list1, plus, list2, equals, plusSum]
    
    for a in zip(*pluslist):
        print(*a)
    print("")

def substractAndDisplayLists(list1, list2):
    zipped_lists = zip(list1, list2)
    minusSum = [x - y for (x, y) in zipped_lists] 
    minuslist = [list1, minus, list2, equals, minusSum]
    
    for a in zip(*minuslist):
        print(*a)
    print("")

def multiplyAndDisplayLists(list1, list2):
    zipped_lists = zip(list1, list2)
    multiplySum = [x * y for (x, y) in zipped_lists] 
    multiplylist = [list1, multiply, list2, equals, multiplySum]
    
    for a in zip(*multiplylist):
        print(*a)
    print("")

def divideAndDisplayLists(list1, list2):
    zipped_lists = zip(list1, list2)
    divideSum = [x * y for (x, y) in zipped_lists] 
    dividelist = [list1, divide, list2, equals, divideSum]
    
    for a in zip(*dividelist):
        print(*a)
    print("")

addAndDisplayLists(list1, list2)
substractAndDisplayLists(list1, list2)
multiplyAndDisplayLists(list1, list2)
divideAndDisplayLists(list1, list2)
