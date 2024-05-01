import random
def randInt(min=0  , max=100 ):
    if min > max or max < 0: 
        print("parameters are invalid ")
        return
    num = random.random() *(max-min)+ min
    num = round(num)
    return num

# print(randInt())
# print(randInt(max=50)) 	
# print(randInt(min=50)) 	
# print(randInt(min=50, max=500))   


    
