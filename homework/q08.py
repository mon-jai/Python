name = input()
birthday = input()

FirstName, LastName = name.split(' ')
yyyy, mm, dd = birthday.split('/')

print(f'{FirstName} is born at year {yyyy} month {mm} day {dd} in {LastName} family.')
