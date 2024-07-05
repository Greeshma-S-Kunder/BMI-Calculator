import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / ((height / 100) ** 2)
    return bmi

def calculate_calories(weight, height, age, gender):
    
    if gender == "Male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:  # Female
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    calorie_count = bmr * 1.55
    return calorie_count

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def get_calorie_feedback(calorie_count):
    if calorie_count < 2000:
        return "Maintain current weight"
    elif 2000 <= calorie_count < 2500:
        return "Lose weight"
    else:
        return "Gain weight"

def main():
    st.set_page_config(page_title="BMI and Calorie Calculator", page_icon=":bar_chart:", layout="wide", initial_sidebar_state="expanded")
    st.markdown("<h1 style='color: #e44d26; text-align: center;'>BMI and Calorie Calculator</h1>", unsafe_allow_html=True)
    st.subheader("Enter Details:")

    with st.container():
        right, left = st.columns(2)
        
        with left:
            name = st.text_input("Name")
            age = st.number_input("Age", min_value=0, max_value=150, step=1)
            gender_options = ["Male", "Female", "Other"]
            gender = st.selectbox("Gender", gender_options)
            weight = st.number_input("Weight in kg", min_value=0.0, max_value=500.0, step=1.0, format="%.1f")
            height = st.number_input("Height in cm", min_value=0.0, max_value=300.0, step=0.1, format="%.1f")

        with right:
           
            st.text("")

        
        st.write("") 
        if st.button("Calculate BMI", key="calculate_bmi_button", help="Calculate BMI"):
            if name and age and gender and weight and height:
                bmi = calculate_bmi(weight, height)
                bmi_category = get_bmi_category(bmi)
                st.success(f"Hi {name}! Your BMI is: {bmi:.2f} ({bmi_category})")
            else:
                st.error("Please enter all details to calculate BMI")

        
        if st.button("Calculate Calorie Count"):
            calorie_count = calculate_calories(weight, height, age, gender)
            calorie_feedback = get_calorie_feedback(calorie_count)
            st.success(f"Your estimated daily calorie count is: {calorie_count:.2f} kcal ({calorie_feedback})")

    st.sidebar.title("Need Help?")

    
    if st.sidebar.button("Exercise Recommendations", key="exercise_recommendations_button"):
        st.sidebar.subheader("Exercise Recommendations")
        st.sidebar.markdown(
            """
            Incorporate a variety of exercises into your routine. Here are some recommendations:

            - **Cardiovascular Exercises:**
                - Include activities like jogging, cycling, or dancing to improve heart health.
                - Aim for at least 150 minutes of moderate-intensity aerobic exercise per week.

            - **Strength Training:**
                - Incorporate weightlifting or bodyweight exercises to build and tone muscles.
                - Strength training 2-3 times a week is beneficial for overall fitness.

            - **Flexibility and Stretching:**
                - Perform stretching exercises to improve flexibility and reduce the risk of injury.
                - Include yoga or Pilates in your routine.

            Remember to start gradually, listen to your body, and consult with a fitness professional if needed.
            """
        )
    if st.sidebar.button("Nutritional Advice", key="nutritional_advice_button"):
     
        st.sidebar.subheader("Nutritional Advice")
        st.sidebar.write("Consume a balanced diet with a mix of proteins, carbs, and fats.")

    if st.sidebar.button("Health Tips", key="health_tips_button"):
       
        st.sidebar.subheader("Health Tips")
        st.sidebar.write("1. Stay hydrated by drinking enough water daily.")
        st.sidebar.write("2. Get regular exercise to maintain a healthy lifestyle.")
        st.sidebar.write("3. Ensure a good night's sleep for overall well-being.")

    if st.sidebar.button("BMI Categories", key="bmi_categories_button"):
        
        st.sidebar.subheader("BMI Categories")
        st.sidebar.write("**Underweight:** BMI less than 18.5")
        st.sidebar.write("**Normal weight:** BMI between 18.5 and 24.9")
        st.sidebar.write("**Overweight:** BMI between 25 and 29.9")
        st.sidebar.write("**Obesity:** BMI of 30 or greater")

    if st.sidebar.button("Reset", key="reset_button"):
        st.experimental_rerun()

    
    if st.sidebar.button("About Us", key="about_us_button"):
        st.sidebar.markdown("<h2 style='color: #27ae60; text-align: center;'>About Us</h2>", unsafe_allow_html=True)
        st.sidebar.write("Welcome to our BMI and Calorie Calculator! We aim to provide you with accurate and useful health information.")
        st.sidebar.write("For any inquiries, please contact us at:")
        st.sidebar.write("Email: 21h21.franklin@sjec.ac.in")
        st.sidebar.write("Phone: +91 9845032412")

if __name__ == "__main__":
    main()
