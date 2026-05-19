from load import load_data, clean_data
from analytics import (
    dataset_overview,
    network_distribution,
    radio_distribution,
    country_distribution,
    range_statistics,
    average_coordinates
)

from visualization import (
    plot_network_distribution,
    plot_radio_distribution,
    plot_range_histogram
)

from utils import print_header


def main():

    print_header("Telecom Data Analysis 2026")

    # Load dataset
    df = load_data()

    if df is None:
        return

    # Clean dataset
    df = clean_data(df)

    # Dataset overview
    dataset_overview(df)

    # Network distribution
    print_header("Network Distribution")
    network_counts = network_distribution(df)
    print(network_counts)

    # Radio distribution
    print_header("Radio Distribution")
    radio_counts = radio_distribution(df)
    print(radio_counts)

    # Country distribution
    print_header("Country Distribution")
    country_counts = country_distribution(df)
    print(country_counts)

    # Range statistics
    print_header("Range Statistics")
    print(range_statistics(df))

    # Coordinates
    print_header("Average Coordinates")
    print(average_coordinates(df))

    # Visualizations
    plot_network_distribution(network_counts)
    plot_radio_distribution(radio_counts)
    plot_range_histogram(df)

    print("\nAnalysis completed successfully.")

    # Clean dataset
    df = clean_data(df)

    # Export cleaned data
    df.to_csv("output/reports/cleaned_telecom_data.csv", index=False)

if __name__ == "__main__":
    main()