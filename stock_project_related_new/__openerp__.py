# -*- coding: utf-8 -*-
#    Odoo, Open Source Management Solution
#    Copyright (C) 2016 Rooms For (Hong Kong) Limited T/A OSCG
#    <https://www.odoo-asia.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

{
    "name": "Stock Project Related",
    "summary": "relate project to stock picking via sales order",
    "version": "8.0.1.0.0",
    "category": "Warehouse",
    "website": "https://www.odoo-asia.com/",
    "author": "Rooms For (Hong Kong) Limited T/A OSCG",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "account_analytic_analysis","stock",
    ],
    "data": [
        "views/stock_view.xml",
    ],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
