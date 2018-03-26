# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import codefield
import utils.dates


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
        ('amara_auth', '0002_auto_20180215_1232'),
        ('videos', '0002_auto_20180215_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityMigrationProgress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_migrated_id', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActivityRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', codefield.CodeField(choices=[(b'video-added', 'Video Added'), (b'video-title-changed', 'Video Title Changed'), (b'comment-added', 'Comment added'), (b'version-added', 'Version added'), (b'video-url-added', 'Video URL added'), (b'translation-added', 'Translation URL added'), (b'subtitle-request-created', 'Subtitle request created'), (b'version-approved', 'Version approved'), (b'member-joined', 'Member Joined'), (b'version-rejected', 'Version Rejected'), (b'member-left', 'Member Left'), (b'version-reviewed', 'Version Reviewed'), (b'version-accepted', 'Version Accepted'), (b'version-declined', 'Version Declined'), (b'video-deleted', 'Video deleted'), (b'video-url-edited', 'Video URL edited'), (b'video-url-deleted', 'Video URL deleted'), (b'video-moved-to-team', 'Video moved to team'), (b'video-moved-from-team', 'Video moved from team'), (b'team-settings-changed', 'Team settings changed'), (b'language-changed', 'Language Changed'), (b'collab-join', 'Collaboration joined'), (b'collab-leave', 'Collaboration left'), (b'collab-assign', 'Collaboration assigned'), (b'collab-reassign', 'Collaboration reassigned'), (b'collab-unassign', 'Collaboration unassigned'), (b'collab-auto-unassigned', 'Collaboration automatically unassigned'), (b'collab-endorse', 'Collaboration endorsed'), (b'collab-send-back', 'Collaboration sent back'), (b'collab-mark-complete', 'Collaboration marked complete'), (b'collab-move-from-team', 'Collaboration moved from team'), (b'collab-move-to-team', 'Collaboration moved to team'), (b'collab-delete', 'Collaboration deleted'), (b'collab-provider-accept', 'Collaboration accepted by provider'), (b'collab-provider-submit', 'Collaboration submitted by provider'), (b'collab-provider-unassign', 'Collaboration unassigned from provider'), (b'collab-set-evaluation-teams', 'Collaboration evaluation teams set'), (b'collab-change-state', 'Collaboration change State'), (b'collab-team-change', 'Collaboration team change')])),
                ('video_language_code', models.CharField(default=b'', max_length=16, blank=True, choices=[(b'ab', 'Abkhazian'), (b'ace', 'Acehnese'), (b'aa', 'Afar'), (b'af', 'Afrikaans'), (b'aka', 'Akan'), (b'sq', 'Albanian'), (b'arq', 'Algerian Arabic'), (b'ase', 'American Sign Language'), (b'amh', 'Amharic'), (b'am', 'Amharic'), (b'ami', 'Amis'), (b'ar', 'Arabic'), (b'an', 'Aragonese'), (b'arc', 'Aramaic'), (b'hy', 'Armenian'), (b'as', 'Assamese'), (b'ast', 'Asturian'), (b'av', 'Avaric'), (b'ae', 'Avestan'), (b'ay', 'Aymara'), (b'az', 'Azerbaijani'), (b'bam', 'Bambara'), (b'ba', 'Bashkir'), (b'eu', 'Basque'), (b'be', 'Belarusian'), (b'bem', 'Bemba (Zambia)'), (b'bn', 'Bengali'), (b'ber', 'Berber'), (b'bh', 'Bihari'), (b'bi', 'Bislama'), (b'bs', 'Bosnian'), (b'br', 'Breton'), (b'bug', 'Buginese'), (b'bg', 'Bulgarian'), (b'my', 'Burmese'), (b'cak', 'Cakchiquel, Central'), (b'ca', 'Catalan'), (b'ceb', 'Cebuano'), (b'ch', 'Chamorro'), (b'ce', 'Chechen'), (b'chr', 'Cherokee'), (b'nya', 'Chewa'), (b'ctd', 'Chin, Tedim'), (b'zh-hans', b'Chinese (Simplified Han)'), (b'zh-hant', b'Chinese (Traditional Han)'), (b'zh-cn', 'Chinese, Simplified'), (b'zh-sg', 'Chinese, Simplified (Singaporean)'), (b'zh-tw', 'Chinese, Traditional'), (b'zh-hk', 'Chinese, Traditional (Hong Kong)'), (b'zh', 'Chinese, Yue'), (b'cho', 'Choctaw'), (b'ctu', 'Chol, Tumbal\xe1'), (b'cu', 'Church Slavic'), (b'cv', 'Chuvash'), (b'ksh', 'Colognian'), (b'rar', 'Cook Islands M\u0101ori'), (b'kw', 'Cornish'), (b'co', 'Corsican'), (b'cr', 'Cree'), (b'ht', 'Creole, Haitian'), (b'hr', 'Croatian'), (b'cs', 'Czech'), (b'da', 'Danish'), (b'prs', 'Dari'), (b'din', 'Dinka'), (b'dv', 'Divehi'), (b'nl', 'Dutch'), (b'nl-be', 'Dutch (Belgium)'), (b'dz', 'Dzongkha'), (b'cly', 'Eastern Chatino'), (b'efi', 'Efik'), (b'arz', 'Egyptian Arabic'), (b'en', 'English'), (b'en-au', 'English (Australia)'), (b'en-ca', 'English (Canada)'), (b'en-in', 'English (India)'), (b'en-ie', 'English (Ireland)'), (b'en-us', 'English (United States)'), (b'en-gb', 'English, British'), (b'eo', 'Esperanto'), (b'et', 'Estonian'), (b'ee', 'Ewe'), (b'fo', 'Faroese'), (b'fj', 'Fijian'), (b'fil', 'Filipino'), (b'fi', 'Finnish'), (b'vls', 'Flemish'), (b'fr', 'French'), (b'fr-be', 'French (Belgium)'), (b'fr-ca', 'French (Canada)'), (b'fr-ch', 'French (Switzerland)'), (b'fy-nl', 'Frisian'), (b'ful', 'Fula'), (b'ff', 'Fulah'), (b'gl', 'Galician'), (b'lg', 'Ganda'), (b'ka', 'Georgian'), (b'de', 'German'), (b'de-at', 'German (Austria)'), (b'de-ch', 'German (Switzerland)'), (b'kik', 'Gikuyu'), (b'got', 'Gothic'), (b'el', 'Greek'), (b'kl', 'Greenlandic'), (b'gn', 'Guaran'), (b'gu', 'Gujarati'), (b'hai', 'Haida'), (b'cnh', 'Hakha Chin'), (b'hb', 'HamariBoli (Roman Hindi-Urdu)'), (b'hau', 'Hausa'), (b'ha', b'Hausa'), (b'hwc', "Hawai'i Creole English"), (b'haw', 'Hawaiian'), (b'haz', 'Hazaragi'), (b'iw', b'Hebrew'), (b'he', 'Hebrew'), (b'hz', 'Herero'), (b'hi', 'Hindi'), (b'ho', 'Hiri Motu'), (b'hmn', 'Hmong'), (b'nan', 'Hokkien'), (b'hus', 'Huastec, Veracruz'), (b'hch', 'Huichol'), (b'hu', 'Hungarian'), (b'hup', 'Hupa'), (b'bnt', 'Ibibio'), (b'is', 'Icelandic'), (b'io', 'Ido'), (b'ibo', 'Igbo'), (b'ilo', 'Ilocano'), (b'id', 'Indonesian'), (b'inh', 'Ingush'), (b'ia', 'Interlingua'), (b'ie', 'Interlingue'), (b'iu', 'Inuktitut'), (b'ik', 'Inupia'), (b'ga', 'Irish'), (b'iro', 'Iroquoian languages'), (b'it', 'Italian'), (b'ja', 'Japanese'), (b'jv', 'Javanese'), (b'kn', 'Kannada'), (b'kau', 'Kanuri'), (b'pam', 'Kapampangan'), (b'kaa', 'Karakalpak'), (b'kar', 'Karen'), (b'ks', 'Kashmiri'), (b'kk', 'Kazakh'), (b'km', 'Khmer'), (b'rw', b'Kinyarwanda'), (b'tlh', 'Klingon'), (b'cku', 'Koasati'), (b'kv', 'Komi'), (b'kon', 'Kongo'), (b'ko', 'Korean'), (b'kj', 'Kuanyama, Kwanyama'), (b'ku', 'Kurdish'), (b'ckb', 'Kurdish (Central)'), (b'ky', 'Kyrgyz'), (b'lld', 'Ladin'), (b'lkt', 'Lakota'), (b'lo', 'Lao'), (b'ltg', 'Latgalian'), (b'la', 'Latin'), (b'lv', 'Latvian'), (b'li', 'Limburgish'), (b'ln', b'Lingala'), (b'lin', 'Lingala'), (b'lt', 'Lithuanian'), (b'dsb', b'Lower Sorbian'), (b'loz', 'Lozi'), (b'lua', 'Luba-Kasai'), (b'lu', 'Luba-Katagana'), (b'luy', 'Luhya'), (b'luo', 'Luo'), (b'lut', 'Lushootseed'), (b'lb', 'Luxembourgish'), (b'rup', 'Macedo'), (b'mk', 'Macedonian'), (b'mad', 'Madurese'), (b'mg', b'Malagasy'), (b'mlg', 'Malagasy'), (b'ms', 'Malay'), (b'ml', 'Malayalam'), (b'mt', 'Maltese'), (b'mnk', 'Mandinka'), (b'mni', 'Manipuri'), (b'gv', 'Manx'), (b'mi', 'Maori'), (b'mr', 'Marathi'), (b'mh', 'Marshallese'), (b'mfe', b'Mauritian Creole'), (b'yua', 'Maya, Yucat\xe1n'), (b'meta-audio', 'Metadata: Audio Description'), (b'meta-geo', 'Metadata: Geo'), (b'meta-tw', 'Metadata: Twitter'), (b'meta-video', 'Metadata: Video Description'), (b'meta-wiki', 'Metadata: Wikipedia'), (b'lus', 'Mizo'), (b'moh', 'Mohawk'), (b'mo', 'Moldavian, Moldovan'), (b'mn', 'Mongolian'), (b'srp', 'Montenegrin'), (b'mos', 'Mossi'), (b'mus', 'Muscogee'), (b'nci', 'Nahuatl, Classical'), (b'ncj', 'Nahuatl, Northern Puebla'), (b'na', 'Naurunan'), (b'nv', 'Navajo'), (b'ng', 'Ndonga'), (b'ne', 'Nepali'), (b'pcm', 'Nigerian Pidgin'), (b'nd', 'North Ndebele'), (b'se', 'Northern Sami'), (b'nso', 'Northern Sotho'), (b'no', 'Norwegian'), (b'nb', 'Norwegian Bokmal'), (b'nn', 'Norwegian Nynorsk'), (b'oc', 'Occitan'), (b'oji', 'Ojibwe'), (b'or', 'Oriya'), (b'orm', 'Oromo'), (b'om', b'Oromo'), (b'os', 'Ossetian, Ossetic'), (b'x-other', 'Other'), (b'pi', 'Pali'), (b'pap', 'Papiamento'), (b'ps', 'Pashto'), (b'fa', 'Persian'), (b'fa-af', 'Persian (Afghanistan)'), (b'pcd', 'Picard'), (b'pl', 'Polish'), (b'pt', 'Portuguese'), (b'pt-pt', b'Portuguese (Portugal)'), (b'pt-br', 'Portuguese, Brazilian'), (b'pa', b'Punjabi'), (b'pan', 'Punjabi'), (b'tsz', 'Purepecha'), (b'tob', b'Qom (Toba)'), (b'que', 'Quechua'), (b'qu', b'Quechua'), (b'qvi', 'Quichua, Imbabura Highland'), (b'raj', 'Rajasthani'), (b'ro', 'Romanian'), (b'rm', 'Romansh'), (b'rn', b'Rundi'), (b'run', 'Rundi'), (b'ru', 'Russian'), (b'ry', 'Rusyn'), (b'kin', 'Rwandi'), (b'sm', 'Samoan'), (b'sg', 'Sango'), (b'sa', 'Sanskrit'), (b'sc', 'Sardinian'), (b'sco', 'Scots'), (b'gd', 'Scottish Gaelic'), (b'trv', 'Seediq'), (b'skx', 'Seko Padang'), (b'sr', 'Serbian'), (b'sr-latn', 'Serbian, Latin'), (b'sh', 'Serbo-Croatian'), (b'crs', 'Seselwa Creole French'), (b'shp', 'Shipibo-Conibo'), (b'sna', 'Shona'), (b'sn', b'Shona'), (b'ii', 'Sichuan Yi'), (b'scn', 'Sicilian'), (b'sgn', 'Sign Languages'), (b'szl', 'Silesian'), (b'sd', 'Sindhi'), (b'si', 'Sinhala'), (b'sk', 'Slovak'), (b'sl', 'Slovenian'), (b'sby', 'Soli'), (b'so', b'Somali'), (b'som', 'Somali'), (b'sot', 'Sotho'), (b'nr', 'Southern Ndebele'), (b'st', 'Southern Sotho'), (b'es', 'Spanish'), (b'es-ec', 'Spanish (Ecuador)'), (b'es-419', 'Spanish (Latin America)'), (b'es-es', b'Spanish (Spain)'), (b'es-ar', 'Spanish, Argentinian'), (b'es-mx', 'Spanish, Mexican'), (b'es-ni', 'Spanish, Nicaraguan'), (b'su', 'Sundanese'), (b'sw', b'Swahili'), (b'swa', 'Swahili'), (b'ss', 'Swati'), (b'sv', 'Swedish'), (b'gsw', 'Swiss German'), (b'tl', 'Tagalog'), (b'ty', 'Tahitian'), (b'tg', 'Tajik'), (b'ta', 'Tamil'), (b'tar', 'Tarahumara, Central'), (b'cta', 'Tataltepec Chatino'), (b'tt', 'Tatar'), (b'te', 'Telugu'), (b'tet', 'Tetum'), (b'th', 'Thai'), (b'bo', 'Tibetan'), (b'ti', b'Tigrinya'), (b'tir', 'Tigrinya'), (b'toj', 'Tojolabal'), (b'to', 'Tonga'), (b'ts', 'Tsonga'), (b'tn', b'Tswana'), (b'tsn', 'Tswana'), (b'aeb', 'Tunisian Arabic'), (b'tr', 'Turkish'), (b'tk', 'Turkmen'), (b'tw', 'Twi'), (b'tzh', 'Tzeltal, Oxchuc'), (b'tzo', 'Tzotzil, Venustiano Carranza'), (b'uk', 'Ukrainian'), (b'umb', 'Umbundu'), (b'hsb', b'Upper Sorbian'), (b'ur', 'Urdu'), (b'ug', 'Uyghur'), (b'uz', 'Uzbek'), (b've', 'Venda'), (b'vi', 'Vietnamese'), (b'vo', 'Volapuk'), (b'wbl', 'Wakhi'), (b'wa', 'Walloon'), (b'wau', 'Wauja'), (b'cy', 'Welsh'), (b'fy', b'Western Frisian'), (b'pnb', 'Western Punjabi'), (b'wol', 'Wolof'), (b'wo', b'Wolof'), (b'xho', 'Xhosa'), (b'xh', b'Xhosa'), (b'tao', 'Yami (Tao)'), (b'yaq', 'Yaqui'), (b'yi', 'Yiddish'), (b'yo', b'Yoruba'), (b'yor', 'Yoruba'), (b'zam', 'Zapotec, Miahuatl\xe1n'), (b'zza', 'Zazaki'), (b'czn', 'Zenzontepec Chatino'), (b'za', 'Zhuang, Chuang'), (b'zu', b'Zulu'), (b'zul', 'Zulu')])),
                ('language_code', models.CharField(default=b'', max_length=16, blank=True, choices=[(b'ab', 'Abkhazian'), (b'ace', 'Acehnese'), (b'aa', 'Afar'), (b'af', 'Afrikaans'), (b'aka', 'Akan'), (b'sq', 'Albanian'), (b'arq', 'Algerian Arabic'), (b'ase', 'American Sign Language'), (b'amh', 'Amharic'), (b'am', 'Amharic'), (b'ami', 'Amis'), (b'ar', 'Arabic'), (b'an', 'Aragonese'), (b'arc', 'Aramaic'), (b'hy', 'Armenian'), (b'as', 'Assamese'), (b'ast', 'Asturian'), (b'av', 'Avaric'), (b'ae', 'Avestan'), (b'ay', 'Aymara'), (b'az', 'Azerbaijani'), (b'bam', 'Bambara'), (b'ba', 'Bashkir'), (b'eu', 'Basque'), (b'be', 'Belarusian'), (b'bem', 'Bemba (Zambia)'), (b'bn', 'Bengali'), (b'ber', 'Berber'), (b'bh', 'Bihari'), (b'bi', 'Bislama'), (b'bs', 'Bosnian'), (b'br', 'Breton'), (b'bug', 'Buginese'), (b'bg', 'Bulgarian'), (b'my', 'Burmese'), (b'cak', 'Cakchiquel, Central'), (b'ca', 'Catalan'), (b'ceb', 'Cebuano'), (b'ch', 'Chamorro'), (b'ce', 'Chechen'), (b'chr', 'Cherokee'), (b'nya', 'Chewa'), (b'ctd', 'Chin, Tedim'), (b'zh-hans', b'Chinese (Simplified Han)'), (b'zh-hant', b'Chinese (Traditional Han)'), (b'zh-cn', 'Chinese, Simplified'), (b'zh-sg', 'Chinese, Simplified (Singaporean)'), (b'zh-tw', 'Chinese, Traditional'), (b'zh-hk', 'Chinese, Traditional (Hong Kong)'), (b'zh', 'Chinese, Yue'), (b'cho', 'Choctaw'), (b'ctu', 'Chol, Tumbal\xe1'), (b'cu', 'Church Slavic'), (b'cv', 'Chuvash'), (b'ksh', 'Colognian'), (b'rar', 'Cook Islands M\u0101ori'), (b'kw', 'Cornish'), (b'co', 'Corsican'), (b'cr', 'Cree'), (b'ht', 'Creole, Haitian'), (b'hr', 'Croatian'), (b'cs', 'Czech'), (b'da', 'Danish'), (b'prs', 'Dari'), (b'din', 'Dinka'), (b'dv', 'Divehi'), (b'nl', 'Dutch'), (b'nl-be', 'Dutch (Belgium)'), (b'dz', 'Dzongkha'), (b'cly', 'Eastern Chatino'), (b'efi', 'Efik'), (b'arz', 'Egyptian Arabic'), (b'en', 'English'), (b'en-au', 'English (Australia)'), (b'en-ca', 'English (Canada)'), (b'en-in', 'English (India)'), (b'en-ie', 'English (Ireland)'), (b'en-us', 'English (United States)'), (b'en-gb', 'English, British'), (b'eo', 'Esperanto'), (b'et', 'Estonian'), (b'ee', 'Ewe'), (b'fo', 'Faroese'), (b'fj', 'Fijian'), (b'fil', 'Filipino'), (b'fi', 'Finnish'), (b'vls', 'Flemish'), (b'fr', 'French'), (b'fr-be', 'French (Belgium)'), (b'fr-ca', 'French (Canada)'), (b'fr-ch', 'French (Switzerland)'), (b'fy-nl', 'Frisian'), (b'ful', 'Fula'), (b'ff', 'Fulah'), (b'gl', 'Galician'), (b'lg', 'Ganda'), (b'ka', 'Georgian'), (b'de', 'German'), (b'de-at', 'German (Austria)'), (b'de-ch', 'German (Switzerland)'), (b'kik', 'Gikuyu'), (b'got', 'Gothic'), (b'el', 'Greek'), (b'kl', 'Greenlandic'), (b'gn', 'Guaran'), (b'gu', 'Gujarati'), (b'hai', 'Haida'), (b'cnh', 'Hakha Chin'), (b'hb', 'HamariBoli (Roman Hindi-Urdu)'), (b'hau', 'Hausa'), (b'ha', b'Hausa'), (b'hwc', "Hawai'i Creole English"), (b'haw', 'Hawaiian'), (b'haz', 'Hazaragi'), (b'iw', b'Hebrew'), (b'he', 'Hebrew'), (b'hz', 'Herero'), (b'hi', 'Hindi'), (b'ho', 'Hiri Motu'), (b'hmn', 'Hmong'), (b'nan', 'Hokkien'), (b'hus', 'Huastec, Veracruz'), (b'hch', 'Huichol'), (b'hu', 'Hungarian'), (b'hup', 'Hupa'), (b'bnt', 'Ibibio'), (b'is', 'Icelandic'), (b'io', 'Ido'), (b'ibo', 'Igbo'), (b'ilo', 'Ilocano'), (b'id', 'Indonesian'), (b'inh', 'Ingush'), (b'ia', 'Interlingua'), (b'ie', 'Interlingue'), (b'iu', 'Inuktitut'), (b'ik', 'Inupia'), (b'ga', 'Irish'), (b'iro', 'Iroquoian languages'), (b'it', 'Italian'), (b'ja', 'Japanese'), (b'jv', 'Javanese'), (b'kn', 'Kannada'), (b'kau', 'Kanuri'), (b'pam', 'Kapampangan'), (b'kaa', 'Karakalpak'), (b'kar', 'Karen'), (b'ks', 'Kashmiri'), (b'kk', 'Kazakh'), (b'km', 'Khmer'), (b'rw', b'Kinyarwanda'), (b'tlh', 'Klingon'), (b'cku', 'Koasati'), (b'kv', 'Komi'), (b'kon', 'Kongo'), (b'ko', 'Korean'), (b'kj', 'Kuanyama, Kwanyama'), (b'ku', 'Kurdish'), (b'ckb', 'Kurdish (Central)'), (b'ky', 'Kyrgyz'), (b'lld', 'Ladin'), (b'lkt', 'Lakota'), (b'lo', 'Lao'), (b'ltg', 'Latgalian'), (b'la', 'Latin'), (b'lv', 'Latvian'), (b'li', 'Limburgish'), (b'ln', b'Lingala'), (b'lin', 'Lingala'), (b'lt', 'Lithuanian'), (b'dsb', b'Lower Sorbian'), (b'loz', 'Lozi'), (b'lua', 'Luba-Kasai'), (b'lu', 'Luba-Katagana'), (b'luy', 'Luhya'), (b'luo', 'Luo'), (b'lut', 'Lushootseed'), (b'lb', 'Luxembourgish'), (b'rup', 'Macedo'), (b'mk', 'Macedonian'), (b'mad', 'Madurese'), (b'mg', b'Malagasy'), (b'mlg', 'Malagasy'), (b'ms', 'Malay'), (b'ml', 'Malayalam'), (b'mt', 'Maltese'), (b'mnk', 'Mandinka'), (b'mni', 'Manipuri'), (b'gv', 'Manx'), (b'mi', 'Maori'), (b'mr', 'Marathi'), (b'mh', 'Marshallese'), (b'mfe', b'Mauritian Creole'), (b'yua', 'Maya, Yucat\xe1n'), (b'meta-audio', 'Metadata: Audio Description'), (b'meta-geo', 'Metadata: Geo'), (b'meta-tw', 'Metadata: Twitter'), (b'meta-video', 'Metadata: Video Description'), (b'meta-wiki', 'Metadata: Wikipedia'), (b'lus', 'Mizo'), (b'moh', 'Mohawk'), (b'mo', 'Moldavian, Moldovan'), (b'mn', 'Mongolian'), (b'srp', 'Montenegrin'), (b'mos', 'Mossi'), (b'mus', 'Muscogee'), (b'nci', 'Nahuatl, Classical'), (b'ncj', 'Nahuatl, Northern Puebla'), (b'na', 'Naurunan'), (b'nv', 'Navajo'), (b'ng', 'Ndonga'), (b'ne', 'Nepali'), (b'pcm', 'Nigerian Pidgin'), (b'nd', 'North Ndebele'), (b'se', 'Northern Sami'), (b'nso', 'Northern Sotho'), (b'no', 'Norwegian'), (b'nb', 'Norwegian Bokmal'), (b'nn', 'Norwegian Nynorsk'), (b'oc', 'Occitan'), (b'oji', 'Ojibwe'), (b'or', 'Oriya'), (b'orm', 'Oromo'), (b'om', b'Oromo'), (b'os', 'Ossetian, Ossetic'), (b'x-other', 'Other'), (b'pi', 'Pali'), (b'pap', 'Papiamento'), (b'ps', 'Pashto'), (b'fa', 'Persian'), (b'fa-af', 'Persian (Afghanistan)'), (b'pcd', 'Picard'), (b'pl', 'Polish'), (b'pt', 'Portuguese'), (b'pt-pt', b'Portuguese (Portugal)'), (b'pt-br', 'Portuguese, Brazilian'), (b'pa', b'Punjabi'), (b'pan', 'Punjabi'), (b'tsz', 'Purepecha'), (b'tob', b'Qom (Toba)'), (b'que', 'Quechua'), (b'qu', b'Quechua'), (b'qvi', 'Quichua, Imbabura Highland'), (b'raj', 'Rajasthani'), (b'ro', 'Romanian'), (b'rm', 'Romansh'), (b'rn', b'Rundi'), (b'run', 'Rundi'), (b'ru', 'Russian'), (b'ry', 'Rusyn'), (b'kin', 'Rwandi'), (b'sm', 'Samoan'), (b'sg', 'Sango'), (b'sa', 'Sanskrit'), (b'sc', 'Sardinian'), (b'sco', 'Scots'), (b'gd', 'Scottish Gaelic'), (b'trv', 'Seediq'), (b'skx', 'Seko Padang'), (b'sr', 'Serbian'), (b'sr-latn', 'Serbian, Latin'), (b'sh', 'Serbo-Croatian'), (b'crs', 'Seselwa Creole French'), (b'shp', 'Shipibo-Conibo'), (b'sna', 'Shona'), (b'sn', b'Shona'), (b'ii', 'Sichuan Yi'), (b'scn', 'Sicilian'), (b'sgn', 'Sign Languages'), (b'szl', 'Silesian'), (b'sd', 'Sindhi'), (b'si', 'Sinhala'), (b'sk', 'Slovak'), (b'sl', 'Slovenian'), (b'sby', 'Soli'), (b'so', b'Somali'), (b'som', 'Somali'), (b'sot', 'Sotho'), (b'nr', 'Southern Ndebele'), (b'st', 'Southern Sotho'), (b'es', 'Spanish'), (b'es-ec', 'Spanish (Ecuador)'), (b'es-419', 'Spanish (Latin America)'), (b'es-es', b'Spanish (Spain)'), (b'es-ar', 'Spanish, Argentinian'), (b'es-mx', 'Spanish, Mexican'), (b'es-ni', 'Spanish, Nicaraguan'), (b'su', 'Sundanese'), (b'sw', b'Swahili'), (b'swa', 'Swahili'), (b'ss', 'Swati'), (b'sv', 'Swedish'), (b'gsw', 'Swiss German'), (b'tl', 'Tagalog'), (b'ty', 'Tahitian'), (b'tg', 'Tajik'), (b'ta', 'Tamil'), (b'tar', 'Tarahumara, Central'), (b'cta', 'Tataltepec Chatino'), (b'tt', 'Tatar'), (b'te', 'Telugu'), (b'tet', 'Tetum'), (b'th', 'Thai'), (b'bo', 'Tibetan'), (b'ti', b'Tigrinya'), (b'tir', 'Tigrinya'), (b'toj', 'Tojolabal'), (b'to', 'Tonga'), (b'ts', 'Tsonga'), (b'tn', b'Tswana'), (b'tsn', 'Tswana'), (b'aeb', 'Tunisian Arabic'), (b'tr', 'Turkish'), (b'tk', 'Turkmen'), (b'tw', 'Twi'), (b'tzh', 'Tzeltal, Oxchuc'), (b'tzo', 'Tzotzil, Venustiano Carranza'), (b'uk', 'Ukrainian'), (b'umb', 'Umbundu'), (b'hsb', b'Upper Sorbian'), (b'ur', 'Urdu'), (b'ug', 'Uyghur'), (b'uz', 'Uzbek'), (b've', 'Venda'), (b'vi', 'Vietnamese'), (b'vo', 'Volapuk'), (b'wbl', 'Wakhi'), (b'wa', 'Walloon'), (b'wau', 'Wauja'), (b'cy', 'Welsh'), (b'fy', b'Western Frisian'), (b'pnb', 'Western Punjabi'), (b'wol', 'Wolof'), (b'wo', b'Wolof'), (b'xho', 'Xhosa'), (b'xh', b'Xhosa'), (b'tao', 'Yami (Tao)'), (b'yaq', 'Yaqui'), (b'yi', 'Yiddish'), (b'yo', b'Yoruba'), (b'yor', 'Yoruba'), (b'zam', 'Zapotec, Miahuatl\xe1n'), (b'zza', 'Zazaki'), (b'czn', 'Zenzontepec Chatino'), (b'za', 'Zhuang, Chuang'), (b'zu', b'Zulu'), (b'zul', 'Zulu')])),
                ('related_obj_id', models.IntegerField(null=True, blank=True)),
                ('created', models.DateTimeField(default=utils.dates.now, db_index=True)),
                ('private_to_team', models.BooleanField(default=False)),
                ('copied_from', models.ForeignKey(related_name='copies', blank=True, to='activity.ActivityRecord', null=True)),
                ('team', models.ForeignKey(related_name='activity', blank=True, to='teams.Team', null=True)),
                ('user', models.ForeignKey(related_name='activity', blank=True, to='amara_auth.CustomUser', null=True)),
                ('video', models.ForeignKey(related_name='activity', blank=True, to='videos.Video', null=True)),
            ],
            options={
                'ordering': ['-created', '-id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubtitleLanguageChange',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('old_language', models.CharField(max_length=512, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeamSettingsChangeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('changes', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='URLEdit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('old_url', models.URLField(max_length=512, blank=True)),
                ('new_url', models.URLField(max_length=512, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VideoDeletion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(max_length=512, blank=True)),
                ('title', models.CharField(max_length=2048, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
