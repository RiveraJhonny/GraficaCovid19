import package.read_csv as get_csv
import package.charts as chart
import package.utils as utils


def run():
    data = get_csv.read_csv("country_covid.csv")
    country = input('Type Country ==> ')
    result = utils.population_by_country(data, country)
    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        chart.generate_chart(labels, values)


if __name__ == "__main__":
    run()
