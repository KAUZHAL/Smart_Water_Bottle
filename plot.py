import matplotlib.pyplot as plt

def plot_data(water_timestamps: list, water_drunk: list) -> None:
    plt.plot(water_timestamps, water_drunk)
    plt.show()

def plot_to_bytes(water_timestamps: list, water_drunk: list):
    pass