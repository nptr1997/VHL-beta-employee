from odoo import api, fields, models, _

class HrWorkContract(models.Model):
    _name = "hr.work.contract"
    _description = "Employee work contract"
    _order = 'contract_id'

    contract_id = fields.Char(string="Contract number", groups="hr.group_hr_user", tracking=True)
    employ_id = fields.Many2one("hr.employee", string="Employee information")
    employee_user = fields.Many2one(string="User account", related="employ_id.user_id", store=True, readonly=False)
    start_date = fields.Date("Onboard date")
    stop_date = fields.Date("Offboard date")