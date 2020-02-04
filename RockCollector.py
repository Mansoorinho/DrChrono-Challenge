#
def get_rock_index(quantity):
    Jamie = quantity
    Ned = sorted(quantity)
    Geoffrey = [sum(x) for x in zip(Ned,Jamie)]
    lastNum = 0
    SortGeof = sorted(Geoffrey)
    #to find the max occurent quantity
    for i in SortGeof:
        num = Geoffrey.count(i)
        if num >= lastNum:
            lastNum = num
            lastFreq = i
    #to find the index of the max most occurent quantity
    quantityIndex = 0
    while quantityIndex < len(Geoffrey):
        if Geoffrey[quantityIndex] == lastFreq:
            lastIndex = quantityIndex
        quantityIndex += 1

    return lastIndex

if __name__=="__main__":
    #if you run the app on local computer comment the following line
    #fptr = open(os.environment['OUTPUT_PATH'],'w')
    #enter the number of qunatity you want to insert
    print("Enter number of qunatity you want to insert:")
    print("> " , end="")
    #2 above lines are just for clarification and is not in the question
    #container of the count of inserts
    quantity_count = int(input().strip())
    quantity = []
    #getting input of every element in the list
    print("Enter %s digits and press enter after each digit" %quantity_count)
    print("> ")
    #the 2 above lines are just for clarification
    for _ in range(quantity_count):
        quantity_item = int(input().strip())
        quantity.append(quantity_item)
    
    res = get_rock_index(quantity)

    #if you run on a local computer comment the following 2 lines
    #fptr.write(str(res) + '\n')
    #fptr.close()
    #just for clarificattion
    print("The last index of the most occurent quantity is: ", end="")
    print(str(res) + '\n')