#def missingelement(arr,n):
 #   for i in range (1,len(1,n)):
#        if i not in arr:
#            return 1       
#n=int(input("enter the input"))      
#if 1 < n <10 ** 6:
#    arr=(input("enter array").split())
#    arr = [int(x) for x in arr]
#    for x in arr:
#    arr(list)
    

#---2----#
#def repeat(n):
 #   arr=[]
  #  n=int(input("enter the value"))

#def find_repeated(arr):
 #   repeated_nums = []
 #   for num in arr:
 #       if arr.count(num) > 1 and num not in repeated_nums:
  #          repeated_nums.append(num)
 #   if repeated_nums:
 #       return repeated_nums
  #  else:
  #      return -1
#arr = [9, 8, 2, 6, 1, 8, 5, 3, 4, 7]
#print(find_repeated(arr))


#--3--#
#n=int(input("enter the value"))
#for i in range(1,n+1):
#    sum=sum+1
#    print("sum",sum)


#--4---#
#def find_second_largest(arr):
    # Check if the array has less than 2 elements
#    if len(arr) < 2:
#        return -1
    
    # Convert the array to a set to remove duplicates, then back to a sorted list
#    unique_arr = sorted(set(arr))
    
    # If there is only one unique element, return -1
#    if len(unique_arr) < 2:
#        return -1
    
    # Return the second largest element
#    return unique_arr[-2]

# Example usage
#arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))
#result = find_second_largest(arr)
#print("The second largest element is:", result)


#--5--#
#def fun(i,n):
#   if i>n:
#       return
#   else:
#       print(i,end=" ")
#       fun(i+1,n)
#n=int(input("Number"))
#fun(1,n)


#--6--#
#arr = []
#n=int(input("enter the value"))
#if 1<=n <= 10 ** 6:
#    for i 


#--7--#
#given an array arr[] of n integer 
#check whether it contains  a triplet that sums up to d zero 
#nt:return 1,if there is at atleast one triplet following d conition else return 0
#ex1:input n=5,  arr[]={0,-1,2,-3,1} , output:1 , explanation:0,-1 and 1 forms a triplet wid sum equal to 0.
#ex2:input n=3,  arr[]={1,2,3} , output:0 , explanation:no triplet wid zero sum exists .
#yout task : u don't need to read input or print anything
#your task is to complete d boolean fun find Triplets() which takes d array arr[] and d size of d array (n) as inputs and 
#print 1 if d fun returns true else print 0
#if d fun returns false

def findTriplets(arr, n):
    # Sort the array
    arr.sort()
    
    # Traverse the array
    for i in range(n - 2):
        # Initialize two pointers
        left = i + 1
        right = n - 1
        
        # Check for the triplet
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == 0:
                return 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    
    # If no triplet with zero sum found
    return 0

# Example usage:
n1 = 5
arr1 = [0, -1, 2, -3, 1]
print(findTriplets(arr1, n1))  # Output: 1

n2 = 3
arr2 = [1, 2, 3]
print(findTriplets(arr2, n2))  # Output: 0
