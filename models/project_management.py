from odoo import models, fields, api

class ProjectManagement(models.Model):
    _name = 'project.management'
    _description = 'Project Management'

    name = fields.Char(string="Project Name", required=True, translate=True)
    description = fields.Text(string="Project Details")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="Deadline")
    status = fields.Selection([
        ('planning', 'Planning'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('on_hold', 'On Hold')
    ], string="Status", default='planning')
    assigned_team = fields.Many2many('hr.employee', string="Assigned Team")
    tasks_ids = fields.One2many('project.task','project_id')
    progress = fields.Float(string='Progress (%)', compute='_compute_progress', store=True)
    project_comments = fields.One2many('project.comment', 'project_id', string="Comments")

    def project_excel_report(self):
        return {
            'type': 'ir.actions.act_url',
            'url': f'/project_management/report/excel/{self.env.context.get("active_ids")}',
            'target': 'new'
        }

    @api.depends('tasks_ids.status')
    def _compute_progress(self):
        for project in self:
            total_tasks = len(project.tasks_ids)
            completed_tasks = len(project.tasks_ids.filtered(lambda task: task.status == 'done'))
            project.progress = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0

    def check_progress(self):
        project_ids = self.search([])
        for record in project_ids:
            if record.progress == 100:
                record.status = 'completed'


class ProjectComment(models.Model):
    _name = 'project.comment'
    _description = 'Project Comments'

    comment = fields.Text(string="Comment", required=True)
    project_id = fields.Many2one('project.management', string="Project", ondelete='cascade', required=True)
    user_id = fields.Many2one('res.users', string="Commented By", default=lambda self: self.env.user, readonly=True)
