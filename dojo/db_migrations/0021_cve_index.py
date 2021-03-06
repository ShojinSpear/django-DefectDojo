# Generated by Django 2.2.4 on 2019-10-28 21:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0020_system_settings_allow_anonymous_survey_repsonse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finding',
            name='cve',
            field=models.CharField(max_length=20, null=True, validators=[django.core.validators.RegexValidator(message="CVE must be entered in the format: 'CVE-9999-9999'. ", regex='^CVE-\\d{4}-\\d{4,7}$')]),
        ),
        migrations.AddIndex(
            model_name='finding',
            index=models.Index(fields=['cve'], name='dojo_findin_cve_dccd4b_idx'),
        ),
    ]
