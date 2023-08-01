import sys

from PySide6.QtWidgets import QApplication

from servicio.persona_principal import PersonaPrincipal
from data.conexion import * 

con = Conexion.obtenerConexion()

app = QApplication()
vtn_principal = PersonaPrincipal()
vtn_principal.show()
sys.exit(app.exec())