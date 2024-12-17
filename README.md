# Alta al servidor + actualizacion del módulo específico.
python odoo-bin -r franco -w franco1234. --addons-path=addons,modules -d odoo5 -u modules/aden
# Alta al servidor con el modulo incluído
python odoo-bin -r franco -w franco1234. --addons-path=addons,modules -d odoo5


# API (Endpoints)
http://127.0.0.1:8069/odoo/inscripciones/x/


1) - Se instaló PostgreSQL y se crearon los respectivos usuarios para ejecutar una instancia de PostgreSQL

2) - Se clonó el repositorio de odoo (ver.17) en una carpeta de mi disco local y se ejecutó el proyecto en VSCode.

3) - Se creó un Módulo "aden" ubicado en > "modules/aden" llamado "Inscripciones de alumnos a programas".

4) - Se creó el manifest.py para configurar nombres y carpetas del modulo.

5) - Se crearon 3 Modelos (Alumno, Programa e Inscripcion).

6) - Se crearon las vistas (carpeta views) con Menues en la parte superior para poder acceder al Módulo de inscripción, lo que permite a su vez, crear: Nuevo alumno, Nuevo programa y nueva inscripción (esta nueva inscripçión, toma alumnos y programas previamente creados como foráneas).

7) -Se crearon 2 grupos de usuarios (Si Edición y No Edición), esto permite que a la hora de agregar un usuario y se le asigne el grupo "Si edición" como por ejemplo un usuario administrativo, permita editar y agregar valores y realizar el CRUD correspondiente, mientras que si a un usuario se le asigna el grupo "No Edición" este usuario no podrá realizar cambios en la base de datos.

8) -Se creó un controlador (carpeta controllers), para que pueda manejar solicitudes http y así crear una API pública, para poder obtener cuantos Alumnos, se encuentran Inscriptos en un determinado programa.
