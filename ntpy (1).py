# Modules for conversion
from urllib import request

import json

""" Main function that returns an error message if invalid data is inputted via conditional statements, 
asks for more input, calls every other function in the program, and includes a while loop that breaks once conversion
is done """


def main():
    while True:
        currency_to_exchange = get_currency_code()
        exchange_rates = get_exchange_rates().get("rates")
        print()

        if currency_to_exchange in exchange_rates:
            currency_rate = exchange_rates[currency_to_exchange]
            eur_rate = exchange_rates['EUR']
            amount_euros = float(
                input(f'How many EUR are we converting to {currency_to_exchange} (rate={currency_rate})?: '))
            print()
            conversion_amount = amount_euros * currency_rate
            print(f'{amount_euros} is {conversion_amount:.2f} {currency_to_exchange} (rate={currency_rate})')
            print()
            break
        else:
            print('Error - Please enter a valid code. ex: the code for the United States Dollar is "USD" ')
            print()


# Function to ask for first user input
def get_currency_code():
    return input('What kind of currency do you want? Enter code: ')


# You do not need to modify any code below here.  There's a call to main at very end of this file.


def get_exchange_rates():
    """" Connect to the exchangeratesapi.io server and request the latest exchange rates,
    relative to Euros.  Return the response as a dictionary. """

    url = 'http://api.exchangeratesapi.io/latest?access_key=157f9c2c4a714d75ae7b6318d936b9c1'

    try:  # Attempt to connect to the exchangeratesapi server
        response = request.urlopen(url).read()  # and get the server's response
        data = json.loads(response)  # convert the response to a Python dictionary
        if data.get('success'):
            return data
        else:
            raise Exception
    except:  # this code runs if there's any error encountered when fetching data.
        # It returns some example data, that has the same structure as real data, to use instead
        # So it's no problem if you don't have an internet connection or the exchangeratesapi server is down.
        print('There was an error fetching real data. Perhaps you are offline? Returning example data.')
        return example_exchange_rates()


# You do not need to modify this function

def example_exchange_rates():
    """ In case the exchangeratesapi.io is not available, the program will use this example data.
     This data has the same structure as real data, so your code does the same thing if real data
     or example data is used. """
    example_data = {
        "success": True,
        "timestamp": 1617808686,
        "base": "EUR",
        "date": "2021-04-07",
        "rates": {
            "AED": 4.371091,
            "AFN": 93.37804,
            "ALL": 123.311638,
            "AMD": 544.974594,
            "ANG": 2.137146,
            "AOA": 747.730588,
            "ARS": 109.882953,
            "AUD": 1.557055,
            "AWG": 2.142102,
            "AZN": 2.019652,
            "BAM": 1.958079,
            "BBD": 2.403961,
            "BDT": 100.95761,
            "BGN": 1.956081,
            "BHD": 0.448719,
            "BIF": 2318.543117,
            "BMD": 1.190057,
            "BND": 1.594144,
            "BOB": 8.221008,
            "BRL": 6.625172,
            "BSD": 1.190568,
            "BTC": 0.000020949418,
            "BTN": 88.229183,
            "BWP": 13.012046,
            "BYN": 3.173245,
            "BYR": 23325.115609,
            "BZD": 2.399857,
            "CAD": 1.500412,
            "CDF": 2377.734202,
            "CHF": 1.103242,
            "CLF": 0.030777,
            "CLP": 849.228039,
            "CNY": 7.784759,
            "COP": 4323.893306,
            "CRC": 729.761943,
            "CUC": 1.190057,
            "CUP": 31.536508,
            "CVE": 110.391798,
            "CZK": 25.845895,
            "DJF": 211.953453,
            "DKK": 7.437297,
            "DOP": 67.7205,
            "DZD": 157.922056,
            "EGP": 18.695317,
            "ERN": 17.850874,
            "ETB": 49.364401,
            "EUR": 1,
            "FJD": 2.449733,
            "FKP": 0.862933,
            "GBP": 0.862881,
            "GEL": 4.075981,
            "GGP": 0.862933,
            "GHS": 6.881704,
            "GIP": 0.862933,
            "GMD": 60.990558,
            "GNF": 11911.882183,
            "GTQ": 9.188686,
            "GYD": 248.864805,
            "HKD": 9.26424,
            "HNL": 28.63261,
            "HRK": 7.575789,
            "HTG": 96.378297,
            "HUF": 358.909474,
            "IDR": 17314.435626,
            "ILS": 3.918798,
            "IMP": 0.862933,
            "INR": 88.490074,
            "IQD": 1737.099858,
            "IRR": 50107.346409,
            "ISK": 150.601311,
            "JEP": 0.862933,
            "JMD": 173.916032,
            "JOD": 0.84377,
            "JPY": 130.476675,
            "KES": 128.823971,
            "KGS": 100.901241,
            "KHR": 4815.972173,
            "KMF": 498.391932,
            "KPW": 1070.963978,
            "KRW": 1328.984426,
            "KWD": 0.359314,
            "KYD": 0.992236,
            "KZT": 516.012701,
            "LAK": 11217.779187,
            "LBP": 1800.16013,
            "LKR": 238.478724,
            "LRD": 205.88007,
            "LSL": 17.446092,
            "LTL": 3.513928,
            "LVL": 0.719854,
            "LYD": 5.398301,
            "MAD": 10.704295,
            "MDL": 21.395075,
            "MGA": 4536.160308,
            "MKD": 61.685853,
            "MMK": 1678.756854,
            "MNT": 3387.186279,
            "MOP": 9.546245,
            "MRO": 424.850115,
            "MUR": 47.718867,
            "MVR": 18.398624,
            "MWK": 934.940888,
            "MXN": 24.010457,
            "MYR": 4.916722,
            "MZN": 77.984019,
            "NAD": 17.446513,
            "NGN": 453.471602,
            "NIO": 41.552077,
            "NOK": 10.042344,
            "NPR": 141.166332,
            "NZD": 1.691095,
            "OMR": 0.458176,
            "PAB": 1.190723,
            "PEN": 4.326051,
            "PGK": 4.181338,
            "PHP": 57.929611,
            "PKR": 182.252269,
            "PLN": 4.569854,
            "PYG": 7591.788155,
            "QAR": 4.332699,
            "RON": 4.917788,
            "RSD": 117.740238,
            "RUB": 91.574171,
            "RWF": 1184.240238,
            "SAR": 4.463239,
            "SBD": 9.505399,
            "SCR": 22.760766,
            "SDG": 452.805653,
            "SEK": 10.231574,
            "SGD": 1.593094,
            "SHP": 0.862933,
            "SLL": 12153.461115,
            "SOS": 697.373227,
            "SRD": 16.844105,
            "STD": 24520.056817,
            "SVC": 10.417966,
            "SYP": 1496.586302,
            "SZL": 17.312485,
            "THB": 37.340452,
            "TJS": 13.575193,
            "TMT": 4.1771,
            "TND": 3.326804,
            "TOP": 2.716126,
            "TRY": 9.71744,
            "TTD": 8.08799,
            "TWD": 33.818916,
            "TZS": 2759.742343,
            "UAH": 33.271416,
            "UGX": 4343.288773,
            "USD": 1.190057,
            "UYU": 52.630231,
            "UZS": 12476.560782,
            "VEF": 246873212022.42874,
            "VND": 27481.389398,
            "VUV": 130.205949,
            "WST": 3.011354,
            "XAF": 656.716834,
            "XAG": 0.047129,
            "XAU": 0.000683,
            "XCD": 3.216188,
            "XDR": 0.83807,
            "XOF": 656.711309,
            "XPF": 121.237015,
            "YER": 297.930609,
            "ZAR": 17.288731,
            "ZMK": 10711.944178,
            "ZMW": 26.33605,
            "ZWL": 383.198722
        }
    }

    return example_data


main()
