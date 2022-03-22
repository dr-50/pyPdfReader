from tkinter import *
import PyPDF2
from tkinter import filedialog

root = Tk()
root.title('PDF Reader Sample')
root.geometry("500x500")

# Create a textbox
my_text = Text(root, height = 30, width=30)
my_text.pack(pady=10)

#Clear text
def clear_text():
    my_text.delete(1.0,END)

#Open pdf
def open_pdf():
    #get filename of pdf
    open_file = filedialog.askopenfilename(
        initialdir="C:/",
        title="Open PDF File",
        filetypes=(
            ("PDF Files", "*.pdf"),
            ("All Files", "*.*")
        )
    )
    
    if open_file:
        # Open pdf
        pdf_file = PyPDF2.PdfFileReader(open_file)
        # set page to read
        page = pdf_file.getPage(0)
        #Extract the text from pdf
        page_content = page.extractText()

        # Add text to textbox window
        my_text.insert(1.0, page_content)
    
#Create a menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Add menu dropdown
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_pdf)
file_menu.add_command(label="Clear", command=clear_text)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()
