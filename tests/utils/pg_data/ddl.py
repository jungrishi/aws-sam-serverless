from sqlalchemy.orm import Session

def create_required_tables(session: Session):
    create_user_table_query = '''
        create table users
            (
                id                     bigserial    not null
                constraint users_pkey
                    primary key,
                name                   varchar(256),
                email                  varchar(256),
                created_at timestamp default now() not null,
                updated_at timestamp default now() not null,
                username               varchar(256),
                password_hash          varchar(256),
                reset_link_timestamp   varchar(256)
            );

    create index users_id_index
        on users (id);

       '''

    session.execute(create_user_table_query)
