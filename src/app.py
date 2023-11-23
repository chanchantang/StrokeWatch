import tkinter
from tkinter import ttk
import customtkinter as ctk
from PIL import Image
import os
import joblib
import numpy as np
import pandas as pd

ctk.set_appearance_mode("dark")

user_input={
	'sex': None,
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


class App(ctk.CTk):
    width = 900
    height = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("CustomTkinter example_background_image.py")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        # load and create background image
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = ctk.CTkImage(Image.open(current_path + "/images/bg_gradient.jpg"),
                                               size=(self.width, self.height))
        self.bg_image_label = ctk.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        self.start_page()


    def start_page(self):
        self.start_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.start_frame.grid(row=0, column=0, sticky="ns")
        self.start_label = ctk.CTkLabel(self.start_frame, text="Are you ready to learn\nyour stroke risk?",
                                                  font=ctk.CTkFont(size=30, weight="bold"))
        self.start_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.start_label = ctk.CTkLabel(self.start_frame, text="Disclaimer: This assessment is in no way a medical assessment.\n Please seek a medical profession for a proper evaluation", font=ctk.CTkFont(size=15), text_color='gray')
        self.start_label.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.start_checkbox = ctk.CTkCheckBox(self.start_frame, text="I have read, understood and agree to the above")
        self.start_checkbox.grid(row=2, column=0, padx=50, pady=(100, 0), sticky="w")
        self.login_button = ctk.CTkButton(self.start_frame, text="Start", command=self.results, width=400, height=40,       bg_color='blue')
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))
        self.error_label = ctk.CTkLabel(self.start_frame, text="", font=ctk.CTkFont(size=15), text_color='red')
        self.error_label.grid(row=4, column=0, padx=30, pady=(15, 15))

    def name_event(self):
        # print("Login pressed - username:", self.username_entry.get(), "password:", self.password_entry.get())
        disclaimer = self.start_checkbox.get()
        # if not disclaimer:
        #     self.error_label.configure(text="Please check the box to indicate that you accept the statement to continue.")
        # else:
        #     self.error_label.configure(text="")
        self.start_frame.grid_forget()
        self.main_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_label = ctk.CTkLabel(self.main_frame, text="CustomTkinter\nMain Page",
                                                font=ctk.CTkFont(size=20, weight="bold"))
        self.main_label.grid(row=0, column=0, padx=30, pady=(30, 15))
        self.back_button = ctk.CTkButton(self.main_frame, text="Back", command=self.back_event, width=200)
        self.back_button.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=100)
    
    def Q1_identity(self):
        self.start_frame.grid_forget()
        self.id_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.id_frame.grid(row=0, column=0, sticky="ns")

        self.id_label = ctk.CTkLabel(self.id_frame, text="Please provide your name so that\nwe may offer you a personalized experience", font=ctk.CTkFont(size=20, weight="bold"))
        self.id_label.grid(row=1, column=0, padx=30, pady=(150, 15))

        self.name_entry = ctk.CTkEntry(self.id_frame, width=400, height=40, placeholder_text="Your first name")
        self.name_entry.grid(row=2, column=0, padx=30, pady=(15, 15))

        self.next_button = ctk.CTkButton(self.id_frame, text="Next", command=self.Q2_self, width=400, height=40,       bg_color='blue')
        self.next_button.grid(row=3, column=0, padx=30, pady=(15, 15))

        self.id_error_label = ctk.CTkLabel(self.id_frame, text="", font=ctk.CTkFont(size=15), text_color='red')
        self.id_error_label.grid(row=4, column=0, padx=30, pady=(15, 15))

    def Q2_self(self):
        self.id_frame.grid_forget()
        self.self_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.self_frame.grid(row=0, column=0, sticky="ns")

        self.sex_label = ctk.CTkLabel(self.self_frame, text="Sex at Birth", font=ctk.CTkFont(size=20, weight="bold"))
        self.sex_label.grid(row=1, column=0, padx=30, pady=(150, 15))
        self.sex = tkinter.StringVar()
        self.sex_button_1 = ctk.CTkRadioButton(self.self_frame, variable=self.sex, value='Male', text="Male")
        self.sex_button_1.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        self.sex_button_2 = ctk.CTkRadioButton(self.self_frame, variable=self.sex, value='Female', text="Female")
        self.sex_button_2.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        self.sex_button_1.invoke()


        self.age_label = ctk.CTkLabel(self.self_frame, text="Age", font=ctk.CTkFont(size=20, weight="bold"))
        self.age_label.grid(row=4, column=0, padx=30, pady=(15, 15))
        self.age_entry = ctk.CTkEntry(self.self_frame, width=400, height=40, placeholder_text="Your age")
        self.age_entry.grid(row=5, column=0, padx=30, pady=(15, 15))

        self.next_button = ctk.CTkButton(self.self_frame, text="Next", command=self.Q3_About, width=400, height=40,       bg_color='blue')
        self.next_button.grid(row=6, column=0, padx=30, pady=(15, 15))

        self.id_error_label = ctk.CTkLabel(self.self_frame, text="", font=ctk.CTkFont(size=15), text_color='red')
        self.id_error_label.grid(row=7, column=0, padx=30, pady=(15, 15))

    def Q3_About(self):
        self.self_frame.grid_forget()
        self.about_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.about_frame.grid(row=0, column=0, sticky="ns")

        self.married_label = ctk.CTkLabel(self.about_frame, text="Have you ever been married?", font=ctk.CTkFont(size=20, weight="bold"))
        self.married_label.grid(row=1, column=0, padx=30, pady=(100, 15))
        self.ever_married = tkinter.StringVar()
        self.married_button_1 = ctk.CTkRadioButton(self.about_frame, variable=self.ever_married, value="Yes", text="Yes")
        self.married_button_1.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        self.married_button_2 = ctk.CTkRadioButton(self.about_frame, variable=self.ever_married, value="No", text="No")
        self.married_button_2.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        self.married_button_1.invoke()

        self.work_type = tkinter.StringVar()
        self.work_label = ctk.CTkLabel(self.about_frame, text="What is your work type?", font=ctk.CTkFont(size=20, weight="bold"))
        self.work_label.grid(row=4, column=0, padx=30, pady=(15, 15))
        self.work_menu = ctk.CTkOptionMenu(self.about_frame, values=["Self-employed", "Children", "Government job", "Private", "Never worked"], variable=self.work_type)
        self.work_menu.set("Self-employed")
        self.work_menu.grid(row=5, column=0, padx=30, pady=(15, 15))


        self.residence_type = tkinter.StringVar()
        self.residence_label = ctk.CTkLabel(self.about_frame, text="Have you ever been married?", font=ctk.CTkFont(size=20, weight="bold"))
        self.residence_label.grid(row=6, column=0, padx=30, pady=(15, 15))
        self.residence_button_1 = ctk.CTkRadioButton(self.about_frame, variable=self.residence_type, value="Urban", text="Urban")
        self.residence_button_1.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        self.residence_button_2 = ctk.CTkRadioButton(self.about_frame, variable=self.residence_type, value="Rural", text="Rural")
        self.residence_button_2.grid(row=8, column=0, pady=10, padx=20, sticky="w")
        self.residence_button_1.invoke()


        self.next_button = ctk.CTkButton(self.about_frame, text="Next", command=self.Q4_Status, width=400, height=40, bg_color='blue')
        self.next_button.grid(row=9, column=0, padx=30, pady=(15, 15))

        self.id_error_label = ctk.CTkLabel(self.about_frame, text="", font=ctk.CTkFont(size=15), text_color='red')
        self.id_error_label.grid(row=10, column=0, padx=30, pady=(15, 15))

    def Q4_Status(self):
        self.about_frame.grid_forget()
        self.status_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.status_frame.grid(row=0, column=0, sticky="ns")

        self.hypertension_label = ctk.CTkLabel(self.status_frame, text="Do you have hypertension?", font=ctk.CTkFont(size=20, weight="bold"))
        self.hypertension_label.grid(row=1, column=0, padx=30, pady=(100, 15))
        self.hypertension = tkinter.StringVar()
        self.hypertension_button_1 = ctk.CTkRadioButton(self.status_frame, variable=self.hypertension, value="Yes", text="Yes")
        self.hypertension_button_1.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        self.hypertension_button_2 = ctk.CTkRadioButton(self.status_frame, variable=self.hypertension, value="No", text="No")
        self.hypertension_button_2.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        self.hypertension_button_1.invoke()


        self.heart_disease = tkinter.StringVar()
        self.heart_disease_label = ctk.CTkLabel(self.status_frame, text="Do you have heart disease?", font=ctk.CTkFont(size=20, weight="bold"))
        self.heart_disease_label.grid(row=4, column=0, padx=30, pady=(15, 15))
        self.heart_disease_button_1 = ctk.CTkRadioButton(self.status_frame, variable=self.heart_disease, value="Yes", text="Yes")
        self.heart_disease_button_1.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        self.heart_disease_button_2 = ctk.CTkRadioButton(self.status_frame, variable=self.heart_disease, value="No", text="No")
        self.heart_disease_button_2.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        self.heart_disease_button_2.invoke()


        self.smoking_status = tkinter.StringVar()
        self.smoke_label = ctk.CTkLabel(self.status_frame, text="What is your smoking status?", font=ctk.CTkFont(size=20, weight="bold"))
        self.smoke_label.grid(row=7, column=0, padx=30, pady=(15, 15))
        self.smoke_menu = ctk.CTkOptionMenu(self.status_frame, values=["Smokes", "Never smoked", "Formerly smoked"], variable=self.smoking_status)
        self.smoke_menu.set("Never smoked")
        self.smoke_menu.grid(row=8, column=0, padx=30, pady=(15, 15))


        self.next_button = ctk.CTkButton(self.status_frame, text="Next", command=self.results, width=400, height=40, bg_color='blue')
        self.next_button.grid(row=9, column=0, padx=30, pady=(15, 15))

        self.id_error_label = ctk.CTkLabel(self.status_frame, text="", font=ctk.CTkFont(size=15), text_color='red')
        self.id_error_label.grid(row=10, column=0, padx=30, pady=(15, 15))

    def results(self):
        # user_input["sex"] = self.sex.get()
        # user_input["age"] = self.age_entry.get()
        # user_input["hypertension"] = self.hypertension.get()
        # user_input["heart_disease"] = self.heart_disease.get()
        # user_input["ever_married"] = self.ever_married.get()
        # user_input["work_type"] = self.work_type.get()
        # user_input["residence_type"] = self.residence_type.get()
        # user_input["avg_glucose_level"] = 0
        # user_input["bmi"] = 0
        # user_input["smoking_status"] = self.smoking_status.get()
        # print(user_input)

        # user_input={
        #     'Residence_type_Rural'
        #     ,'Residence_type_Urban'
        #     ,'age','avg_glucose_level','bmi,ever_married_No','ever_married_Yes','gender_Female','gender_Male','gender_Other','heart_disease','hypertension','id','smoking_status_Unknown','smoking_status_formerly smoked,smoking_status_never smoked,smoking_status_smokes,work_type_Govt_job,work_type_Never_worked,work_type_Private,work_type_Self-employed,work_type_children,stroke
        #     'sex': None,
        #     'age': None,
        #     'hypertension' : None,
        #     'heart_disease' : None,
        #     'ever_married' : None,
        #     'work_type' : None,
        #     'Residence_type' : None,
        #     'avg_glucose_level' : None,
        #     'bmi' : None,
        #     'smoking_status' : None
        # }


        # input = [26,1,0,66.0,116.55,31.1,0,1,1,0,0,0,1,27169,0,1,0,0,1,0,0,0,0]
        # array = np.array(input)
        # array = array.reshape(1,-1)

        test = './raw_data/test.csv'
        test_data = pd.read_csv(test)
        print(test_data)

        model = joblib.load('./saved_models/random_forest.joblib')
        output = model.predict(test_data)
        print(output)

        self.result_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.result_frame.grid(row=0, column=0, sticky="ns")
        self.result_label = ctk.CTkLabel(self.start_frame, text="Here are your results",
                                                  font=ctk.CTkFont(size=30, weight="bold"))
        self.result_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.result_label = ctk.CTkLabel(self.result_frame, text="Disclaimer: This assessment is in no way a medical assessment.\n Please seek a medical profession for a proper evaluation", font=ctk.CTkFont(size=15), text_color='gray')
        self.result_label.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.login_button = ctk.CTkButton(self.result_frame, text="Start", command="", width=400, height=40,       bg_color='blue')

        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))
        self.error_label = ctk.CTkLabel(self.result_frame, text="", font=ctk.CTkFont(size=15), text_color='red')
        self.error_label.grid(row=4, column=0, padx=30, pady=(15, 15))

        if output:
            self.error_label.configure(text="Hurray, you have a stroke!")
        else:
            self.error_label.configure(text="Unfortunately, you do not have a stroke")


    def back_event(self):
        self.main_frame.grid_forget()  # remove main frame
        self.start_frame.grid(row=0, column=0, sticky="ns")  # show login frame


if __name__ == "__main__":
    app = App()
    app.mainloop()
