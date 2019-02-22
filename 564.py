/*
I've not simpfied the code, hope someone can help me deal with some python logic, I don't think I need that much variables.
My logic is simply return n-1 when its digit less than 2 and return 9 if that is 11, because if I need to deal with these logic, it will slow down my code with more logic and it's not necessary.
I will setup 2 candidates, one is smaller than the string and the other is larger and that is what we need. By slice the string and reverse then append, I will generate 1 candidate, by define whether it's a larger or smaller one, I will then generate the other. If that is equal to string(which mean string is palindrome.), The logic will generate 2 candidates.
The last one is just return the closest one.
*/

if int(n) <=10 and int(n)>0:
    return str(int(n)-1)
if n == '11':
    return '9'
flag=0
b=0
c=0
if len(n)%2 != 0:
    flag=1
    _first=n[0:int(len(n)/2)+1]
    a=_first+_first[::-1][1:]
else:
    _first=n[0:int(len(n)/2)]
    a=_first+_first[::-1]
int_a = int(a)
int_n = int(n)
int_first=int(_first)
if int_a>=int_n:
    _second = str(int_first - 1)
    if len(_second) < len(_first):
        b = _second + _second[::-1]+'9' if flag == 0 else _second + _second[::-1]
    else:
        b = _second + _second[::-1] if flag == 0 else _second + _second[::-1][1:]
    c=a
if int_a<=int_n:
    _third = str(int_first + 1)
    if len(_third) > len(_first):
        c = _third+_third[::-1][1:] if flag == 0 else _third[:-1]+_third[::-1][1:]
    else:
        c = _third + _third[::-1] if flag == 0 else _third + _third[::-1][1:]
    if not b:
        b=a

return b if abs(int(b)-int(n))<=abs(int(c)-int(n)) else c
