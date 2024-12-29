Here’s a tailored `README.md` for your GitHub repository:

````markdown
# QuizLang - Document QA with Google Gemini

QuizLang is an interactive Document Question Answering (QA) application powered by Google Gemini and LangChain. It helps users analyze documents (PDF, DOCX, or CSV format), extract answers for exam-related questions, identify important topics for exam preparation, and interact with the AI to clarify doubts on specific topics.

## Features

- **Upload Documents**: Supports PDF, DOCX, and CSV file uploads.
- **Answer Extraction**: Automatically extracts answers for questions from the uploaded documents.
- **Topic Identification**: Identifies key topics that are important for exam preparation.
- **Interactive Doubt Resolution**: Ask questions based on important topics and get AI-powered responses for clarification.

## Prerequisites

To run the application, you'll need the following:

- **Python 3.7 or higher**: Ensure you're using Python 3.7 or higher.
- **Google Gemini API Key**: You’ll need a Google Gemini API key to use the model. You can obtain this from [Google Cloud's Gemini](https://cloud.google.com/genai).

## Setup Instructions

### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/Sathya4683/QuizLang.git
cd QuizLang
```
````

### Step 2: Install Dependencies

Once you've cloned the repository, install the required dependencies using `pip`:

```bash
pip install --upgrade torch transformers langchain langchain-core langchain-community langchain_google_genai python-docx PyPDF2 pandas
```

This will install the following necessary packages:

- `torch`: Deep learning framework for model inference.
- `transformers`: For working with transformer-based models like Google Gemini.
- `langchain`: A framework for integrating AI models into applications.
- `langchain-google-genai`: Google Gemini integration.
- `python-docx`: For reading DOCX files.
- `PyPDF2`: For reading PDF files.
- `pandas`: For reading CSV files.

### Step 3: Set Up Google Gemini API Key

1. **Obtain your Google Gemini API key** from [Google Gemini](https://cloud.google.com/genai).
2. Once you have the API key, you will be prompted to enter it in the application when you run it.

### Step 4: Run the Application

To launch the app, use the following command:

```bash
streamlit run app.py
```

This will start the Streamlit server, and you can access the app in your web browser at `http://localhost:8501`.

### Step 5: Using the Application

1. **Upload a Document**:

   - Click on the file uploader in the app to upload a PDF, DOCX, or CSV file.

2. **Enter your Google Gemini API Key**:

   - When prompted, paste your Google Gemini API key into the input field.

3. **Get the Answers**:

   - The app will automatically extract answers to the exam-related questions from the uploaded document.

4. **View Important Topics**:

   - The app will display the important topics based on the document’s content.

5. **Ask Doubts**:
   - You can interact with the AI by typing in doubts related to important topics. The AI will respond with explanations.

### Step 6: Customize the Application

If you wish to customize the app, you can edit the following files:

- `LangChain_model.py`: This contains the functions for initializing the model, processing documents, extracting answers, identifying important topics, and handling Q&A.
- `app.py`: The main Streamlit app file that sets up the UI and calls functions from `LangChain_model.py`.

### Troubleshooting

- **Error: "API key is invalid"**:

  - Ensure you have entered a valid Google Gemini API key.

- **Error: "Unsupported file type"**:

  - Verify that the uploaded file is in PDF, DOCX, or CSV format.

- **Error: "No questions found"**:
  - Ensure your document contains questions that can be extracted for answering.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- This project leverages LangChain and Google Gemini for powerful document analysis and question answering.
