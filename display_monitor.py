from screeninfo import get_monitors
import math

def get_display_info():
    monitors = get_monitors()
    for monitor in monitors:
        width_inch = monitor.width_mm / 25.4  # Convert mm to inches
        height_inch = monitor.height_mm / 25.4  # Convert mm to inches
        diagonal_inch = math.sqrt(width_inch**2 + height_inch**2)  # Calculate diagonal
        print(f"Name: {monitor.name}")
        print(f"Width: {monitor.width}")
        print(f"Height: {monitor.height}")
        print(f"Width (mm): {monitor.width_mm}")
        print(f"Height (mm): {monitor.height_mm}")
        print(f"Is Primary: {monitor.is_primary}\n")
        print(f"Diagonal Size (inches): {diagonal_inch:.2f}寸\n")

if __name__ == "__main__":
    get_display_info()
