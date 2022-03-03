# print('hello')
# import json
#
# cont = {
#     "user1": "898989",
#     'user2': "233434"
# }
# ls = [3,4,5,6]
#
# print(type(cont))
# print(type(ls))
# json_cont = json.dumps(cont)
#
# print(type(json_cont))
#
# const = json.loads(json_cont)
#
# print(type(const))
import boto3

s3 = boto3.resource('s3')

# bucket = s3.create_bucket(Bucket='headstart334455')
s3.Bucket('headstart334455').delete()
buckets = s3.buckets.all()

print(type(buckets))

for bucket in buckets:
    print(bucket.name)


class Car:
    def __init__(self, max_speed: int):
        self.max_speed = max_speed
        self.speed=0
    def acc(self, speed:int):
        self.speed = self.speed+speed

mycar = Car(220)

print(mycar.max_speed)
print(mycar.speed)

mycar.acc(120)

print(mycar.speed)