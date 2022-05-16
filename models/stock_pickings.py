
from odoo import api,fields,models,_
class StockPickings(models.Model):
    _inherit = "stock.picking"

    x_origin = fields.Char(string=u"项目号")
    
    @api.onchange('x_origin')
    def get_origin(self):

        att_model = self.env['mrp.production']
        query = [("state","!=","draft"),("state","!=","cancel"),("state","!=","done")]
        for i in att_model.search(query):
            if i.name in self.origin:
                # self.x_origin=i.product_id.name
                self.write({'x_origin':i.product_id.name})
