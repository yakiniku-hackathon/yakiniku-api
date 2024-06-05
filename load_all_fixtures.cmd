@echo off
for /R %%f in (fixtures\*.json) do python manage.py loaddata "%%f"