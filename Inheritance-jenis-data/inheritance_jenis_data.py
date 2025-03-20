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

class AdvanceDataProcessor(DataProcessor):
    def __init__(self, data_tuple, data_list, data_dict):
        super().__init__(data_tuple, data_list, data_dict)

    def add_to_list(self, item):
        """Menambahkan Item ke Dalam data_list"""
        self.data_list.append(item)
        print(f"Item '{item}' ditambahkan ke data_list")
    
    def update_dict(self, key, value):
        """Mengupdate nilai dalam data_dict"""
        if key in self.data_dict:
            self.data_dict[key] = value
            print(f"Key {key} diupdate dengan nilai {value}")
        else:
            print(f"Key {key} tidak ditemukan dalam data_dict")
        
    def count_tuple_elements(self):
        """Menghitung jumlah elemen dalam data_tuple"""
        count = len(self.data_tuple)
        print(f"Jumlah elemen dalam data_tuple {count}")


if __name__ == "__main__":
    data_tuple = (1,2,3,4,5)
    data_list = ["Apel", "Pisang", "Ceri"]
    data_dict = {"nama": "John", "usia": 25, "kota": "Jakarta"}

    processor = AdvanceDataProcessor(data_tuple, data_list, data_dict)

    processor.display_tuple()
    processor.display_list()
    processor.display_dict()

    processor.add_to_list("Durian")
    processor.update_dict("Usia", 26)
    processor.count_tuple_elements()

    print("\nSetelah Manipulasi data")
    processor.display_list()
    processor.display_dict()
