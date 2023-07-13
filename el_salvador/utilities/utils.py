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

    #number_format = round(float(number), 2)
    number_format = format(float(number), ".2f")

    result = str(number_format).partition('.')

    # Integer part
    integer = num2words(result[0], lang='es')
    integer = integer.capitalize()

    # Decimal part
    decimal = str(result[2] + '/100 Dolares')

    return integer + ' ' + decimal