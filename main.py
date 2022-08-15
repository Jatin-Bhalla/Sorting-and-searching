from tkinter import *
#import tkinter
window= Tk()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
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
#The basic thing about selection sort is to look at 2 consecutive values and then compare for which is bigger or smaller
#if asc: it sees 2 values compares and then tells which is smaller and swaps it with the bigger value then the same loop continues till the value it is sorted
# if the value is smaller then it compares it with the next value all the same while identifying it as minimum
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
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
def display_1():
    # .get is used to obtain the current value
    # of entry_1 widget (This is always a string)
    print(entry_1.get())

def display_2():
    num = entry_2.get()
    # Try convert a str to int
    # If unable eg. int('hello') or int('5.5')
    # then show an error.
    try:
       num = int(num)
    # ValueError is the type of error expected from this conversion
    except ValueError:
        #Display Error Window (Title, Prompt)
        showerror('Non-Int Error', 'Please enter an integer')
    else:
        print(num)

def display_3():
    # Ask Integer Window (Title, Prompt)
    # Returned value is an int
    ans = askinteger('Enter Integer', 'Please enter an integer')
    # If the user clicks cancel, None is returned
    if ans is not None:
        print(ans)
def asc(): pass
def desc(): pass
def submit(): pass
def delete():entry.delete(0,END)
def backspace():entry.delete(len(entry.get())-1 ,END)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#Basic GUI and window is made
#change the size of the window
#Width x height

window.geometry("1024x856")
window.title("Algo Analyzr")
#this will lock the max size so you can  not drag the box to increase its size
#the same thing is applicable for minsize
window.minsize(600,500)
window.maxsize(10000,10000)
#background colour
window.config(background="#C0A9BD")#enter a colour or a hex value
#----------------
# Entry widget =textbox to accept an input from the user

entry= Entry (window,font=("Arial",50))
entry.pack(side=LEFT )
# ------------------
entry_1 = tk.Entry(window)
btn_1 = tk.Button(window, text = "Display Text", command = display_1)

entry_2 = tk.Entry(window)
btn_2 = tk.Button(window, text = "Display Integer", command = display_2)

btn_3 = tk.Button(window, text = "Enter Integer", command = display_3)

# Grid is used to add the widgets to window
# Alternatives are Pack and Place
entry_1.grid(row = 0, column = 0)
btn_1.grid(row = 1, column = 0)
entry_2.grid(row = 0, column = 1)
btn_2.grid(row = 1, column = 1)

btn_3.grid(row = 2, column = 0)
btn_4.grid(row = 2, column = 1)
#-------------------
# BUTTONS= performs a specific funtion given by the command or linked using it
backspace_button =Button(window,text='backspace',command = backspace)
backspace_button.pack(side=RIGHT)

delete_button =Button(window,text='DELETE',command =delete)
delete_button.pack(side=RIGHT)

submit_button =Button(window,text='SUBMIT',command = submit)
submit_button.pack(side=RIGHT)


# -------------------
#add an image to the project folder and link them
icon = PhotoImage(file='logo.png')
window.iconphoto(True,icon)
#label is aarea holding image or text
inpt= Label(window,
            text="Input",
            font=('Arial',16,'bold'),
            fg='',""" text colour"""
            bg=''  """colour of the baground behind text"""
            )
#https://www.color-hex.com/
#colour value in hexadecimal
inpt.pack()

#button: click it and it does action
button =Button.(window,
                text="Input",
                command =click,
                font=("Arial",16,'bold'),
                fg='',""" text colour"""
                bg=''  """colour of the baground behind text""",
                activeforeground="#00FF00",
                activebackground="BLACK"
                state =ACTIVE )
button.pack()
#------------------------------------------------------------------------------------------------------------
#check buttons
#probably add fg and bg colour and active foreground and active background

linear_button = Checkbutton(window, text = "LINEAR", variale ="x" , onvalue =1 , offvalue =0 , command=linear_search ,font =('Arial',15) ) 
linear_button.pack(side=LEFT)

binary_button = Checkbutton(window, text = "BINARY", variale ="X" , onvalue =1 , offvalue =0 , command= binary_search,font =('Arial',15) ) 
binary_button.pack(side=LEFT)

quick_button = Checkbutton(window, text = "QUICK", variale ="x" , onvalue =1 , offvalue =0 , command= quick_sort,font =('Arial',15) ) 
quick_button.pack(side=RIGHT)

bubble_button = Checkbutton(window, text = "BUBBLE", variale ="x" , onvalue =1 , offvalue =0 , command=bubble_sort,font =('Arial',15) ) 
bubble_button.pack(side=RIGHT)

select_button = Checkbutton(window, text = "SELECT", variale ="x" , onvalue =1 , offvalue =0 , command= selection_sort,font =('Arial',15) ) 
select_button.pack(side=RIGHT)
#------------------------------------------------------------------------------------------------------------
window.mainloop()  # this will place window on screen and also look for events in it
