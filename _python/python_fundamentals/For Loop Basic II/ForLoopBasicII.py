def BiggieSize(list):
    for x in range(0, len(list), 1):
        if list[x] > 0: 
            list[x] = "big"
    return list

print(BiggieSize([2,-3,5,-8,10,-15]))




def CountPositives(list):
    count = 0
    for x in range(0, len(list), 1):
        if list[x] > 0: 
            count += 1
    list[len(list)-1] = count

    return list
print(CountPositives([1,6,-4,-2,-7,-2]))





def SumTotal(list): 
    sum = 0
    for x in range(0, len(list), 1):
        sum += list[x]
    return sum

#print(SumTotal([6,3,-2]))



def Average(list):
    sum = 0
    for x in range(0, len(list), 1):
        sum += list[x]
    avg = sum / len(list)
    return avg 

#print(Average([1,2,3,4]))


def length(list):
    count = 0
    for x in range(0, len(list), 1):
        count += 1
    return count 

print(length([37,2,1,-9]))


def Minimum(list):
    if len(list) == 0:
        return False
    min = list[0]
    for x in range(1, len(list), 1):
        if min > list[x]:
            min = list[x] 
    return min 

print(Minimum([37,-20,1,-9]))




def maximum(list):
    if len(list) == 0:
        return False
    max = list[0]
    for x in range(1, len(list), 1):
        if max < list[x]:
            max = list[x] 
    return max 

print(max([37,50,1,-9]))



def UltimateAnalysis(list): 
    analysis_dict = {}
    analysis_dict["SumTotal"] = SumTotal(list)
    analysis_dict["Average"] = Average(list)
    analysis_dict["length"] = length(list)
    analysis_dict["Minimum"] = Minimum(list)
    analysis_dict["Maximum"] = maximum(list)

    return analysis_dict

print(UltimateAnalysis([37,50,1,-9]))

def ReverseList(list):
    new_list = []
    for i in range(len(list)-1, -1, -1):
        new_list.append(list[i])
    return new_list


print(ReverseList([37,50,1,-9]))








    

