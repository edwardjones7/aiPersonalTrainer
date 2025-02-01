from flask import Flask, request, jsonify, render_template
import sqlite3
import openai

app = Flask(__name__)

# Initialize OpenAI
openai.api_key = '   '  # Replace with your OpenAI API key

# Database path
DATABASE = 'user_data.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

# Define a prompt template with required fields
base_prompt_template = """
You are an enthusiastic and knowledgeable AI personal trainer dedicated to helping people achieve their fitness goals. 
Whether it's designing effective workout routines, offering nutritional advice, or answering fitness-related questions, 
you're here to provide personalized and expert guidance. Your friendly and supportive approach makes you the perfect companion 
for anyone looking to improve their health and well-being. From beginners to seasoned athletes, you're ready to assist with 
workouts, nutrition plans, and everything in between, ensuring that everyone stays motivated and on track to reach their full potential. 

VERY SHORT CONCISE TO THE POINT RESPONSES

MAKE SURE TO USE USER DATA ALWAYS IN RESPONSES 

Don't say nothing about consulting other people for additional help, you are the help

American metrics only
"""

# Route to serve the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submissions
@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    name = data.get('name')
    age = data.get('age')
    height = data.get('height')
    weight = data.get('weight')
    gender = data.get('gender')
    activity_level = data.get('activity_level')
    notes = data.get('notes')
    goals = data.get('goals')

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO user_inputs (name, age, height, weight, gender, activity_level, notes, goals) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                   (name, age, height, weight, gender, activity_level, notes, goals))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Data saved successfully'})

# Route to handle chat requests
@app.route('/chat', methods=['POST'])
def chat():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM user_inputs ORDER BY id DESC LIMIT 1')
    user_data = cursor.fetchone()
    conn.close()

    if user_data:
        user_profile = {
            'name': user_data[1] if len(user_data) > 1 else "No name provided",
            'age': user_data[2] if len(user_data) > 2 else "No age provided",
            'height': user_data[3] if len(user_data) > 3 else "No height provided",
            'weight': user_data[4] if len(user_data) > 4 else "No weight provided",
            'gender': user_data[5] if len(user_data) > 5 else "No gender provided",
            'activity_level': user_data[6] if len(user_data) > 6 else "No activity level provided",
            'notes': user_data[7] if len(user_data) > 7 else "No notes provided",
            'goals': user_data[8] if len(user_data) > 8 else "No goals provided"
        }

        user_profile_str = ", ".join([f"{key.capitalize()}: {value}" for key, value in user_profile.items()])
    else:
        user_profile_str = "No user data available."

    data = request.json
    user_input = data.get('user_input')

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": base_prompt_template},
            {"role": "user", "content": user_profile_str},
            {"role": "user", "content": user_input}
        ],
        max_tokens=200,
        temperature=0.2,
    )
    message = response.choices[0].message['content'].strip()

    print(user_profile_str)

    # Format the message for better readability
    formatted_message = message.replace("\n", "<br>").replace("- ", "• ")

    return jsonify({'message': f"<strong>Trainer:</strong><br>{formatted_message}"})

@app.route('/nutrition', methods=['POST'])
def nutrition():
    data = request.json
    name = data.get('name')
    age = data.get('age')
    height = data.get('height')
    weight = data.get('weight')
    gender = data.get('gender')
    activity_level = data.get('activity_level')
    goals = data.get('goals')
    
    user_profile = f"Name: {name}, Age: {age}, Height: {height}, Weight: {weight} lbs, Gender: {gender}, Activity Level: {activity_level}, Goals: {goals}"
    
    prompt = f"{base_prompt_template}\nUser Profile: {user_profile}\n\nCalculate the average daily calories, protein, carbs, and fats needed to reach their goals."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": base_prompt_template},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200,
        temperature=0.2,
    )
    
    message = response.choices[0].message['content'].strip()
    return jsonify({'message': message})



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
