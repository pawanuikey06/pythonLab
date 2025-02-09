doubles =[x*2 for x in range(1,11) if x%2==1]

print(doubles)

# match case statement

def dey_of_week(day):
    if day==1:
        return "It is Sunday"
    elif day==2:
        return "It is Monday"
    elif day==3:
        return "It is Tuesday"
    elif day==4:
        return "It is WednesDay"
    elif day==5:
        return " It is ThursDay"
    elif day==6:
        return "It is Firday"
    elif day==7:
        return "It is SaturDay"
    else:
        return "Not a valid day"
    


print(dey_of_week(1))