from odoo import http
from odoo.http import request

class ProjectDashboardController(http.Controller):

    @http.route('/project/dashboard/count', type='json', auth='user')
    def get_project_count(self):
        project_count = request.env['project.management'].search_count([])
        return {'projects_count': project_count}

    @http.route('/project/dashboard/data', type='json', auth='user')
    def get_project_data(self):
        projects = request.env['project.management'].search([])
        project_data = []
        for project in projects:
            project_data.append({
                'name': project.name,
                'progress': project.progress,
                'end_date': project.end_date,
            })
        return {'projects': project_data}