#immutable - it mean it can not be changed

s3_bucket_list = ("payal_demo_bucket","anshal_demo_bucket")
print (type(s3_bucket_list))

#length function in tuple is worked
s3_bucket_list = ("payal_demo_bucket","sonu_demo_bucket","anshal_demo_bucket","dev_demo_bucket")
print(len(s3_bucket_list))





'''
# when we try to add new item it give error
s_names = ("payal","ram","sonu","dev","anshal")
s_names.append("hit")
print(s_names)

<class 'tuple'>
Traceback (most recent call last):
AttributeError: 'tuple' object has no attribute 'append' '''

