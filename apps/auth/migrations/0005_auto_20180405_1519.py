# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amara_auth', '0004_customuser_last_hidden_message_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='preferred_language',
            field=models.CharField(blank=True, max_length=16, choices=[(b'ar', 'Arabic'), (b'ast', 'Asturian'), (b'az-az', 'Azerbaijani'), (b'be', 'Belarusian'), (b'bg', 'Bulgarian'), (b'bn', 'Bengali'), (b'br', 'Breton'), (b'bs', 'Bosnian'), (b'ca', 'Catalan'), (b'cs', 'Czech'), (b'cy', 'Welsh'), (b'da', 'Danish'), (b'de', 'German'), (b'el', 'Greek'), (b'en', 'English'), (b'en-gb', 'English, British'), (b'eo', 'Esperanto'), (b'es', 'Spanish'), (b'es-ar', 'Spanish, Argentinian'), (b'es-mx', 'Spanish, Mexican'), (b'et', 'Estonian'), (b'eu', 'Basque'), (b'fa', 'Persian'), (b'fi', 'Finnish'), (b'fr', 'French'), (b'fy-nl', 'Frisian'), (b'ga', 'Irish'), (b'gl', 'Galician'), (b'he', 'Hebrew'), (b'hi', 'Hindi'), (b'hr', 'Croatian'), (b'hu', 'Hungarian'), (b'hy', 'Armenian'), (b'ia', 'Interlingua'), (b'id', 'Indonesian'), (b'is', 'Icelandic'), (b'it', 'Italian'), (b'ja', 'Japanese'), (b'ka', 'Georgian'), (b'kk', 'Kazakh'), (b'km', 'Khmer'), (b'kn', 'Kannada'), (b'ko', 'Korean'), (b'ku', 'Kurdish'), (b'ky', 'Kyrgyz'), (b'lo', 'Lao'), (b'lt', 'Lithuanian'), (b'lv', 'Latvian'), (b'mk', 'Macedonian'), (b'ml', 'Malayalam'), (b'mn', 'Mongolian'), (b'mr', 'Marathi'), (b'ms', 'Malay'), (b'my', 'Burmese'), (b'nb', 'Norwegian Bokmal'), (b'nl', 'Dutch'), (b'nn', 'Norwegian Nynorsk'), (b'pl', 'Polish'), (b'ps', 'Pashto'), (b'pt', 'Portuguese'), (b'pt-br', 'Portuguese, Brazilian'), (b'ro', 'Romanian'), (b'ru', 'Russian'), (b'sco', 'Scots'), (b'sk', 'Slovak'), (b'sl', 'Slovenian'), (b'sq', 'Albanian'), (b'sr', 'Serbian'), (b'sr-latn', 'Serbian, Latin'), (b'sv', 'Swedish'), (b'ta', 'Tamil'), (b'te', 'Telugu'), (b'th', 'Thai'), (b'tr', 'Turkish'), (b'ug', 'Uyghur'), (b'uk', 'Ukrainian'), (b'ur', 'Urdu'), (b'uz', 'Uzbek'), (b'vi', 'Vietnamese'), (b'zh', 'Chinese, Yue'), (b'zh-cn', 'Chinese, Simplified'), (b'zh-tw', 'Chinese, Traditional')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userlanguage',
            name='language',
            field=models.CharField(max_length=16, verbose_name=b'languages', choices=[(b'ar', 'Arabic'), (b'ast', 'Asturian'), (b'az-az', 'Azerbaijani'), (b'be', 'Belarusian'), (b'bg', 'Bulgarian'), (b'bn', 'Bengali'), (b'br', 'Breton'), (b'bs', 'Bosnian'), (b'ca', 'Catalan'), (b'cs', 'Czech'), (b'cy', 'Welsh'), (b'da', 'Danish'), (b'de', 'German'), (b'el', 'Greek'), (b'en', 'English'), (b'en-gb', 'English, British'), (b'eo', 'Esperanto'), (b'es', 'Spanish'), (b'es-ar', 'Spanish, Argentinian'), (b'es-mx', 'Spanish, Mexican'), (b'et', 'Estonian'), (b'eu', 'Basque'), (b'fa', 'Persian'), (b'fi', 'Finnish'), (b'fr', 'French'), (b'fy-nl', 'Frisian'), (b'ga', 'Irish'), (b'gl', 'Galician'), (b'he', 'Hebrew'), (b'hi', 'Hindi'), (b'hr', 'Croatian'), (b'hu', 'Hungarian'), (b'hy', 'Armenian'), (b'ia', 'Interlingua'), (b'id', 'Indonesian'), (b'is', 'Icelandic'), (b'it', 'Italian'), (b'ja', 'Japanese'), (b'ka', 'Georgian'), (b'kk', 'Kazakh'), (b'km', 'Khmer'), (b'kn', 'Kannada'), (b'ko', 'Korean'), (b'ku', 'Kurdish'), (b'ky', 'Kyrgyz'), (b'lo', 'Lao'), (b'lt', 'Lithuanian'), (b'lv', 'Latvian'), (b'mk', 'Macedonian'), (b'ml', 'Malayalam'), (b'mn', 'Mongolian'), (b'mr', 'Marathi'), (b'ms', 'Malay'), (b'my', 'Burmese'), (b'nb', 'Norwegian Bokmal'), (b'nl', 'Dutch'), (b'nn', 'Norwegian Nynorsk'), (b'pl', 'Polish'), (b'ps', 'Pashto'), (b'pt', 'Portuguese'), (b'pt-br', 'Portuguese, Brazilian'), (b'ro', 'Romanian'), (b'ru', 'Russian'), (b'sco', 'Scots'), (b'sk', 'Slovak'), (b'sl', 'Slovenian'), (b'sq', 'Albanian'), (b'sr', 'Serbian'), (b'sr-latn', 'Serbian, Latin'), (b'sv', 'Swedish'), (b'ta', 'Tamil'), (b'te', 'Telugu'), (b'th', 'Thai'), (b'tr', 'Turkish'), (b'ug', 'Uyghur'), (b'uk', 'Ukrainian'), (b'ur', 'Urdu'), (b'uz', 'Uzbek'), (b'vi', 'Vietnamese'), (b'zh', 'Chinese, Yue'), (b'zh-cn', 'Chinese, Simplified'), (b'zh-tw', 'Chinese, Traditional')]),
            preserve_default=True,
        ),
    ]
