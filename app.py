import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

def create_meal_prediction_model():
    data = {
        'age': [20, 25, 30, 35, 40, 45, 50, 55, 60],
        'weight': [60, 65, 70, 75, 80, 85, 90, 95, 100],
        'loss': [3, 3, 2, 2, 2, 2, 2, 1, 1],
        'gain': [5, 5, 4, 4, 3, 3, 3, 2, 2]
    }
    df = pd.DataFrame(data)


    X_loss = df[['age', 'weight']]
    y_loss = df['loss']

    X_gain = df[['age', 'weight']]
    y_gain = df['gain']

    model_loss = LinearRegression()
    model_loss.fit(X_loss, y_loss)

    model_gain = LinearRegression()
    model_gain.fit(X_gain, y_gain)

    return model_loss, model_gain


def predict_meals(model_loss, model_gain, age, weight):
    meal_l = model_loss.predict([[age, weight]])[0]
    meal_g = model_gain.predict([[age, weight]])[0]

    return meal_l, meal_g


def display_profile_info():
    st.subheader("Profile Information 📝📝 :")
    name = st.text_input("Name 🖋️🖋️:")
    age = st.number_input("Age 👶:", min_value=0, max_value=150)
    height = st.number_input("Height ©️Ⓜ️(cm):", min_value=0.0)
    weight = st.number_input("Weight ⚖️(kg):", min_value=0.0)
    phone_number = st.text_input("Phone Number:📞")
    username = st.text_input("Username:")

    if st.button("Save Information "):
        st.success("Information saved successfully!✔️✔️")

    if st.button(f"Show Info of {name} "):
        st.write(f"Name:🟰 {name}")
        st.write(f"Age:🟰 {age}")
        st.write(f"Height: 🟰{height} cm")
        st.write(f"Weight:🟰 {weight} kg")
        st.write(f"Phone Number: 🟰{phone_number}")
        st.write(f"Username:🟰 {username}")


def display_health():
    st.subheader("Health 🧑‍⚕️🧑‍⚕️ Information")
    weight_key = "weight_input"
    age_key = "age_input"

    weight = st.number_input("enter Weight (kg):", min_value=0.0, key=weight_key)
    age = st.number_input("enter Age:", min_value=0, max_value=150, value=30, key=age_key)

    if st.button("Predict Exercise Duration ⌛⌛"):
        predicted_hour = predict_exercise_duration(age, weight)
        st.write(f"Your predicted exercise duration is ⌚⌚: {predicted_hour:.2f} hour(s)")


def predict_exercise_duration(age, weight):
    data1 = {
        'age': [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 40, 41, 45, 50, 55, 60, 69],
        'weight': [45, 48, 53, 55, 60, 62, 64, 65, 66, 67, 67, 67, 68, 70, 72, 75, 75, 78, 80, 77, 75, 81, 76, 78, 70],
        'hour': [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 0]
    }
    df = pd.DataFrame(data1)

    # define Features and target
    X = df[['age', 'weight']]
    y = df['hour']

    # Train the model
    model = LinearRegression()
    model.fit(X, y)

    new_data = pd.DataFrame([[age, weight]], columns=['age', 'weight'])
    predicted_hour = model.predict(new_data)

    return predicted_hour[0]


def display_weight():
    st.subheader("Weight Management")
    weight_option = st.radio("Select an option:", ["Increase Weight", "Loss Weight", "Maintain Weight"])

    if weight_option == "Increase Weight":
        if st.button("Diet for Weight Gain"):
            st.write("1. Butter🧈🧈")
            st.write("2. Milk products🥛🥛")
            st.write("3. Eggs🥚🥚")
            st.write("4. Chicken🍗🍗")
            st.write("5. Nuts and their butter 🥜🥜")

        if st.button("Exercise for Weight Gain🟢🟢"):
            st.write("\n1. Strength exercises:")
            st.write("   a. Push-up")
            st.write("   b. Pull-ups")
            st.write("   c. Sit-ups")

    elif weight_option == "Loss Weight":
        if st.button("Diet for Weight Loss 🔴🔴"):
            st.write("""
            1. Eat whole foods🍎🥭: eatts fruit
            2. Drink water💧💧: Stay hydrated—it helps control hunger.
            3. Avoid processed foods 🍔❌: Snacks and packaged meals avoid .
            4. Plan meals📝📝
            
            """)

        if st.button("Exercise for Weight Loss"):
            st.write("""
            - Walking 🚶‍♂️ : walk daily 15 min.
            - Running/jogging 🏃‍♂️: daily 15 - 20 min.
            - Cycling🚴: daily 15 - 20 min..
            - Swimming🏊‍♂️: as your choice
            - Jumping rope🦘: daily 10 - 15 mins
            """)

    st.write("---")
    st.subheader("Meal Prediction 🍴🍴")

    age = st.slider("Select your age 👶:", min_value=20, max_value=60, value=30)
    weight = st.slider("Select your weight ⚖️(kg):", min_value=60, max_value=100, value=75)

    if st.button("Predict Meals 🍴🍴"):
        model_loss, model_gain = create_meal_prediction_model()
        meals_loss, meals_gain = predict_meals(model_loss, model_gain, age, weight)

        st.write(f"Predicted meals for weight loss 🔴 : {meals_loss:.2f}")
        st.write(f"Predicted meals for weight gain🟢 : {meals_gain:.2f}")


def display_height():
    st.subheader("Height Information  ")
    age = st.number_input("Enter your age:", min_value=0, max_value=150, value=30)

    if st.button("Check Height Possibility"):
        if age < 25:
            st.write("You still can increase your height 😀😀.")
        else:
            st.write("Less chances.")

    if st.button("Diet for Height Increase"):
        st.write("""
        Foods that may contribute to height increase:
        - Beans 
        - Quinoa 
        - Almonds 🥜 
        - Low-fat dairy 🥛
        - Eggs 🥚
        - Sweet potatoes 🥔
        """)

    if st.button("Exercises for Height Increase "):
        st.write("""
        Exercises that may help in increasing height:
        - Bar hanging
        - Swimming 🏊🏊
        - Cobra stretch
        - Skipping 🪢🪢
        """)


def display_strength():
    st.subheader("🏋️‍♂️🏋️‍♂️Strength Training Information 🏋️‍♂️🏋️‍♂️")

    if st.button("Heavy Exercises ⚡⚡⚡:: "):
        st.write("""
        Heavy exercises to build strength:
        - Overhead press
        - Bench press
        - Deadlift
        - Weightlifting
        - Lifting
        - Ego lifting
        """)

    if st.button("Light Weight Exercises 🏋️‍♂️🏋️‍♂️🏋️‍♂️:: "):
        st.write("""
        Light weight exercises to build strength:
        - Lifting
        - Deadlifting
        - Presses
        - Overhead presses
        - Lifting
        - Ego
        """)

    if st.button("Folks ➿➿➿➿:: "):
        st.write("""
        Here's a list of the four folks in the 2022
        first folks from all there's to
        """)




def display_meditation():
    st.subheader("Mental Health Checker")

    sleep_hours = st.slider("Sleep hour:", min_value=0, max_value=12, value=7)
    anxiety_level = st.slider("Anxiety Level (0-10):", min_value=0, max_value=10, value=5)
    depression_level = st.slider("Depression Level (0-10):", min_value=0, max_value=10, value=5)
    bipolar_disorder = st.checkbox("Bipolar Disorder")

    mental_h = assess_mental_health(sleep_hours, anxiety_level, depression_level, bipolar_disorder)

    st.write(f"Your health condition is : {mental_h}")

def assess_mental_health(sleep_hours, anxiety_level, depression_level, bipolar_disorder):
    data1 = {
        'sleep_hours': [7, 5, 9, 6, 8],
        'anxiety_level': [3, 7, 2, 5, 4],
        'depression_level': [2, 6, 3, 4, 5],
        'mental_h': ['Good👍', 'Bad👎', 'Good👍', 'Normal🆗', 'Normal🆗']  # Categorical target
    }
    df = pd.DataFrame(data1)

    X = df[['sleep_hours', 'anxiety_level', 'depression_level']]
    y = df['mental_h']

    # Create and train the logistic regression model
    model = LogisticRegression(max_iter=1000, multi_class='auto')
    model.fit(X, y)

    # Predict the mental health condition based on input data
    input_data = [[sleep_hours, anxiety_level, depression_level]]
    pred = model.predict(input_data)[0]

    return pred


def input_daily_exercise_duration():
    st.subheader("Daily Exercise Duration ⏲️⏲️")

    exercise_duration = {}

    for i, day in enumerate(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']):
        exercise_duration[day] = st.number_input(f"{day} Exercise Duration (hours):", min_value=0.0, key=f"day_{i}")

    if st.button("Calculate Weekly Progress"):
        total_hours = sum(exercise_duration.values())

        if total_hours < 1:
            progress_category = "Bad Progress👎"
        elif total_hours < 2:
            progress_category = "Normal Progress🆗"
        elif total_hours < 3:
            progress_category = "Good Progress👍"
        else:
            progress_category = "Amazing Progress 🫡🫡"

        st.write(f"Total Exercise Hours This Week --> : {total_hours:.2f}")
        st.write(f"Progress Category --> : {progress_category}")


def main():
    st.sidebar.title("Free Hospital")
    page = st.sidebar.radio("Page Navigation", ["Home", "Profile", "Health", "Progress", "Other"])

    if page == "Home":
        st.title("✨✨ Welcome to Free Health Tracker")

    elif page == "Profile":
        display_profile_info()

    elif page == "Health":
        display_health()

    elif page == "Progress":
        input_daily_exercise_duration()

    elif page == "Other":
        st.title("# Ranjit and team")
        st.write("Thanks to use our simple project or website 🙏🙏🙏.")
        st.write("Our main pupose is : \n 1. care about the health🧑‍⚕️ \n 2. provide a free 🆓services")

    if page == "Health":
        section = st.sidebar.radio("Health Navigation", ["Weight", "Height", "Strength", "Meditation"])
        if section == "Weight":
            display_weight()
        elif section == "Height":
            display_height()
        elif section == "Strength":
            display_strength()
        elif section == "Meditation":
            display_meditation()


if __name__ == "__main__":
    main()
