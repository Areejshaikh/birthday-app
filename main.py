import streamlit as st
from datetime import date

class Birthday:
    def __init__(self, name, birthday_date):
        self.name = name
        self.birthday_date = birthday_date

    def main(self):
        st.title("🎉 Welcome to Your Birthday Party App 🎂")
        
        name = st.text_input("🎈 What's your name?")
        birthday_date = st.date_input(
            "📅 Select your birthday:",
            min_value=date(1990, 1, 1),
            max_value=date.today()
        )

        st.markdown("## 🍰 Birthday Fun Questions")

        cake_choice = st.radio(
            "Which cake would you like today?",
            ["Chocolate 🍫", "Vanilla 🍦", "Strawberry 🍓", "Black Forest 🍒"]
        )

        gift_choice = st.selectbox(
            "Choose your dream gift 🎁",
            ["Laptop 💻", "Smartphone 📱", "Vacation 🌴", "Books 📚", "Surprise Me 🎉"]
        )

        rating = st.slider("⭐ Rate your best birthday ever", 1, 5)

        if st.button("🎊 Celebrate Now!"):
            if name and birthday_date:
                today = date.today()
                age = today.year - birthday_date.year - (
                    (today.month, today.day) < (birthday_date.month, birthday_date.day)
                )

                st.balloons()
                st.success(f"🎉 Happy {age}th Birthday, {name}! 🎉")
                st.image("birthday.gif", width=300, caption="🎂 Your Party is Ready!")

                st.markdown("---")
                st.subheader("🎁 Your Birthday Profile")
                st.markdown(f"**🧁 Cake:** {cake_choice}")
                st.markdown(f"**🎁 Gift:** {gift_choice}")
                st.markdown(f"**⭐ Best Birthday Rating:** {rating}/5")
                st.markdown(f"**📅 Birthday:** {birthday_date}")
                st.markdown("🕊️ _May your life be filled with peace, your heart with Imaan, and your path guided by the light of the Qur’an._May Allah increase you in knowledge, faith, health, and happiness. May you grow closer to Him with each passing year. 📖")
            else:
                st.error("❗ Please fill in your name and birthday date.")

if __name__ == "__main__":
    app = Birthday("", "")
    app.main()
