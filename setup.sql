create role evp superuser login password 'evp123';
create database evp;
grant ALL privileges on database evp to evp;
\c evp postgres
grant ALL on schema public to evp;