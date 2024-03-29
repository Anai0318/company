# Generated by Django 4.2.5 on 2024-01-30 18:28

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "会社名",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="会社名"
                    ),
                ),
                (
                    "売上高",
                    models.FloatField(blank=True, null=True, verbose_name="売上高3年平均"),
                ),
                (
                    "営業利益",
                    models.FloatField(blank=True, null=True, verbose_name="営業利益3年平均"),
                ),
                ("roe", models.FloatField(blank=True, null=True, verbose_name="ROE")),
                (
                    "有形固定資産",
                    models.FloatField(blank=True, null=True, verbose_name="有形固定資産"),
                ),
                ("固定負債", models.FloatField(blank=True, null=True, verbose_name="固定負債")),
                (
                    "自己資本比率",
                    models.FloatField(blank=True, null=True, verbose_name="自己資本比率"),
                ),
                ("pbr", models.FloatField(blank=True, null=True, verbose_name="pbr")),
                (
                    "営業利益率",
                    models.FloatField(blank=True, null=True, verbose_name="営業利益率"),
                ),
                (
                    "株価上昇率",
                    models.FloatField(blank=True, null=True, verbose_name="3年の株価上昇率"),
                ),
                ("粗利率", models.FloatField(blank=True, null=True, verbose_name="粗利率")),
                ("per", models.FloatField(blank=True, null=True, verbose_name="per")),
                (
                    "industry",
                    models.IntegerField(
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
                (
                    "会社ロゴ",
                    models.ImageField(
                        blank=True, null=True, upload_to="company", verbose_name="会社ロゴ"
                    ),
                ),
                ("勤続年数", models.FloatField(blank=True, null=True, verbose_name="勤続年数")),
                (
                    "平均年収",
                    models.IntegerField(blank=True, null=True, verbose_name="平均年収"),
                ),
                ("平均年齢", models.FloatField(blank=True, null=True, verbose_name="平均年齢")),
                (
                    "従業員数",
                    models.IntegerField(blank=True, null=True, verbose_name="従業員数"),
                ),
                (
                    "持ち株",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="持ち株"
                    ),
                ),
                ("事業内容", models.TextField(blank=True, null=True, verbose_name="事業内容")),
                (
                    "上場年数",
                    models.IntegerField(blank=True, null=True, verbose_name="上場年数"),
                ),
                (
                    "人件費_純利益",
                    models.FloatField(blank=True, null=True, verbose_name="純利益に占める人件費"),
                ),
                (
                    "取締役報酬",
                    models.FloatField(blank=True, null=True, verbose_name="取締役報酬"),
                ),
                (
                    "従業員一人当たりの売上",
                    models.FloatField(
                        blank=True, null=True, verbose_name="従業員一人当たりの売上"
                    ),
                ),
                ("流動比率", models.FloatField(blank=True, null=True, verbose_name="流動比率")),
                (
                    "研究開発売上比率",
                    models.FloatField(blank=True, null=True, verbose_name="研究開発売上比率"),
                ),
                (
                    "cluster",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (0, "平均的な会社"),
                            (1, "建物を大量に保有"),
                            (2, "利益成長バケモノ"),
                            (3, "出来杉くん(優秀)"),
                        ],
                        null=True,
                        verbose_name="クラスター",
                    ),
                ),
            ],
        ),
    ]
