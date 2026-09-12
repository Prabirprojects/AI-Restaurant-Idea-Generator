# 🍽️ AI Restaurant Idea Generator

> **An AI-powered restaurant concept generator that transforms simple business requirements into a complete, structured restaurant business idea.**

The **AI Restaurant Idea Generator** is a Generative AI application built with **Python and Streamlit**. Users provide details such as cuisine, location, budget, target customers, theme, and food preferences, and the application uses an LLM to generate a complete restaurant concept.

The generated result includes the **restaurant name, tagline, concept, target audience, ambience, signature dishes, sample menu, pricing strategy, marketing ideas, unique selling points, and launch plan**.

---

## 🚀 Live Project

**GitHub Repository:**
https://github.com/Prabirprojects/AI-Restaurant-Idea-Generator

---

## ✨ Features

* 🍴 Generate creative restaurant names
* 🏷️ Generate a restaurant tagline
* 💡 Generate a complete restaurant concept
* 🎯 Identify the target audience
* 🎨 Suggest restaurant ambience and theme
* 🍽️ Generate signature dishes
* 📋 Create a sample menu
* 💰 Suggest estimated menu pricing
* 📈 Generate a pricing strategy
* 📢 Generate marketing ideas
* ⭐ Generate unique selling points (USPs)
* 🚀 Create a basic restaurant launch plan
* 📥 Download the generated restaurant idea as JSON
* 🧩 Structured AI output using Pydantic models
* 🖥️ Interactive web interface using Streamlit

---

## 🧠 How It Works

The application follows a simple Generative AI pipeline:

```text
User Input
    ↓
Restaurant Requirements
    ↓
Prompt Engineering
    ↓
LangChain
    ↓
OpenRouter LLM
    ↓
Structured AI Response
    ↓
Pydantic Validation
    ↓
Streamlit UI
    ↓
Complete Restaurant Concept
```

### Example

A user can provide:

```text
Cuisine: Indian
Location: Bhubaneswar, India
Budget: Medium
Target Customers: College Students
Theme: Trendy / Instagrammable
Food Preferences: Vegetarian, Spicy
```

The AI then generates a complete restaurant business concept based on those requirements.

---

## 🛠️ Tech Stack

| Technology            | Purpose                                  |
| --------------------- | ---------------------------------------- |
| 🐍 Python             | Application development                  |
| 🎈 Streamlit          | Interactive web interface                |
| 🔗 LangChain          | LLM orchestration and prompt management  |
| 🤖 OpenRouter         | Access to the selected LLM               |
| 📦 Pydantic           | Structured output validation             |
| 🔐 python-dotenv      | Environment variable management          |
| 🧠 Prompt Engineering | Controlling and structuring AI responses |
| 📄 JSON               | Structured output and download format    |

---

## 🏗️ Project Architecture

```text
                    ┌──────────────────────┐
                    │      User Input      │
                    │ Cuisine / Location   │
                    │ Budget / Theme etc.  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Streamlit App      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Prompt Template    │
                    │     LangChain        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     OpenRouter       │
                    │        LLM           │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Structured Response  │
                    │       Pydantic       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Restaurant Idea    │
                    │ Menu / Pricing / USP │
                    │ Marketing / Launch   │
                    └──────────────────────┘
```

---

## 📂 Project Structure

```text
AI-Restaurant-Idea-Generator/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variable template
├── .gitignore              # Ignored files and secrets
├── LICENSE                 # Project license
└── README.md               # Project documentation
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Prabirprojects/AI-Restaurant-Idea-Generator.git
```

```bash
cd AI-Restaurant-Idea-Generator
```

---

### 2. Create a virtual environment

#### Windows PowerShell

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\Activate.ps1
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create a `.env` file in the project root.

Example:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

> ⚠️ **Never upload your real API key to GitHub.**

The `.env` file should remain ignored by Git.

The repository includes `.env.example` as a safe template.

---

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🖥️ Application Workflow

### Step 1 — Enter Restaurant Requirements

Provide information such as:

* Cuisine
* Location
* Budget
* Target customers
* Restaurant theme
* Food preferences

### Step 2 — Generate

The application sends the requirements to the LLM through OpenRouter.

### Step 3 — AI Processing

LangChain manages the prompt and LLM interaction.

### Step 4 — Structured Output

The generated response is validated using Pydantic.

### Step 5 — View Result

The application displays:

* Restaurant name
* Tagline
* Concept
* Target audience
* Ambience
* Signature dishes
* Menu
* Pricing strategy
* Marketing ideas
* USPs
* Launch plan

### Step 6 — Download

The generated restaurant concept can be downloaded as a JSON file.

---

## 📸 Screenshots

> Add screenshots of your working Streamlit application here.

Recommended screenshots:

1. **Input screen**
2. **Generated restaurant concept**
3. **Menu and pricing section**
4. **Marketing and launch plan**
5. **JSON download/output**

Example:

```text
screenshots/
├── input.png
├── generated-result.png
└── menu.png
```

---

## 💡 Example Generated Concept

### Restaurant Name

**Spice Route**

### Tagline

**Experience the flavors of India, reimagined.**

### Concept

A modern Indian restaurant combining traditional Indian flavors with contemporary presentation.

### Signature Dishes

* Butter Chicken Brioche
* Tandoori Paneer Tacos
* Saffron Kulfi Cheesecake

### Target Audience

Young professionals, college students, food enthusiasts, and customers interested in modern Indian cuisine.

---

## 🎯 Skills Demonstrated

This project demonstrates practical experience with:

* Generative AI
* Large Language Models
* Prompt Engineering
* LangChain
* OpenRouter API
* Pydantic Data Validation
* Structured AI Output
* Python
* Streamlit
* Environment Variable Management
* JSON Processing
* Error Handling
* Git & GitHub

---

## 🔐 Security

API credentials are managed through environment variables.

Sensitive files such as `.env` should never be committed to GitHub.

The repository only contains `.env.example` with placeholder values.

---

## 🧪 Error Handling

The application includes handling for common AI-generation problems such as:

* Invalid or incomplete model responses
* JSON parsing failures
* Structured-output validation errors
* Missing API configuration
* Unexpected LLM responses

This helps prevent the application from crashing when the model returns an unexpected response.

---

## 🚧 Future Improvements

Planned improvements include:

* [ ] Add restaurant logo generation
* [ ] Add PDF export
* [ ] Add multiple LLM/model selection
* [ ] Add conversation history
* [ ] Add restaurant concept regeneration
* [ ] Add multilingual support
* [ ] Add deployment on Streamlit Cloud
* [ ] Add automated tests
* [ ] Add logging and monitoring
* [ ] Improve structured-output reliability

---

## 📚 What I Learned

While building this project, I worked with:

1. Generative AI application development
2. LLM prompt design
3. LangChain integration
4. OpenRouter API integration
5. Pydantic structured data models
6. JSON parsing and validation
7. Streamlit application development
8. Environment-variable security
9. Error handling for LLM applications
10. Git and GitHub project management

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you would like to contribute:

```bash
git clone https://github.com/Prabirprojects/AI-Restaurant-Idea-Generator.git
```

Create a new branch, make your changes, and submit a pull request.

---

## 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more information.

---

## 👨‍💻 Author

**Prabir Pattanayak**

AI/ML & Data Science Enthusiast

Interested in:

* Artificial Intelligence
* Machine Learning
* Generative AI
* Data Science
* Large Language Models

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.

**GitHub:**
https://github.com/Prabirprojects/AI-Restaurant-Idea-Generator
