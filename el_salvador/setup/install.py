# -*- coding: utf-8 -*-
# Copyright (c) 2024, Heavy Web Design
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields



def after_install():

    custom_fields = {
        "Supplier": [
            dict(fieldname='custom_nrc', label='NRC', fieldtype='Data', insert_after='tax_id')
        ],
        "Customer": [
            dict(fieldname='custom_nrc', label='NRC', fieldtype='Data', insert_after='tax_id')
        ]
    }

    create_custom_fields(custom_fields)