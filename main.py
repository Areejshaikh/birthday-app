# import streamlit
import streamlit as st
from datetime import  date, datetime, timedelta

class Birthday():
    def __init__(self,name , date):
        self.name = name
        self.date = date
        
    def name(self):
        return self.name
    
    def date(self):
        return self.date
    def main(self):
        st.title("Birthday Celebration")
        st.write("Welcome to the Birthday Celebration App!")
        
        
        name = st.text_input("Enter Your Name: ")
        date = st.date_input("Enter You Birthday Date:")
        
        
        if st.button("Submit Details"):
            if name and date:
                today = date.today()
                bmb = today.year - date.year -((today.month, today.day) < (date.month, date.day))
                birthday = Birthday(name, date)
                
                
               
                st.write(f"Hello {birthday.name}, your birthday is on {birthday.date}.")
                st.balloons()
                st.success(f"Birthday for {birthday.name} on {birthday.date}")
                st.info(f"{birthday.name} is celebrating their {bmb}th birthday today!")
                st.image("birthday.gif", caption="Happy Birthday Dear" + f" {birthday.name}!", use_column_width=True)
                
            else:
                st.error("Please fill in both fields.")
                
                
if __name__ == "__main__":
    birthday_app = Birthday("", "")
    birthday_app.main()