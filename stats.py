import matplotlib.pyplot as plt

fhand = open('StudentExercise.csv')

plot_data = list()
next(fhand)
for line in fhand:
    new_line = line.split(',')
    num1 = new_line[0]
    if len(num1) > 0:
        plot_data.append(float(num1))

plot_data.sort()
#print(plot_data)
plt.hist(plot_data,bins = 10)
plt.show()

    
