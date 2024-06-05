find . -type f -name "*.json" -path "*/fixtures/*" | while read -r file; do
    python manage.py loaddata "$file"
don