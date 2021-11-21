# number of seconds as days-hours-minutes-seconds

seconds_input = int(input('Введите число секунд: '))

days = seconds_input // (60*60*24)
hours = (seconds_input // (60*60)) % 24
minutes = (seconds_input // 60) % 60
seconds = seconds_input % 60

print('{} дней {} часов {} минут {} секунд'.format(days, hours, minutes, seconds))
