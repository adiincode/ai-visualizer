# 🐍 Python AI Visualizer

### Turn Python code into a visual, step-by-step learning experience.

**Python AI Visualizer** is an interactive learning tool that helps beginners understand **what actually happens when their Python code runs**.

Instead of simply showing the final output, it breaks execution into individual steps, tracks variable changes, highlights the currently executed line, and uses AI to explain the complete execution in simple language.

> **Write code → Run it → Watch it execute → Understand why it works.**

🌐 **Live Demo:**

---

## 💡 The Problem

Learning Python is easy until a beginner reaches code like:

```python
x = 10

for i in range(3):
    x += 20

print(x)
```

A beginner may understand the syntax, but still wonder:

* What happens inside the loop?
* How does `x` change after every iteration?
* Which line executes first?
* What is the value of each variable at a particular moment?
* Why does the final output become `70`?

Most coding platforms show the **code and final output**.

But understanding programming requires seeing the **journey between them**.

That's the problem Python AI Visualizer is designed to solve.

---

# 🚀 What is Python AI Visualizer?

Python AI Visualizer combines:

### 🐍 Python Execution Tracing

Tracks the execution of Python code line-by-line.

### 📊 Interactive Visualization

Lets users move through execution steps and inspect variable states.

### 🤖 AI Explanation

Uses an LLM to explain the code and its execution in beginner-friendly language.

Together, these turn static code into an interactive learning experience.

---

# ⭐ Our USP

## **Don't just see the output. See how Python reaches it.**

That's the core idea behind Python AI Visualizer.

Most beginner tools answer:

> **"What is the output?"**

Python AI Visualizer focuses on:

> **"What happened at every step that produced this output?"**

The product connects three things that beginners usually have to understand separately:

```text
Python Code
     ↓
Actual Execution
     ↓
Variable State Changes
     ↓
Visual Timeline
     ↓
AI Explanation
```

This makes the tool particularly useful for understanding:

* Loops
* Variables
* Conditions
* Assignments
* Function execution
* Step-by-step program flow
* Beginner programming mistakes

---

# ✨ Key Features

## 1. 📝 Write Python Code

Users can directly enter Python code into the application.

Example:

```python
x = 10

for i in range(3):
    x += 20

print(x)
```

---

## 2. ▶️ Execute & Trace

Instead of treating the program as one black box, the application captures its execution history.

For example:

```text
Step 1 → x = 10
Step 2 → loop starts
Step 3 → x = 30
Step 4 → x = 50
Step 5 → x = 70
Step 6 → print(x)
```

---

## 3. 📊 Interactive Execution Timeline

Users can move through execution using a step selector.

At each step they can inspect:

* Current line
* Variable values
* Execution state
* Code being executed

This creates a simple mental model of how a program runs.

---

## 4. 🎯 Current Line Highlighting

The currently executed line is visually highlighted.

Instead of asking:

> "Which line is Python executing?"

the user can **see it immediately**.

---

## 5. 📦 Variable State Tracking

The application shows how variables change during execution.

Example:

| Step | Variable | Value |
| ---- | -------- | ----: |
| 1    | `x`      |    10 |
| 2    | `x`      |    30 |
| 3    | `x`      |    50 |
| 4    | `x`      |    70 |

This is especially useful for understanding loops and assignments.

---

## 6. 🤖 AI Code Explanation

After execution, users can ask the AI to explain the program.

The AI considers:

* Original source code
* Execution history
* Variable changes
* Loop behaviour
* Final output

The explanation is structured into beginner-friendly sections:

1. What the code does
2. Line-by-line explanation
3. Execution steps
4. Loop explanation
5. Final output
6. Real-life analogy
7. Common beginner mistakes
8. Short summary

---

# 🧠 Why This is Different

Python AI Visualizer isn't designed to replace a coding environment.

It is designed to sit **between writing code and understanding code**.

Think of it as:

```text
Traditional Learning

Code → Run → Output
              ↓
          "Why?" 🤔


Python AI Visualizer

Code
 ↓
Execution
 ↓
Step-by-step state
 ↓
Visual understanding
 ↓
AI explanation
 ↓
"Now I understand." 💡
```

---

# 🎓 Who is it for?

### 👨‍🎓 Students

Understand programming fundamentals without getting lost in execution flow.

### 👩‍🏫 Teachers

Use execution visualization to demonstrate programming concepts in class.

### 🌱 Python Beginners

Understand loops, variables and program flow visually.

### 💻 Coding Learners

Debug their mental model of how Python executes code.

### 🧑‍💻 Educators

Use it as a lightweight interactive teaching aid.

---

# 🛠️ How It Works

The product uses a simple pipeline:

```text
                User
                 │
                 ▼
          Python Source Code
                 │
                 ▼
          PythonTracer
                 │
                 ▼
       Execution History
                 │
        ┌────────┴────────┐
        ▼                 ▼
  Visualization       AI Analysis
        │                 │
        ▼                 ▼
 Variable States     Explanation
        │                 │
        └────────┬────────┘
                 ▼
          Learning Experience
```

### Core Components

| Component       | Purpose                                                     |
| --------------- | ----------------------------------------------------------- |
| Python          | Core programming language                                   |
| Streamlit       | Interactive web interface                                   |
| Python Tracer   | Captures execution behaviour                                |
| Execution State | Stores execution information                                |
| Groq API        | Provides AI-powered explanations                            |
| LLM             | Converts execution data into beginner-friendly explanations |

---

# 🧩 Tech Stack

```text
Frontend / UI
└── Streamlit

Core
└── Python

Execution Analysis
└── Python tracing

AI Layer
└── Groq API
└── LLM

Environment
└── python-dotenv
```

---

# 🚀 Getting Started

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai_visualizer.git
cd ai_visualizer
```

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure the API key

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

**Never commit `.env` to GitHub.**

---

## 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 📁 Project Structure

```text
ai_visualizer/
│
├── app.py
│       └── Streamlit application
│
├── model.py
│       └── AI explanation engine
│
├── tracer.py
│       └── Python execution tracer
│
├── execution_state.py
│       └── Execution state/history management
│
├── requirements.txt
│       └── Project dependencies
│
├── .gitignore
│       └── Files excluded from Git
│
└── README.md
```

---

# 🔮 Product Roadmap

Python AI Visualizer is currently focused on the fundamentals of Python execution.

Future versions can expand the product into a more complete programming learning platform.

### Planned Ideas

* [ ] Function call visualization
* [ ] Call stack visualization
* [ ] Condition/branch visualization
* [ ] Better loop animation
* [ ] Data structure visualization
* [ ] List / dictionary state tracking
* [ ] Error explanation
* [ ] Debugging assistant
* [ ] Execution timeline animation
* [ ] Interactive quizzes
* [ ] Beginner learning mode
* [ ] Teacher/classroom mode
* [ ] Support for additional programming languages

---

# 🌟 Product Vision

The long-term goal is simple:

> **Make program execution understandable, not mysterious.**

Programming shouldn't feel like:

```text
"I wrote the code.
It gave me this output.
I have no idea why."
```

It should feel like:

```text
"I can see what Python is doing.
I can see how my variables change.
I understand why the output happened."
```

Python AI Visualizer is a step toward that experience.

---

# 🤝 Contributing

Contributions, ideas and feedback are welcome.

If you have an idea that could make programming easier to understand, feel free to open an issue or submit a pull request.

---

# 📜 License

This project is intended for educational and learning purposes.

---

## Built with 🐍 + 🤖 + ☕

**Python AI Visualizer**

### *See the code. See the execution. Understand the logic.*
