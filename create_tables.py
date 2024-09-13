from db_manager import execute_query


def create_tables():
    queries = [
        """
        create table if not exists mavsum (
        id serial primary key,
        taklif_status boolean,
        is_active boolean
        );
        """,
        """
        create table if not exists users (
        id serial primary key,
        name varchar(64) not null,
        password varchar(256) not null,
        phone varchar(13) not null,
        is_active boolean
        );
        """,
        """
        create table if not exists categories (
        id serial primary key,
        name varchar(16),
        num_of_winners integer
        );
        """,
        """
        create table if not exists takliflar (
        id serial primary key,
        mavsum_id integer,
        user_id integer,
        description text,
        status varchar(16) default 'kutilmoqda',
        category_id integer,
        foreign key (mavsum_id) references mavsum(id),
        foreign key (user_id) references users(id),
        foreign key (category_id) references categories(id)
        );
        """,
        """
        create table if not exists ovozlar (
        id serial primary key,
        mavsum_id integer,
        user_id integer,
        taklif_id integer,
        foreign key (mavsum_id) references mavsum(id),
        foreign key (user_id) references users(id),
        foreign key (taklif_id) references takliflar(id)
        );
        """
    ]

    for query in queries:
        execute_query(query)


if __name__ == '__main__':
    print(create_tables())