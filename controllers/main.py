from odoo import http
from odoo.http import request
import json

class MiModuloController(http.Controller):

    @http.route('/odoo/inscripciones/<int:programa_id>', type='http', auth='public', methods=['GET'], website=True)
    def get_alumnos_inscriptos(self, programa_id):
        # Obtener los alumnos inscritos en el programa
        alumnos = request.env['mi.modulo.inscripcion'].search([('programa_id', '=', programa_id)])
        
        # Crear la lista de respuestas
        result = []
        for inscripcion in alumnos:
            alumno = inscripcion.alumno_id
            result.append({
                'nombre': alumno.nombre,
                'apellido': alumno.apellido,
                'legajo': alumno.nro_legajo,
                'fecha_nacimiento': str(alumno.fecha_nacimiento),
                'email': alumno.email,
                'telefono': alumno.telefono,
                'pais': {
                    'id': alumno.pais.id,
                    'nombre': alumno.pais.name
                }
            })
        
        # Devolver la respuesta como JSON
        return json.dumps(result)
