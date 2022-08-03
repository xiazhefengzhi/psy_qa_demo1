import  pandas as pd
my_file1=pd.read_json("../Chinese-Psychological-QA-DataSet-master/data/ques_ans1.json")
temp1=my_file1.head(10)
print(temp1)