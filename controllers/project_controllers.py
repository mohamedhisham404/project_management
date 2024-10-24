import json
from odoo import http
from odoo.http import request

class ProjectController(http.Controller):
    @http.route("/create/project", type="http", auth="none",methods=["POST"],csrf=False)
    def create_project(self):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        if not vals.get('name'):
            return request.make_json_response({
                "message":'Name is required'
            },status=400)
        try:
            res = request.env['project.management'].sudo().create(vals)
            if res:
                return request.make_json_response({
                    "message":'success'
                },status=201)
        except Exception as error:
            return request.make_json_response({
                "message":error
            },status=400)

    @http.route("/update/project/<int:project_id>", type="http", auth="none", methods=["PUT"],csrf=False)
    def update_project(self, project_id):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        project = request.env['project.management'].sudo().search([('id','=',project_id)])
        if not project:
            return request.make_json_response({
                "message":'Project not found'
            },status=404)
        try:
            project.write(vals)
            return request.make_json_response({
                "message":'success'
            },status=200)
        except Exception as error:
            return request.make_json_response({
                "message":error
            },status=400)

    @http.route("/project/<int:project_id>", type="http", auth="none", methods=["GET"],csrf=False)
    def get_project(self, project_id):
        project = request.env['project.management'].sudo().search([('id','=',project_id)])
        try:
            if not project:
                return request.make_json_response({
                    "message":'Project not found'
                },status=404)
            return request.make_json_response({
                "project": project.read()[0]
            },status=200)
        except Exception as error:
            return request.make_json_response({
                "message":error
            },status=400)

    @http.route("/delete/project/<int:project_id>", type="http", auth="none", methods=["DELETE"],csrf=False)
    def delete_project(self, project_id):
        project = request.env['project.management'].sudo().search([('id','=',project_id)])
        if not project:
            return request.make_json_response({
                "message":'Project not found'
            },status=404)
        try:
            project.unlink()
            return request.make_json_response({
                "message":'success'
            },status=200)
        except Exception as error:
            return request.make_json_response({
                "message":error
            },status=400)


    @http.route("/projects", type="http", auth="none", methods=["GET"],csrf=False)
    def get_projects(self):
        projects = request.env['project.management'].sudo().search([])
        try:
            return request.make_json_response({
                "projects": [project.read()[0] for project in projects]
            },status=200)
        except Exception as error:
            return request.make_json_response({
                "message":error
            },status=400)




