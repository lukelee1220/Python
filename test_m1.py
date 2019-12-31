import math

def cal_remainder(dividend, divisor):
    ''' return quotient, remainder, position '''
    input1 = str(dividend)
    input2 = str(divisor)
    tmpStr = ""
    count = 0
    for n in input1: #,len(input2):
        if(count < len(input2)):
            count +=1
    #        print(n)
            tmpStr +=n
        else:
            if(int(tmpStr)< divisor):
                count +=1
                tmpStr +=n
            break
    #print(divisor)
    #print(tmpStr)
    #print(int(tmpStr)//divisor, int(tmpStr)%divisor)
    return int(tmpStr)//divisor, int(tmpStr)%divisor, count



input1 = input("pls input dividend number:")
input2 = input("pls input divisor number:")

if((not input1.isdigit()) or (not input2.isdigit())):
    print("input error")
    exit
dividend = int(input1)
divisor = int(input2)

if(dividend <= divisor):
    print("quotient=",(dividend)//divisor,"remainder=",dividend%divisor )
    exit

lst_q = []
lst_p = []

first_pos = 0
tmp_dividend = dividend
pos = 1
while(pos<= len(str(dividend))):
    tmp_dividend_str = ""
    #print("start",tmp_dividend,divisor)
    result = cal_remainder(tmp_dividend, divisor)
    #print(":::",result[0],result[1], result[2])
    if(result[0] == 0 and pos == len(str(dividend))):
        lst_p.append(tmp_dividend)
        break

    lst_q.append(result[0])
    lst_p.append(tmp_dividend)
    lst_p.append( result[0]*divisor)
    if(pos == 1):
        pos = int(result[2])
        first_pos = pos
    else:
        pos += 1
    tmp_dividend_str = str(result[1])
    if (result[1] == 0):
        lst_q.append(0)
        

    cnt = 1
    for n in str(dividend):
        if(cnt<=pos):
            cnt+=1
            continue
        else:
            tmp_dividend_str +=n
    #print("tmp_dividend_str:",tmp_dividend_str, "pos:", pos)
    tmp_dividend = int(tmp_dividend_str)

    
# print(lst_q)
# for n in lst_p:
#     print(n)

first_line = ""
first_line =" "*(len(input2)+first_pos)
for n in lst_q:
    first_line +=str(n)

second_line =" "*(len(input2)+1)
second_line +="-"*len(input1)

thrid_line= input2 +"|"+ str(lst_p[0])

print(first_line)
print(second_line)
print(thrid_line)
total_len = len(thrid_line)
for n in range(1, len(lst_p)):
    if(n%2!=0):
        #space_len = (len(input2)+first_pos+1-len(str(lst_p[n])))
        if(n==1):
            space_len = first_pos+len(input2)-len(str(lst_p[n]))
        else:
            space_len =  len(input2) + len(input1) - len(str(lst_p[n-1]))
    else:
        space_len = len(input2) + len(input1) - len(str(lst_p[n]))
    print(" "*space_len,str(lst_p[n]))
    if(n%2 !=0):
        #print(" "*(len(input2)+first_pos-len(str(lst_p[n]))),"-"*len(str(lst_p[n])))
        print(" "*space_len,"-"*len(str(lst_p[n])))



#cal units tens hund etc 
#str1 = str(dividend)
#print(str1)

# for n in str1:
#     print(n)
# print(len(str1), str1[0])