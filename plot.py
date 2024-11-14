import matplotlib.pyplot as plt
from io import BytesIO


def plot_data(water_timestamps: list, water_drunk: list) -> None:
    plt.plot(water_timestamps, water_drunk)
    plt.show()

def plot_to_bytes(water_timestamps: list, water_drunk: list) -> BytesIO:
    img = BytesIO()
    plt.figure(figsize=(10, 10))
    plt.plot(water_timestamps, water_drunk)
    plt.title("Water intake.")
    plt.xlabel("Time")
    plt.ylabel("Water intake in ml")
    plt.grid()
    plt.savefig(img, format='png')
    img.seek(0)
    
    return img