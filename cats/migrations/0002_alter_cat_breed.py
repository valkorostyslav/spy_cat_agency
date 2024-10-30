# Generated by Django 5.1.2 on 2024-10-30 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='breed',
            field=models.CharField(choices=[('Abyssinian', 'Abyssinian'), ('Aegean', 'Aegean'), ('American Bobtail', 'American Bobtail'), ('American Curl', 'American Curl'), ('American Shorthair', 'American Shorthair'), ('American Wirehair', 'American Wirehair'), ('Arabian Mau', 'Arabian Mau'), ('Australian Mist', 'Australian Mist'), ('Balinese', 'Balinese'), ('Bambino', 'Bambino'), ('Bengal', 'Bengal'), ('Birman', 'Birman'), ('Bombay', 'Bombay'), ('British Longhair', 'British Longhair'), ('British Shorthair', 'British Shorthair'), ('Burmese', 'Burmese'), ('Burmilla', 'Burmilla'), ('California Spangled', 'California Spangled'), ('Chantilly-Tiffany', 'Chantilly-Tiffany'), ('Chartreux', 'Chartreux'), ('Chausie', 'Chausie'), ('Cheetoh', 'Cheetoh'), ('Colorpoint Shorthair', 'Colorpoint Shorthair'), ('Cornish Rex', 'Cornish Rex'), ('Cymric', 'Cymric'), ('Cyprus', 'Cyprus'), ('Devon Rex', 'Devon Rex'), ('Donskoy', 'Donskoy'), ('Dragon Li', 'Dragon Li'), ('Egyptian Mau', 'Egyptian Mau'), ('European Burmese', 'European Burmese'), ('Exotic Shorthair', 'Exotic Shorthair'), ('Havana Brown', 'Havana Brown'), ('Himalayan', 'Himalayan'), ('Japanese Bobtail', 'Japanese Bobtail'), ('Javanese', 'Javanese'), ('Khao Manee', 'Khao Manee'), ('Korat', 'Korat'), ('Kurilian', 'Kurilian'), ('LaPerm', 'LaPerm'), ('Maine Coon', 'Maine Coon'), ('Malayan', 'Malayan'), ('Manx', 'Manx'), ('Munchkin', 'Munchkin'), ('Nebelung', 'Nebelung'), ('Norwegian Forest Cat', 'Norwegian Forest Cat'), ('Ocicat', 'Ocicat'), ('Oriental', 'Oriental'), ('Persian', 'Persian'), ('Pixie-bob', 'Pixie-bob'), ('Ragamuffin', 'Ragamuffin'), ('Ragdoll', 'Ragdoll'), ('Russian Blue', 'Russian Blue'), ('Savannah', 'Savannah'), ('Scottish Fold', 'Scottish Fold'), ('Selkirk Rex', 'Selkirk Rex'), ('Siamese', 'Siamese'), ('Siberian', 'Siberian'), ('Singapura', 'Singapura'), ('Snowshoe', 'Snowshoe'), ('Somali', 'Somali'), ('Sphynx', 'Sphynx'), ('Tonkinese', 'Tonkinese'), ('Toyger', 'Toyger'), ('Turkish Angora', 'Turkish Angora'), ('Turkish Van', 'Turkish Van'), ('York Chocolate', 'York Chocolate')], max_length=50),
        ),
    ]
