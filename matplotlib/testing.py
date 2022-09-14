from matplotlib import pyplot as plt

from scratch. import

#
# years = [1950, 1960, 1970, 1980, 1990, 2000, 2010] #Годы
# gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3] #ВВП
# plt.plot(years, gdp, color='blue', marker='z', linestyle='solid')
# plt.title('Номинальный ВВП')
# plt.ylabel("Млрд $")
# plt.show()

movies = [ "Энни Холл", "Бен-Гур", "Касабланка", "Ганди", "Вестсайдская история"]
num_oscars = [5, 11, 3, 8, 10]

plt.bar(range(len(movies)), num_oscars, 0.5)

plt.title("My favorite movies")
plt.ylabel("# of prizes")

plt.xticks(range(len(movies)), movies)
plt.show()