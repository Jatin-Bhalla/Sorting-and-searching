from tkinter import *
#import tkinter
root= Tk()
#Basic GUI and root is made
#GUI LOGIC
#Width x height

#root.geometry(" 4195x61681")
#root.minsize("400x400")
# root.maxsize("10000x10000")
#this will lock the max size so you can  not drag the box to increase its size
#the same thing is applicable for minsize
inpt= Label (text="input")
inpt.pack()

root.mainloop()
#this is an iterative approach for linear search
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
def Linear_search(arr, x):
     for i in range(len(arr)):
         if arr[i] == x:
            return i
          #return arr[i]
 
    return -1
#----  ------ ------ ----- ----- ---- ----- ---- ---- ---- ---- ---- ----- ----- ----- ----- ----- ----- ----- ----- ---- ----- ---- ----- ----- ----- ---- ---- 
""" # another linear search code:
def linear_search(arr,n,t):
    for i in range (0,n):
        if(arr[i]==k):
            return i
            #returnarr[i]
    return -1
    """
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
def binary_search(arr , target):
  #we input an array (list) and an int value to search through the list of numbers
  #we give l as th left most value as 0 of the index
  # r is the right most value in the list but because the indexing is from 0  and the list length does not start from 0 so teo
  # even out the end value to match the indexing value which is n+1 we sub 1 from the right most value to match the index value
  l=0
  r=arr.length-1 
  #len(arr)-1
 # for the binary search we go to the middle most value of the list to check if target is there
  while l<=r: m=(l+r)/2
 # if that is the target we use its value as the output of the function
  if arr[m]==target: return m
 #otherwise
# L--------M---------R
# L<-----(T<M)---->M<------(T>M)---->R
  if target<arr[m]:r=m-1
    #L<------>r-M______R
  else: l=m+1
    #L_____M-l<----->R
  return -1
#IF NONE THEN RETURN
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
# time complexity O(n*n)
#sorting by finding min_index
def selectionSort(array, size):
    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
