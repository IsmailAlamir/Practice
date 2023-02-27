def rearrange_odds_and_evens(arr):

    odd,even = [], []
    for num in arr:
        if num %2==0 :
            even.append(num)
        else :
            odd.append(num)
    
    res=[]
    if len(odd)>len(even):
        while even:
            res.append(odd.pop(0))
            res.append(even.pop(0))
        res+=odd
    else:
        while odd:
            res.append(odd.pop(0))
            res.append(even.pop(0))
        res+=even
    return res
    
def not_Dublicates(arr):
    counts={}
    res=[]

    for num in arr:
        if num in counts:
            counts[num]+=1
        else:
            counts[num]=1

    for num,count in counts.items():
        if count==1:
            res.append(num)

    return res

def charactusrnumve(string):
    charCounter=0
    numberCounter=0
    speicalCounter=0
    for char in string:
        if (ord(char)>=65 and ord(char)<90) or(ord(char)>=97 and ord(char)<122):
            charCounter+=1
        elif  (ord(char)>=48 and ord(char)<57):
            numberCounter+=1
        else:
            speicalCounter+=1
    return charCounter,numberCounter,speicalCounter


def missing_number(arr):
    num = 0
    max_val = max(arr)

    for j in range(max_val):
        if j not in arr:
            num = j
            break

    return num



def index_of_repeated_integer_index(arr):
    seen = set()
    for i in range(len(arr)):
        if arr[i] in seen:
            return i
        seen.add(arr[i])
    return "no"

def index_of_repeated_integer_index(arr):
    seen = set()
    
    for i in reversed(range(len(arr))):
        print(i)
        if arr[i] in seen:
            return i
        seen.add(arr[i])
    return "no"
    
def two_sum(arr, target):
    hashtable = {}
    arr2 = [0, 0]

    for i in range(len(arr)):
        if target - arr[i] in hashtable:
            arr2[0] = hashtable[target - arr[i]]
            arr2[1] = i
        else:
            hashtable[arr[i]] = i
    
    return arr2


def two_sum(arr, target):
    sum=0
    hash={}
    for num in arr:
        value=target-num
        if value in hash:
            return [value,num]
        else :
            hash[num]=True
    
def repeated_integers_with(arr):
    hashtable = {}

    for num in arr:
        if num in hashtable:
            hashtable[num] += 1
        else:
            hashtable[num] = 1

    for key, value in hashtable.items():
        print(key, value)
arr = [1, 2, 3, 3, 3, 4, 4, 4, 4]
repeated_integers_with(arr)


# x=4
# y=5
# x+=y
# y=x-y
# x=x-y

# print("x=",x , "y=", y)


def sum2num(arr):
    pointer1 = arr[0]
    pointer2 = arr[0]
    result = []
    
    for i in range(1, len(arr)):
        if arr[i] == pointer1:
            pointer2 += arr[i]
        else:
            result.append(pointer2)
            pointer1 = arr[i]
            pointer2 = arr[i]
    result.append(pointer2)
    
    return result



    
def isValid( s: str) -> bool:
    pairdict = {
        "(":")",
        "[":"]",
        "{":"}"
    }
    stack = []
    for char in s:
        if char in pairdict:
            stack.append(char)
        elif not stack or pairdict[stack.pop()] != char:
            return False

    return not stack

 
def pyramid_of_stars(base):
    for i in reversed(range(base+1)):
        print ((i)*"*")

