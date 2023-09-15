import os
import pandas as pd

def xlsx_to_csv(folder_path):
    # List all files in the folder
    file_list = os.listdir(folder_path)
    
    # Filter the list to include only .xlsx files
    xlsx_files = [f for f in file_list if f.endswith('.xlsx')]
    
    for xlsx_file in xlsx_files:
        # Construct full path to the .xlsx file
        xlsx_file_path = os.path.join(folder_path, xlsx_file)
        
        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel(xlsx_file_path)
        
        # Construct the name of the output .csv file
        csv_file = os.path.splitext(xlsx_file)[0] + '.csv'
        csv_file_path = os.path.join(folder_path, csv_file)
        
        # Write DataFrame to .csv file
        df.to_csv(csv_file_path, index=False)

# Define the folder containing .xlsx files
# Use os.path.dirname(__file__) to get the directory of the current script
# Then append '/data/' to point to the 'data' folder in that directory
folder_path = os.path.join(os.path.dirname(__file__), 'data')

# Call the function
xlsx_to_csv(folder_path)
