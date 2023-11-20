import tkinter as tk
from tkinter import ttk

# Main application class
class strokeApp(tk.Tk):
	def __init__(self, *args, **kwargs): 
		tk.Tk.__init__(self, *args, **kwargs)
		
		# Window settings
		self.title('Stroke assessment')
		self.geometry('450x450')
		
		# To store user input
		self.input={
			'gender': None,
			'age': None,
			'hypertension' : None,
			'heart_disease' : None,
			'ever_married' : None,
			'work_type' : None,
			'Residence_type' : None,
			'avg_glucose_level' : None,
			'bmi' : None,
			'smoking_status' : None
		}
		# Container frame
		container = tk.Frame(self) 
		container.pack(side = "top", fill = "both", expand = True) 

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# Creating dictionary of frames 
		self.frames = {} 
		for F in (MainMenu, Q1_Gender, Q2_Age):
			frame = F(container, self)
			self.frames[F] = frame 
			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(MainMenu)
		self.mainloop()

		# Print user input after user quits 
		print(self.input)

	# Used to swap frames
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

	# Quit application
	def quit(self):
		self.destroy()
	
# Main menu of app
class MainMenu(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)
		
		# Main menu widgets
		lbl_title = ttk.Label(self, text="Welcome to your stroke assessment", font=30).pack(padx= 20, pady=20)
		lbl_information = ttk.Label(self, text="This assessment is in no way a medical assessment, please seek a medical profession for a proper evaluation", wraplength=250, justify='left').pack(padx=20, pady=60)
		
		# Go to quesetion 2
		btn_begin = ttk.Button(self, text ="Begin", command = lambda : controller.show_frame(Q1_Gender)).pack()
		
# Q1: Gender
# TODO: make sure user has selected value before clicking onto next ubtton
class Q1_Gender(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		# Q1 widgets
		lbl_question = ttk.Label(self, text ="What is your gender?").pack(padx= 20, pady=20)
		var = tk.IntVar()
		var.set("")
		rb_gender = ttk.Radiobutton(self, text="Male", variable=var, value=0).pack(padx=20, pady=20)
		rb_gender = ttk.Radiobutton(self, text="Female", variable=var, value=1).pack(padx=20, pady=20)
		rb_gender = ttk.Radiobutton(self, text="Other", variable=var, value=2).pack(padx=20, pady=20)
		rb_gender = ttk.Radiobutton(self, text="Prefer not to say", variable=var, value=3).pack(padx=20, pady=20)
		
		# Go to question 2
		btn_next = ttk.Button(self, text ="Question 2",command = lambda : self.next_question(var.get(), controller)).pack()
							
	def next_question(self, value, controller):
		controller.input['gender'] = value
		controller.show_frame(Q2_Age)

# Q2: age
class Q2_Age(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		# Q2 widgets
		lbl_question = ttk.Label(self, text ="What is your age?").pack(padx= 20, pady=20)
		var = tk.IntVar()
		scale_age = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL, variable=var).pack(padx=20, pady=20)

		# Go to question 3
		btn_next = ttk.Button(self, text ="Finish", command = lambda : self.next_question(var.get(), controller)).pack()
							
	def next_question(self, value, controller):
		controller.input['age'] = value
		controller.quit()

# Start application
app = strokeApp()