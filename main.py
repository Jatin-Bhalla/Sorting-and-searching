from tkinter import *
#import tkinter
root= Tk()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
def Linear_Search(arr, x):
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
def Binary_Search(arr , target):
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
def SelectionSort(array, size):
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
def Bubble_Sort():pass
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
def Quick_Sort():pass
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
def Submit(): pass
def Delete():entry.delete(0,END)
def Backspace():entry.delete(len(entry.get())-1 ,END)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#Basic GUI and window is made
#change the size of the window
#Width x height

window.geometry(" 1024x 856")
window.title("Algo Analyzr")
#this will lock the max size so you can  not drag the box to increase its size
#the same thing is applicable for minsize
window.minsize("733x434")
window.maxsize("10000x10000")
#background colour
window.config(background="")#enter a colour or a hex value
#----------------
# Entry widget =textbox to accept an input from the user

entry= Entry (window,font=("Arial",50))
entry.pack(side=LEFT )
# ------------------
# BUTTONS= performs a specific funtion given by the command or linked using it
backspace_button =Button(window,text='backspace',command = Backspace)
backspace_button.pack(side=RIGHT)

delete_button =Button(window,text='DELETE',command = Delete)
delete_button.pack(side=RIGHT)

submit_button =Button(window,text='SUBMIT',command = Submit)
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

linear_button = Checkbutton(window, text = "LINEAR", variale ="x" , onvalue =1 , offvalue =0 , command=Linear_Search ,font =('Arial',15) ) 
linear_button.pack(side=LEFT)

binary_button = Checkbutton(window, text = "BINARY", variale ="X" , onvalue =1 , offvalue =0 , command= Binary_Search,font =('Arial',15) ) 
binary_button.pack(side=LEFT)

quick_button = Checkbutton(window, text = "QUICK", variale ="x" , onvalue =1 , offvalue =0 , command= Quick_Sort,font =('Arial',15) ) 
quick_button.pack(side=RIGHT)

bubble_button = Checkbutton(window, text = "BUBBLE", variale ="x" , onvalue =1 , offvalue =0 , command=Bubble_Sort,font =('Arial',15) ) 
bubble_button.pack(side=RIGHT)

select_button = Checkbutton(window, text = "SELECT", variale ="x" , onvalue =1 , offvalue =0 , command= Selection_Sort,font =('Arial',15) ) 
select_button.pack(side=RIGHT)
#------------------------------------------------------------------------------------------------------------
window.mainloop()  # this will place window on scree and also look for events in it
