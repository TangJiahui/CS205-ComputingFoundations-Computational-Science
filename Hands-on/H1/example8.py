def square(n): 
    return (n*n) 

if __name__ == "__main__": 
    # input list 
    mylist = [1, 2, 3, 4, 5] 
    
    # empty list to store result 
    result = [] 
    
    for num in mylist: 
        result.append(square(num)) 
    
    print(result) 
