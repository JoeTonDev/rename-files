import os
import pandas as pd

def rename_files(folder_path, excel_file):
  # Read the Excel file into a pandas dataframe
  df = pd.read_excel(excel_file)
  
  # Loop through each row of the dataframe
  for i, row in df.iterrows():
    original_name = row['Original Name']
    final_name = row['Final Name']
    
    # Build the full path of the original file
    original_path = os.path.join(folder_path, original_name)
    
    # Check if the file exists
    if os.path.exists(original_path):
      # Build the full path of the final file
      final_path = os.path.join(folder_path, final_name)
      
      # Rename the file
      os.rename(original_path, final_path)
      
# Example usage
rename_files('/path/to/folder', '/path/to/excel_file.xlsx')