import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import data
df = pd.read_csv('medical_examination.csv')

# Add overweight column
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# Normalize data
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Draw Categorical Plot
def draw_cat_plot():
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    df_cat['total'] = 1
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).count()

    # Rename the 'total' column to 'total'
    df_cat.rename(columns={'total': 'total'}, inplace=True)

    # Draw the catplot
    fig = sns.catplot(data=df_cat, x='variable', y='total', hue='value', kind='bar', col='cardio')
    fig.set_axis_labels('variable', 'total')
    fig = fig.fig

    # Save plot to file
    plt.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = corr.where(~(abs(corr) < 0.1), True)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 8))

    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', center=0, square=True, linewidths=.5, cbar_kws={'shrink': .5})

    # Save plot to file
    plt.savefig('heatmap.png')
    return fig