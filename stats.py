import matplotlib.pyplot as plt
import statistics

def median(ls):
    if len(ls) % 2 == 0:
        return (ls[len(ls)/2] + ls[(len(ls)/2)+1])/2
    else:
        return (ls[len(ls)//2])
    

fhand = open('StudentExercise.csv')

plot_data = list()
next(fhand)
for line in fhand:
    new_line = line.split(',')
    num1 = new_line[0]
    if len(num1) > 0:
        plot_data.append(float(num1))

plot_data.sort()
plt.hist(plot_data,bins = 10)
plt.show()

#########a###########
average = statistics.mean(plot_data)
print(average)


#########b###########
count = 0
for element in plot_data:
    if element > average:
        count+=1

prop_stud = count/len(plot_data)
print(prop_stud)


#########c###########
print(median(plot_data))

