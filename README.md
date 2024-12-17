# Alta al servidor + actualizacion del módulo específico.
python odoo-bin -r franco -w franco1234. --addons-path=addons,modules -d odoo5 -u modules/aden
# Alta al servidor con el modulo incluído
python odoo-bin -r franco -w franco1234. --addons-path=addons,modules -d odoo5


# API (Endpoints) > reemplazar "x" por el id del programa que se desaea buscar quienes están inscriptos
http://127.0.0.1:8069/odoo/inscripciones/x/


1) - Se instaló PostgreSQL y se crearon los respectivos usuarios para ejecutarlo en el Sistema Operativo.

2) - Se clonó el repositorio de odoo (ver.17) en una carpeta de mi disco local y se ejecutó el proyecto en VSCode.

3) - Se creó un Módulo "aden" ubicado en > "modules/aden" llamado "Inscripciones de alumnos a programas".

4) - Se creó el manifest.py para configurar nombres, descripciones y carpetas del modulo.

5) - Se crearon 3 Modelos (Alumno, Programa e Inscripcion).

6) - Se crearon las vistas (carpeta views) con Menúes en la parte superior para poder acceder al listado de Alumnos, Programas e Inscripciones, a su vez agregar y eliminar los mismos.

7) - Se crearon 2 grupos de usuarios ("Si Edición" y "No Edición"), esto permite que a la hora de agregar un usuario y se le asigne el grupo "Si edición" como por ejemplo un usuario administrativo, permita editar y agregar valores y realizar el CRUD correspondiente, mientras que si a un usuario se le asigna el grupo "No Edición" este usuario no podrá realizar cambios en la base de datos.

8) - Se creó un controlador (carpeta controllers), para que pueda manejar solicitudes http y así crear una API pública, para poder obtener cuantos Alumnos, se encuentran Inscriptos en un determinado programa.
