import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

class BaseModel:
    def __init__(self):
        self.GEMINI_API_KEY = GEMINI_API_KEY
        

    def get_model(self):
        try:
            genai.configure(api_key=self.GEMINI_API_KEY)
            model = genai.GenerativeModel("gemini-2.5-flash")
            return model
        except Exception as e:
            print(f"Error retrieving model: {e}")
            

class AppFeatures(BaseModel):
    def __init__(self):
        self.__database={}
        super().__init__() 

    def first_menu(self):
        first_input = input("""


        Welcome to the App!
        Please choose an option:
                            1. Not a registered user? Register here.
                            2. Already a registered user? Login here.
                            3. Exit.""")
        
        if first_input == "1":
            #register
            self.__register_user()

        elif first_input == "2":
            #login
            self.__login_user()

        else:
            print("Exiting the application. Goodbye!")
            exit()


    
    def __sentiment_analysis(self):
        user_text = input("Enter the text for sentiment analysis: ")
        model = self.get_model()
        response = model.generate_content(
            f"Analyze the sentiment of the following text and respond with Positive, Negative, or Neutral:\n\nText: {user_text}"
        )

        result=response.text
        print(f"Sentiment Analysis Result: {result}")

    def __language_translation(self):
        user_text = input("Enter the text for Language Translation: ")
        model = self.get_model()
        response = model.generate_content(
            f"Translate the following text into Bangla:\n\nText: {user_text}"
        )

        result=response.text
        print(f"Translation Result: {result}")

    def logout(self):
        pass



    def __register_user(self):
        username = input("Enter a username for registration: ")
        password = input("Enter a password for registration: ")

        if username in self.__database:
            print("Username already exists. Please try a different username.")
        
        else:
            self.__database[username] = password
            print("Registration successful!")
            self.first_menu()

    def __login_user(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in self.__database:
            if self.__database[username] == password:
                print("Login successful!")
                logged_in_input = input("""
                            Choose an option:
                                1. Sentiment Analysis
                                2. Language Translation
                                3. Logout
                                        
                                        """)
                
                if logged_in_input == "1":
                    self.__sentiment_analysis()
                    self.__login_user()

                elif logged_in_input == "2":
                    self.__language_translation()
                    self.__login_user()

                else:
                    exit()
                    

                    



            else:
                print("Invalid password. Please try again.")
                self.__login_user()  
                
        else:
            print("Invalid username. Please try again.")
            

            
        


obj=AppFeatures()
obj.first_menu()