
##SCRIPT FOR TRAINING MODEL
import pandas as pd
from sklearn import linear_model

# Load the trained model
data = pd.read_csv("dataset.csv")
array = data.values

for i in range(len(array)):
    if array[i][0] == "Male":
        array[i][0] = 1
    else:
        array[i][0] = 0

df = pd.DataFrame(array)

maindf = df[[0, 1, 2, 3, 4, 5, 6]]
mainarray = maindf.values

temp = df[7]
train_y = temp.values
train_y = temp.values

for i in range(len(train_y)):
    train_y[i] = str(train_y[i])

mul_lr = linear_model.LogisticRegression(
    multi_class="multinomial", solver="newton-cg", max_iter=1000
)
mul_lr.fit(mainarray, train_y)

##SCRIPT FOR GUI

import tkinter as tk

root = tk.Tk()
root.title("Personality Predictor")

# function to predict personality
def pred(gender, age, openness, neuroticism, conscientiousness, agreeableness, extraversion):
    # code to predict personality based on input values
    # replace with your implementation
    age=int(age)
    openness=int(openness)
    neuroticism=int(neuroticism)
    conscientiousness=int(conscientiousness)
    agreeableness=int(agreeableness) 
    extraversion=int(extraversion)
    if gender.lower() == "male":
        gender = 1
    else:
        gender = 0
    if age < 17:
        age = 17
    elif age > 28:
        age = 28
    input_data = [[gender, age, openness, neuroticism, conscientiousness, agreeableness, extraversion]]
    prediction = mul_lr.predict(input_data)

    predicted_personality = prediction[0]

    # update the label with predicted personality
    personality_label.configure(text="Predicted Personality: " + predicted_personality)

# create label and input for gender
gender_label = tk.Label(root, text="Gender")
gender_label.pack()
gender_var = tk.StringVar(value="Male")
gender_menu = tk.OptionMenu(root, gender_var, "Male", "Female")
gender_menu.pack()

# create label and input for age
age_label = tk.Label(root, text="Age")
age_label.pack()
age_input = tk.Entry(root)
age_input.pack()

# create labels and inputs for personality traits
traits_label = tk.Label(root, text="Personality Traits")
traits_label.pack()

openness_label = tk.Label(root, text="Openness")
openness_label.pack()
openness_input = tk.Entry(root)
openness_input.pack()

neuroticism_label = tk.Label(root, text="Neuroticism")
neuroticism_label.pack()
neuroticism_input = tk.Entry(root)
neuroticism_input.pack()

conscientiousness_label = tk.Label(root, text="Conscientiousness")
conscientiousness_label.pack()
conscientiousness_input = tk.Entry(root)
conscientiousness_input.pack()

agreeableness_label = tk.Label(root, text="Agreeableness")
agreeableness_label.pack()
agreeableness_input = tk.Entry(root)
agreeableness_input.pack()

extraversion_label = tk.Label(root, text="Extraversion")
extraversion_label.pack()
extraversion_input = tk.Entry(root)
extraversion_input.pack()

# create submit button
submit_button = tk.Button(root, text="Submit", command=lambda: pred(gender_var.get(), age_input.get(), openness_input.get(), neuroticism_input.get(), conscientiousness_input.get(), agreeableness_input.get(), extraversion_input.get()))
submit_button.pack()

# create label to display predicted personality
personality_label = tk.Label(root, text="")
personality_label.pack()

root.mainloop()



