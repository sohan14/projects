from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont


class Watermark:

    def __init__(self):
        self.window = Tk()
        self.window.title('WaterMark Image')
        self.menubar = Menu(self.window)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open", command=self.open_img)
        self.filemenu.add_separator()
        self.editmenu = Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Watermark", command=self.water_mark)
        self.editmenu.add_command(label='Save', command=self.save_img)
        self.filemenu.add_command(label='Exit', command=self.window.quit)
        self.menubar.add_cascade(label='File', menu=self.filemenu)
        self.menubar.add_cascade(label='Edit', menu=self.editmenu)
        self.canvas = Canvas(height=0, width=300)
        self.canvas.config(bg='blue')
        self.canvas.grid(row=0, column=0)

        self.window.config(menu=self.menubar)
        self.window.mainloop()
        self.im = None

    def open_img(self):
        path = filedialog.askopenfilename()
        self.im = Image.open(path)
        self.show_img()

    def show_img(self):
        imag = self.im
        while imag.size[0] > 1500 or imag.size[1]>650:
            imag = imag.resize((round(imag.size[0] * 0.9), round(imag.size[1] * 0.9)))
        render = ImageTk.PhotoImage(imag)
        self.canvas.config(height=render.height(), width=render.width())
        img = Label(self.window, image=render)
        img.image = render
        img.place(x=0, y=0)

    def water_mark(self):
        width, height = self.im.size
        draw = ImageDraw.Draw(self.im)
        text = 'Sample'
        s = round(width * 0.05)
        font = ImageFont.truetype('arial.ttf', s)
        textwidth, textheight = draw.textsize(text, font)
        margin = 10
        x = width - textwidth - margin
        y = height - textheight - margin
        draw.text((x, y), text, font=font)
        self.show_img()

    def save_img(self):
        self.im.save(self.im.filename.split('/')[-1])
