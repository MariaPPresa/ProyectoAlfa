import sys
import random
import json
from PyQt5.QtWidgets import *
    
class WeeklyMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def read_data(self):
        """
        Reads comidas.json and returns a tuple:
            [0] list of all breakfasts
            [1] list of all lunches
            [2] list of all dinners

        """
        with open("comidas.json", "r") as file:
            data = json.load(file)
        
        all_breakfasts = [meal for meal in data if "Breakfast" in meal["time"]]
        all_lunches = [meal for meal in data if "Lunch" in meal["time"]]
        all_dinners =[meal for meal in data if "Dinner" in meal["time"]]
        return all_breakfasts,  all_lunches, all_dinners
        
    def get_lastMenu(filename):
      with open(filename, "r") as f:
        lines = f.readlines()

      # Split each line into a list of strings.
      list1 = []
      list2 = []
      list3 = []
      for line in lines:
        list_of_strings = line.split()
        list1.append(list_of_strings[0])
        list2.append(list_of_strings[1])
        list3.append(list_of_strings[2])

      return list1, list2, list3


    def write_thisMenu(filename, list1, list2, list3):
      with open(filename, "w") as f:
        for i in range(len(list1)):
          f.write(f"{list1[i]} {list2[i]} {list3[i]}\n")
    
    
    def generate_breakfast(self):
        """
            Generate the 7 breakfast meals of the week 
            From Monday to Saturday it is always "Desayuno". Only special breakfast on Sundays
        
            Returns a list of 7 dishes:breakfast
        """
        
        all_breakfasts = self.read_data()[0]      

        meal_names = [meal["name"] for meal in all_breakfasts]
        breakfast_list = ["Desayuno"] * 6 + random.sample(meal_names, 1)
        return breakfast_list
        """
            Generate the 7 breakfast meals of the week
        
            Returns a list of 7 dishes:breakfast
        """
        
        all_breakfasts = read_data()[0]      

        meal_names = [meal["name"] for meal in all_breakfasts]

        # Choose 7 random meals from the smaller list
        breakfast_list = "Desayuno" * 6 + random.sample(meal_names, 1)
        return breakfast_list

    def get_lastWeek(self):
        """
            Reads txt (previous week)
            Returns 3 lists [breakfast][lunch][dinner]
        """
        all_lunches = self.read_data()[1]             
        all_dinners = self.read_data()[2]   
        
        # Create lists for each category
        fish_list = [meal for meal in all_lunches if meal["category"] == "Pescado"]
        meat_list = [meal for meal in all_lunches if meal["category"] == "Carne"]
        pasta_list = [meal for meal in all_lunches if meal["category"] == "Pasta"]
        legumbres_list = [meal for meal in all_lunches if meal["category"] == "Legumbres"]
        arroz_list = [meal for meal in all_lunches if meal["category"] == "Arroz"]
        verdura_list = [meal for meal in all_lunches if meal["category"] == "Verdura"]

        meal_names = [meal["name"] for meal in all_dinners]
        lunch_list = random.sample(meal_names, 7)
        dinner_list = random.sample(meal_names, 7)
        return lunch_list,dinner_list
    
    def generate_lunch_dinner(self, breakfast_list):
        """
            Generate the 7 dinner meals of the week. Takes into consideration lunches and breaksfasts.
        
            Returns a list of 7 dishes:dinner
        """
        all_lunches = self.read_data()[1]             
        all_dinners = self.read_data()[2]   
        
        # Create lists for each category
        fish_list = [meal for meal in all_lunches if meal["category"] == "Pescado"]
        meat_list = [meal for meal in all_lunches if meal["category"] == "Carne"]
        pasta_list = [meal for meal in all_lunches if meal["category"] == "Pasta"]
        legumbres_list = [meal for meal in all_lunches if meal["category"] == "Legumbres"]
        arroz_list = [meal for meal in all_lunches if meal["category"] == "Arroz"]
        verdura_list = [meal for meal in all_lunches if meal["category"] == "Verdura"]

        meal_names = [meal["name"] for meal in all_dinners]
        lunch_list = random.sample(meal_names, 7)
        dinner_list = random.sample(meal_names, 7)
        return lunch_list,dinner_list
        
    def initUI(self):
        
        #Creates new window
        self.setWindowTitle("Menú Semanal")
        self.setGeometry(100, 100, 600, 400)

        #Create grid
        layout = QGridLayout()
        self.setLayout(layout)
        
        self.week_days = ["LUNES", "MARTES", "MIÉRCOLES", "JUEVES", "VIERNES", "SÁBADO", "DOMINGO"]
        
        self.breakfast_entries = []
        self.lunch_entries = []
        self.dinner_entries = []

        breakfastList = self.generate_breakfast()
        lunchList = self.generate_lunch_dinner(breakfastList)[0]
        dinnerList = self.generate_lunch_dinner(breakfastList)[1]
        
        for day in self.week_days:
            day_frame = QFrame(self)
            day_frame.setStyleSheet("background-color: #3498db; border-radius: 5px;")  # Cambia el color de fondo y el borde
            h_layout = QHBoxLayout(day_frame)
            
            day_button = QPushButton(day, day_frame)
            day_button.clicked.connect(lambda checked, day=day: self.regenerate_menu(day))
            h_layout.addWidget(day_button)
    
            layout.addWidget(day_frame, 0, self.week_days.index(day))
            
            breakfast_entry = QLineEdit()
            breakfast_entry.setReadOnly(True)
            breakfast_entry.setText(breakfastList[self.week_days.index(day)])
            layout.addWidget(breakfast_entry, 2, self.week_days.index(day))
            self.breakfast_entries.append(breakfast_entry)
            
            lunch_entry = QLineEdit()
            lunch_entry.setReadOnly(True)
            lunch_entry.setText(lunchList[self.week_days.index(day)])
            layout.addWidget(lunch_entry, 4, self.week_days.index(day))
            self.lunch_entries.append(lunch_entry)
            
            dinner_entry = QLineEdit()
            dinner_entry.setReadOnly(True)
            dinner_entry.setText(dinnerList[self.week_days.index(day)])
            layout.addWidget(dinner_entry, 6, self.week_days.index(day))
            self.dinner_entries.append(dinner_entry)
            
        # Add a spacer to the layout to ensure that it is evenly spaced
        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer, 7, 0)

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