# 🍽️ AI Restaurant Idea Generator

An AI-powered Streamlit application that generates a complete restaurant concept from simple business inputs.

## Features

- Generate a restaurant name and tagline
- Create a complete restaurant concept
- Identify the target audience
- Suggest ambience and theme
- Generate signature dishes
- Create a sample menu with estimated prices
- Suggest pricing strategy
- Generate marketing ideas
- Generate unique selling points
- Create a simple launch plan
- Download the generated idea as JSON

## Tech Stack

- Python
- Streamlit
- OpenAI API
- Prompt Engineering
- python-dotenv

## Project Structure

```text
AI-Restaurant-Idea-Generator/
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Setup

### 1. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Create your environment file

Copy `.env.example` to `.env`:

```powershell
Copy-Item .env.example .env
```

Open `.env` and replace:

```text
OPENAI_API_KEY=your_api_key_here
```

with your API key.

**Never upload `.env` to GitHub.** It is already included in `.gitignore`.

### 4. Run the application

```powershell
streamlit run app.py
```

The browser will open the Streamlit application.

## Example Input

```text
Cuisine: Indian
Location: Bhubaneswar, India
Budget: Medium
Target Customers: College Students
Theme: Trendy / Instagrammable
Food Preferences: Vegetarian, Spicy
```

The AI then creates a restaurant concept, menu, signature dishes, pricing strategy, marketing plan and launch plan.

## GitHub

Before pushing to GitHub, verify:

```powershell
git status
```

Make sure `.env` is NOT listed as a file to be committed.

Then:

```powershell
git init -b main
git add .
git commit -m "Initial commit"
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```
