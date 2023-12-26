# Copyright (c) 2023, Heavy Web Design
# License:

import frappe


@frappe.whitelist()
def currency_to_words(number):
    """
    Converts a currency amount to words,
    based on more widely used in El Salvador
    """

    from num2words import num2words

    # number_format = round(float(number), 2)
    number_format = format(float(number), ".2f")

    result = str(number_format).partition('.')

    # Integer part
    integer = num2words(result[0], lang='es')
    integer = integer.capitalize()

    # Decimal part
    decimal = str(result[2] + '/100 Dolares')

    return integer + ' ' + decimal


@frappe.whitelist()
def month_to_string(month, abrr=False):
    """
    Converts a month number (MM) to string in Spanish
    """

    match month:
        case 1:
            return "Enero"
        case 2:
            return "Febrero"
        case 3:
            return "Marzo"
        case 4:
            return "Abril"
        case 5:
            return "Mayo"
        case 6:
            return "Junio"
        case 7:
            return "Julio"
        case 8:
            return "Agosto"
        case 9:
            return "Septiembre"
        case 10:
            return "Octubre"
        case 11:
            return "Noviembre"
        case 12:
            return "Diciembre"
        case _:
            return ""
