import pandas as pd

# **Step 1: Read the CSV file**
# Replace 'your_file.csv' with the actual file name in your container filesystem
file_path = 'iris.csv'

try:
    # Load the CSV file into a DataFrame
    data = pd.read_csv(file_path)
    print("CSV file loaded successfully!")
    
    # **Step 2: Summarize the data**
    # Replace 'numeric_column' with the actual column name you want to analyze
    numeric_column = 'numeric_column'
    
    if numeric_column in data.columns:
        mean_value = data[numeric_column].mean()
        min_value = data[numeric_column].min()
        max_value = data[numeric_column].max()
        
        # Display the summary
        print(f"Summary for column '{numeric_column}':")
        print(f"Mean: {mean_value}")
        print(f"Min: {min_value}")
        print(f"Max: {max_value}")
    else:
        print(f"Column '{numeric_column}' not found in the CSV file.")
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
