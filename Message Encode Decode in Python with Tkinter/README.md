***Message Encode-Decode Python Project***
In this project, users have to enter the message to encode or decode. Users have to select the mode to choose the encoding and decoding process. 
The same key must be used to process the encoding and decoding for the same message.

***Project Prerequisites***
Tkinter is a standard GUI python library.
Base64 module provides a function to encode the binary data to ASCII characters and decode that ASCII characters back to binary data.

***Project File Structure***
These are the step to build message encode – decode python project

**Import module**
The first step is to import tkinter and base64 libraries.

**Create display window**
root is the name which we refer to our window.
text which we display on the label.
font in which the text is written.
pack organized widget in block.

**Define function**
Text variable stores the message to encode and decode.
private_key variable store the private key used to encode and decode.
mode is used to select that is either encoding or decoding.
Result store the result.

*Function to encode*
enc = [] is an empty list.
We run loop till the length of the message.
i% of len(key) gives the remainder of division between i and len(key) and that remainder used as an index of key the value of key at that index is stored in key_c.
ord (message[i]) convert the value of message at index i into the integer value.
ord(key_c) converts the key_c value to integer value.
ord(message[i]) + ord(key_c)) % 256 gives the remainder of division of addition of ord(message[i]) and ord( key_c) with 256 and passes that remainder to chr() function.
base64.urlsafe_b64encode encode a string.
return gives the result of the encoded string.

*Function to Decode*
dec=[] is an empty list
Decode the content from input and write the result in binary to the output.
We ran the loop till the length of the message.
256 + ord(message[i]) – ord(key_c)) % 256 gives the remainder of addition of 256 with subtraction of ord(message[i]) – ord( key_c) and then division with 256 and passes that remainder to chr() function.
return “”.join(dec) return the result.

*Function to set mode*
If the mode set by the user is ‘e’ then the Encode() function will be called.
If the mode set to ‘d‘ then the Decode() function will be called.
Else print ‘invalid mode’.
private_key.get() and Text.get() values are pass to the arguments of Encode() and Decode() function.

*Function to exit window*
root.destroy() will quit the program by stopping the mainloop().

*Function to reset window*
This function set all variables to empty string.

**Define labels and buttons**
root is the name which we refer to our window.
text which we display on the label.
font in which the text is written.
insertwidth use to set the width of the insertion cursor.
bg sets the background colour.
command is call when the button is click.
textvariable used to retrieve the current text to the entry widget.
root.mainloop() is a method that executes when we want to run our program.
