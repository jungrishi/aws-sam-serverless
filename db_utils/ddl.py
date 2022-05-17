create_database = '''create database ge_coding_task;'''

def create_required_tables():
    # create user table and add a user
    create_user_table_query = '''
        create table users
            (
                id                     bigserial    not null
                constraint users_pkey
                    primary key,
                name                   varchar(255),
                email                  varchar(255),
                created_at timestamp default now() not null,
                updated_at timestamp default now() not null,
                username               varchar(255),
                password_hash          varchar(255),
                reset_link_timestamp   timestamp with time zone
            );

    create index users_id_index
        on users (id);

       '''
