import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader

def get_pdf_text(pdf_docs):
     text = ""
     for pdf in pdf_docs:
          pdf_reader = PdfReader(pdf)
          for page in pdf_reader.pages:
               text += page.extract_text()

     return text


def main():
     load_dotenv()
     st.set_page_config(page_title="Acumen PDF - Chat unlimited with Multiple PDFS",page_icon=":books:")

     st.header("Acumen PDF - Chat unlimited with Multiple PDFS:books:")
     st.text_input("Ask a question about your document: ")

     with st.sidebar:
          st.subheader("Your Documents")
          pdf_docs = st.file_uploader("Upload your PDFs here and click on 'Process'",accept_multiple_files=True)
          if st.button('Process'):
               with st.spinner("Processing"):
                    #Extract the pdf texts
                    
                    raw_text = get_pdf_text(pdf_docs)

                    #Extract the chunks of text


                    #Create vector store




if __name__=='__main__':
     main()