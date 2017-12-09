from Tkinter import *

def take():
    file_name = e1.get()
    pix_size_cam = e2.get()
    focal_length = e3.get()
    im_wid_p = e4.get()
    im_hei_p = e5.get()
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    int(pix_size_cam)
    int(focal_length)
    int(im_wid_p)
    int(im_hei_p)
    return

master = Tk()
Label(master, text="File Name").grid(row=0)
Label(master, text="Camera Pixel Size (mm)").grid(row=1)
Label(master, text="Focal Length (mm)").grid(row=2)
Label(master, text="Image Width (pixels)").grid(row=3)
Label(master, text="Image Height (pixels)").grid(row=3)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)

Button(master, text='Quit', command=master.quit).grid(row=5, column=0, sticky=W, pady=4)
Button(master, text='Enter', command=take).grid(row=5, column=1, sticky=W, pady=4)



mainloop( )

