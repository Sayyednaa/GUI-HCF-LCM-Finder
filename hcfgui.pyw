from tkinter import*
import hcf
from tkinter import messagebox



class Main_Code:
    def __init__(self,root):
        self.root=root
        self.root.geometry("550x300")
        self.root.title("HCF/GCD Finder")

        # Labels

        title=Label(self.root,text="HCF/GCD Finder",font=("times new roman",30),bg="green",fg="white").place(x=0,y=0,relwidth=1)
        title2=Label(self.root,text="Developer: Sayyed Nawab Abdul Ali\n Github:- https://github.com/Sayyednaa/GUI-Hcf-Finder",font=("times new roman",10),).place(x=0,y=50,relwidth=1)
       

        number1=Label(self.root,text="Enter First Number:",font=("times new roman",15)).place(x=25,y=100)
        number2=Label(self.root,text="Enter Second Number:",font=("times new roman",15)).place(x=25,y=130)

        self.Fnumber=Entry(root,font=("times new roman",16))
        self.Fnumber.place(x=250,y=100)



        self.Snumber=Entry(root,font=("times new roman",16))
        self.Snumber.place(x=250,y=130)
        self.btn_Button=Button(self.root,bg="white",text="Find",font=("Impact",15),command=self.Generate)
        self.btn_Button.place(x=250,y=180)

    def callback(url):
        webbrowser.open_new(url)  

    def Generate(self):
        
       
        self.x=self.Fnumber.get()
        self.y=self.Snumber.get()
       
        if self.x or self.y is not int:
            self.Error=Label(self.root,text="Enter  Integers(Numbers)",fg="red",font=("times new roman",25,"bold"))
            self.Error.place(x=0,y=250,relwidth=1)
       
            
        x=int(self.Fnumber.get())
        y=int(self.Snumber.get())

        Result=hcf.compute_hcf(x,y)
        Text=(f'The Hcf Of {x} and {y} is {Result}')
            
           

        Ressultpr=Label(self.root,text=Text,fg="green",font=("times new roman",25,"bold")).place(x=0,y=250,relwidth=1)




root=Tk()
obj=Main_Code(root)
root.mainloop()
