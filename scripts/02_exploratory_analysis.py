import pandas as pd

def analyze_data(input_file, output_file):
    df = pd.read_csv(input_file)

    # Summary statistics
    summary = df['homeschool_students'].describe()

    # Number of unique school districts and states
    unique_districts = df['lea_id'].nunique()
    unique_states = df['state'].nunique()

    # States with highest and lowest homeschooling rates
    state_avg = df.groupby('state')['homeschool_students'].mean().sort_values()
    top_states = state_avg.tail(5)
    bottom_states = state_avg.head(5)

    # Save results
    with open(output_file, 'w') as f:
        f.write("Summary Statistics:\n")
        f.write(summary.to_string() + "\n\n")
        f.write(f"Unique School Districts: {unique_districts}\n")
        f.write(f"Unique States: {unique_states}\n\n")
        f.write("Top 5 States with Highest Homeschooling Rates:\n")
        f.write(top_states.to_string() + "\n\n")
        f.write("Bottom 5 States with Lowest Homeschooling Rates:\n")
        f.write(bottom_states.to_string())

if __name__ == "__main__":
    analyze_data("../outputs/cleaned_data.csv", "../outputs/summary_statistics.txt")
