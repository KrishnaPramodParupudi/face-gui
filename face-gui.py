from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageDraw
from PIL import ImageTk
import face_recognition
import math

def eye_masking():
    global panelA,panelB
    path = filedialog.askopenfilename()
    if(len(path)>0):
        image = face_recognition.load_image_file(path)
        face_landmarks_list = face_recognition.face_landmarks(image)
        picture = Image.fromarray(image)
        pil_image = Image.fromarray(image)
        d = ImageDraw.Draw(pil_image)
        for face_landmarks in face_landmarks_list:
            le = face_landmarks.get('left_eye')
            re = face_landmarks.get('right_eye')
            x1 = le[1][0] 
            x2 = le[4][0] 
            y1 = le[1][1] 
            y2 = le[4][1] 
            dist = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
            d.line((le[0],re[3]),width=int(dist)+1)
        image = ImageTk.PhotoImage(picture)
        output_image = ImageTk.PhotoImage(pil_image)
    if panelA is None or panelB is None:
        panelA = Label(image=image)
        panelA.image=image
        panelA.pack(side="left",padx=10,pady=10)
        panelB = Label(image=output_image)
        panelB.image=output_image
        panelB.pack(side="right",padx=10,pady=10)
    else:
        panelA.configure(image=image)
        panelB.configure(image=output_image)
        panelA.image=image
        panelB.image=output_image

def facial_features():
    global panelA,panelB
    path = filedialog.askopenfilename()
    if(len(path)>0):
        image = face_recognition.load_image_file(path)
        face_landmarks_list = face_recognition.face_landmarks(image)
        picture = Image.fromarray(image)
        pil_image = Image.fromarray(image)
        d = ImageDraw.Draw(pil_image)
        for face_landmarks in face_landmarks_list:
          for facial_feature in face_landmarks.keys():
             d.line(face_landmarks[facial_feature],width=5) 
        image = ImageTk.PhotoImage(picture)
        output_image = ImageTk.PhotoImage(pil_image)
    if panelA is None or panelB is None:
        panelA = Label(image=image)
        panelA.image=image
        panelA.pack(side="left",padx=10,pady=10)
        panelB = Label(image=output_image)
        panelB.image=output_image
        panelB.pack(side="right",padx=10,pady=10)
    else:
        panelA.configure(image=image)
        panelB.configure(image=output_image)
        panelA.image=image
        panelB.image=output_image   

root = Tk()
T = Text(root,height=2,width=30)
T.pack()
T.insert(END,"Select the operation you want to perform")
panelA = None
panelB = None
btn1 = Button(root,text="Eye Masking",command=eye_masking)
btn1.pack(side="bottom",fill="both",expand="yes",padx="10",pady="10")
btn2 = Button(root,text="Facial Features",command=facial_features)
btn2.pack(side="bottom",fill="both",expand="yes",padx="10",pady="10")
root.mainloop()
