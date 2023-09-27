import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS


def get_pdf_text(pdf_docs):
     'Function to read pdf and extract text from all uploaded PDFs'
     text = ""
     for pdf in pdf_docs:
          pdf_reader = PdfReader(pdf)
          for page in pdf_reader.pages:
               text += page.extract_text()

     return text


def get_text_chunks(raw_text):
     'Function to split raw extracted data into chunks using langchain'
     text_splitter = CharacterTextSplitter(
          separator="\n",
          chunk_size=1000,
          chunk_overlap=100,
          length_function=len         
     )

     chunks = text_splitter.split_text(raw_text)
     return chunks


def get_vector_store(text_chunks):
     'Create a vector store using FAISS'
     embeddings = OpenAIEmbeddings()
     vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
     return vectorstore


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
                    #st.write(raw_text)
               
                    #Extract the chunks of text
                    text_chunks = get_text_chunks(raw_text)
                    st.write(text_chunks)

                    #Create vector store
                    vector_store = get_vector_store(text_chunks)



if __name__=='__main__':
     main()