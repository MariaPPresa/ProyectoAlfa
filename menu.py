import sys
import random
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGridLayout, QFrame, QHBoxLayout
    
class WeeklyMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def read_data(self):
        with open("comidas.json", "r") as f:
            data = f.read()

        dishes = json.loads(data)

        return dishes 
        
    def generate_dinners(self):
        """
            Genera las 7 cenas aleatorias de la semana.
        
            Returns:
                Una lista de 7 cenas
                """

        # Leer los datos del JSON
        dishes = self.read_data()

        # Obtener una lista de las cenas
        #dinners = [dish["name"] for dish in dishes if int(dish["time"].count("Cena")) > 0]
        dinners = [dish for dish in dishes]
        few_dinners = []
    
        # Usar una comprensión de lista para obtener solo los nombres
        nombres_platos = [plato["name"] for plato in dishes]

        # Elegir 7 cenas aleatorias
        dinners_list = random.sample(nombres_platos, 7)
        return dinners_list
        
    def initUI(self):
        self.setWindowTitle("Menú Semanal")
        self.setGeometry(100, 100, 600, 400)

        layout = QGridLayout()
        self.setLayout(layout)
        
        self.week_days = ["LUNES", "MARTES", "MIÉRCOLES", "JUEVES", "VIERNES", "SÁBADO", "DOMINGO"]
        
        self.breakfast_entries = []
        self.lunch_entries = []
        self.dinner_entries = []
        
        dinnerList = self.generate_dinners()
        
        for day in self.week_days:
            day_frame = QFrame(self)
            day_frame.setStyleSheet("background-color: #3498db; border-radius: 5px;")  # Cambia el color de fondo y el borde
            h_layout = QHBoxLayout(day_frame)
    
            day_button = QPushButton(day, day_frame)
            day_button.clicked.connect(lambda checked, day=day: self.regenerate_menu(day))
            h_layout.addWidget(day_button)
    
            layout.addWidget(day_frame, 0, self.week_days.index(day))
            
            breakfast_label = QLabel("breakfast")
            layout.addWidget(breakfast_label, 1, self.week_days.index(day))
            breakfast_entry = QLineEdit()
            breakfast_entry.setReadOnly(True)
            breakfast_entry.setText(str(random.randint(1, 1000)))
            layout.addWidget(breakfast_entry, 2, self.week_days.index(day))
            self.breakfast_entries.append(breakfast_entry)
            
            lunch_label = QLabel("luncha")
            layout.addWidget(lunch_label, 3, self.week_days.index(day))
            lunch_entry = QLineEdit()
            lunch_entry.setReadOnly(True)
            lunch_entry.setText(str(random.randint(1, 1000))
            )
            layout.addWidget(lunch_entry, 4, self.week_days.index(day))
            self.lunch_entries.append(lunch_entry)
            
            dinner_label = QLabel("dinner")
            layout.addWidget(dinner_label, 5, self.week_days.index(day))
            dinner_entry = QLineEdit()
            dinner_entry.setReadOnly(True)
            dinner_entry.setText(dinnerList[self.week_days.index(day)])
            layout.addWidget(dinner_entry, 6, self.week_days.index(day))
            self.dinner_entries.append(dinner_entry)



    def regenerte_menu(self, day):
        day_index = self.week_days.index(day)
        breakfast = random.randint(1, 1000)
        lunch = random.randint(1, 1000)
        dinner = random.randint(1, 1000)
        self.breakfast_entries[day_index].setText(str(breakfast))
        self.lunch_entries[day_index].setText(str(lunch))
        self.dinner_entries[day_index].setText(str(dinner))

def main():
    """
    La funcion tal hace tal
     - app: llama a tal y devuelve esto
    """
    app = QApplication(sys.argv)
    weekly_menu = WeeklyMenu()
    weekly_menu.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
