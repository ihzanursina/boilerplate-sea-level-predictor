import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
  df = pd.read_csv('epa-sea-level.csv')

  plt.figure(figsize=(10,6))
  plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Original Data')

  res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
  x_all = pd.Series(range(1880, 2051))
  y_all = res_all.slope * x_all + res_all.intercept
  plt.plot(x_all, y_all, color='red', label='Fit: 1880-2050')

  df_recent = df[df['Year'] >= 2000]
  res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
  x_recent = pd.Series(range(2000, 2051))
  y_recent = res_recent.slope * x_recent + res_recent.intercept
  plt.plot(x_recent, y_recent, color='green', label='Fit: 2000-2050')

  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
