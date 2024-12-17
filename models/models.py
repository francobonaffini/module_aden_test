from odoo import models, fields, api

class Alumno(models.Model):
    _name = 'mi.modulo.alumno'
    _description = 'Alumno'
    _rec_name = 'nombre_completo'  # Campo representativo
    
    nombre = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellido', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento', required=True)
    nro_legajo = fields.Char(string='Número de Legajo', required=True)
    email = fields.Char(string='Email')
    telefono = fields.Char(string='Teléfono')
    direccion = fields.Text(string='Dirección')
    pais = fields.Many2one('res.country', string='País')

    # Campo calculado para mostrar nombre completo
    nombre_completo = fields.Char(string='Nombre Completo', compute='_compute_nombre_completo', store=True)

    @api.depends('nombre', 'apellido')
    def _compute_nombre_completo(self):
        for record in self:
            record.nombre_completo = f"{record.nombre} {record.apellido}"

class Programa(models.Model):
    _name = 'mi.modulo.programa'
    _description = 'Programa'
    _rec_name = 'nombre'
    
    nombre = fields.Char(string='Nombre del Programa', required=True)
    descripcion = fields.Text(string='Descripción')

class Inscripcion(models.Model):
    _name = 'mi.modulo.inscripcion'
    _description = 'Inscripción de Alumno a Programa'

    alumno_id = fields.Many2one('mi.modulo.alumno', string='Alumno', required=True)
    programa_id = fields.Many2one('mi.modulo.programa', string='Programa', required=True)
    fecha_inscripcion = fields.Date(string='Fecha de Inscripción', default=fields.Date.today)
