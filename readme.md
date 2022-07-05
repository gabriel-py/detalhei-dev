# Step by Step

## Step 1 - Install the dependencies
```bash
pip install -r requirements.txt
```

## Step 2 - Making the migrations
```bash
python manage.py migrate
```

### If something in step 2 goes wrong
```bash
python manage.py migrate usuarios
python manage.py migrate produtos
```

## Step 3 - Create your superuser
```bash
python manage.py createsuperuser --settings=src.settings.local
```

## Step 4 - Use the software
```bash
python manage.py runserver --settings=src.settings.local
```

### Enpoints
> http://127.0.0.1:8000/sync/1
>> Update the ranking from area which id is equal 1

> http://127.0.0.1:8000/sync/detailed_ranking/1
>> Get the datailed data from area which id is igual 1


#### Access
> root:root
>> Homolog admin