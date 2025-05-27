def read_sensor_data(path):
    """Baca data sensor dari CSV, kembalikan list floats."""
    with open(path) as f:
        return [float(line.strip()) for line in f if line.strip()]

def average(data):
    """Hitung rata-rata list angka."""
    return sum(data) / len(data)

if __name__ == "__main__":
    data = read_sensor_data("data.csv")
    print(f"Average sensor value: {average(data):.2f}")