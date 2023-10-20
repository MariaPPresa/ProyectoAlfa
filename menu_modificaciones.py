
import sys
import random
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGridLayout, QFrame, QHBoxLayout

class MenuSemanal(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.datos_platos= None
        
    def leer_datos_de_base_de_datos(self):
        conn = sqlite3.connect("mi_base_de_datos.db")  # Reemplaza "mi_base_de_datos.db" con la ubicación de tu base de datos
        cursor = conn.cursor()

        # Realizar una consulta para recuperar datos
        cursor.execute("SELECT Nombre, Sano, Ofi FROM comidas")

        # Recuperar los resultados de la consulta
        resultados = cursor.fetchall()

        # Procesar los resultados y actualizar la interfaz gráfica
        self.datos_platos = {}
        for fila in resultados:
            nombre, tipo, detalles = fila
            if tipo not in self.datos_platos:
                self.datos_platos[tipo] = []
            self.datos_platos[tipo].append((nombre, detalles))

        conn.close()
        
    def initUI(self):
        self.setWindowTitle("Menú Semanal")
        self.setGeometry(100, 100, 600, 400)

        layout = QGridLayout()
        self.setLayout(layout)
        
        self.dias_semana = ["LUNES", "MARTES", "MIÉRCOLES", "JUEVES", "VIERNES", "SÁBADO", "DOMINGO"]
        
        self.desayuno_entries = []
        self.comida_entries = []
        self.cena_entries = []

        for dia in self.dias_semana:
            dia_frame = QFrame(self)
            dia_frame.setStyleSheet("background-color: #3498db; border-radius: 5px;")  # Cambia el color de fondo y el borde
            h_layout = QHBoxLayout(dia_frame)
    
            dia_button = QPushButton(dia, dia_frame)
            dia_button.clicked.connect(lambda checked, dia=dia: self.regenerar_menu(dia))
            h_layout.addWidget(dia_button)
    
            layout.addWidget(dia_frame, 0, self.dias_semana.index(dia))
            
            desayuno_label = QLabel("Desayuno")
            layout.addWidget(desayuno_label, 1, self.dias_semana.index(dia))
            desayuno_entry = QLineEdit()
            desayuno_entry.setReadOnly(True)
            desayuno_entry.setText(str(random.randint(1, 1000)))
            layout.addWidget(desayuno_entry, 2, self.dias_semana.index(dia))
            self.desayuno_entries.append(desayuno_entry)
            
            comida_label = QLabel("Comida")
            layout.addWidget(comida_label, 3, self.dias_semana.index(dia))
            comida_entry = QLineEdit()
            comida_entry.setReadOnly(True)
            comida_entry.setText(str(random.randint(1, 1000))
            )
            layout.addWidget(comida_entry, 4, self.dias_semana.index(dia))
            self.comida_entries.append(comida_entry)
            
            cena_label = QLabel("Cena")
            layout.addWidget(cena_label, 5, self.dias_semana.index(dia))
            cena_entry = QLineEdit()
            cena_entry.setReadOnly(True)
            cena_entry.setText(str(random.randint(1, 1000)))
            layout.addWidget(cena_entry, 6, self.dias_semana.index(dia))
            self.cena_entries.append(cena_entry)

    def regenerar_menu(self, dia):
        dia_index = self.dias_semana.index(dia)
        if self.datos_platos is not None:
            tipo_comida = None
            if dia_index == 0:  # Lunes
                tipo_comida = "Desayuno"
            elif dia_index == 1:  # Martes
                tipo_comida = "Comida"
            elif dia_index == 2:  # Miércoles
                tipo_comida = "Cena"

            if tipo_comida is not None:
                platos_disponibles = self.datos_platos.get(tipo_comida, [])
                if platos_disponibles:
                    plato, detalles = random.choice(platos_disponibles)
                    self.desayuno_entries[dia_index].setText(f"{plato}\n{detalles}")

def main():
    app = QApplication(sys.argv)
    menu_semanal = MenuSemanal()
    menu_semanal.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()