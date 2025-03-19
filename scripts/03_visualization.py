import pandas as pd
import matplotlib.pyplot as plt

def generate_plots(input_file, output_dir):
    df = pd.read_csv(input_file)

    # Histogram of homeschooling students
    plt.figure(figsize=(8, 5))
    df['homeschool_students'].hist(bins=30, edgecolor='black')
    plt.xlabel('Number of Homeschooling Students')
    plt.ylabel('Frequency')
    plt.title('Distribution of Homeschooling Students')
    plt.savefig(f"{output_dir}/histogram.png")
    plt.close()

    # Line plot of homeschooling trends for selected states
    selected_states = ['CA', 'TX', 'NY', 'FL']
    df_filtered = df[df['state'].isin(selected_states)]
    df_pivot = df_filtered.pivot_table(values='homeschool_students', index='year', columns='state', aggfunc='mean')

    plt.figure(figsize=(8, 5))
    df_pivot.plot(marker='o')
    plt.xlabel('Year')
    plt.ylabel('Average Number of Homeschooling Students')
    plt.title('Trends in Homeschooling Across Selected States')
    plt.legend(title='State')
    plt.savefig(f"{output_dir}/trends.png")
    plt.close()

if __name__ == "__main__":
    generate_plots("../outputs/cleaned_data.csv", "../outputs")
