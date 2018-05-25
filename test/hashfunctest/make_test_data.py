filename=r".\hp.txt"
targetfile=r".\testdata.h" 

head='''
/*
该文本来自哈利波特
*/


const char * teststr[]={
'''

end1='''};
'''
end2='''
/*包含{}个字符，{}个字符串*/

#define MAX_STR {}
'''



if __name__=="__main__":
	count=0
	chars=0
	with open(filename,"r") as file:
		with open(targetfile,"w") as file2:
			file2.write(head)
			for i in file.readlines():
				i=i.replace("\n","")
				i=i.replace("\\","\\\\")
				i=i.replace("\"","\\\"")
				i=i.replace("\f","")
				if len(i)>2:
					chars+=len(i)
					count+=1	
					j="\""+i+"\",\n"
					file2.write(j)
			file2.write(end1)		
			file2.write(end2.format(chars,count,count))	
	print(chars)		
	print(count)		