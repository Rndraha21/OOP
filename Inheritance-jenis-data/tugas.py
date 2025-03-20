class DataProcessor:
    def __init__(self, data_tuple, data_list, data_dict):
        self.data_tuple = data_tuple
        self.data_list = data_list
        self.data_dict = data_dict

    def display_tuple(self):
        print("Data Tuple: ", self.data_tuple)

    def display_list(self):
        print("Data List: ", self.data_list)

    def display_dict(self):
        print("Data Dictionary: ", self.data_dict)

class DataAnalyzer(DataProcessor):
    def __init__(self, data_tuple, data_list, data_dict):
        super().__init__(data_tuple, data_list, data_dict)

    def average_tuple(self):
        if all(isinstance(x, (int, float)) for x in self.data_tuple):
            rata_rata = sum(self.data_tuple)/len(self.data_tuple)
            print(f"Rata-rata data tuple: {rata_rata}")
        else:
            print("Rata-rata tidak dapat dijumlahkan")
        
    def max_min(self):
        if all(isinstance(x, (int, float)) for x in self.data_list):
            maksimum = max(self.data_list)
            minimum = min(self.data_list)
            print(f"Nilai list: Maksimum {maksimum} dan {minimum} Minimum")
        else:
            print("Maksimum dan minimum tidak diketahui")

    def display_dict(self):
        print(f"Key data dictionary : {list(self.data_dict.keys())}")

if __name__ == "__main__":
    data_tuple = (30,23,50,84,100)
    data_list = ["30",23,50,84,100]
    data_dict = {"nama" : "Robin", "umur" : 20, "kab/kota": "Nias"}
    
    analisis = DataAnalyzer(data_tuple, data_list, data_dict)
    analisis.display_tuple()
    analisis.average_tuple()
    analisis.display_list()
    analisis.max_min()
    analisis.display_dict()