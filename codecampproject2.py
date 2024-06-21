import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read the dataset
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100

    # What percentage of people with advanced education (> 12 years) make more than 50K?
    higher_education = df[df['education-num'] > 12]
    higher_education_rich = (higher_education['salary'] == '>50K').mean() * 100

    # What percentage of people without advanced education make more than 50K?
    lower_education = df[df['education-num'] <= 12]
    lower_education_rich = (lower_education['salary'] == '>50K').mean() * 100

    # What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = (num_min_workers['salary'] == '>50K').mean() * 100

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = (df[df['salary'] == '>50K']['native-country']
                               .value_counts(normalize=True).idxmax())
    highest_earning_country_percentage = (df[df['salary'] == '>50K']['native-country']
                                          .value_counts(normalize=True).max() * 100)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = (df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
                         ['occupation'].value_counts().idxmax())

    # Print the results
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", round(average_age_men, 1))
        print(f"Percentage with Bachelors degrees: {round(percentage_bachelors, 1)}%")
        print(f"Percentage with higher education that earn >50K: {round(higher_education_rich, 1)}%")
        print(f"Percentage without higher education that earn >50K: {round(lower_education_rich, 1)}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {round(rich_percentage, 1)}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {round(highest_earning_country_percentage, 1)}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation
    }