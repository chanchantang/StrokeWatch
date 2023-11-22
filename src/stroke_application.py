import tkinter as tk
from tkinter import ttk

user_input={
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

# Main application class
class strokeApp(tk.Tk):
	def __init__(self, *args, **kwargs): 
		tk.Tk.__init__(self, *args, **kwargs)
		
		# Window settings
		self.title('Stroke assessment')
		self.geometry('450x450')
		
		# To store user input
		# Container frame
		container = tk.Frame(self) 
		container.pack(side = "top", fill = "both", expand = True) 

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# Creating dictionary of frames 
		self.frames = {} 
		for F in (MainMenu, Q1_Gender, Q2_Age, Q3_Hypertension, Q4_HeartDisease, Q5_EverMarried, Q6_WorkType, Q7_ResidenceType, Q8_AvgGlucoseLevel, Q9_BMI, Q10_SmokingStatus, Results):
			frame = F(container, self, user_input)
			self.frames[F] = frame 
			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(MainMenu, user_input)
		self.mainloop()

	# Used to swap frames
	def show_frame(self, page, input):
		frame = self.frames[page]
		frame.tkraise()
		frame.input = input
		if page == Results:
			frame.show_results()

	# Quit application
	def quit(self):
		self.destroy()
	
# Main menu of app
class MainMenu(tk.Frame):
	def __init__(self, parent, controller, input): 
		tk.Frame.__init__(self, parent)
		self.input = input
		
		# Main menu widgets
		lbl_title = ttk.Label(self, text="Welcome to your stroke assessment", font=30).pack(padx= 20, pady=20)
		lbl_information = ttk.Label(self, text="Disclaimer: This assessment is in no way a medical assessment, please seek a medical profession for a proper evaluation", wraplength=250, justify='left').pack(padx=20, pady=60)
		
		# Go to quesetion 2
		btn_begin = ttk.Button(self, text ="Begin", command = lambda : controller.show_frame(Q1_Gender, self.input)).pack()
		
class Q1_Gender(tk.Frame):
	def __init__(self, parent, controller, input):
		tk.Frame.__init__(self, parent)
		self.input = input

		# Q1 widgets
		lbl_question = ttk.Label(self, text ="What is your gender?").pack(padx= 20, pady=20)
		var = tk.IntVar()
		var.set(-1)
		rb_gender_M = ttk.Radiobutton(self, text="Male", variable=var, value=0).pack(padx=20, pady=20)
		rb_gender_F = ttk.Radiobutton(self, text="Female", variable=var, value=1).pack(padx=20, pady=20)
		rb_gender_O = ttk.Radiobutton(self, text="Other", variable=var, value=2).pack(padx=20, pady=20)
		rb_gender_NA = ttk.Radiobutton(self, text="Prefer not to say", variable=var, value=3).pack(padx=20, pady=20)
		
		# Go to question 2
		btn_next = ttk.Button(self, text ="Question 2",command = lambda : self.next_question(var.get(), controller)).pack()
							
	def next_question(self, value, controller):
		if value == -1:
			return
		self.input['gender'] = value
		controller.show_frame(Q2_Age, self.input)

class Q2_Age(tk.Frame):
	def __init__(self, parent, controller, input):
		tk.Frame.__init__(self, parent)
		self.input = input

		# Q2 widgets
		lbl_question = ttk.Label(self, text ="What is your age?").pack(padx= 20, pady=20)
		var = tk.IntVar()
		scale_age = tk.Scale(self, from_=1, to=110, orient=tk.HORIZONTAL, variable=var).pack(padx=20, pady=20)

		# Go to question 3
		btn_next = ttk.Button(self, text ="next", command = lambda : self.next_question(var.get(), controller)).pack()
							
	def next_question(self, value, controller):
		self.input['age'] = value
		controller.show_frame(Q3_Hypertension, self.input)

class Q3_Hypertension(tk.Frame):
	def __init__(self, parent, controller, input):
		tk.Frame.__init__(self, parent)
		self.input = input
		# Q3 widgets
		lbl_question = ttk.Label(self, text ="Do you have hypertension?").pack(padx= 20, pady=20)
		var = tk.IntVar()
		var.set(-1)
		rb_yes = ttk.Radiobutton(self, text="Yes", variable=var, value=1).pack(padx=20, pady=20)
		rb_no = ttk.Radiobutton(self, text="No", variable=var, value=0).pack(padx=20, pady=20)

		# Go to question 4
		btn_next = ttk.Button(self, text ="next", command = lambda : self.next_question(var.get(), controller)).pack()
							
	def next_question(self, value, controller):
		if value == -1:
			return
		self.input['hypertension'] = value
		controller.show_frame(Q4_HeartDisease, self.input)

class Q4_HeartDisease(tk.Frame):
	def __init__(self, parent, controller, input):

		tk.Frame.__init__(self, parent)
		self.input = input
		# Q4 widgets
		lbl_question = ttk.Label(self, text ="Do you have heart disease?").pack(padx= 20, pady=20)
		var = tk.IntVar()
		var.set(-1)
		rb_yes = ttk.Radiobutton(self, text="Yes", variable=var, value=1).pack(padx=20, pady=20)
		rb_no = ttk.Radiobutton(self, text="No", variable=var, value=0).pack(padx=20, pady=20)

		# Go to question 5
		btn_next = ttk.Button(self, text ="next", command = lambda : self.next_question(var.get(), controller)).pack()
							
	def next_question(self, value, controller):
		if value == -1:
			return
		self.input['heart_disease'] = value
		controller.show_frame(Q5_EverMarried, self.input)

class Q5_EverMarried(tk.Frame):
	def __init__(self, parent, controller, input):
		tk.Frame.__init__(self, parent)
		self.input = input

		# Q5 widgets
		lbl_question = ttk.Label(self, text ="Have you ever been married?").pack(padx= 20, pady=20)
		var = tk.IntVar()
		var.set(-1)
		rb_yes = ttk.Radiobutton(self, text="Yes", variable=var, value=1).pack(padx=20, pady=20)
		rb_no = ttk.Radiobutton(self, text="No", variable=var, value=0).pack(padx=20, pady=20)

		# Go to question 6
		btn_next = ttk.Button(self, text ="next", command = lambda : self.next_question(var.get(), controller)).pack()
							
	def next_question(self, value, controller):
		if value == -1:
			return
		self.input['ever_married'] = value
		controller.show_frame(Q6_WorkType, self.input)

class Q6_WorkType(tk.Frame):
	def __init__(self, parent, controller, input):
		tk.Frame.__init__(self, parent)
		self.input = input

		# Q6 widgets
		lbl_question = ttk.Label(self, text ="What is your work type?").pack(padx= 20, pady=20)
		var = tk.StringVar()
		var.set("")
		rb_private = ttk.Radiobutton(self, text="Private", variable=var, value='Private').pack(padx=20, pady=20)
		rb_self_employed = ttk.Radiobutton(self, text="Self-employed", variable=var, value='Self-employed').pack(padx=20, pady=20)
		rb_government = ttk.Radiobutton(self, text="Government job", variable=var, value='Govt_job').pack(padx=20, pady=20)
		rb_children = ttk.Radiobutton(self, text="Children", variable=var, value='Children').pack(padx=20, pady=20)
		rb_never_worked = ttk.Radiobutton(self, text="Never worked", variable=var, value='Never_worked').pack(padx=20, pady=20)

		# Go to question 7
		btn_next = ttk.Button(self, text ="next", command = lambda : self.next_question(var.get(), controller)).pack()
							
	def next_question(self, value, controller):
		if value == "":
			return
		self.input['work_type'] = value
		controller.show_frame(Q7_ResidenceType, self.input)

class Q7_ResidenceType(tk.Frame):
	def __init__(self, parent, controller, input):
		tk.Frame.__init__(self, parent)
		self.input = input

		# Q7 widgets
		lbl_question = ttk.Label(self, text ="What is your residence type?").pack(padx= 20, pady=20)
		var = tk.StringVar()
		var.set("")
		rb_urban = ttk.Radiobutton(self, text="Urban", variable=var, value='Urban').pack(padx=20, pady=20)
		rb_rural = ttk.Radiobutton(self, text="Rural", variable=var, value='Rural').pack(padx=20, pady=20)

		# Go to question 8
		btn_next = ttk.Button(self, text ="next", command = lambda : self.next_question(var.get(), controller)).pack()
							
	def next_question(self, value, controller):
		if value == "":
			return
		self.input['Residence_type'] = value
		controller.show_frame(Q8_AvgGlucoseLevel, self.input)

class Q8_AvgGlucoseLevel(tk.Frame):
	def __init__(self, parent, controller, input):
		tk.Frame.__init__(self, parent)
		self.input = input

		# Q8 widgets
		lbl_question = ttk.Label(self, text ="What is your average glucose level in mg/dL?").pack(padx= 20, pady=20)
		var = tk.IntVar()
		scale_age = tk.Scale(self, from_=50, to=275, orient=tk.HORIZONTAL, variable=var).pack(padx=20, pady=20)

		# Go to question 9
		btn_next = ttk.Button(self, text ="next", command = lambda : self.next_question(var.get(), controller)).pack()
							
	def next_question(self, value, controller):
		self.input['avg_glucose_level'] = value
		controller.show_frame(Q9_BMI, self.input)

class Q9_BMI(tk.Frame):
	def __init__(self, parent, controller, input):
		tk.Frame.__init__(self, parent)
		self.input = input

		# Q9 widgets
		lbl_question = ttk.Label(self, text ="What is your BMI?").pack(padx= 20, pady=20)
		var = tk.IntVar()
		scale_age = tk.Scale(self, from_=2, to=100, orient=tk.HORIZONTAL, variable=var).pack(padx=20, pady=20)

		# Go to question 10
		btn_next = ttk.Button(self, text ="next", command = lambda : self.next_question(var.get(), controller)).pack()
							
	def next_question(self, value, controller):
		self.input['bmi'] = value
		controller.show_frame(Q10_SmokingStatus, self.input)


class Q10_SmokingStatus(tk.Frame):
	def __init__(self, parent, controller, input):
		tk.Frame.__init__(self, parent)
		self.input = input
		# Q9 widgets
		lbl_question = ttk.Label(self, text ="What is your smoking status?").pack(padx= 20, pady=20)
		var = tk.StringVar()
		var.set("")
		rb_formerly = ttk.Radiobutton(self, text="Formerly smoked", variable=var, value='formerly smoked').pack(padx=20, pady=20)
		rb_never_smoked = ttk.Radiobutton(self, text="Never smoked", variable=var, value='never smoked').pack(padx=20, pady=20)
		rb_smokes = ttk.Radiobutton(self, text="Smokes", variable=var, value='smokes').pack(padx=20, pady=20)

		# Go to question 10
		btn_next = ttk.Button(self, text ="next", command = lambda : self.next_question(var.get(), controller)).pack()
							
	def next_question(self, value, controller):
		if value == "":
			return
		self.input['smoking_status'] = value
		controller.show_frame(Results, self.input)

# Results of survey
class Results(tk.Frame):
	def __init__(self, parent, controller, input, finished=False):
		tk.Frame.__init__(self, parent)
		self.input = input
							
	def next_question(self, controller):
		controller.show_frame(MainMenu)
	
	def show_results(self):
		results = ttk.Label(self, text = 'Here are your results\n' + str(self.input), wraplength=250, justify='left').pack(padx= 20, pady=20)

# Start application
app = strokeApp()