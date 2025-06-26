<<<<<<< HEAD
import re
import logging
from datetime import datetime
from dateutil.parser import parse
from typing import Optional, Union
import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)

def clean_text(text: str) -> str:
    """Clean text by removing extra spaces and special characters"""
    if not isinstance(text, str):
        return str(text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'[^\w\s.,-]', '', text)
    return text

def parse_date(date_str: str) -> Optional[str]:
    """Parse various date formats into YYYY-MM-DD format"""
    try:
        if pd.isna(date_str) or date_str in ['', ' ', None]:
            return None
        date_obj = parse(date_str, dayfirst=True)
        return date_obj.strftime(DATE_FORMAT)
    except (ValueError, TypeError) as e:
        logger.warning(f"Could not parse date: {date_str} - {str(e)}")
        return None

def clean_amount(amount: Union[str, float]) -> Optional[float]:
    """Clean and convert amount strings to float"""
    if pd.isna(amount) or amount in ['', ' ', None]:
        return None
    
    try:
        if isinstance(amount, (int, float)):
            return float(amount)
        
        # Remove currency symbols and thousands separators
        cleaned = re.sub(r'[^\d.-]', '', str(amount))
        if cleaned in ['', '.', '-']:
            return None
        return float(cleaned)
    except (ValueError, TypeError) as e:
        logger.warning(f"Could not parse amount: {amount} - {str(e)}")
        return None

def validate_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Validate and clean the extracted dataframe"""
    if df.empty:
        return df
    
    # Clean text columns
    text_cols = df.select_dtypes(include=['object']).columns
    for col in text_cols:
        df[col] = df[col].apply(clean_text)
    
    # Convert date columns
    date_cols = [col for col in df.columns if 'date' in col.lower()]
    for col in date_cols:
        df[col] = df[col].apply(parse_date)
    
    # Convert amount columns
    amount_cols = [col for col in df.columns if any(x in col.lower() for x in ['amount', 'debit', 'credit', 'balance'])]
    for col in amount_cols:
        df[col] = df[col].apply(clean_amount)
    
    # Drop empty rows and columns
    df.replace('', np.nan, inplace=True)
    df.dropna(how='all', inplace=True)
    df.dropna(axis=1, how='all', inplace=True)
    
    return df 
=======
import re
import logging
from datetime import datetime
from dateutil.parser import parse
from typing import Optional, Union
import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)

def clean_text(text: str) -> str:
    """Clean text by removing extra spaces and special characters"""
    if not isinstance(text, str):
        return str(text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'[^\w\s.,-]', '', text)
    return text

def parse_date(date_str: str) -> Optional[str]:
    """Parse various date formats into YYYY-MM-DD format"""
    try:
        if pd.isna(date_str) or date_str in ['', ' ', None]:
            return None
        date_obj = parse(date_str, dayfirst=True)
        return date_obj.strftime(DATE_FORMAT)
    except (ValueError, TypeError) as e:
        logger.warning(f"Could not parse date: {date_str} - {str(e)}")
        return None

def clean_amount(amount: Union[str, float]) -> Optional[float]:
    """Clean and convert amount strings to float"""
    if pd.isna(amount) or amount in ['', ' ', None]:
        return None
    
    try:
        if isinstance(amount, (int, float)):
            return float(amount)
        
        # Remove currency symbols and thousands separators
        cleaned = re.sub(r'[^\d.-]', '', str(amount))
        if cleaned in ['', '.', '-']:
            return None
        return float(cleaned)
    except (ValueError, TypeError) as e:
        logger.warning(f"Could not parse amount: {amount} - {str(e)}")
        return None

def validate_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Validate and clean the extracted dataframe"""
    if df.empty:
        return df
    
    # Clean text columns
    text_cols = df.select_dtypes(include=['object']).columns
    for col in text_cols:
        df[col] = df[col].apply(clean_text)
    
    # Convert date columns
    date_cols = [col for col in df.columns if 'date' in col.lower()]
    for col in date_cols:
        df[col] = df[col].apply(parse_date)
    
    # Convert amount columns
    amount_cols = [col for col in df.columns if any(x in col.lower() for x in ['amount', 'debit', 'credit', 'balance'])]
    for col in amount_cols:
        df[col] = df[col].apply(clean_amount)
    
    # Drop empty rows and columns
    df.replace('', np.nan, inplace=True)
    df.dropna(how='all', inplace=True)
    df.dropna(axis=1, how='all', inplace=True)
    
    return df 
>>>>>>> da9861285137d7690c9c82b14b5d0efeb26e646c
