🩺 Medical Symptom Checker & PDF Report Generator
Real-World AI Assistant for Safer, Smarter Self-Assessment
Built with Python, Streamlit, OpenAI GPT, and PDF Export

🚀 Overview
Medical Symptom Checker is a GenAI-powered assistant that helps users enter symptoms in natural language, get instant AI-generated insights, view only trusted medical sources, and download a clean PDF report—all within a privacy-focused, user-friendly Streamlit web app.

Safety-First: All outputs include clear disclaimers, no diagnoses, and direct links to reputable medical organizations.
Production-Ready Patterns: Includes OpenAI API integration, modular Python code, and PDF report export.
Portfolio-Level Design: Demonstrates prompt engineering, external API orchestration, UI/UX, and information retrieval best practices.

🌟 Features

Natural Language Input: Users describe symptoms just like chatting.
LLM-Generated Insights: GPT-3.5/4 provides possible conditions (not a diagnosis!), with human-friendly advice.
Curated Medical Resources: Keyword-matched, authoritative links for further reading.
PDF Export: Download a professionally formatted report—ideal for sharing with healthcare providers.
Streamlit UI: Instantly accessible in the browser.
No Login Needed: Local privacy by default.

💡 Why This App?
Beyond ChatGPT: Purpose-built UX, consistent safety, and trusted link curation—more than just prompting a chatbot.
Expandable: Easy to add history, user accounts, reminders, localization, or new health fields.
Enterprise Potential: Can be white-labeled or integrated into health portals, clinics, or telemedicine solutions.

🛠️ Tech Stack
Python 3.9+
Streamlit (web app)
OpenAI API (LLM)
FPDF (PDF report generation)
python-dotenv (config/secrets management)

⚡ Quickstart
1. Clone

2. Install Dependencies
pip install -r requirements.txt

3. Set Up OpenAI API Key
Create a .env file in the project root:
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx

4. Run the App
streamlit run main.py
✨ Usage
Describe your symptoms in the input box.
Click "Check Symptoms" to get AI-generated possible conditions, plain-language explanations, and safety advice.
View trusted resource links for more information.
Download your PDF report—perfect for sharing with a doctor.
Read and respect the disclaimer! This app is not a replacement for professional medical advice.

📁 File Structure
symptom_checker/
├── main.py
├── requirements.txt
├── .env             # Your API key
🔒 Privacy & Safety
No data is stored; all logic is local except the (encrypted) OpenAI API call.
All advice is strictly general; the app never diagnoses or stores personal info.
Includes strong, unavoidable disclaimers in all outputs.

📄 License
MIT License

⭐ Recruiter Notes
GenAI prompt safety
API engineering
Streamlit UI/UX
PDF export patterns
Expandability

Contact: Bhavesh Kalluru
