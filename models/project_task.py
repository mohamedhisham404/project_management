from odoo import models, fields

class ProjectTask(models.Model):
    _name = 'project.task'
    _description = 'Project Task'

    name = fields.Char(string="Task Name", required=True, translate=True)
    project_id = fields.Many2one('project.management', string="Project", ondelete="cascade")
    description = fields.Text(string="Task Details")
    assigned_to = fields.Many2one('hr.employee', string="Assigned To")
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], string="Priority", default='medium')
    status = fields.Selection([
        ('to_do', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')
    ], string="Status", default='to_do')
    task_comments = fields.One2many('task.comment', 'task_id', string="Comments")


class TaskComment(models.Model):
    _name = 'task.comment'
    _description = 'Task Comments'

    comment = fields.Text(string="Comment", required=True)
    task_id = fields.Many2one('project.task', string="Task", ondelete='cascade', required=True)
    user_id = fields.Many2one('res.users', string="Commented By", default=lambda self: self.env.user, readonly=True)

