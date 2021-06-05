import csv
import statistics

with open('HeightWeight.csv',  newline = '') as f :
    data = csv.reader(f)
    file_data = list(data)


print(file_data[:5])
file_data.pop(0)

heights = []
sum_height = 0

for i in range(len(file_data)):
    h = file_data[i][1]
    sum_height +=  float(h)
    heights.append(float(h))

     




def mean():
    mean =  sum_height/len(heights)
    print( 'mean of heights :',mean )

mean()

print( 'median :', statistics.median(heights) )  
print('mode : ' , statistics.mode(heights) )  

