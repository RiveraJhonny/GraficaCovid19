import matplotlib.pyplot as plt


def generate_chart(labelbs, values):
    fig, ax = plt.subplots()
    bar_labels = ['Confirmados', 'Muertes', 'Recuperados', 'Activos', '% Muertes', '% Recuperados']
    bar_colors = ['tab:grey', 'tab:red', 'tab:blue', 'tab:orange', 'tab:red', 'tab:blue']
    ax.bar(labelbs, values, label=bar_labels, color=bar_colors)
    ax.set_ylabel('Numero de Casos')
    ax.set_title('Datos COVID-19')
    ax.legend(title='Casos')
    plt.show()


def generate_pie_chart(labelbs, values):
    fix, ax = plt.subplots()
    ax.pie(values, labels=labelbs)
    ax.axis("equal")
    plt.show()
