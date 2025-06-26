<<<<<<< HEAD
import os
import logging
import pandas as pd
import pdfplumber
from typing import Optional, Tuple
from config import OUTPUT_DIR, CSV_ENCODING, CSV_SEPARATOR
import numpy as np

logger = logging.getLogger(__name__)

class PDFProcessor:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        # Optimized table extraction settings for bank statements
        self.table_settings = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "lines",
            "intersection_y_tolerance": 15,
            "intersection_x_tolerance": 15,
            "explicit_vertical_lines": [],
            "explicit_horizontal_lines": []
        }

    def extract_tabular_data(self) -> pd.DataFrame:
        """
        Main method to extract and clean tabular data from bank statements
        Returns: Pandas DataFrame with structured data
        Raises: ValueError if no table data found
        """
        try:
            with pdfplumber.open(self.pdf_path) as pdf:
                all_tables = []
                
                for page in pdf.pages:
                    # Extract tables with visual debugging (uncomment to debug)
                    tables = page.extract_tables(self.table_settings)
                    
                    # Debugging: Visualize table detection (uncomment if needed)
                    # debug_img = page.to_image(resolution=200)
                    # debug_img.debug_tablefinder(self.table_settings).show()
                    
                    if tables:
                        for table in tables:
                            # Convert to DataFrame and clean
                            df = pd.DataFrame(table)
                            df = self._clean_table(df)
                            if not df.empty:
                                all_tables.append(df)

                if not all_tables:
                    raise ValueError("No tabular data detected in PDF")
                
                combined_df = pd.concat(all_tables, ignore_index=True)
                return self._structure_data(combined_df)
                
        except Exception as e:
            logger.error(f"Table extraction failed: {str(e)}")
            raise ValueError(f"Failed to extract table data: {str(e)}")

    def _clean_table(self, df: pd.DataFrame) -> pd.DataFrame:
        """Internal method to clean raw extracted table"""
        # Remove empty rows/columns
        df.replace('', np.nan, inplace=True)
        df.dropna(how='all', inplace=True)
        df.dropna(axis=1, how='all', inplace=True)
        
        # Set first row as header if it contains typical bank columns
        if any(col in str(df.iloc[0]).lower() for col in ['date', 'desc', 'amount']):
            df.columns = df.iloc[0]
            df = df[1:]
        
        return df

    def _structure_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Convert extracted data to proper bank statement format"""
        # Standardize column names
        df.columns = [str(col).strip().lower() for col in df.columns]
        
        # Convert date columns
        date_cols = [col for col in df.columns if 'date' in col]
        for col in date_cols:
            df[col] = pd.to_datetime(df[col], errors='coerce')
        
        # Convert amount columns
        amount_cols = [col for col in df.columns if any(x in col for x in ['amount', 'balance', 'debit', 'credit'])]
        for col in amount_cols:
            df[col] = pd.to_numeric(
                df[col].astype(str).str.replace('[^\d.-]', '', regex=True),
                errors='coerce'
            )
        
        return df.dropna(how='all')

    def save_to_csv(self, df: pd.DataFrame) -> str:
        """Save processed data to CSV"""
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        output_path = os.path.join(OUTPUT_DIR, 
                                 f"bank_statement_{os.path.basename(self.pdf_path)}.csv")
        df.to_csv(output_path, index=False, 
                 encoding=CSV_ENCODING, 
                 sep=CSV_SEPARATOR,
                 date_format='%Y-%m-%d')
=======
import os
import logging
import pandas as pd
import pdfplumber
from typing import Optional, Tuple
from config import OUTPUT_DIR, CSV_ENCODING, CSV_SEPARATOR
import numpy as np

logger = logging.getLogger(__name__)

class PDFProcessor:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        # Optimized table extraction settings for bank statements
        self.table_settings = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "lines",
            "intersection_y_tolerance": 15,
            "intersection_x_tolerance": 15,
            "explicit_vertical_lines": [],
            "explicit_horizontal_lines": []
        }

    def extract_tabular_data(self) -> pd.DataFrame:
        """
        Main method to extract and clean tabular data from bank statements
        Returns: Pandas DataFrame with structured data
        Raises: ValueError if no table data found
        """
        try:
            with pdfplumber.open(self.pdf_path) as pdf:
                all_tables = []
                
                for page in pdf.pages:
                    # Extract tables with visual debugging (uncomment to debug)
                    tables = page.extract_tables(self.table_settings)
                    
                    # Debugging: Visualize table detection (uncomment if needed)
                    # debug_img = page.to_image(resolution=200)
                    # debug_img.debug_tablefinder(self.table_settings).show()
                    
                    if tables:
                        for table in tables:
                            # Convert to DataFrame and clean
                            df = pd.DataFrame(table)
                            df = self._clean_table(df)
                            if not df.empty:
                                all_tables.append(df)

                if not all_tables:
                    raise ValueError("No tabular data detected in PDF")
                
                combined_df = pd.concat(all_tables, ignore_index=True)
                return self._structure_data(combined_df)
                
        except Exception as e:
            logger.error(f"Table extraction failed: {str(e)}")
            raise ValueError(f"Failed to extract table data: {str(e)}")

    def _clean_table(self, df: pd.DataFrame) -> pd.DataFrame:
        """Internal method to clean raw extracted table"""
        # Remove empty rows/columns
        df.replace('', np.nan, inplace=True)
        df.dropna(how='all', inplace=True)
        df.dropna(axis=1, how='all', inplace=True)
        
        # Set first row as header if it contains typical bank columns
        if any(col in str(df.iloc[0]).lower() for col in ['date', 'desc', 'amount']):
            df.columns = df.iloc[0]
            df = df[1:]
        
        return df

    def _structure_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Convert extracted data to proper bank statement format"""
        # Standardize column names
        df.columns = [str(col).strip().lower() for col in df.columns]
        
        # Convert date columns
        date_cols = [col for col in df.columns if 'date' in col]
        for col in date_cols:
            df[col] = pd.to_datetime(df[col], errors='coerce')
        
        # Convert amount columns
        amount_cols = [col for col in df.columns if any(x in col for x in ['amount', 'balance', 'debit', 'credit'])]
        for col in amount_cols:
            df[col] = pd.to_numeric(
                df[col].astype(str).str.replace('[^\d.-]', '', regex=True),
                errors='coerce'
            )
        
        return df.dropna(how='all')

    def save_to_csv(self, df: pd.DataFrame) -> str:
        """Save processed data to CSV"""
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        output_path = os.path.join(OUTPUT_DIR, 
                                 f"bank_statement_{os.path.basename(self.pdf_path)}.csv")
        df.to_csv(output_path, index=False, 
                 encoding=CSV_ENCODING, 
                 sep=CSV_SEPARATOR,
                 date_format='%Y-%m-%d')
>>>>>>> da9861285137d7690c9c82b14b5d0efeb26e646c
        return output_path