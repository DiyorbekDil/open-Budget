from auth_menu import register, login, logout
from admin_functions import create_season, show_all_seasons, add_category, show_all_categories
from admin_functions import stop_accepting_offers, stop_accepting_votes
from user_functions import show_active_season, send_offer, check_my_offer, vote
from admin_functions import get_all_offers, approve_or_reject_offer


def auth_menu():
    text = """
    1.Register
    2.Login
    3.Exit
    """
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        register()
        auth_menu()
    elif user_input == '2':
        result = login()
        if result == 'admin':
            return admin_menu()
        elif result == 'user':
            return user_menu()
        else:
            print(result)
        auth_menu()
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
    7.Kategoriya qo'shish
    8.Barcha kategoriyalarni ko'rish
    9.Orqaga
    """
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        create_season()
        admin_menu()
    elif user_input == '2':
        work_with_offers()
    elif user_input == '3':
        stop_accepting_offers()
        admin_menu()
    elif user_input == '4':
        stop_accepting_votes()
        admin_menu()
    elif user_input == '5':
        pass
    elif user_input == '6':
        show_all_seasons()
        admin_menu()
    elif user_input == '7':
        add_category()
        admin_menu()
    elif user_input == '8':
        show_all_categories()
        admin_menu()
    elif user_input == '9':
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
        get_all_offers('all')
        work_with_offers()
    elif user_input == '2':
        approve_or_reject_offer()
        work_with_offers()
    elif user_input == '3':
        get_all_offers('approved')
        work_with_offers()
    elif user_input == '4':
        get_all_offers('rejected')
        work_with_offers()
    elif user_input == '5':
        get_all_offers('pending')
        work_with_offers()
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
    8.Barcha kategoriyalarni ko'rish
    9.Barcha mavsumlarni ko'rish
    10.Orqaga
    """
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        show_active_season()
        user_menu()
    elif user_input == '2':
        send_offer()
        user_menu()
    elif user_input == '3':
        check_my_offer()
        user_menu()
    elif user_input == '4':
        get_all_offers('approved')
        user_menu()
    elif user_input == '5':
        vote()
        user_menu()
    elif user_input == '6':
        pass
    elif user_input == '7':
        pass
    elif user_input == '8':
        show_all_categories()
        user_menu()
    elif user_input == '9':
        show_all_seasons()
        user_menu()
    elif user_input == '10':
        logout()
        return auth_menu()
    else:
        print('Unexpected character, try again!')
        return user_menu()


if __name__ == '__main__':
    auth_menu()
