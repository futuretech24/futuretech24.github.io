def decode_bday(s):
    result = pow(s, 667, 1255)
    day = result % 100
    month = result // 100

    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    if 1 <= month <= 12 and 1 <= day <= 31:
        return f"{months[month - 1]} {day:02d}"
    else:
        return "Invalid date"

secret_num = int(input("Enter the secret number: "))
bday = decode_bday(secret_num)
print(f'Birthday: {bday}')
