import streamlit as st
from dotenv import load_dotenv

def main():
     st.set_page_config(page_title="Acumen PDF - Chat unlimited with Multiple PDFS",page_icon=":books:")

     st.header("Acumen PDF - Chat unlimited with Multiple PDFS:books:")
     st.text_input("Ask a question about your document: ")

     with st.sidebar:
          st.subheader("Your Documents")
          st.file_uploader("Upload your PDFs here and click on 'Process'")
          st.button('Process')




if __name__=='__main__':
     main()