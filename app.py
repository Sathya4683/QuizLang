# app.py

import streamlit as st
from src.LangChain_model import initialize_model, process_file_parallel, handle_doubts_based_on_topics

# Streamlit UI
st.title("Document QA with Google Gemini")

# API Key input field
API_KEY = st.text_input("Enter your Google Gemini API Key:", type="password")

if API_KEY:
    # Initialize the model with the API key
    model = initialize_model(API_KEY)
    
    # File upload section
    uploaded_file = st.file_uploader("Choose a document", type=["docx", "pdf", "csv"])

    if uploaded_file:
        # Check if the answers and important topics are already stored in session state
        if "answers" not in st.session_state or "important_topics" not in st.session_state:
            try:
                # Process the file to extract answers and important topics
                answers, important_topics, chunks = process_file_parallel(uploaded_file, model)
                
                # Store the extracted answers and important topics in session state
                st.session_state.answers = answers
                st.session_state.important_topics = important_topics
                st.session_state.chunks = chunks

                # Display answers and important topics
                st.subheader("Final Answers:")
                st.write(st.session_state.answers)

                st.subheader("Important Topics to Ace the Exam:")
                st.write(st.session_state.important_topics)
            
            except Exception as e:
                st.error(f"Error processing the document: {e}")
        else:
            # If answers and topics are already in session state, just display them
            st.subheader("Final Answers:")
            st.write(st.session_state.answers)

            st.subheader("Important Topics to Ace the Exam:")
            st.write(st.session_state.important_topics)

        # Start the doubt Q&A session
        handle_doubts_based_on_topics(model)
    
    else:
        st.warning("Please upload a document to get started.")
else:
    st.warning("Please enter your Google Gemini API key to proceed.")
