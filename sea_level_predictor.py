import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Ler os dados do arquivo CSV
    df = pd.read_csv('epa-sea-level.csv')

    # Criar o scatter plot (dispersão) com os dados
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    # Primeira linha de melhor ajuste - Usando todos os dados
    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Criar os anos de 1880 até 2050 para prever o nível do mar
    years_extended = pd.Series(range(1880, 2051))
    sea_level_pred1 = slope1 * years_extended + intercept1
    plt.plot(years_extended, sea_level_pred1, 'r', label='Best fit line: All data')

    # Segunda linha de melhor ajuste - Usando apenas dados de 2000 em diante
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    # Prever de 2000 até 2050
    years_recent = pd.Series(range(2000, 2051))
    sea_level_pred2 = slope2 * years_recent + intercept2
    plt.plot(years_recent, sea_level_pred2, 'green', label='Best fit line: Since 2000')

    # Configurar rótulos e título
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Salvar o gráfico
    plt.savefig('sea_level_plot.png')

    # Retornar o objeto do gráfico para testes
    return plt.gca()