{
    "name": "Inventário de TI",
    "version": "15.0.0.0.0",
    'sequence': 1,
    'description': "Módulo de categorização/anotação de requisitos de hardware e software utilizados por "
                   "usuários e departamentos",
    "depends": [
        "hr",
        "product",
        "stock",
        "project_requests",
    ],
    "author": "Gustavo Salgado Lima",
    "category": "Inventory",
    "website": "http://superglass.com.br",
    "data": [
        "security/groups.xml",
        "security/ir.model.access.csv",
        "views/hr_inventory_view.xml",
        "views/product_inherit_view.xml",
        "views/ti_category_view.xml",
        "views/product_product_inherit_view.xml",
        "views/hr_employee_inherit_view.xml",
        "views/project_request_view.xml"
    ],
    'installable': True,
    'application': True,
}
