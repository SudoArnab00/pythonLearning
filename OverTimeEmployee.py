def emp_of_month(mytime = []):
    employee = ''
    hrs = 0
    for emp,time in mytime:
        if time > hrs:
            employee = emp
            hrs = time
    return employee,hrs

overTime = [('Alice',190),('Ben',780),('Mary',672)]
print(emp_of_month(overTime))