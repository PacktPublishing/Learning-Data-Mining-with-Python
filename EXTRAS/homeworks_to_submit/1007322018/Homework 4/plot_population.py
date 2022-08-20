import requests
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt
import numpy as np
from itertools import count
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

x_values = []
y_values = []

index = count()


def animate(i):
    page  = requests.get("https://countrymeters.info/en/World")
    soup = BeautifulSoup(page.content, 'html.parser')
    Numbers = soup.select('.counter')
    NumberPopulation="".join(re.findall(r'(\d+)',str(Numbers[0])))[1:]
    x_values.append(next(index))
    y_values.append(NumberPopulation)
    plt.cla()
    plt.plot(x_values, y_values)
    plt.title('World Population')


ani = FuncAnimation(fig, animate, 1000)
plt.tight_layout()
plt.show()
