# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "custext",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("custext")
		},
		{
			"module_name": "Alignpos",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Alignpos")
		}
	]
