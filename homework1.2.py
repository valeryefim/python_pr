# Задача 2. Данные об email-адресах студентов хранятся в словаре:
emails = {'mgu.edu': ['andrei_ivanov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
      	'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
      	'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
      	'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
      	'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
      	'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}

# Нужно написать функцию, которая вывела бы все адреса в алфавитном порядке и в формате имя_пользователя@домен.
'''
def print_emails(emails_data: dict) -> None:
    for domain, users in emails_data.items():
		users_sorted = sorted(users)
		for user in users_sorted:
			print(f'{user}@{domain})
print(print_emails)
'''

def print_emails(emails_data: dict) -> None:
    for domain, users in emails_data.items():
        users_sorted = sorted(users)
        for user in users_sorted:
            print(f"{user}@{domain}")
print_emails(emails)