# import library
import statistics

class StatAnalyzer:
    def __init__(self, data: list):


        self.__data = list(data)

    # Getter untuk mengambil nilai data
    def get_data(self) -> list:
        return self.__data

    #method untuk menghitung rata-rata
    def mean(self) -> float:
        return statistics.mean(self.__data)

    #method untuk menghitung nilai tengah
    def median(self) -> float:
        return statistics.median(self.__data)

    #method untuk menghitung standar deviasi
    def std(self) -> float:

        if len(self.__data) < 2:
            return 0.0
        return statistics.stdev(self.__data)

    def display_results(self):
        print("=== Analisis Statistik ===")
        print(f"Mean          : {self.mean():.2f}")
        print(f"Median        : {self.median()}")
        print(f"Std Deviation : {self.std():.4f}")

# Uji coba pada List
angka = [5, 7, 3, 9, 2]
analyzer = StatAnalyzer(angka)
analyzer.display_results()