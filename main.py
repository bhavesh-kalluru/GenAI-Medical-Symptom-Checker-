import os
import openai
from dotenv import load_dotenv
import streamlit as st
from fpdf import FPDF
import tempfile

# Load API Key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

TRUSTED_LINKS = [
    "https://www.mayoclinic.org",
    "https://www.webmd.com",
    "https://www.nhs.uk"
]

DISCLAIMER = (
    "\n\n[Disclaimer: This is NOT medical advice. Please consult a healthcare professional for a diagnosis.]\n"
)

def get_advice(symptoms: str) -> str:
    prompt = (
        f"A user describes the following symptoms: {symptoms}\n"
        "1. List the top 3 possible common medical conditions (not rare ones).\n"
        "2. For each, provide a brief explanation in simple language.\n"
        "3. Offer one general safety tip for the user.\n"
        "4. Remind the user to consult a doctor. Do not give a diagnosis.\n"
        "5. Format with numbered list and bullet points."
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=400,
            temperature=0.5
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error contacting OpenAI: {e}"

def get_links(symptoms: str):
    keywords = {
        "cough": "https://www.mayoclinic.org/diseases-conditions/cough/symptoms-causes/syc-20351310",
        "fever": "https://www.webmd.com/children/fever-causes-symptoms-treatments",
        "headache": "https://www.nhs.uk/conditions/headaches/",
        "stomach": "https://www.mayoclinic.org/symptoms/abdominal-pain/basics/when-to-see-doctor/sym-20050728",
        "rash": "https://www.webmd.com/skin-problems-and-treatments/guide/common-childhood-skin-problems"
    }
    links = set()
    for word in keywords:
        if word in symptoms.lower():
            links.add(keywords[word])
    if links:
        return list(links)
    return TRUSTED_LINKS

def export_to_pdf(symptoms, advice, links):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Symptom Check Report", ln=1, align='C')
    pdf.ln(4)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 8, txt=f"Symptoms: {symptoms}\n")
    pdf.multi_cell(0, 8, txt=f"Advice:\n{advice}\n")
    pdf.multi_cell(0, 8, txt="Trusted Links:")
    for link in links:
        pdf.cell(0, 8, txt=link, ln=1, link=link)
    pdf.ln(2)
    pdf.set_font("Arial", style='I', size=9)
    pdf.multi_cell(0, 7, txt=DISCLAIMER)
    # Save to a temp file and return the path
    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(temp.name)
    return temp.name

st.set_page_config(page_title="Medical Symptom Checker", page_icon="🩺", layout="centered")

st.title("🩺 Medical Symptom Checker & PDF Export")
st.write("Describe your symptoms and receive AI-generated, general advice plus trusted resource links. You can also download your result as a PDF report.")
st.warning(DISCLAIMER)

symptoms = st.text_area("Enter your symptoms here:")

if st.button("Check Symptoms"):
    if symptoms.strip() == "":
        st.error("Please enter your symptoms.")
    else:
        with st.spinner("Thinking..."):
            advice = get_advice(symptoms)
            links = get_links(symptoms)
        st.subheader("AI-Generated Advice")
        st.markdown(advice)
        st.subheader("Trusted Links")
        for l in links:
            st.markdown(f"- [{l}]({l})")
        st.info(DISCLAIMER)
        # Export to PDF
        pdf_path = export_to_pdf(symptoms, advice, links)
        with open(pdf_path, "rb") as f:
            st.download_button(
                label="Download PDF Report",
                data=f.read(),
                file_name="symptom_report.pdf",
                mime="application/pdf"
            )
