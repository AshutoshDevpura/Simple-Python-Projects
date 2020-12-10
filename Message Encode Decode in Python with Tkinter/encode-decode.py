##importing modules

from tkinter import *
import base64

##initialize window

#Tk() initialized tkinter which means window created
root = Tk()
root.geometry('500x300')
#resizable(0,0) set the fixed size of the window
root.resizable(0,0)

##title of the window

#title() set the title of the window
root.title("Ashutosh Devpura - Message Encode and Decode")



##label

#Label() widget use to display one or more than one line of text that users aren’t able to modify.
Label(root, text ='ENCODING / DECODING USING PYTHON', font = 'Helvetica 20 bold').pack()
Label(root, text ='BY ASHUTOSH DEVPURA', font = 'Helvetica 20 bold').pack(side =BOTTOM)


##define variables

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()


#######define function#####

#function to encode

def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        #ord() function takes string argument of a single unicode character and return its integer unicode value.
        #chr() function converts that integer value to string and store to enc.
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
     #The join() method joins each element of list, string, and tuple by a string separator and returns the concatenated string.
     #encode() method returns utf-8 encoded message of the string.
     #decode() method decodes the string.   
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

#function to decode

def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        #chr() function convert integer value to string and store to dec
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
        
    return "".join(dec)

#function to set mode

def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')



#Function to exit window
        
def Exit():
    root.destroy()


#Function to reset
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")


#################### Label and Button #############

#Label() widget use to display one or more than one line of text that users aren’t able to modify.
#Entry() widget used to create an input text field.
#Message
Label(root, font= 'Helvetica 12 bold', text='MESSAGE').place(x= 60,y=60)
Entry(root, font = 'Helvetica 10', textvariable = Text, bg = 'ghost white').place(x=290, y = 60)

#key
Label(root, font = 'Helvetica 12 bold', text ='KEY').place(x=60, y = 90)
Entry(root, font = 'Helvetica 10', textvariable = private_key , bg ='ghost white').place(x=290, y = 90)


#mode
Label(root, font = 'Helvetica 12 bold', text ='MODE' + '\n( e-encode / d-decode)').place(x=10, y = 120)
Entry(root, font = 'Helvetica 10', textvariable = mode , bg= 'ghost white').place(x=290, y = 120)



#result
Entry(root, font = 'Helvetica 10 bold', textvariable = Result, bg ='ghost white').place(x=290, y = 155)

######result button
#Button() widget used to display button on our window
Button(root, font = 'Helvetica 10 bold', text = 'RESULT'  ,padx =2,bg ='LightGray' ,command = Mode).place(x=60, y = 160)


#reset button
Button(root, font = 'Helvetica 10 bold' ,text ='RESET' ,width = 6, command = Reset,bg = 'LimeGreen', padx=2).place(x=160, y = 200)

#exit button
Button(root, font = 'Helvetica 10 bold',text= 'EXIT' , width = 6, command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=260, y = 200)
root.mainloop()
