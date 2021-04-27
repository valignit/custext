from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Settings"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Alignpos Settings",
					"description": _("Database of potential customers."),
					"onboard": 1,
				}
			]
		}
	]
