# openspace.py
import random
from typing import List
from src.table import Table  # Import Table from table.py

class OpenSpace:
    def __init__(self, number_of_tables: int, seats_per_table: int):
        self.tables = [Table(seats_per_table) for _ in range(number_of_tables)]
    
    def organize(self, names: List[str]):
        random.shuffle(names)
        for name in names:
            for table in self.tables:
                if table.assign_seat(name):
                    break
    
    def display(self):
        for i, table in enumerate(self.tables, 1):
            print(f"Table {i}:")
            for seat in table.seats:
                occupant = seat.occupant if seat.occupant else "Empty"
                print(f"  - {occupant}")
    
    def store(self, filename: str):
        import pandas as pd
        data = []
        for table_idx, table in enumerate(self.tables, 1):
            for seat_idx, seat in enumerate(table.seats, 1):
                data.append({"Table": table_idx, "Seat": seat_idx, "Occupant": seat.occupant or "Empty"})
        
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)
