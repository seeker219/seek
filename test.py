with open('/var/opt/check.txt', 'w') as file:
    for _ in range(3):
        file.write('test123\n')
