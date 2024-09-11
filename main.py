def auth_menu():
    text = """
    1.Register
    2.Login
    3.Exit
    """
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        pass
    elif user_input == '2':
        pass
    elif user_input == '3':
        return
    else:
        print('Unexpected character, try again!')
        return auth_menu()


def admin_menu():
    text = """
    1.Mavsum yaratish va takliflar qabul qilishni boshlash
    2.Takliflar bilan ishlash 
    3.Takliflarni to'xtatish va ovoz berishni boshlash
    4.Ovoz berishni to'xtatish va g'oliblarni aniqlash
    5.Faol mavsum real vaqt natijalarini olish
    6.Barcha mavsumlarni ko'rish
    7.Orqaga
    """
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        pass
    elif user_input == '2':
        work_with_offers()
    elif user_input == '3':
        pass
    elif user_input == '4':
        pass
    elif user_input == '5':
        pass
    elif user_input == '6':
        pass
    elif user_input == '7':
        return auth_menu()
    else:
        print('Unexpected character, try again!')
        return admin_menu()


def work_with_offers():
    text = """
    1.Faol mavsum barcha kelgan takliflarni ko'rish
    2.Taklifni id orqali ma'qullash yoki rad etish
    3.Barcha ma'qullangan takliflar
    4.Barcha rad etilgan takliflar
    5.Barcha kutilayotgan takliflar
    6.Orqaga
    """
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        pass
    elif user_input == '2':
        pass
    elif user_input == '3':
        pass
    elif user_input == '4':
        pass
    elif user_input == '5':
        pass
    elif user_input == '6':
        return admin_menu()
    else:
        print('Unexpected character, try again!')
        return work_with_offers()


def user_menu():
    text = """
    1.Faol mavsum haqida ma'lumot
    2.Faol mavsumga taklif berish
    3.Taklif holatini tekshirish
    4.Barcha ma'qullangan takliflar
    5.Ovoz berish
    6.Faol mavsum real vaqt natijalarini olish
    7.Mavsum g'oliblarini id orqali ko'rish
    8.Orqaga
    """
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        pass
    elif user_input == '2':
        pass
    elif user_input == '3':
        pass
    elif user_input == '4':
        pass
    elif user_input == '5':
        pass
    elif user_input == '6':
        pass
    elif user_input == '7':
        pass
    elif user_input == '8':
        return auth_menu()
    else:
        print('Unexpected character, try again!')
        return user_menu()

auth_menu()
