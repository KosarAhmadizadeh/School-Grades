#!/usr/bin/env python
# coding: utf-8

# In[6]:


student_names = input().split(',')#takes string for names

course_names = input().split(',')#takes string for courses

#taking scores
matrix = []
for i in range(0,len(course_names)):
    a = input().split(',')#takes score for each lesson
    #score[i] = score[i].split(",")[ :len(student_names)-1]
    matrix.append(a)

#find max of each score
for i in range(0,len(course_names)):
    matrix[i] = [int(j) for j in matrix[i]] 
    
for i in range(0,len(course_names)):
    max = matrix[i][0]
    for j in range(0,len(student_names)):
        if max < matrix[i][j]:
            max = matrix[i][j]
    print("max -->",course_names[i],":",max)
        
#find max of each student
for i in range(0,len(student_names)):
    max = matrix[0][i]
    for j in range(0,len(course_names)):
        if max < matrix[j][i]:
            max = matrix[j][i]
    print("max -->",student_names[i],":",max)
    
#finding mode of each lesson   
import statistics
for i in range(0,len(course_names)):
    b = statistics.multimode(matrix[i][:])
    print("mode -->",course_names[i],':',b)
    if b[0]<10:
        print(course_names[i],"scores are not standard.")
        
#finding mode of each student
for i in range(0,len(student_names)):
    b=[]
    for j in range(0,len(course_names)):
        b.append(matrix[j][i])
    b = statistics.multimode(b)
    print("mode -->",student_names[i],':',b)
    if b[0]<10:
        print(student_names[i],"scores are not standard.")
#histogram of courses        
for i in range(0,len(course_names)):
    print(course_names[i],":")
    for j in range (0,len(student_names)):
        a = matrix[i][j]
        for m in range (j+1,len(student_names)):
            k=1
            if matrix[i][m] ==a:
                k+=1
        print(matrix[i][j],":","*"*k)
        
#histogram of students        
for i in range(0,len(student_names)):
    print(student_names[i],":")
    for j in range (0,len(course_names)):
        a = matrix[j][i]
        for m in range (j+1,len(course_names)):
            k=1
            if matrix[m][i] ==a:
                k+=1
        print(matrix[j][i],":","*"*k)

