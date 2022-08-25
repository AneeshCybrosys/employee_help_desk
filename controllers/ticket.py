from odoo import http
from odoo.http import request


class WebsiteForm(http.Controller):
    @http.route(['/help_desk'], type='http', auth="user", website=True)
    def ticket(self):
        employees = request.env['hr.employee'].sudo().search([])
        values = {
            'employees': employees,
        }
        return request.render(
            "employee_help_desk.website_help_desk_form", values)

    @http.route(['/ticket/submit'], type='http', auth="user",
                website=True)
    def ticket_form_submit(self, **post):
        complaint = request.env['employee.ticket'].sudo().create({
            'employee_id': int(post.get('employee_id')),
            'subject': post.get('subject')
        })
        vals = {
            'booking': complaint,
        }
        return request.render("employee_help_desk.form_register", vals)
