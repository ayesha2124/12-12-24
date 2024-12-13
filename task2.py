#accept basic salery and find gross salary in python
#gs=hra+da+basic
#basic<10000
#-- HRA-67% on basic salary
#--da is :73% on basic salary
#basic b/w 10k & 20k
#-- HRA-69% on basic salary
#--da is :76% on basic salary
#basic above 20k:
##--da is :89% on basic salary
sal = float(input("Enter basic salary: "))
if(sal< 10000):
    hra = 0.67 *sal
    da = 0.73 * sal
elif(sal>=10000 and sal <= 20000):
    hra = 0.69 * sal
    da = 0.76 * sal
else:
    hra = 0.73 * sal
    da = 0.89 * sal
gross_salary = sal + hra + da
print(f"Gross Salary: {gross_salary}")
