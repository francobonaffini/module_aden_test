# Alta al servidor sin necesidad de reiniciar el servidor completo para actualizar cambios.
python odoo-bin -r franco -w franco1234. --addons-path=addons,modules -d odoo5 -u modules/aden
# Alta al servidor con el modulo incluído
python odoo-bin -r franco -w franco1234. --addons-path=addons,modules -d odoo5


# API (Endpoints)
http://127.0.0.1:8069/odoo/inscripciones/x/


Se instaló PostgreSQL y se crearon los respectivos usuarios para ejecutar una instancia de PostgreSQL
Se clonó el repositorio de odoo (ver.17) en una carpeta de mi disco local y se ejecutó el proyecto en VSCode.
Se creó un Módulo "modules/aden" llamado "Inscripciones de alumnos a programas".
Se creó el manifest.py para configurar nombres y carpetas del modulo.
Se crearon 3 Modelos (Alumno, Programa e Inscripcion).
Se crearon las vistas (carpeta views) con Menues en la parte superior para poder acceder al Módulo de inscripción, lo que permite a su vez, crear: Nuevo alumno, Nuevo programa y nueva inscripción (esta nueva inscripçión, toma alumnos y programas previamente creados como foráneas)
Se crearon permisos en la carpeta security desde el archivo "ir.model.access.csv" para que solo el usuario "admin" pueda crear o borrar nuevos registros de sólo de Alumnos.
Se creó un controlador (carpeta controllers), para que pueda manejar solicitudes http y así crear una API pública, para poder obtener cuantos Alumnos, se encuentran Inscriptos en un determinado programa.
