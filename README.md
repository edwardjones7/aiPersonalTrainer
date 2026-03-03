# AI Personal Trainer 🏋️‍♂️

An intelligent fitness consultation application that creates personalized workout and nutrition recommendations based on your unique profile.

![Python](https://img.shields.io/badge/Python-45.6%25-3776AB?style=flat&logo=python&logoColor=white)
![HTML](https://img.shields.io/badge/HTML-18.3%25-E34F26?style=flat&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-19.6%25-1572B6?style=flat&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-16.5%25-F7DF1E?style=flat&logo=javascript&logoColor=black)

---

## 📋 Overview

AI Personal Trainer is a web application that collects user information including height, weight, activity level, fitness goals, and personal notes, then leverages AI to provide expert-level fitness consultation tailored to each individual.

### How It Works

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   User Input    │────►│   AI Engine     │────►│  Personalized   │
│                 │     │                 │     │  Consultation   │
│ • Height        │     │ • Analysis      │     │                 │
│ • Weight        │     │ • Processing    │     │ • Workout Plan  │
│ • Activity      │     │ • Generation    │     │ • Nutrition     │
│ • Goals         │     │                 │     │ • Tips          │
│ • Notes         │     │                 │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

---

## ✨ Features

- **Personalized Profile** — Input your physical stats and fitness goals
- **Activity Level Assessment** — Tailored recommendations based on your current activity level
- **AI-Powered Consultation** — Intelligent analysis and expert fitness advice
- **Goal-Oriented Planning** — Whether you want to lose weight, build muscle, or improve endurance
- **Custom Notes** — Add specific requirements, injuries, or preferences
- **Web-Based Interface** — Access from any device with a browser

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/edwardjones7/aiPersonalTrainer.git
   cd aiPersonalTrainer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables** (if using an AI API)
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   ```
   http://localhost:5000
   ```

---

## 📁 Project Structure

```
aiPersonalTrainer/
├── AI Personal Trainer/    # Main application directory
│   ├── app.py              # Flask/Python backend
│   ├── templates/          # HTML templates
│   │   └── index.html
│   ├── static/
│   │   ├── css/            # Stylesheets
│   │   └── js/             # JavaScript files
│   └── ...
└── README.md
```

---

## 💡 Usage

1. **Enter Your Profile**
   - Height (feet/inches or cm)
   - Weight (lbs or kg)
   - Current activity level (sedentary, moderate, active, very active)

2. **Define Your Goals**
   - Weight loss
   - Muscle building
   - Endurance improvement
   - General fitness
   - Sport-specific training

3. **Add Notes** (Optional)
   - Dietary restrictions
   - Previous injuries
   - Available equipment
   - Time constraints

4. **Get Your Consultation**
   - Receive AI-generated workout recommendations
   - Nutrition guidance
   - Progress tracking tips

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Python (Flask/FastAPI) |
| **Frontend** | HTML, CSS, JavaScript |
| **AI/ML** | OpenAI API / Custom Model |
| **Styling** | CSS3 |

---

## 📊 Input Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| Height | User's height | 5'10" or 178 cm |
| Weight | Current weight | 175 lbs or 79 kg |
| Activity Level | Daily activity | Sedentary / Moderate / Active |
| Goals | Fitness objectives | Build muscle, Lose fat |
| Notes | Additional context | "Bad knee, no running" |

---

## 🔮 Future Enhancements

- [ ] Progress tracking dashboard
- [ ] Workout video demonstrations
- [ ] Meal planning integration
- [ ] Mobile app version
- [ ] Wearable device sync
- [ ] Community features

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## ⚠️ Disclaimer

This application provides general fitness information and AI-generated recommendations. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult with a qualified healthcare provider or certified personal trainer before starting any new exercise program.

---

## 📬 Contact

Edward Jones - [@edwardjones7](https://github.com/edwardjones7)

Project Link: [https://github.com/edwardjones7/aiPersonalTrainer](https://github.com/edwardjones7/aiPersonalTrainer)
