def get_population(country_dict):
    population_dict = {
        'Confirmed': float(country_dict['Confirmed']),
        'Deaths': float(country_dict['Deaths']),
        'Recovered': float(country_dict['Recovered']),
        'Active': float(country_dict['Active']),
        'Perc_Deaths': float(country_dict['Perc_Deaths']),
        'Perc_Recovered': float(country_dict['Perc_Recovered'])
    }
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values


def population_by_country(data, country):
    result = list(filter(lambda item: item['Country'] == country, data))
    return result
