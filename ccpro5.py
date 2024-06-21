import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Read data
df = pd.read_csv('epa-sea-level.csv')

def draw_plot():
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Original Data')

    # Linear regression for all data
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_values = range(df['Year'].min(), 2051)
    y_values = slope * x_values + intercept
    plt.plot(x_values, y_values, color='red', label='Best Fit Line (1880-2050)')

    # Linear regression for data from 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_values_recent = range(2000, 2051)
    y_values_recent = slope_recent * x_values_recent + intercept_recent
    plt.plot(x_values_recent, y_values_recent, color='green', label='Best Fit Line (2000-2050)')

    # Set labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Add legend
    plt.legend()

    # Save plot to file
    plt.savefig('sea_level_plot.png')

    # Return the plot
    return plt.gca()