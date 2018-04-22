#to create and read file
fw=open('sample.txt','w')
fw.write('I love me \n')
fw.write('I love my family')
fw.close()

fr=open('sample.txt','r')
text=fr.read()
print(text)
fr.close()