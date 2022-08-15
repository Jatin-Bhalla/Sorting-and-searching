from tkinter import *

window = Tk()
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#BASIC functions
def asc():pass
def desc():pass
def submit():pass
def submit_query():pass
def delete():inptt.delete(0,END)
def backspace():inptt.delete(len(entry.get())-1 ,END)
def delete_exit():outptt.delete(0,END)
def delete_query():query.delete(0,END)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# DSA funcitons
def linear_search(arr, x):
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
  #we input an array (list) and an int value to search through the list of numbers
  #we give l as th left most value as 0 of the index
  # r is the right most value in the list but because the indexing is from 0  and the list length does not start from 0 so teo
  # even out the end value to match the indexing value which is n+1 we sub 1 from the right most value to match the index value
def binary_search(arr , target):
  l=0
  r=arr.length-1 
  #len(arr)-1
 # for the binary search we go to the middle most value of the list to check if target is there
  while l<=r: m=(l+r)/2
 # if that is the target we use its value as the output of the function
  if arr[m]==target: return m
 #otherwise
# L--------M---------R# L<-----(T<M)---->M<------(T>M)---->R
  if target<arr[m]:r=m-1
    #L<------>r-M______R
  else: l=m+1    #L_____M-l<----->R
  return -1
#IF NONE THEN RETURN
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
def selection_sort(array, size):
    #array name , size of the array
    for value in range(size):
          #usually the first value is pointed min
        min_index = value
 
        for j in range(value + 1, size):
          # value+1 is used cuz in loops iteration the value needs to exceed till the point it is equal to size for termination of the loop
            # select the minimum element in every iteration
            # Ascending order :   >
            # Descending order:   <      
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (array[value], array[min_index]) = (array[min_index], array[value])
          #this is a basic swap code piece(x,y)=(y,x) 
          #the akshay kumar meme
# time complexity O(n*n)  #sorting by finding min_index#The basic thing about selection sort is to look at 2 consecutive values and then compare for which is bigger or smaller#if asc: it sees 2 values compares and then tells which is smaller and swaps it with the bigger value then the same loop continues till the value it is sorted# if the value is smaller then it compares it with the next value all the same while identifying it as minimum
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
def bubble_sort(array):
  #instead of n or another variable with len(array) we directly use it
  # honestly it is less confusing when you read code
  # loop to access each array element # loop for the iteration .... n elements
  for i in range(len(array)):
    # loop to compare array elements ...n-1-i comparisons for where i slowly equals n-1
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        (array[j] , array[j + 1])=(array[j + 1],array[j])
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#QUICK SORT
def partition(array, l, r):

  # choose the rightmost element as pivot
  pivot = array[r]
  # pointer for greater element
  i = l - 1
  # traverse through all elements
  # compare each element with pivot
  for j in range(l, r):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1
      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[r]) = (array[r], array[i + 1])

  # return the position from where partition is done
  return i + 1
   
def quick_sort(array , l ,r):
     if  l>=r:return 
     p=partition(array ,l,r)
     Quick_Sort(array ,l,p-1)
     Quick_Sort(array,p+1,r)
     # well think of quick aort a bit like divide and conquer ! well conquer the problem
     #break the array into 2 sub arrays and a centre 'pivot' 
      # one array is consisting of values>pivot
      # another has values < pivot
 # now call the same funciton to  do the same  on both and further and further till a sorted array forms.
#there will be 2 functions used here
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#add an image to the project folder and link them
icon = PhotoImage(file='logo.png')
window.iconphoto(True,icon)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

window.geometry("644x344")
window.title("Algo Analyzr")
Label(window, text="Search and Sort", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

#Text for our form
inptt = Label(window, text="INPUT ")
outptt= Label(window, text="ENTER QUERY")
query = Label(window, text="OUTPUT")
# time_taken= Label(window, text="TIME TAKEN")
# complexity = Label(window, text="O()")

#Pack text for our form
inptt.grid(row=1, column=2)
outptt.grid(row=2, column=2)
query.grid(row=3, column=2)
# time_taken.grid(row=4, column=2)
# comparisons.grid(row=5, column=2)

# Tkinter variable for storing entries
inpttvalue = IntVar()
outpttvalue = IntVar()
queryvalue = IntVar()
# time_takenvalue = DoubleVar()
# complexityevalue = StringVar()
inputtbackspace = StringVar()
inputtdelete = StringVar()
inputtsubmit = StringVar()
exitdelete = StringVar()
querydelete = StringVar()
querysubmit = StringVar()



#Entries for our form
inpttentry = Entry(window, textvariable=inpttvalue)
outpttentry = Entry(window, textvariable=outpttvalue)
queryentry = Entry(window, textvariable=queryvalue)
# time_takenentry = Entry(window, textvariable=time_takenvalue)
# complexityentry = Entry(window, textvariable=complexityevalue)

# Packing the Entries
inpttentry.grid(row=1, column=3)
outpttentry.grid(row=2, column=3)
queryentry.grid(row=3, column=3)
# time_takenentry.grid(row=4, column=3)
#  complexityentry.grid(row=5, column=3)

#Checkbox & Packing

backspace_button =Button(window,text='BACKSPACE',command = backspace,bg ="#F2E9EB",fg="#647295")
backspace_button.grid( row=6, column=3)

delete_button =Button(window,text='DELETE',command = delete, bg ="#F2E9EB",fg="#647295")
delete_button.grid( row=6, column=6)

submit_button =Button(window,text='SUBMIT',command = submit, bg ="#F2E9EB",fg="#647295")
submit_button.grid(row=6, column=9)

delete_exit_button =Button(window,text='DELETE',command = delete_exit, bg ="#F2E9EB",fg="#647295")
delete_exit_button.grid( row=7, column=3)

delete_query_button =Button(window,text='DELETE',command = delete_query, bg ="#F2E9EB",fg="#647295")
delete_query_button.grid( row=7, column=6)

query_button =Button(window,text='RUN QUERY',command = submit_query, bg ="#F2E9EB",fg="#647295")
query_button.grid(row=7, column=9)
# --------------------
#Button & packing it and assigning it a command
# Button(text="Submit to Harry Travels", ).grid(row=7, column=3)



window.mainloop()
