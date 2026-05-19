import matplotlib.pyplot as plt
import seaborn as sns
import os

from config import OUTPUT_CHARTS

# Style
sns.set_style("whitegrid")


def plot_network_distribution(network_counts):
    """
    Plot network distribution
    """

    plt.figure(figsize=(10, 6))

    network_counts.plot(kind="bar")

    plt.title("Telecom Network Distribution")
    plt.xlabel("Network")
    plt.ylabel("Number of Towers")

    save_path = os.path.join(
        OUTPUT_CHARTS,
        "network_distribution.png"
    )

    plt.savefig(save_path)

    plt.show()


def plot_radio_distribution(radio_counts):
    """
    Plot radio distribution
    """

    plt.figure(figsize=(8, 6))

    radio_counts.plot(
        kind="pie",
        autopct="%1.1f%%"
    )

    plt.title("Radio Technology Distribution")

    plt.ylabel("")

    save_path = os.path.join(
        OUTPUT_CHARTS,
        "radio_distribution.png"
    )

    plt.savefig(save_path)

    plt.show()


def plot_range_histogram(df):
    """
    Plot telecom range histogram
    """

    plt.figure(figsize=(10, 6))

    sns.histplot(
        df["RANGE"],
        bins=30
    )

    plt.title("Tower Range Distribution")
    plt.xlabel("Range")
    plt.ylabel("Frequency")

    save_path = os.path.join(
        OUTPUT_CHARTS,
        "range_histogram.png"
    )

    plt.savefig(save_path)

    plt.show()