{
    "name": "Transport Management System",
    "version": "1.0",
    "category": "Inventory/Transport Management System",
    "summary": "A module for managing transport ",
    "description": """
        This module allows users to manage transport based on picking batches
        This module is developed by ruja-odoo.
    """,
    "author": "ruja-odoo",
    "depends": ["base", "fleet", "stock_picking_batch"],
    "data": [
            "views/model_category_view.xml",
            "views/tms_picking_batch.xml",
            "views/tmsVol_views.xml",
    ],
    "demo": [
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    }
