class City:
    """Şehri sıcaklığıyla birlikte ifade eden class."""
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature

    def __str__(self):
        return f"{self.name}: {self.temperature}°C"


class WeatherForecast:
    """Hava durumu tahmin class'ı."""
    def __init__(self):
        self.cities = {}

    def add_city(self, name, temperature):
        """Şehir sıcaklığı ekleme veya güncelleme."""
        self.cities[name.lower()] = City(name, temperature)
        print(f"'{name}' şehrinin sıcaklığı bu değer ile ' ' {temperature} değiştirildi veya bu değer' ' {temperature} eklendi°C.")

    def get_weather(self, name):
        """Seçilen bir şehrin hava durumunu getirir."""
        city = self.cities.get(name.lower())
        if city:
            print(f"{city.name} şehrinin hava durumu: {city.temperature}°C")
            return city
        else:
            print(f"'{name}'şehir sistemde bulunamadı.")
            return None

    def get_advice(self, name):
        """Şehrin sıcaklığına göre önderi."""
        city = self.get_weather(name)
        if city:
            temp = city.temperature
            if temp < 0:
                advice = "Soğuk, sıkı giyinin."
            elif 0 <= temp <= 15:
                advice = "Serin, mont almayı unutmayın."
            else:
                advice = "Hava güzel, rahat giyin."
            print(f"Öneri: {advice}")


# Örnek kullanım;
if __name__ == "__main__":
    weather_system = WeatherForecast()

    while True:
        print("\n1. Şehir ve sıcaklık ekle/güncelle")
        print("2. Şehir hava durumunu sorgula")
        print("3. Çıkış")
        choice = input("Bir seçenek seçin: ")

        if choice == "1":
            city_name = input("Şehir adını girin: ")
            try:
                temperature = float(input(f"{city_name} için sıcaklığı girin (°C): "))
                weather_system.add_city(city_name, temperature)
            except ValueError:
                print("Geçerli bir sıcaklık değeri giriniz.")

        elif choice == "2":
            city_name = input("Hava durumunu sorgulamak istediğiniz şehir adını girin: ")
            weather_system.get_advice(city_name)

        elif choice == "3":
            print("Çıkılıyor...")
            break

        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
