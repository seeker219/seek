with open('/var/meta/check.txt', 'w') as file:
    for _ in range(3):
        file.write('it works\n')
