from faker import Faker, Factory

# 通过工厂函数来创建
fake1 = Factory.create()
# 通过构造函数来创建
fake2 = Faker()
fake_cn = Faker("zh_CN")


# print(fake2.name())
print(fake_cn.name())
# print(fake2.company())
print(fake_cn.company())
print(fake_cn.ssn(min_age=16, max_age=90))

print(fake2.random_number(4))
a=5
