import pandas as pd

#oi quem estiver corrigindo, deixei uns comentários aqui no código pra que eu possa visitar o código e consultar os comandos quando necessário.

def calculate_demographic_data(print_data=True):
    data = pd.read_csv('adult.data.csv')
    df = data
    # essa parte lê o arquivo da base de dados e chama a função de cálculos demográficos.

    # imprime quantas pessoas de cada raça estão no dataset e retorna um dicionário com os resultados
    race_count = df['race'].value_counts()

    # essa parte calcula a média de idade dos homens no dataset e retorna o resultado arredondado para uma casa decimal
    average_age_men = round(df[df['sex']== 'Male']['age'].mean(), 1)

    # essa parte calcula a porcentagem (*100) de pessoas com diploma de bacharelado e retorna o resultado arredondado para uma casa decimal (1)
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # essa parte calcula a porcentagem de pessoas com educação superior que ganham mais de 50K e retorna o resultado arredondado para uma casa decimal (1)
    advanced = ['Bachelors', 'Masters', 'Doctorate']
    higher_education = df[df['education'].isin(advanced)]
    lower_education = df[~df['education'].isin(advanced)]

    higher_education_rich = round((higher_education['salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((lower_education['salary'] == '>50K').mean() * 100, 1)

    # essa parte encontra o número mínimo de horas trabalhadas por semana no dataset e retorna o resultado
    min_work_hours = df['hours-per-week'].min()

    # essa parte calcula a porcentagem de pessoas que trabalham o número mínimo de horas por semana e ganham mais de 50K, retornando o resultado arredondado para uma casa decimal (1)
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

    # essa parte encontra o país com a maior porcentagem de pessoas que ganham mais de 50K e retorna o nome do país e a porcentagem arredondada para uma casa decimal (1)
    country_percentages = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()) * 100
    highest_earning_country = country_percentages.idxmax()
    highest_earning_country_percentage = round(country_percentages.max(), 1)

    # essa parte encontra a ocupação mais comum entre pessoas da Índia que ganham mais de 50K e retorna o nome da ocupação
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }