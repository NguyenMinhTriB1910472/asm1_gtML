from operator import index
# Task 1
# import thư viện 
import pandas as pd
import re
# Nhập tên file cần tìm
filename = input("Enter a class file to grade (i.e. class1 for class1.txt): ")
print(f'Successfully opened {filename}.txt')
print('**** ANALYZING ****\n')
# đọc file
try: 
    data=pd.read_csv(f'Data Files\{filename}.txt',sep=' ',header=None)
except:
    print("Sorry, Can not find this filename")
# Task 2
# khởi tạo List 
list=[]
error_valid_N=[]
error_valid_26=[]


# xử lý lỗi
for i in range(len(data)):
  c= (data[0][i]).split(sep=",")
  list.append(c)
  if len(c)!=26:
    print('Invalid line of data: does not contain exactly 26 values: \n',data[0][i])
    error_valid_26.append(c)
    data.drop( index=[i] , inplace=True)
    list.remove(c)
  elif len(c[0]) != 9:
    print('Invalid line of data: N# is invalid \n',data[0][i])
    error_valid_N.append(c)
    data.drop(index=[i] , inplace =True)
    list.remove(c)
  elif len(c[0])==9:
    regex= re.compile(r'^N(\d{8})$')
    if bool(regex.match(c[0])) == False:
      print('Invalid line of data: N# is invalid \n',data[0][i])
      error_valid_N.append(c)
      data.drop(index=[i],inplace=True)
      list.remove(c)

# print('Lỗi 26 ký tự va lỗi Ký tự 'N')


if len(error_valid_N) + len(error_valid_26) ==0:
  print('No errors found!\n')
print('**** REPORT ****')

print('Total valid lines of data: {}'.format(len(data)))
print('Total invalid lines of data: {}'.format(len(error_valid_N) + len(error_valid_26)))

# Task 3
list_score=[]
list_name=[]
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
list_answer=answer_key.split(sep=",")
# tính điểm
for core in list:
    mark=0
    name=''
    for j,answer in enumerate(core):
        if 'N' in answer:
            name=answer
        elif answer == list_answer[j-1]:
            mark+=4
        elif answer =='':
            mark+=0
        elif answer != list_answer[j-1]:
            mark+=-1
    list_name.append(name)
    list_score.append(mark)

df = pd.DataFrame(
    {
        'name': list_name,
        'score':list_score
    }
) 

# tính các giá trị theo yêu cầu đề , dùng pandas
avg= df.score.mean()
min= df.score.min()
max= df.score.max()
Range =max-min
Median = df.score.median()
print(avg,min,max,Range,Median)

# task 4
df.to_csv(f"{filename}_grades.txt",index=False,header=None)