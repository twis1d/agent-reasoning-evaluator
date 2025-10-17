# 🤖 Agent Reasoning Evaluator

### 🧠 Overview
**Agent Reasoning Evaluator** is a lightweight web app built with **Streamlit** that analyzes and annotates reasoning trajectories of AI agents.  
It simulates how intelligent agents reason, make decisions, and sometimes make logical or factual errors — allowing users to evaluate and visualize their performance.

The project was inspired by **agentic AI concepts** and practical insights from workshops on **NVIDIA NeMo Toolkit** and **AgentToolkit**.

---

### 🚀 Live Demo
👉 [https://agent-reasoning-evaluator.streamlit.app/](https://agent-reasoning-evaluator.streamlit.app/)

---

### 🧩 Features
- ✅ Upload agent reasoning data (`agent_data.json`)
- 🔍 Automatically evaluate outputs for factual or logical errors
- 🧾 Generate structured annotations (`annotations.json`)
- 📊 View accuracy metrics and error distributions
- 💾 Download annotated results
- 🌐 Clean and intuitive Streamlit interface

---

### 🧰 Tech Stack
- **Python 3.11+**
- **Streamlit**
- **Pandas**
- **JSON**

---

### 📁 Project Structure
agent-reasoning-evaluator/
│
├── app.py # Streamlit dashboard
├── evaluate_agent.py # Command-line evaluation script
├── agent_data.json # Sample reasoning trajectories
├── annotations.json # Generated annotations
├── summary.csv # Summary results
└── README.md

### ⚙️ How to Run Locally
1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/agent-reasoning-evaluator.git
   cd agent-reasoning-evaluator
2. **Install dependencies**
   pip install streamlit pandas
3. **Run the Streamlit app**
streamlit run app.py
4. Open your browser at locahost

💡 Future Enhancements

Add detailed reasoning step visualization

Integrate with real-world agent reasoning traces

Enable multi-file uploads and bulk evaluation

Add charts for reasoning accuracy trends

🧑‍💻 Author

Chinmay Kadu
Web Developer | AI Enthusiast | Agentic Systems Learner
🌐 https://agent-reasoning-evaluator.streamlit.app/
📧 chinmayrkadu@gmail.com

