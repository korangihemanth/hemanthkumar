import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data
df = pd.read_csv('fcc-forum-pageviews.csv')

# Set date column as index
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Copy DataFrame
    df_copy = df.copy()

    # Create line plot
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.plot(df_copy.index, df_copy['value'], color='red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    plt.xticks(rotation=45)

    # Save plot to file
    plt.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy DataFrame
    df_copy = df.copy()

    # Create new columns for year and month
    df_copy['year'] = df_copy.index.year
    df_copy['month'] = df_copy.index.month_name()

    # Create pivot table
    df_pivot = df_copy.pivot_table(index='year', columns='month', values='value', aggfunc='mean')
    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    df_pivot = df_pivot.reindex(columns=month_order)

    # Create bar plot
    fig = df_pivot.plot(kind='bar', figsize=(12, 10))
    plt.legend(title='Months')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.title('Average Daily Page Views for Each Month Grouped by Year')

    # Save plot to file
    plt.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Copy DataFrame
    df_copy = df.copy()

    # Create new columns for year and month
    df_copy['year'] = df_copy.index.year
    df_copy['month'] = df_copy.index.month_name()

    # Create box plots
    fig, ax = plt.subplots(1, 2, figsize=(20, 10))
    sns.boxplot(x='year', y='value', data=df_copy, ax=ax[0])
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')
    ax[0].set_title('Year-wise Box Plot (Trend)')

    sns.boxplot(x='month', y='value', data=df_copy, ax=ax[1],
                order=['January', 'February', 'March', 'April', 'May', 'June',
                       'July', 'August', 'September', 'October', 'November', 'December'])
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')
    ax[1].set_title('Month-wise Box Plot (Seasonality)')

    # Save plot to file
    plt.savefig('box_plot.png')
    return fig