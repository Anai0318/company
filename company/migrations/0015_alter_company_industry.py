# Generated by Django 4.2.5 on 2024-01-30 06:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("company", "0014_alter_company_industry"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="industry",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (1, "電気機器"),
                    (2, "情報・通信"),
                    (3, "医薬品"),
                    (4, "輸送用機器"),
                    (5, "機械"),
                    (6, "卸売"),
                    (7, "小売"),
                    (8, "化学"),
                    (9, "サービス"),
                    (10, "銀行"),
                    (11, "精密機器"),
                    (12, "食料品"),
                    (13, "陸運"),
                    (14, "不動産"),
                    (15, "鉱業"),
                    (16, "ゴム製品"),
                    (17, "保険"),
                    (18, "その他製品"),
                    (19, "建設"),
                    (20, "鉄鋼"),
                    (21, "石油・石炭製品"),
                    (22, "海運"),
                    (23, "ガラス・土石製品"),
                    (24, "その他金融業"),
                    (25, "倉庫・運輸関連"),
                    (26, "その他金融"),
                    (27, "金属製品"),
                    (28, "精密機器"),
                    (29, "繊維製品"),
                    (30, "パルプ・紙"),
                    (31, "非鉄金属"),
                    (32, "電気・ガス"),
                ],
                null=True,
                verbose_name="業種",
            ),
        ),
    ]
