import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import norm
import openpyxl

# 1. Subplots matriz 2x1
def plot_exercise_1():
    x = [5, 5, 5, 4, 3, 2, 4, 1, 1, 1, 3, 3, 3, 3, 3, 3, 2, 3, 1, 2, 1, 2, 5, 4, 3, 1, 3]
    fig, axes = plt.subplots(2, 1, figsize=(8, 6))

    axes[0].plot(x, marker='o', linestyle='')
    axes[0].set_title("Pontos")

    axes[1].hist(x, bins=5, edgecolor='black')
    axes[1].set_title("Histograma sem normalização")

    plt.tight_layout()
    plt.show()

# 2. Subplots matriz 2x2
def plot_exercise_2():
    p = [6, 7, 8, 7, 5, 5, 6, 4, 7, 10, 10, 11, 10, 11, 10, 12, 9, 8, 7, 8, 6, 7]
    returns = np.diff(p) / p[:-1]

    fig, axes = plt.subplots(2, 2, figsize=(10, 8))

    axes[0, 0].plot(p, marker='o', linestyle='')
    axes[0, 0].set_title("Pontos")

    axes[0, 1].plot(returns, marker='o', linestyle='')
    axes[0, 1].set_title("Retornos")

    axes[1, 0].hist(returns, bins=5, density=True, edgecolor='black')
    x_vals = np.linspace(min(returns), max(returns), 100)
    axes[1, 0].plot(x_vals, norm.pdf(x_vals, np.mean(returns), np.std(returns)))
    axes[1, 0].set_title("Histograma normalizado")

    plt.tight_layout()
    plt.show()

# 3. Subplots matriz 3x1
def plot_exercise_3():
    dados = [-2, -3, -1, -1, -1, 1, 2, 1, -1, -2, 1, 1, 2, 2, 1, 1, 2, 2, 3, 2, 1, 1, -1, -1, 2, 3, 2, 1, 2, -1, -3, 2]
    returns = np.diff(dados) / dados[:-1]

    fig, axes = plt.subplots(3, 1, figsize=(8, 12))

    axes[0].plot(dados, marker='o', linestyle='')
    axes[0].set_title("Dados")

    axes[1].plot(returns, marker='o', linestyle='')
    axes[1].set_title("Retornos")

    axes[2].hist(returns, bins=5, density=True, edgecolor='black')
    x_vals = np.linspace(min(returns), max(returns), 100)
    axes[2].plot(x_vals, norm.pdf(x_vals, np.mean(returns), np.std(returns)))
    axes[2].set_title("Histograma e ajuste normal")

    plt.tight_layout()
    plt.show()

# 4. Subplots matriz 3x1 com Boxplot
def plot_exercise_4():
    pts = [5, 6, 7, 6, 7, 5, 6, 4, 5, 6, 4, 5, 6, 4, 9, 10, 8, 7, 9, 2, 1, 0, 2, 3, 2, 3, 1, 1, 2, 3, 4, 3, 1, 2, 3, 5, 4, 3]

    fig, axes = plt.subplots(3, 1, figsize=(8, 12))

    axes[0].plot(pts, marker='o', linestyle='')
    axes[0].set_title("Pontos")

    axes[1].hist(pts, bins=5, density=True, edgecolor='black')
    x_vals = np.linspace(min(pts), max(pts), 100)
    axes[1].plot(x_vals, norm.pdf(x_vals, np.mean(pts), np.std(pts)))
    axes[1].set_title("Histograma normalizado e ajuste")

    axes[2].boxplot(pts)
    axes[2].set_title("Boxplot")

    plt.tight_layout()
    plt.show()

# 5. Importar dados do Excel e calcular média e mediana
def plot_exercise_5():
    data = pd.read_excel('ExPy.xlsx', header=None)
    d = data.iloc[:, 0]

    mean_val = d.mean()
    median_val = d.median()

    print(f"Média: {mean_val}")
    print(f"Mediana: {median_val}")

    plt.plot(d, marker='o', linestyle='')
    plt.title("Pontos do Excel")
    plt.show()

# 6. Subplots 3x1 com retornos e intervalo de confiança
def plot_exercise_6():
    dad = [1.2, 1.3, 1.1, 1.4, 1.5, 1.7, 1.6, 1.5, 1.4, 1.4, 1.6, 1.7, 1.8, 1.7, 1.1, 1.2, 1.1, 1.5, 1.4, 1.2, 1.5, 1.3, 1.1]
    returns = np.diff(dad) / dad[:-1]

    mean_ret = np.mean(returns)
    std_ret = np.std(returns)
    conf_interval = (mean_ret - 1.96 * std_ret, mean_ret + 1.96 * std_ret)

    print(f"Intervalo de confiança de 95%: {conf_interval}")

    fig, axes = plt.subplots(3, 1, figsize=(8, 12))

    axes[0].plot(dad, marker='o', linestyle='')
    axes[0].set_title("Dados")

    axes[1].plot(returns, marker='o', linestyle='')
    axes[1].set_title("Retornos")

    axes[2].hist(returns, bins=5, density=True, edgecolor='black')
    x_vals = np.linspace(min(returns), max(returns), 100)
    axes[2].plot(x_vals, norm.pdf(x_vals, mean_ret, std_ret))
    axes[2].set_title("Histograma normalizado e ajuste normal")

    plt.tight_layout()
    plt.show()

# 7. Subplots 3x1 para ListaDupla.xlsx
def plot_exercise_7():
    data = pd.read_excel('ListaDupla.xlsx')
    x = data['A'].tolist()
    y = data['B'].tolist()

    fig, axes = plt.subplots(3, 1, figsize=(8, 12))

    axes[0].plot(x, marker='o', linestyle='')
    axes[0].set_title("Dados de x")

    axes[1].plot(y, marker='o', linestyle='')
    axes[1].set_title("Dados de y")

    axes[2].hist(x, bins=5, density=True, alpha=0.5, label='x', edgecolor='black')
    axes[2].hist(y, bins=5, density=True, alpha=0.5, label='y', edgecolor='black')
    x_vals_x = np.linspace(min(x), max(x), 100)
    x_vals_y = np.linspace(min(y), max(y), 100)
    axes[2].plot(x_vals_x, norm.pdf(x_vals_x, np.mean(x), np.std(x)), label='x ajuste')
    axes[2].plot(x_vals_y, norm.pdf(x_vals_y, np.mean(y), np.std(y)), label='y ajuste')
    axes[2].legend()
    axes[2].set_title("Histogramas normalizados e ajustes")

    plt.tight_layout()
    plt.show()

# 8. Dados do Ibovespa em formato 2x2
def plot_exercise_8():
    data = pd.read_excel('Ibovespa.xlsx')
    ibov = data['Fechamento'].tolist()
    returns = np.diff(ibov) / ibov[:-1]

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    axes[0, 0].plot(ibov)
    axes[0, 0].set_title("Ibovespa")

    axes[0, 1].plot(returns)
    axes[0, 1].set_title("Retorno Diário")

    axes[1, 0].hist(returns, bins=10, density=True, edgecolor='black')
    x_vals = np.linspace(min(returns), max(returns), 100)
    axes[1, 0].plot(x_vals, norm.pdf(x_vals, np.mean(returns), np.std(returns)))
    axes[1, 0].set_title("Histograma e Ajuste")

    axes[1, 1].boxplot(ibov)
    axes[1, 1].set_title("Boxplot")

    stats = {
        'Média': np.mean(ibov),
        'Mediana': np.median(ibov),
        'Desvio Padrão': np.std(ibov),
        'Máximo': np.max(ibov),
        'Mínimo': np.min(ibov),
    }
    print("Estatísticas do Ibovespa:", stats)

    plt.tight_layout()
    plt.show()

# 9. Comparação Ibovespa e PETR4
def plot_exercise_9():
    data = pd.read_excel('Ibovespa_PETR4.xlsx')
    ibov = data['Ibovespa'].tolist()
    petr4 = data['PETR4'].tolist()

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    axes[0, 0].plot(ibov)
    axes[0, 0].set_title("Ibovespa")

    axes[0, 1].plot(petr4)
    axes[0, 1].set_title("PETR4")

    axes[1, 0].hist(ibov, bins=10, density=True, alpha=0.5, label='Ibovespa', edgecolor='black')
    axes[1, 0].hist(petr4, bins=10, density=True, alpha=0.5, label='PETR4', edgecolor='black')
    axes[1, 0].legend()
    axes[1, 0].set_title("Histogramas Normalizados")

    axes[1, 1].boxplot([ibov, petr4], labels=['Ibovespa', 'PETR4'])
    axes[1, 1].set_title("Boxplot Comparativo")

    plt.tight_layout()
    plt.show()

# 10. Dados do Bitcoin
def plot_exercise_10():
    data = pd.read_excel('Bitcoin.xlsx')
    btc = data['Fechamento'].tolist()
    returns = np.diff(btc) / btc[:-1]

    fig, axes = plt.subplots(2, 1, figsize=(10, 8))

    axes[0].plot(btc)
    axes[0].set_title("Bitcoin Fechamento")

    axes[1].plot(returns)
    axes[1].set_title("Retorno Diário")

    top_10 = sorted(btc, reverse=True)[:10]
    stats = {
        'Média dos 10 maiores': np.mean(top_10),
        'Mediana': np.median(top_10),
        'Desvio Padrão': np.std(top_10),
        'Máximo': np.max(top_10),
        'Mínimo': np.min(top_10),
    }
    print("Estatísticas do Bitcoin (Top 10):", stats)

    plt.tight_layout()
    plt.show()

plot_exercise_1()
plot_exercise_2()
plot_exercise_3()
plot_exercise_4()
plot_exercise_5()
plot_exercise_6()
plot_exercise_7()
plot_exercise_8()
plot_exercise_9()
plot_exercise_10()
