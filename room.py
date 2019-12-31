

def cal_room(people):
        
    room6=0
    room4=0
    room2=0
    total_price=10000
    for room6_num in range(0,6):
        for room4_num in range(0,8):
            for room2_num in range(0,14):
                if((room6_num*6+room4_num*4+room2_num*2)>=people):
                    num=room6_num*120+room4_num*100+room2_num*80
                    if num <= total_price:
                        total_price=num
                        room6=room6_num
                        room4=room4_num
                        room2=room2_num
                        print (room6, room4, room2, total_price)
    print (room6, room4, room2)

cal_room(16)
cal_room(26)





