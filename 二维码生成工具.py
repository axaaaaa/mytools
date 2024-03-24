import tkinter as tk
from tkinter import messagebox
import qrcode
from barcode import EAN13
from barcode.writer import ImageWriter
from PIL import ImageTk, Image

class BarcodeGenerator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Barcode/QR code generator")
        self.master.geometry('800x600')  # 设置窗口大小
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label1 = tk.Label(self, text="请输入要生成的二维码或条码内容：")
        self.label1.pack(side="top")

        self.entry1 = tk.Entry(self, width=50)
        self.entry1.pack(side="top")

        self.button1 = tk.Button(self, text="生成二维码", command=self.generate_qr)
        self.button1.pack(side="left")

        self.button2 = tk.Button(self, text="生成条码", command=self.generate_barcode)
        self.button2.pack(side="left")

        self.canvas = tk.Canvas(self, width=300, height=300)
        self.canvas.pack(side="bottom")

    def generate_qr(self):
        data = self.entry1.get()
        if data:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img = img.resize((300, 300), Image.ANTIALIAS)
            img_tk = ImageTk.PhotoImage(img)
            self.canvas.create_image(0, 0, anchor="nw", image=img_tk)
            self.canvas.image = img_tk
        else:
            messagebox.showerror("错误", "请输入要生成的内容！")

    def generate_barcode(self):
        data = self.entry1.get()
        if data:
            barcode = EAN13(data, writer=ImageWriter())
            filename = barcode.save("barcode")
            img = Image.open(filename)
            img = img.resize((300, 300), Image.ANTIALIAS)
            img_tk = ImageTk.PhotoImage(img)
            self.canvas.create_image(0, 0, anchor="nw", image=img_tk)
            self.canvas.image = img_tk
        else:
            messagebox.showerror("错误", "请输入要生成的内容！")

if __name__ == '__main__':
    root = tk.Tk()
    app = BarcodeGenerator(master=root)
    app.mainloop()
