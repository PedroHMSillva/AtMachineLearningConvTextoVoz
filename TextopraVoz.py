from tkinter import *

from pydub import AudioSegment

from pydub.playback import play

from gtts import gTTS



root = Tk()
root.geometry('720x500')
root.resizable(0, 0)
root.config(bg='ghost white')
root.title('SOFTWARE DE TEXTO PARA VOZ')

Label(root, text='CONVERSOR DE TEXTO PARA VOZ', font='arial 20 bold', bg='white smoke').pack()
Label(root, text='PROJETO IA', font='arial 15 bold', bg='white smoke').pack(side=BOTTOM)

Label(root, text='Digite o texto:', font='arial 15 bold', bg='white smoke').place(x=20, y=60)

Msg = StringVar()

entry_field = Entry(root, textvariable=Msg, width='60')
entry_field.place(x=20, y=100)


def Text_to_Speech():
    Message = entry_field.get()
    speech = gTTS(text=Message, lang='PT-BR')
    speech.save('projetoia.mp3')
    speech = AudioSegment.from_mp3("projetoia.mp3")
    play(speech)
    
    
def Sair():
    root.destroy()
Button(root, text="SAIR", font='arial 15 bold', command=Sair, bg='Red').pack(side=BOTTOM, fill=BOTH)

def Apagar():
    Msg.set("")
Button(root, text="APAGAR", font='arial 15 bold', command=Apagar, bg='Yellow').pack(side=BOTTOM, fill=BOTH)
Button(root, text="INICIAR", font='arial 15 bold', command=Text_to_Speech, bg='Green').pack(side=BOTTOM, fill=BOTH)


root.mainloop()






#Button(root, text="INICIAR", command=Text_to_Speech)
#Button(root, text="SAIR", command=Sair, bg='Orange')
#Button(root, text="REINICIAR", command=Reiniciar).place()



#Msg = StringVar()

#entry_field = Entry(root, textvariable=Msg, width='60')
#entry_field.place(x=20, y=100)


#def Text_to_Speech():
    #Message = entry_field.get()
    #speech = gTTS(text=Message)
    #speech.save('projetoia.mp3')
    #playsound('projetoia.mp3')


#def Sair():
    #root.destroy()


#def Reiniciar():
   # Msg.set("")


#Button(root, text="COMEÇAR", font='arial 15 bold', command=Text_to_Speech)
#Button(root, text="SAIR", font='arial 15 bold', command=Sair, bg='Orange')
#Button(root, text="REINICIAR", font='arial 15 bold', command=Reiniciar).place()

