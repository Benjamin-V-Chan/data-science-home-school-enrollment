import pandas as pd

def preprocess_data(input_file, output_file):
    df = pd.read_csv(input_file)

    # Drop duplicate rows
    df = df.drop_duplicates()

    # Drop rows with missing homeschool_students
    df = df.dropna(subset=['homeschool_students'])

    # Fill missing lea_name and lea_id with "Unknown"
    df['lea_name'].fillna("Unknown", inplace=True)
    df['lea_id'].fillna("Unknown", inplace=True)

    # Convert 'year' to numeric format
    df['year'] = df['year'].str[:4].astype(int)  # Extract the first four digits

    # Save cleaned data
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    preprocess_data("../data/home_school_district.csv", "../outputs/cleaned_data.csv")
