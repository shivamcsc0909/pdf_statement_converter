<<<<<<< HEAD
import os
import time
import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile
from typing import Tuple
from pdf_processor import PDFProcessor
from config import MAX_FILE_SIZE_MB, SUPPORTED_MIME_TYPES, OUTPUT_DIR
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set page config
st.set_page_config(
    page_title="PDF Bank Statement to CSV Converter",
    page_icon=":bank:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .stProgress > div > div > div > div {
        background-color: #1f77b4;
    }
    .st-eb {
        padding: 10px;
        border-radius: 5px;
    }
    .reportview-container .main .block-container {
        padding-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

def validate_uploaded_file(uploaded_file: UploadedFile) -> Tuple[bool, str]:
    """Validate the uploaded PDF file"""
    if uploaded_file is None:
        return False, "No file uploaded"
    
    if uploaded_file.type not in SUPPORTED_MIME_TYPES:
        return False, "Only PDF files are supported"
    
    file_size = uploaded_file.size / (1024 * 1024)  # Convert to MB
    if file_size > MAX_FILE_SIZE_MB:
        return False, f"File size exceeds {MAX_FILE_SIZE_MB}MB limit"
    
    return True, "File is valid"

def save_uploaded_file(uploaded_file: UploadedFile) -> str:
    """Save uploaded file to temporary location"""
    temp_dir = os.path.join(os.getcwd(), "temp_uploads")
    os.makedirs(temp_dir, exist_ok=True)
    
    file_path = os.path.join(temp_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    return file_path

def display_results(df: pd.DataFrame, process_time: float):
    """Display extraction results"""
    st.success("✅ Bank statement data extracted successfully!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Transactions", len(df))
    with col2:
        st.metric("Processing Time", f"{process_time:.2f} seconds")
    
    st.subheader("Statement Preview")
    st.dataframe(df.head(100), height=400)
    
    st.subheader("Financial Summary")
    if 'amount' in df.columns or 'balance' in df.columns:
        amount_col = 'amount' if 'amount' in df.columns else 'balance'
        st.metric("Total Amount", f"₹{df[amount_col].sum():,.2f}")

def main():
    """Main Streamlit application"""
    st.title("📄 PDF Bank Statement to CSV Converter")
    st.markdown("""
        Convert your bank statement PDFs into clean, structured CSV files.
        Works best with digital PDF statements containing clear tables.
    """)
    
    with st.expander("ℹ️ How to use this tool"):
        st.write("""
            1. Upload your bank statement PDF (must be searchable/text-based)
            2. Click 'Process Statement'
            3. Preview and verify the extracted transactions
            4. Download the CSV file
            5. For best results, ensure your statement has clear table borders
        """)
    
    # File upload section
    uploaded_file = st.file_uploader(
        "Upload Bank Statement PDF", 
        type=["pdf"],
        help="Supported banks: HDFC, ICICI, SBI, Axis, etc."
    )
    
    if uploaded_file is not None:
        # Validate file
        is_valid, validation_msg = validate_uploaded_file(uploaded_file)
        if not is_valid:
            st.error(validation_msg)
            return
        
        st.success(validation_msg)
        st.caption(f"Filename: {uploaded_file.name} | Size: {uploaded_file.size/(1024*1024):.2f} MB")
        
        if st.button("Process Statement", type="primary", help="Extract transaction data"):
            with st.spinner("Processing your bank statement..."):
                start_time = time.time()
                temp_file_path = save_uploaded_file(uploaded_file)
                
                try:
                    # Initialize and process PDF
                    processor = PDFProcessor(temp_file_path)
                    df = processor.extract_tabular_data()  # Using the new focused method
                    csv_path = processor.save_to_csv(df)
                    process_time = time.time() - start_time
                    
                    # Display results
                    display_results(df, process_time)
                    
                    # Download button
                    with open(csv_path, "rb") as f:
                        st.download_button(
                            label="Download CSV",
                            data=f,
                            file_name=f"bank_statement_{os.path.basename(csv_path)}",
                            mime="text/csv",
                            help="Contains all extracted transactions"
                        )
                    
                except ValueError as e:
                    st.error(f"Extraction failed: {str(e)}")
                    st.info("""
                        Troubleshooting tips:
                        - Ensure PDF has visible table borders
                        - Try a different statement format
                        - Check if PDF is password protected
                        - Contact support if issue persists
                    """)
                except Exception as e:
                    logger.exception("Unexpected error")
                    st.error("An unexpected error occurred. Please try again.")
                finally:
                    if os.path.exists(temp_file_path):
                        os.remove(temp_file_path)
    
    # Footer
    st.markdown("---")
    st.caption("""
        Note: This tool runs in your browser. No files are stored on our servers.
        For support, please contact the developer.
    """)

if __name__ == "__main__":
=======
import os
import time
import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile
from typing import Tuple
from pdf_processor import PDFProcessor
from config import MAX_FILE_SIZE_MB, SUPPORTED_MIME_TYPES, OUTPUT_DIR
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set page config
st.set_page_config(
    page_title="PDF Bank Statement to CSV Converter",
    page_icon=":bank:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .stProgress > div > div > div > div {
        background-color: #1f77b4;
    }
    .st-eb {
        padding: 10px;
        border-radius: 5px;
    }
    .reportview-container .main .block-container {
        padding-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

def validate_uploaded_file(uploaded_file: UploadedFile) -> Tuple[bool, str]:
    """Validate the uploaded PDF file"""
    if uploaded_file is None:
        return False, "No file uploaded"
    
    if uploaded_file.type not in SUPPORTED_MIME_TYPES:
        return False, "Only PDF files are supported"
    
    file_size = uploaded_file.size / (1024 * 1024)  # Convert to MB
    if file_size > MAX_FILE_SIZE_MB:
        return False, f"File size exceeds {MAX_FILE_SIZE_MB}MB limit"
    
    return True, "File is valid"

def save_uploaded_file(uploaded_file: UploadedFile) -> str:
    """Save uploaded file to temporary location"""
    temp_dir = os.path.join(os.getcwd(), "temp_uploads")
    os.makedirs(temp_dir, exist_ok=True)
    
    file_path = os.path.join(temp_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    return file_path

def display_results(df: pd.DataFrame, process_time: float):
    """Display extraction results"""
    st.success("✅ Bank statement data extracted successfully!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Transactions", len(df))
    with col2:
        st.metric("Processing Time", f"{process_time:.2f} seconds")
    
    st.subheader("Statement Preview")
    st.dataframe(df.head(100), height=400)
    
    st.subheader("Financial Summary")
    if 'amount' in df.columns or 'balance' in df.columns:
        amount_col = 'amount' if 'amount' in df.columns else 'balance'
        st.metric("Total Amount", f"₹{df[amount_col].sum():,.2f}")

def main():
    """Main Streamlit application"""
    st.title("📄 PDF Bank Statement to CSV Converter")
    st.markdown("""
        Convert your bank statement PDFs into clean, structured CSV files.
        Works best with digital PDF statements containing clear tables.
    """)
    
    with st.expander("ℹ️ How to use this tool"):
        st.write("""
            1. Upload your bank statement PDF (must be searchable/text-based)
            2. Click 'Process Statement'
            3. Preview and verify the extracted transactions
            4. Download the CSV file
            5. For best results, ensure your statement has clear table borders
        """)
    
    # File upload section
    uploaded_file = st.file_uploader(
        "Upload Bank Statement PDF", 
        type=["pdf"],
        help="Supported banks: HDFC, ICICI, SBI, Axis, etc."
    )
    
    if uploaded_file is not None:
        # Validate file
        is_valid, validation_msg = validate_uploaded_file(uploaded_file)
        if not is_valid:
            st.error(validation_msg)
            return
        
        st.success(validation_msg)
        st.caption(f"Filename: {uploaded_file.name} | Size: {uploaded_file.size/(1024*1024):.2f} MB")
        
        if st.button("Process Statement", type="primary", help="Extract transaction data"):
            with st.spinner("Processing your bank statement..."):
                start_time = time.time()
                temp_file_path = save_uploaded_file(uploaded_file)
                
                try:
                    # Initialize and process PDF
                    processor = PDFProcessor(temp_file_path)
                    df = processor.extract_tabular_data()  # Using the new focused method
                    csv_path = processor.save_to_csv(df)
                    process_time = time.time() - start_time
                    
                    # Display results
                    display_results(df, process_time)
                    
                    # Download button
                    with open(csv_path, "rb") as f:
                        st.download_button(
                            label="Download CSV",
                            data=f,
                            file_name=f"bank_statement_{os.path.basename(csv_path)}",
                            mime="text/csv",
                            help="Contains all extracted transactions"
                        )
                    
                except ValueError as e:
                    st.error(f"Extraction failed: {str(e)}")
                    st.info("""
                        Troubleshooting tips:
                        - Ensure PDF has visible table borders
                        - Try a different statement format
                        - Check if PDF is password protected
                        - Contact support if issue persists
                    """)
                except Exception as e:
                    logger.exception("Unexpected error")
                    st.error("An unexpected error occurred. Please try again.")
                finally:
                    if os.path.exists(temp_file_path):
                        os.remove(temp_file_path)
    
    # Footer
    st.markdown("---")
    st.caption("""
        Note: This tool runs in your browser. No files are stored on our servers.
        For support, please contact the developer.
    """)

if __name__ == "__main__":
>>>>>>> da9861285137d7690c9c82b14b5d0efeb26e646c
    main()