#li=['Dip',(25,35,65,65),{"name":"dip","age":25},25,35.6,[25,36,54],{'jan',"feb"}]
'''
for i in range(1,6,1):
    li.append(input("Enter Any Value"))
'''
#print(li[2])
#print(li[1][2])
#print(li[2]["name"])
#print(li[3])
#print(li[6][1])
#print(list(li[7])[1])
#print(li[1:])

#print(li[0:3])
#print(li[-1])
#print(li[::-1])

#===========================
li=[[35,32],[36,12,32],[0,8,-5,5],[5],[65,1,245]]
#li=[5,0,-5,6,9,0,4,2,5,1,99,2]
#print(sorted(li,key=len))
'''for i in li:
    i.sort()

print(li)
'''
'''
import re
filename=[
    "image15.jpg",
    "image0.5.jpg",
    "image1.jpg",
    "image5.jpg",
    "image9.jpg",
    "image7.jpg",
    "image10.jpg",
    "image8.jpg"
]
filename.insert(0,"image20.jpg")
#filename[0:6]=["image14.jpg","img19.jpg","img21.jpg","img23.jpg","img22.jpg","img28.jpg"]
#x=["image14.jpg","img19.jpg","img21.jpg","img23.jpg","img22.jpg","img28.jpg"]
for jj in x:
    filename.append(jj)
def fetchData(fname):
    return float(re.findall(r"\d+",fname)[0])

'''

#filename.sort(key=fetchData)
#print(filename)
'''
for i in filename:
    print(fetchData(i))
    '''
#=======================
x=[55,66,88,66,55,44,98]
li=[20,65,12,45,78,45,65,78,45,787,67,65]
#li.append(x)
li.extend(x)
print(li)
#li2=[20,65,12,45,78,45,65,78,45,787,67,65]
#li3=li+li2
#print(li3)
#print(li.count(65))
#li.sort(reverse=True)
#print(li)
#li.reverse()
#print(li)
#v=li.copy()
#v=li
#print(v)
#print(li*3)
#x=10,20,50,50,50,2,658,12,654,12
#y=list(x)
#print(type(y))
#li.remove(650)
#li.pop(25)
#del li[0:5]
#print(len(li))
#print(max(li))
#print(min(li))
#print(sum(li))
'''import re
def fetchData(fname):
    return (re.findall(r"\d+",fname)[1])
x=fetchData("d25.jpg36")
print(x)'''