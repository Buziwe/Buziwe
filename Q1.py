# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:06:57 2020

@author: 212560141
"""
# Summative Assessment 
    #Question 1
#Generate a dummy dataset of 32 sensor clusters 
for x  in range(1,33): #Generates sequential 32 sensor clusters
    import random      #Import random.random built in to generate 16 float entries between 0 and 1 for each cluster
    cluster = [random.random() for i in range(1,17)] #Generates 16 floats entries
    print('cluster', x,cluster) #Prints out dataset of 32 clusters with 16 float entries each
    
    
    #Question 2
file = open ("SensorClusters.txt","w")

for x  in range(1,33):
    file.write("\n")
    import random
    cluster = [random.random() for i in range(1,17)]
    print('cluster', x,cluster)
    file.write("cluster")
    file.write(str(x))
    file.write(str(cluster))
else:
    file.close()
    print("finished")
    
 
