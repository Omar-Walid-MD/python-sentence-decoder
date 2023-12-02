import dict
import json
import pyperclip
from tkinter import *

words_dict = dict.get_dict()
shuffled_dict = None

def main():

    def trim_word(word):
        while not word[-1].isalpha():
            word = word[:-1]
        while not word[0].isalpha():
            word = word[1:]
        return word

    def encode(sentence):
        sentence = sentence.lower().split()
        if not len(sentence):
            return
        output = []
        for word in sentence:
            word = trim_word(word)
            if words_dict.get(word[0],False) is not False:
                try:
                    i = words_dict[word[0]].index(word)
                    output.append(shuffled_dict[word[0]][i])
                except ValueError:
                    for letter in word:
                        if letter.isalpha():
                            i = words_dict[letter].index(letter)
                            output.append(shuffled_dict[letter][i])
        result = " ".join(output)
        resultLabel.config(text="Result (Encoded)")
        resultText.delete('1.0', END)
        resultText.insert(INSERT,result)

    def decode(sentence):
        sentence = sentence.lower().split()
        if not len(sentence):
            return
        output = []
        for word in sentence:
            word = trim_word(word)
            if words_dict.get(word[0],False) is not False:
                try:
                    i = shuffled_dict[word[0]].index(word)
                    output.append(words_dict[word[0]][i])
                except ValueError:
                    continue
        result = " ".join(output)
        resultLabel.config(text="Result (Decoded)")
        resultText.delete('1.0', END)
        resultText.insert(INSERT,result)

    # while True:

    #     m = ""
    #     while m!="e" and m!="d" and m!="c":
    #         m = input("Encode (e), Decode (d), Close (c): ").lower()

    #     if m=="c":
    #         break
    #     elif m=="e":
    #         encode()
    #     elif m=="d":
    #         decode()

    def print_key(var, index, mode):
        if keyUpdateBtn['state']=="disabled":
            keyUpdateBtn['state'] = "normal"

        if shuffle_key.get()=="":
            keyUpdateBtn['state'] = "disabled"

    def set_shuffled_dict():
        global shuffled_dict

        if shuffle_key.get() == "":
            return
        
        shuffled_dict = dict.get_shuffled_dict(words_dict,int(shuffle_key.get()))
        keyUpdateBtn['state'] = "disabled"
        
        encodeBtn['state'] = "normal"
        decodeBtn['state'] = "normal"

    def clear():
        resultLabel.config(text="Result")
        resultText.delete('1.0', END)

    root = Tk()
    root.title("Shuffled Dictionary Cypher")
    root.geometry("500x335")
    root.resizable(False,False)
    root.iconbitmap("icon.ico")


    shuffle_key = StringVar()
    shuffle_key.trace_add("write",print_key)

    input_text = StringVar()
    # input_text.trace_add("write")
  
    keyFrame = Frame(root)
    keyFrame.pack(anchor="w",padx=20,pady=(20,0))

    Label(keyFrame,text="Enter Key:").pack(anchor="w",side="top")
    keyInput = Entry(keyFrame,textvariable=shuffle_key,validate="key",validatecommand=(root.register(lambda x: x.isdigit()),"%S"))
    keyInput.bind("<Return>",lambda event: set_shuffled_dict())
    keyInput.pack(side="left",padx=(0,20),ipady=2)

    keyUpdateBtn = Button(keyFrame,text="Update Key",command=set_shuffled_dict,state="disabled")
    keyUpdateBtn.pack()

    Label(text="Enter Text:",anchor="w").pack(padx=20,pady=(20,0),fill="x")
    textInput = Entry(textvariable=input_text,width=80)
    textInput.pack(padx=20,ipady=2)

    buttonsFrame = Frame(root)
    buttonsFrame.pack(anchor="w",pady=(10,20))

    encodeBtn = Button(buttonsFrame,text="Encode",state=DISABLED,command=lambda: encode(input_text.get()))
    decodeBtn = Button(buttonsFrame,text="Decode",state=DISABLED,command=lambda: decode(input_text.get()))

    encodeBtn.pack(padx=(20,0),side="left")
    decodeBtn.pack(padx=(10,0),side="right")

    resultFrame = Frame(root)
    resultFrame.pack(fill="both",expand="yes",padx=20)

    resultLabel = Label(resultFrame,text="Result:")
    resultLabel.pack(anchor="w")

    resultText = Text(resultFrame,height=4,width=55)
    resultText.pack(side="left")

    # resultScroll = Scrollbar(resultFrame,orient="vertical",command=resultText.yview)
    # resultScroll.pack(fill="y",side="right") 

    # resultText['yscrollcommand'] = resultScroll.set

    bottomButtonsFrame = Frame(root)
    bottomButtonsFrame.pack(anchor="w",pady=(10,20))

    copyBtn = Button(bottomButtonsFrame,text="Copy",command=lambda: pyperclip.copy(resultText.get('1.0',END)))
    clearBtn = Button(bottomButtonsFrame,text="Clear",command=clear)

    copyBtn.pack(padx=(20,0),side="left")
    clearBtn.pack(padx=(10,0),side="right")


    root.mainloop()

if __name__=="__main__":
    main()