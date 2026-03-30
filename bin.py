# def binray(number):
#     bnry=[]
#     while (number):
#         bnry.append(str(number%2))
#         number=number//2
#     bnry.reverse()
#     num="".join(bnry)
#     print(num)
# def octal(number):
#     oct=[]
#     while(number):
#         oct.append(str(number%8))
#         number=number//8
#     oct.reverse()
#     num="".join(oct)
#     print(num)
# def hexadecimal(number):
#     hexa=[]
#     while(number):
#         temp=str(number%16)
#         if (temp=="10"):
#             temp="A"
#         elif (temp=="11"):
#             temp="B"
#         elif (temp=="12"):
#             temp="C"
#         elif (temp=="13"):
#             temp="D"
#         elif (temp=="14"):
#             temp="E"
#         elif (temp=="15"):
#             temp="F"
#         hexa.append(temp)
#         number=number//16
#     hexa.reverse()
#     num="".join(hexa)
#     print(num)
        
# num=1000
# binray(num)
# octal(num)
# hexadecimal(num)



def rangolli(size):
    count=0
    length=size*2-1
    width=size*4-3
    for i in range(length):
        lst=[]
        for j in range(count*2+1):
            if j<=count:
                off=j
            else:
                off=2*count-j
            lst.append(chr(size+96-off))
            
        format="-".join(lst)
        print(format.center(width, "-"))
        
        if (i<size-1):
            count+=1
        else:
            count-=1
rangolli(3)
            