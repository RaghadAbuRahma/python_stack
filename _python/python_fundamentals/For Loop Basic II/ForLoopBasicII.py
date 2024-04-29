# def BiggieSize(list):
#     for x in range(0, len(list), 1):
#         if list[x] > 0: 
#             list[x] = "big"
#     return list

# print(BiggieSize([2,-3,5,-8,10,-15]))




# def CountPositives(list):
#     count = 0
#     for x in range(0, len(list), 1):
#         if list[x] > 0: 
#             count += 1
#     list[len(list)-1] = count

#     return list
# print(CountPositives([1,6,-4,-2,-7,-2]))





# def SumTotal(list): 
#     sum = 0
#     for x in range(0, len(list), 1):
#         sum += list[x]
#     return sum

# print(SumTotal([6,3,-2]))



# def Average(list):
#     sum = 0
#     for x in range(0, len(list), 1):
#         sum += list[x]
#     avg = sum / len(list)
#     return avg 

# print(Average([1,2,3,4]))


# def length(list):
#     count = 0
#     for x in range(0, len(list), 1):
#         count += 1
#     return count 

# print(length([37,2,1,-9]))


def Minimum(list):
    if len(list) == 0:
        return False
    
    