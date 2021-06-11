from tkinter import *
from PIL import ImageTk,Image
import matlab.engine

eng = matlab.engine.start_matlab()

font11 = "-family Arial -size 19 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"
font12 = "-family Arial -size 12 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"
font14 = "-family Arial -size 15 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"
font15 = "-family Arial -size 12 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"

root = Tk()
TFrame1 = Frame(root)
TFrame1.place(relx=0.01, rely=0.02, relheight=0.94, relwidth=0.48)
TFrame1.configure(relief=GROOVE)
TFrame1.configure(borderwidth="2")
TFrame1.configure(relief=GROOVE)
TFrame1.configure(width=465)

TLabel = Label(TFrame1)
TLabel.place(relx=0.3, rely=0.04, height=38, width=350)
TLabel.configure(background="#d9d9d9")
TLabel.configure(foreground="#000000")
TLabel.configure(font=font11)
TLabel.configure(relief=FLAT)
TLabel.configure(text='''Enter Patient's data ''')

#--------------------------------INPUT 1-------------------------------
TLabel1 = Label(TFrame1)
TLabel1.place(relx=0.02, rely=0.15, height=39, width=150)
TLabel1.configure(background="#d9d9d9")
TLabel1.configure(foreground="#000000")
TLabel1.configure(font=font12)
TLabel1.configure(relief=FLAT)
TLabel1.configure(text='''Clump Thickness''')

TEntry_Clump = Entry(TFrame1)
TEntry_Clump.place(relx=0.24, rely=0.15, relheight=0.05, relwidth=0.53)
TEntry_Clump.configure(width=246)
TEntry_Clump.configure(takefocus="")
TEntry_Clump.configure(cursor="ibeam")

#---------------------------------INPUT 2-------------------------------
TLabel2 = Label(TFrame1)
TLabel2.place(relx=0.02, rely=0.24, height=39, width=150)
TLabel2.configure(background="#d9d9d9")
TLabel2.configure(foreground="#000000")
TLabel2.configure(font=font12)
TLabel2.configure(relief=FLAT)
TLabel2.configure(text='''Uniformity Cell Size''')

TEntry_UCellSize = Entry(TFrame1)
TEntry_UCellSize.place(relx=0.24, rely=0.24, relheight=0.05, relwidth=0.53)
TEntry_UCellSize.configure(width=246)
TEntry_UCellSize.configure(takefocus="")
TEntry_UCellSize.configure(cursor="ibeam")

#---------------------------------INPUT 3-------------------------------

TLabel3 = Label(TFrame1)
TLabel3.place(relx=0.02, rely=0.33, height=39, width=150)
TLabel3.configure(background="#d9d9d9")
TLabel3.configure(foreground="#000000")
TLabel3.configure(font=font12)
TLabel3.configure(relief=FLAT)
TLabel3.configure(text='''Uniformity Cell Shape''')

TEntry_UCellShape = Entry(TFrame1)
TEntry_UCellShape.place(relx=0.24, rely=0.33, relheight=0.05, relwidth=0.53)
TEntry_UCellShape.configure(width=246)
TEntry_UCellShape.configure(takefocus="")
TEntry_UCellShape.configure(cursor="ibeam")

#----------------------------------------INPUT 4----------------------------------

TLabel4 = Label(TFrame1)
TLabel4.place(relx=0.02, rely=0.41, height=39, width=150)
TLabel4.configure(background="#d9d9d9")
TLabel4.configure(foreground="#000000")
TLabel4.configure(font=font12)
TLabel4.configure(relief=FLAT)
TLabel4.configure(text='''Marginal Adhesion''')

TEntry_MarAdh = Entry(TFrame1)
TEntry_MarAdh.place(relx=0.24, rely=0.41, relheight=0.05, relwidth=0.53)
TEntry_MarAdh.configure(width=246)
TEntry_MarAdh.configure(takefocus="")
TEntry_MarAdh.configure(cursor="ibeam")

#-----------------------------INPUT 5-----------------------------------------

TLabel5 = Label(TFrame1)
TLabel5.place(relx=0.02, rely=0.5, height=39, width=150)
TLabel5.configure(background="#d9d9d9")
TLabel5.configure(foreground="#000000")
TLabel5.configure(font=font12)
TLabel5.configure(relief=FLAT)
TLabel5.configure(text='''Single Epi Cell Size''')

TEntry_EpiCellSize =Entry(TFrame1)
TEntry_EpiCellSize.place(relx=0.24, rely=0.5, relheight=0.05, relwidth=0.53)
TEntry_EpiCellSize.configure(width=246)
TEntry_EpiCellSize.configure(takefocus="")
TEntry_EpiCellSize.configure(cursor="ibeam")

#-----------------------------INPUT 6--------------------------------------

TLabel6 = Label(TFrame1)
TLabel6.place(relx=0.02, rely=0.61, height=39, width=150)
TLabel6.configure(background="#d9d9d9")
TLabel6.configure(foreground="#000000")
TLabel6.configure(font=font12)
TLabel6.configure(relief=FLAT)
TLabel6.configure(text='''Bare Nuclei''')

TEntry_Bare = Entry(TFrame1)
TEntry_Bare.place(relx=0.24, rely=0.61, relheight=0.05, relwidth=0.53)
TEntry_Bare.configure(width=246)
TEntry_Bare.configure(takefocus="")
TEntry_Bare.configure(cursor="ibeam")

#-----------------------------INPUT 7------------------------------------

TLabel7 = Label(TFrame1)
TLabel7.place(relx=0.02, rely=0.70, height=39, width=150)
TLabel7.configure(background="#d9d9d9")
TLabel7.configure(foreground="#000000")
TLabel7.configure(font=font12)
TLabel7.configure(relief=FLAT)
TLabel7.configure(text='''Bland Chromatin''')

TEntry_Chromatin = Entry(TFrame1)
TEntry_Chromatin.place(relx=0.24, rely=0.70, relheight=0.05, relwidth=0.53)
TEntry_Chromatin.configure(width=246)
TEntry_Chromatin.configure(takefocus="")
TEntry_Chromatin.configure(cursor="ibeam")

#---------------------------INPUT 8----------------------------------------

TLabel8 = Label(TFrame1)
TLabel8.place(relx=0.02, rely=0.79, height=39, width=150)
TLabel8.configure(background="#d9d9d9")
TLabel8.configure(foreground="#000000")
TLabel8.configure(font=font12)
TLabel8.configure(relief=FLAT)

TLabel8.configure(text='''Normal Nucleoli''')

TEntry_Normal = Entry(TFrame1)
TEntry_Normal.place(relx=0.24, rely=0.79, relheight=0.05, relwidth=0.53)
TEntry_Normal.configure(width=246)
TEntry_Normal.configure(takefocus="")
TEntry_Normal.configure(cursor="ibeam")

#---------------------------------INPUT 9-------------------------------
TLabel9 = Label(TFrame1)
TLabel9.place(relx=0.02, rely=0.88, height=39, width=150)
TLabel9.configure(background="#d9d9d9")
TLabel9.configure(foreground="#000000")
TLabel9.configure(font=font12)
TLabel9.configure(relief=FLAT)
TLabel9.configure(text='''Mitosis''')

TEntry_Mitosis = Entry(TFrame1)
TEntry_Mitosis.place(relx=0.24, rely=0.88, relheight=0.05, relwidth=0.53)
TEntry_Mitosis.configure(width=246)
TEntry_Mitosis.configure(takefocus="")
TEntry_Mitosis.configure(cursor="ibeam")

# -----------------------------------------------------------------------

TButton_eval = Button(TFrame1,command=lambda w=TFrame1: get_all_entry_widgets_text_content(w))
TButton_eval.place(relx=0.34, rely=0.95, height=35, width=126)
TButton_eval.configure(takefocus="")
TButton_eval.configure(text='''Evaluate''')

# -----------------------------------------------------------------------

TLabel_Output = Label(root)
TLabel_Output.place(relx=0.60, rely=0.06, height=38, width=436)
TLabel_Output.configure(background="#d9d9d9")
TLabel_Output.configure(foreground="#000000")
TLabel_Output.configure(font=font11)
TLabel_Output.configure(relief=FLAT)
TLabel_Output.configure(anchor=CENTER)
TLabel_Output.configure(text='''Breast Cancer Stage :''')
TLabel_Output.configure(width=436)

Canvas_Graph = Canvas(root)
Canvas_Graph.place(relx=0.51, rely=0.16, relheight=0.66, relwidth=0.47)
Canvas_Graph.configure(background="white")
Canvas_Graph.configure(borderwidth="2")
Canvas_Graph.configure(highlightbackground="#e0ded1")
Canvas_Graph.configure(highlightcolor="black")
Canvas_Graph.configure(insertbackground="black")
Canvas_Graph.configure(relief=RIDGE)
Canvas_Graph.configure(selectbackground="#cac8bc")
Canvas_Graph.configure(selectforeground="black")
Canvas_Graph.configure(width=456)
    
TLabel_OutputText = Label(root)
TLabel_OutputText.place(relx=0.60, rely=0.87, height=38, width=500)
TLabel_OutputText.configure(background="#d9d9d9")
TLabel_OutputText.configure(foreground="#000000")
TLabel_OutputText.configure(font=font14)
TLabel_OutputText.configure(relief=FLAT)
TLabel_OutputText.configure(anchor=CENTER)
TLabel_OutputText.configure(width=500)

    
    
def get_all_entry_widgets_text_content(parent_widget):
    args = []
    children_widgets = parent_widget.winfo_children()
    for child_widget in children_widgets:
        if child_widget.winfo_class() == 'Entry':
            args.append(child_widget.get())
    #print(args)
    #print(type(args[1]))
    # check if all inputs are valid or not also non of the input field is null
    doMATLABProcessing(args)
    

def doMATLABProcessing(data):

        # contacting MATLAB using its API
        for i in range(len(data)):
            data[i] = float(data[i])
        val = eng.evalFuzzy(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8])
        outputMsg(val)
        eng.createOutputGraph(val,nargout=0)
        tk_img = ImageTk.PhotoImage(Image.open("output.jpg"))

        Canvas_Graph.create_image((150, 100), image=tk_img, anchor=NW)
        Canvas_Graph.tk_img = tk_img


def outputMsg(val):
    if val > 0.8:
        text = "You are at high risk of Breast Cancer"
    elif val <0.8 and val >0.6:
        text = "You are at medium risk of Breast Cancer"
    else:
        text = "You are at low risk of Breast Cancer"
    TLabel_OutputText['text'] = text


root.mainloop()