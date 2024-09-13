from db_manager import execute_query
from user_functions import get_offer_active_season


def create_season():
    query = """insert into mavsum (taklif_status, is_active) values (True, False); """
    execute_query(query)
    print('Mavsum yaratildi!')


def show_all_seasons():
    query = """select * from mavsum"""
    seasons = execute_query(query, fetch='all')
    print("Mavsum id - taklif qabuli - ovoz qabuli")
    for season in seasons:
        print(f"{season[0]} - {season[1]} - {season[2]}")


def add_category():
    try:
        name = input('Kategoriya nomini kiriting: ')
        num_of_winners = int(input("G'oliblar sonini kiriting: "))
        params = name, num_of_winners
        query = "insert into categories (name, num_of_winners) values (%s, %s);"
        execute_query(query, params)
        print('Added')
    except ValueError:
        print("G'oliblar soni butun son bo'lishi kerak")


def show_all_categories():
    query = """select * from categories"""
    categories = execute_query(query, fetch='all')
    print("Kategoriya id - nomi - g'oliblar soni")
    for category in categories:
        print(f"{category[0]} - {category[1]} - {category[2]}")


def stop_accepting_offers():
    try:
        season_id = int(input('Mavsum idsini kiriting: '))
        if not get_season_by_id(season_id):
            print('Bunaqa raqamli mavsum yo\'q')

        params = (season_id,)
        query = "update mavsum set is_active=True where id=%s"
        execute_query(query, params)
        print('Muvaffaqiyatli')
    except ValueError:
        print('Mavsum id butun sondir')


def stop_accepting_votes():
    try:
        season_id = int(input('Mavsum idsini kiriting: '))
        params = (season_id,)
        query = "update mavsum set is_active=False, taklif_status=False where id=%s"
        execute_query(query, params)
        print('Muvaffaqiyatli')
    except ValueError:
        print('Mavsum id butun sondir')


def get_season_by_id(season_id):
    query = """select * from mavsum where id = %s"""
    params = season_id,
    return execute_query(query, params, fetch='one')


def get_all_offers(condition):
    try:
        season_id = int(input('Mavsum idsini kiriting: '))
        if not get_season_by_id(season_id):
            print('Bunaqa raqamli mavsum yo\'q')

        if condition == 'all':
            query = """select * from takliflar where mavsum_id = %s"""
        elif condition == 'approved':
            query = """select * from takliflar where mavsum_id = %s and status='ma_qullansin';"""
        elif condition == 'rejected':
            query = """select * from takliflar where mavsum_id = %s and status='rad etilsin';"""
        else:
            query = """select * from takliflar where mavsum_id = %s and status='kutilmoqda';"""

        params = season_id,
        results = execute_query(query, params, fetch='all')
        print('id, mavsum_id, user_id, description, status, category_id')
        for result in results:
            print(result)
    except ValueError:
        print('Mavsum id butun sondir!')


def approve_or_reject_offer():
    try:
        season_id = int(input('Mavsum idsini kiriting: '))
        if not get_season_by_id(season_id):
            print('Bunaqa raqamli mavsum yo\'q')

        offer_id = int(input('Taklif idsini kiriting: '))
        status = input("Ma'qullash - 1 | Rad etish - 0 >>> ")
        if status == '1':
            status = "ma_qullansin"
        elif status == '0':
            status = 'rad etilsin'
        else:
            print('Xato belgi')
            return

        query = 'update takliflar set status=%s where mavsum_id=%s and id=%s returning id'
        params = status, season_id, offer_id
        if not execute_query(query, params, fetch='one'):
            print('Nimadir xato ketdi')
        else:
            print('Saqlandi')
    except ValueError:
        print('Taklif id butun sondir')


def get_num_of_winners_of_category(category_id):
    query = """select num_of_winners from categories where id = %s"""
    params = category_id,
    return execute_query(query, params, fetch='one')


def determine_winners():
    try:
        season_id = int(input('Enter season id: '))
        if not get_season_by_id(season_id):
            print('Bunaqa iddagi mavsum yo\'q')
            return
        category_id = int(input('Enter category id: '))
        num_of_winners = get_num_of_winners_of_category(category_id)
        if not num_of_winners:
            print('Bunaqa iddagi kategoriya yo\'q')

        query = """select t.description, count(*) from ovozlar o inner join takliflar t 
        on o.taklif_id = t.id
        where o.mavsum_id = %s and t.category_id = %s
        group by description order by count(*) limit %s 
        """
        params = season_id, category_id, num_of_winners[0]
        results = execute_query(query, params, fetch='all')
        if not results:
            print('G\'oliblar mavjud emas!')
            return
        print('Taklif - Ovozlar soni')
        for result in results:
            print(result)
    except ValueError:
        print('mavsum yoki kategoriya idsi noto\'g\'ri, qayta urining')


def votes_statistics():
    try:
        season_id = int(input('Enter season id: '))
        if not get_season_by_id(season_id):
            print('Bunaqa iddagi mavsum yo\'q')
            return
        query = """select c.name, count(*) from ovozlar o inner join takliflar t 
                on o.taklif_id = t.id
                inner join categories c
                on t.category_id = c.id
                group by c.name
                """
        results = execute_query(query, fetch='all')
        if not results:
            print('Nimadir xato ketdi')
            return
        print('Kategoriya - Ovozlar soni')
        for result in results:
            print(result)
    except ValueError:
        print('mavsum idsi noto\'g\'ri, qayta urining')