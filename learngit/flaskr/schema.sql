drop table if exists entries;
create table entries(
    id integer primary key autoincrement,
    title text no null,
    text text not null
)