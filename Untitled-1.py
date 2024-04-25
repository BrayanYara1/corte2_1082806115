class Car:
    def __init__(self, brand, model, year, color, category_id):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.category_id = category_id

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}), Color: {self.color}"

    def save_to_db(self, conn):
        query = "INSERT INTO cars (brand, model, year, color, category_id) VALUES (?, ?, ?, ?, ?)"
        conn.execute(query, (self.brand, self.model, self.year, self.color, self.category_id))
        conn.commit()

    @staticmethod
    def get_all_cars(conn):
        query = "SELECT * FROM cars"
        cursor = conn.execute(query)
        return cursor.fetchall()
