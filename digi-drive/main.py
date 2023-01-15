import tkinter as tk
from tkinter import ttk
import subprocess as sub

import datetime

class ScreenSizing:
      def __init__(self, sizes, window):
            self.appSize = sizes
            self.window = window
            self.position = [self.calpostion(0), self.calpostion(1)]

      def create(self):
            return f'{self.appSize[0]}x{self.appSize[1]}+' + f'{self.position[0]}+{self.position[1]}'

      def calpostion(self ,iteration):
            return int((self.window[iteration] / 2) - (self.appSize[iteration] / 2))

# Const Text
DETAILS_STRING = "Technology innovation is increasing day by day making it more miniature and more efficient to work to give the user a better experience but still if we compare mobile phones with computers are far better in performance. So we can say there are many tasks that a computer can do better than mobile phones one of the tasks is managing data in hard drives. A mobile cannot provide you with the handling of the data in 1TB but a computer can do that. The computer can manage the data, transfer, view, or even can  manipulate it and have changes to it as the user wants it to be. But still, the most portable computers are laptop, which still requires a small bag to carry it. So we are creating the DIGI DRIVES Our vision is to make a device that is running on a microcomputer, specialized for a single task of only data management, and is more portable, with a better outcome. We are going to innovate the hard drives so that they can be smarter. We are going to make digital hard drives that will not only provide you the portability but will also let you see your data on your hard drive that data can be transferred, viewed, and can be used as you want it to be but it will surely make it more secure by having the security layers in it. The security layers will make sure that the data in that hard drive is encrypted with the user password to access only. Any of the devices that are connected to the smart hard drive through the micro-computer will be scanned to get rid of the malware, to prevent the device from any harm. There will be software in this digital hard drive that will provide the user an experience of better data management in just a small device that can be held as a tablet device providing more functionality and more features than both tablet and smartphone devices specializing in the only given one task of data management which will surely let the user carry it instead of carrying a device like a laptop which is double the price of that device and a multi-tasking device which user don’t want to have any roblem in it. So the better choice is to have a device with better features in a very small, easy to carry, and better working device."
DETAILS_BUTTON = "Automate Disable after 24 hours"


# Const Time
SPLASH_ANIMATION = 1500

# FONTS
PRIMARYFONT =("Inter", 16, "bold")
SECONDARYFONT =("Inter", 8)
BUTTONFONT =("Inter", 9)
SPECIALFONT =("Itim", 10)
EVENTFONT =("Itim", 15, "bold")

# COLORS
PRIMARYCOLOR = "#000000"
SECONDARYCOLOR = "#001AFF"
BTN_BLOCK = "RED"
BTN_UNBLOCK = "GREEN"



# Commands
USERNAME = "whoami"
USERID = "id -u"
USERGROUP = "id -g"
PCNAME = "hostname"

ISBLOCK = "true"
AUTOBLOCK = "true"
DATE = "00"



class cmd:
	def __init__(self, command):
		self.command = command
		self.output = ""
		self.err = ""
		self.exit_code = ""

	def run(self):
		self.output = sub.check_output(self.command, shell=True).decode("utf-8")
		return self.output.replace("\n", "")
	
	def runFile(self):
		sub.call(self.command, shell=True)

	def run2(self):
		self.process = sub.Popen(self.command, stdout=sub.PIPE, shell=True)
		(self.output, self.err) = self.process.communicate()
		self.exit_code = self.process.wait()
		self.output = self.output.decode('utf-8')
		self.err = self.err.decode('utf-8')


class RoundedButton(tk.Canvas):
    def __init__(self, parent, width, height, cornerradius, padding, color, sttext:str="", command=None):
        tk.Canvas.__init__(self, parent, borderwidth=0, relief="flat", highlightthickness=0)
        self.command = command
		
        if cornerradius > 0.5*width:
            print("Error: cornerradius is greater than width.")
            return None

        if cornerradius > 0.5*height:
            print("Error: cornerradius is greater than height.")
            return None

        rad = 2*cornerradius

        def shape():
            self.create_polygon((padding,height-cornerradius-padding,padding,cornerradius+padding,padding+cornerradius,padding,width-padding-cornerradius,padding,width-padding,cornerradius+padding,width-padding,height-cornerradius-padding,width-padding-cornerradius,height-padding,padding+cornerradius,height-padding), fill=color, outline=color)
            self.create_arc((padding,padding+rad,padding+rad,padding), start=90, extent=90, fill=color, outline=color)
            self.create_arc((width-padding-rad,padding,width-padding,padding+rad), start=0, extent=90, fill=color, outline=color)
            self.create_arc((width-padding,height-rad-padding,width-padding-rad,height-padding), start=270, extent=90, fill=color, outline=color)
            self.create_arc((padding,height-padding-rad,padding+rad,height-padding), start=180, extent=90, fill=color, outline=color)


        shape()
        (x0,y0,x1,y1)  = self.bbox("all")
        width = (x1-x0)
        height = (y1-y0)
        self.configure(width=width, height=height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event):
        self.configure(relief="sunken")

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command is not None:
            self.command()

class Pages(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		
		self.image = []
		self.frames = {}
		self.listScreens = [SplashScreen, OnBorading, General, Aboutus]
		
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = 1)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		self.initializeData()
		self.inizialize()


		for F in (self.listScreens):
			frame = F(container, self, self.image)
			self.frames[F] = frame

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(self.listScreens[0])

	def initializeData(self):
		try:
			f = open("./cache/config.txt", "r")

			DATE = (f.readline()).replace("\n", "")
			ISBLOCK = (f.readline()).replace("\n", "")
			AUTOBLOCK = (f.readline()).replace("\n", "")

			f.close()
			current_time = datetime.datetime.now()			

			if(current_time.day != int(DATE) and AUTOBLOCK == "true"):
				if(ISBLOCK != "true"):
						self.blockUsb()
				else:
					self.blockUsb()
		finally:
			pass

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

	def inizialize(self):
		self.image = [
			tk.PhotoImage(file = './assets/bg.png'),
			tk.PhotoImage(file = './assets/image-01.png'),
			tk.PhotoImage(file = './assets/image-01.png'),
			tk.PhotoImage(file = './assets/icons/image-01.png'),
			tk.PhotoImage(file = './assets/icons/image-02.png'),
			tk.PhotoImage(file = './assets/icons/image-03.png'),
			tk.PhotoImage(file = './assets/icons/image-04.png'),
			tk.PhotoImage(file = './assets/icons/image-05.png'),
			tk.PhotoImage(file = './assets/icons/image-06.png'),
			tk.PhotoImage(file = './assets/icons/image-07.png')
		]

	def write(self):
		global ISBLOCK
		global AUTOBLOCK

		try:
			if(ISBLOCK == "true"):
					ISBLOCK = "false"
			else:
				ISBLOCK = "true"
			
			f = open("./cache/config.txt", "w")
			f.write(f"{datetime.datetime.now().day}\n")
			f.write(f"{ISBLOCK}\n")
			f.write(f"{AUTOBLOCK}")
				
			f.close()
		finally:
			pass 

	def blockUsb(self):
		try:
			script = ""
			self.write()
			
			if(ISBLOCK == "false"): 
					script = "un"
			
			cmd(f"sh ./Script/{script}Block/{script}block.sh").runFile()

		finally:
			pass
	
# Screen Code

class SplashScreen(tk.Frame):
	def __init__(self, parent, controller, images):
		tk.Frame.__init__(self, parent)

		# label of frame 
		label1 = ttk.Label(self, image = images[0])
		label1.image = images[0]
		label1.place(x = 0, y = 0)
		label1.after(SPLASH_ANIMATION, lambda: controller.show_frame(OnBorading))

class OnBorading(tk.Frame):
	def __init__(self, parent, controller, images):
			tk.Frame.__init__(self, parent)
			
			ttk.Label(self, text = f"{(cmd(USERNAME)).run()}", font=PRIMARYFONT).place(x = 15, y = 20)
			ttk.Label(self, text = DETAILS_BUTTON, font=SPECIALFONT).place(x = 375, y = 59)
			
			
			ScanUpdate = (ttk.Label(self, text ="Scan Connected devices", font = SECONDARYFONT, foreground = SECONDARYCOLOR))
			
			
			color = BTN_BLOCK if ISBLOCK == "true" else BTN_UNBLOCK
			text = "Block" if ISBLOCK == "true" else "Unblock"

			self.btn = RoundedButton(self, 90, 30, 15, 1, color, command = lambda : self.BlockBTN_Change(controller))
			self.btnText = self.btn.create_text(45, 15, text =text+" USB", fill="white", font=BUTTONFONT)
			
			# Place widgts
			ScanUpdate.place(x = 15, y = 50)
			self.btn.place(x=450, y=25)

			ScanUpdate.bind("<Button-1>", lambda e: (cmd("sh ./Script/scan.sh").runFile()))
			
			array = [
							 ["General",  images[3], 1,   1, General],
							 ["Sercuity", images[4], 1,   2, General],
							 ["User",     images[5], 1,   3, General],
							 ["Wifi",     images[6], 1,   4, General],
							 ["Update",   images[7], 2, 1.5, General],
							 ["USB",      images[8], 2, 2.5, General],
							 ["About us", images[9], 2, 3.5, Aboutus], 
			]

			for i in array:
				canvas = tk.Canvas(self, width= 110, height= 110)
				canvas.create_image(15, 15, anchor = tk.NW, image = i[1])
				
				canvas.place(x=(95 * i[3]), y=(100 * i[2]), width= 110, height= 110)

				canvas.bind("<Button-1>", lambda event, arg=i[4]: controller.show_frame(arg))
	# end of __init__

	def BlockBTN_Change(self, controller):
		global ISBLOCK

		if(ISBLOCK == "true"):
			self.btn.itemconfig(self.btnText, text = "Unblock USB")
			self.btn.config(bg=BTN_UNBLOCK) 
		else:
			self.btn.itemconfig(self.btnText, text = "Block USB")
			self.btn.config(bg=BTN_BLOCK)

		controller.blockUsb()


class Aboutus(tk.Frame):
	def __init__(self, parent, controller, images):
		tk.Frame.__init__(self, parent)

		# Create a Label Widget to display the text or Image of back
		btnBack = ttk.Label(self, image=images[1])
		btnBack.image = images[1]
		btnBack.place(x=0, y=10)
		btnBack.bind("<Button-1>", lambda e: controller.show_frame(OnBorading))

		(ttk.Label(self, text ="Digi Drive", font = PRIMARYFONT)).place(x=275, y=25)

		# Create a Label Widget to display the text or Image of back
		v = tk.Scrollbar(self, orient='vertical')
		v.place(x=590, y=10)

		# Add a text widget
		text=tk.Text(self, font=("Georgia, 10"), yscrollcommand=v.set,wrap=tk.WORD, borderwidth=0, highlightthickness=0, relief=tk.FLAT,  padx=50, pady=10)
		text.insert(tk.END, DETAILS_STRING)


		# Attach the scrollbar with the text widget
		v.config(command=text.yview)
		text.place(x=0, y=65, width=600, height=235)

class General(tk.Frame):
	def __init__(self, parent, controller, images):
		tk.Frame.__init__(self, parent)

		btnBack = ttk.Label(self, image=images[1])
		btnBack.image = images[1]
		btnBack.bind("<Button-1>", lambda e: controller.show_frame(OnBorading))


		master = tk.Frame(self, width=400, height= 300, )
		master.place(x=100, y=50)


		tk.Label(master, text="Basic Settings", font=EVENTFONT).grid(row=0, column=0, sticky=tk.W, pady=2)
		tk.Label(master, text = "User Name").grid(row = 1, column = 0, sticky = tk.W, pady = 2)
		tk.Label(master, text = "PC Name").grid(row = 2, column = 0, sticky = tk.W, pady = 2)
		
			
		uName, pcName = (cmd(USERNAME)).run(), (cmd(PCNAME)).run()

		self.e1 = tk.Entry(master, width=100)
		self.e2 = tk.Entry(master, width=100)
		
		self.e1.insert(0,uName)
		self.e2.insert(0,pcName)

		self.e1.grid(row = 1, column = 1,pady = 2, sticky = tk.EW)
		self.e2.grid(row = 2, column = 1,pady = 2, sticky = tk.EW)
		
		self.dataCheckbox = [tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar()]

		(tk.Checkbutton(master, text = "Mute Volumn", onvalue=1, offvalue=0, variable=self.dataCheckbox[0])).grid(row = 3, column = 0, sticky = tk.W)
		(tk.Checkbutton(master, text = "Automate Turn off all usb Port(12 hours)", onvalue=1, offvalue=0, variable=self.dataCheckbox[1])).grid(row = 3, column = 1, sticky = tk.W,)
		(tk.Checkbutton(master, text = "Autmoate update", onvalue=1, offvalue=0, variable=self.dataCheckbox[2])).grid(row = 4, column = 0, sticky = tk.W,)
		(tk.Checkbutton(master, text = "Automate Upgrade check", onvalue=1, offvalue=0, variable=self.dataCheckbox[3])).grid(row = 5, column = 0, sticky = tk.W,)
		
		if AUTOBLOCK == 'true':
			self.dataCheckbox[0].set(1) 

		
		self.btnSave = tk.Button(master, text = "Save", bg = "#717171", width = 10, command = self.save)
		self.btnSave.grid(row = 7, column = 0, sticky = tk.W)
		
		btnBack.place(x=0, y=10)

	def save(self):
		print(self.e1.get())
		print(self.e2.get())
		print(self.dataCheckbox[0].get())
		print(self.dataCheckbox[1].get())
		print(self.dataCheckbox[2].get())
		print(self.dataCheckbox[3].get())

	
# Driver Code
app = Pages()
app.title("Digi Drive")
screen = ScreenSizing( [600, 300], [app.winfo_screenwidth(), app.winfo_screenheight()] )
app.geometry(screen.create())
app.resizable(0, 0)
app.mainloop()