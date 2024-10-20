{
    'name':"Project Management",
    'author':"Mohamed Hisham",
    'version':'17.0.0.1.0',
    'depends':['base','hr','sale_management','web'],
    'data':[
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/tasks.xml',
        'views/projects.xml',
        'views/projects_dashboard_view.xml',
        'reports/project_report.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'project_management/static/src/css/dashboard.css',
            'project_management/static/src/js/dashboard.js',
            'project_management/static/src/xml/dashboard.xml',
        ]},
    'installable': True,
    'application':True,
}
