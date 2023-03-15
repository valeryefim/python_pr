# Задача 3. В базе данных ветеринарной клиники информация о пациентах-котах хранится в списке кортежей.
# Данные о кошках и их владельцах записаны в формате «Кличка животного, Возраст животного, Имя владельца, Фамилия владельца»:
cats = [('Мартин', 5, 'Алексей', 'Егоров'),
('Фродо', 3, 'Анна', 'Самохина'),
('Вася', 4, 'Андрей', 'Белов'),
('Муся', 7, 'Игорь', 'Бероев'),
('Изольда', 2, 'Игорь', 'Бероев'),
('Снейп', 1, 'Марина', 'Апраксина'),
('Лютик', 4, 'Виталий', 'Соломин'),
('Снежок', 3, 'Марина', 'Апраксина'),
('Марта', 5, 'Сергей', 'Колесников'),
('Буся', 12, 'Алена', 'Федорова'),
('Джонни', 10, 'Игорь', 'Андропов'),
('Мурзик', 1,'Даниил', 'Невзоров'),
('Барсик', 2, 'Виталий', 'Соломин'),
('Рыжик', 7, 'Владимир', 'Медведев'),
('Матильда', 8, 'Андрей', 'Белов'),
('Гарфилд', 3, 'Александр', 'Березуев')]

# Обнаружилось, что имена некоторых владельцев повторяются, потому что у них несколько кошек.
# Необходимо написать функцию, которая оптимизирует хранение данных таким образом, чтобы для каждого владельца данные о всех его животных отображались в одной строке:
# Игорь Бероев: Муся, 7; Изольда, 2
def print_optimized(cats_data: list) -> None:
    array = []
    for i in range(len(array)):
        name = array[i]
        for item in cats:
            if item != name in array:
                item = set(item)
                array.append(item)
            else:
                continue
    return print_optimized
print_optimized(cats)
