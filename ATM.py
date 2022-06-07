def password(password):
    if len(password) == 4:
        return password
    else:
        return False

def lang(language):
    if language == 'EN' or language == 'RU':
        return language
    else:
        return False

def act_RU (action):
    if action == '1':
        print('Ваш баланс равен 1500 BY')
    if action == '2':
        print(input('Введите сумму:  '))
    if action == '3':
        print('Вставьте купюры в купюроприёмник ')

def act_EN (action):
    if action == '1':
        print('Your balance is 1500 BY')
    if action == '2':
        print(input('Enter amount: '))
    if action == '3':
        print('Insert banknotes into bill acceptor')

def bank():
    pas = input('Ввeдите пароль ****: ')
    if password(pas) != False:
        language = input('Выберите язык (RU/EN) -  ')
        if language == 'RU':
            if lang(language) != False:
                action = input('Выберите номер действия с картой: 1. Проверка баланса 2. Снятие наличных 3. Пополнить счёт')
                act_RU(action)
        if language == 'EN':
            if lang(language) != False:
                action = input('Select the card action number: 1. Balance check 2. Cash withdrawal 3. Top up account')
                act_EN(action)

bank()