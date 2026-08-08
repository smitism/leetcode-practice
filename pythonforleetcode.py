#python syntax for leetcode

#variable
hello = ""
a = 1

#classes
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

node = ListNode(1)
print(node.val)
node.val = 10
print(node.val)

#loops
arr = [1,2,3,4]

for i in range(len(arr)):
    print(arr[i])

print("-----")

index = len(arr)-1

while index >=0:
    print(arr[index])
    index -= 1

#max and min 

result = min(5,4)
print(result)

#dictionary
dict = {}
{
    "key" : "value"
}

dict[10] = "smit"
dict["a"] = 9

print(dict)

if "a" in dict:
    print("true")
else:
    print("false")

dict["a"]+=1
print(dict)

for key,value in dict.items():
    print(str(key) + ": " + str(value))

#strings

str = "ab cd e"
splitstr = str.split( )
print(splitstr)
for arr in splitstr:
    print(arr)

result = "".join(splitstr)
print(result)