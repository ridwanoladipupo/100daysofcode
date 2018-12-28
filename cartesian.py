# A Python program for cartesian product
# function to find cartesian product of two sets  

def cartProduct(set_a, set_b): 

    result =[] 

    for i in range(0, len(set_a)): 

        for j in range(0, len(set_b)): 

            # for handling case having cartesian 

            # prodct first time of two sets 

            if type(set_a[i]) != list:          

                set_a[i] = [set_a[i]] 


            # coping all the members 
            # of set_a to temp 

            temp = [fig for fig in set_a[i]] 
            # add member of set_b to  
            # temp to have cartesian product      

            temp.append(set_b[j])              

            result.append(temp)   

    return result 

  
# Function to do a cartesian  
# product of N sets  

def Cartesian(list_a, n):
    # result of cartesian product 
    # of all the sets taken two at a time 
    
    temp = list_a[0] 
    # do product of N sets  
    for i in range(1, n): 
        temp = cartProduct(temp, list_a[i]) 

    print(temp) 

list_a = [[1, 2, 3], ['B'],['x', 'y', 'z']]   

            
# number of sets 

n = len(list_a)  

    
# Calling function to find the cartesian product on list_a of size n  
Cartesian(list_a, n) 
