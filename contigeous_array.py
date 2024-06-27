'''program to find the max of sum of 4 numbers (example list=[-2,0,2,4] find max of sum 2 numbers
the answer would be 4 -->2+4=6,-2+2=0,etc)'''
'''You are competing in a basketball contest. In this contest the score for each 
successful shot depends on both the distance from the basket and the player's 
position. The ball is shot N times, successfully. You are given an array A containing the 
distance of a player from basket for N shots. The index of array represents 
the position of the player. Score is calculated by multiplying the position with the 
distance from the basket.
Your task is to find and return an integer value, representing the maximum possible 
score you can achieve by choosing a contiguous subarray of size K from the given 
array.
Given: 
K=3
A=[4,3,2,7,1,9]'''



def max_sum(array,number):
    narray=len(array)
    if number>narray:
        return 'subarray of size greater than the array isnot possible'
    current_sum=sum(array[:number])
    max_sum=float('-inf')
    for i in range(1,narray-number+1):
        current_sum=current_sum-array[i-1]+array[i+number-1]
        max_sum=max(max_sum,current_sum)
    return max_sum


array1=[4,3,2,7,1,9]
number=3
print(max_sum(array1,number))


