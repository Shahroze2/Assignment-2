import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load the CSV file
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        data['Date'] = pd.to_datetime(data['Date'])
        return data
    except FileNotFoundError:
        print("Error: File not found. Make sure the CSV file is in the correct location.")
        return None

# Display basic statistics
def display_statistics(data):
    print("\n--- Data Statistics ---")
    print(data.describe())

# Generate trend line using linear regression
def generate_trend(data):
    data['Timestamp'] = data['Date'].apply(lambda x: x.timestamp())
    
    x = data['Timestamp']
    y = data['PurchaseAmount']
    
    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    
    data['Trend'] = intercept + slope * x

    plt.figure(figsize=(10, 6))
    plt.scatter(data['Date'], data['PurchaseAmount'], label='Actual Data', color='blue')
    plt.plot(data['Date'], data['Trend'], label='Trend Line', color='red')
    plt.title('Customer Purchase Trends Over Time')
    plt.xlabel('Date')
    plt.ylabel('Purchase Amount')
    plt.legend()
    plt.show()

    print(f"\n--- Trend Line Information ---")
    print(f"Slope: {slope}")
    print(f"Intercept: {intercept}")
    print(f"R-squared: {r_value**2}")
    print(f"P-value: {p_value}")
    print(f"Standard Error: {std_err}")

# Display data summary
def display_data(data):
    print("\n--- Loaded Data ---")
    print(data)

# Command Line Interface
def main():
    file_path = 'customer_data.csv'
    data = load_data(file_path)
    
    if data is not None:
        while True:
            print("\n--- Customer Data Processing Tool ---")
            print("1. Display Data")
            print("2. Display Statistics")
            print("3. Generate Trend Report")
            print("4. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                display_data(data)
            elif choice == '2':
                display_statistics(data)
            elif choice == '3':
                generate_trend(data)
            elif choice == '4':
                print("Exiting the tool. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
