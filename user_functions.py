from db_manager import execute_query


def show_active_season():
    query = "select * from mavsum where taklif_status=True or is_active=True"
    result = execute_query(query, fetch='one')
    print(f"mavsum id - {result[0]} |"
          f" Taklif qabuli - {result[1]} |"
          f" Ovoz qabuli - {result[2]}")


def get_offer_active_season():
    query = "select * from mavsum where taklif_status=True and is_active=False"
    return execute_query(query, fetch='one')


def get_vote_active_season():
    query = "select * from mavsum where is_active=True and taklif_status=True"
    return execute_query(query, fetch='one')


def get_active_user():
    query = "select * from users where is_active=True"
    return execute_query(query, fetch='one')


def send_offer():
    try:
        mavsum = get_offer_active_season()
        if not mavsum:
            print('Taklif qabul qiladigan faol mavsum yo\'q')
            return
        active_user = get_active_user()
        description = input('Taklifga ta\'rif bering: ')
        status = 'kutilmoqda'
        category_id = int(input('Kategoriya raqamini kiriting: '))
        params = mavsum[0], active_user[0], description, status, category_id
        query = """insert into takliflar (mavsum_id, user_id, description, status, category_id) values 
        (%s, %s, %s, %s, %s) returning id
        """
        result = execute_query(query, params, fetch='one')
        if not result:
            print('Bunaqa raqamli kategoriya yo\'q')
        else:
            print('Yuborildi!')
    except ValueError:
        print('Kategoriya raqami butun sondir')


def check_my_offer():
    active_user = get_active_user()[0]
    query = """select * from takliflar where user_id=%s"""
    params = active_user,
    result = execute_query(query, params, fetch='one')
    if not result:
        print('Siz taklif yubormagansiz')
        return
    print('Tavsif - Holati')
    print(f"{result[3]} - {result[4]}")


def get_offer_by_id(offer_id):
    query = """select * from takliflar where id = %s"""
    params = offer_id,
    return execute_query(query, params, fetch='one')


def is_user_voted(season_id, user_id):
    query = """select * from ovozlar where user_id = %s and mavsum_id = %s;"""
    params = user_id, season_id
    return execute_query(query, params, fetch='one')


def vote():
    try:
        season = get_vote_active_season()
        if not get_vote_active_season():
            print('Hali ovoz berish boshlangani yo\'q')
            return
        else:
            season_id = season[0]
        user_id = get_active_user()[0]

        if is_user_voted(season_id, user_id):
            print('Siz ovoz bergansiz')
            return

        offer_id = int(input('Taklif raqamini kiriting: '))
        if not get_offer_by_id(offer_id):
            print('Bunaqa raqamli taklif yoq')
            return

        query = """insert into ovozlar (mavsum_id, user_id, taklif_id) values (%s, %s, %s);"""
        params = season_id, user_id, offer_id
        execute_query(query, params)
        print('Ovozingiz qabul etildi')
    except ValueError:
        print('Taklif raqami butun sondir')





