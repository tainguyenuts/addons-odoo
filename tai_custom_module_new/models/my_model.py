# models/my_model.py
from odoo import models, fields

class JobStatusOption(models.Model):
    _name = 'job.status.option'  # New model to store job status options
    _description = 'Job Status Option'

    name = fields.Char(string='Job Status', required=False)

class InfluenceLevelOption(models.Model):
    _name = 'influence.level.option'  # Model for Influence Level
    _description = 'Influence Level Option'

    name = fields.Char(string='Influence Level', required=False)

class ResPartner(models.Model):
    _inherit = 'res.partner'

    buyer_role = fields.Char(string='Buyer Role (Vai trò bên mua)')
    influence_level = fields.Many2one('influence.level.option',string='Influence Level (Sức ảnh hưởng)')
    job_status = fields.Many2one('job.status.option',string='Job Status (Trạng thái công việc))')
    attitude = fields.Float(string='Attitude (Thái độ)')
    flag_alert = fields.Char(string='Flag Alert (Cờ báo động)')
    total_score = fields.Float(string='Total Score (Tổng điểm)')
    winning = fields.Char(string='Winning', placeholder='Enter Winning')
    remarks_notes = fields.Char(string='Remarks/Notes (Đánh giá/Lưu ý)')
    customer_care_assignment = fields.Many2one('res.users', string='Customer Care Assignment (Phân vai chăm sóc)')
