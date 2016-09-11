"""
Prototype PBLL Project Metadata Scheme

BASE (These descriptors are defined for the model: ProjectPrototype)
--------

    title
    creator
    origin
    description
    publisher
    publish_date
    contributors
    rights
    uri

EXTENDED (These descriptors are defined here, as a metadat schema for ProjectPrototype's)
--------
    subject
    language

    WORLD READINESS STANDARD (wr)
    wr_goal_area.communication
    wr_goal_area.cultures
    wr_goal_area.connections
    wr_goal_area.comparisons
    wr_goal_area.communities

    21ST CENTURY SKILLS (cs)
    cs_interdisciplinary_themes
    cs_info_media_technology_skills
    cs_like_career_skills

    INSTRUCTIONAL_CONTEXT (ic)
    ic_heritage_learners
    ic_target_audience.description
    ic_target_audience.role
    ic_target_audience.location
    ic_product.description
    ic_product.target_culture

    LANGUAGE_PROFICIENCY (lp)
    lp_actfl_scale
    lp_ilr_scale.listening
    lp_ilr_scale.reading
    lp_ilr_scale.speaking
    lp_ilr_scale.writing
"""

"""
The following tuples are used by reposite.models.PrototypeMetaElement 
to enforce the definition of metadata types and categories. New metadata 
definitions and or categories should be added to these tuples to ensure
they are enforced in the PrototypeMetaElement model and relevant table.

Format: <metadata identifier>, <metadata display string>

Note: each of the types listed below must have a corresponding form definition
added to PrototypeMetadataForm defined in this file. This ensures that the relative
form used to create metadata elements are properly associated. 

Additionally, a controlled vocabulary may be defined for each metatdata type to constrain the data. 
"""

METADATA_CATEGORIES = (
    ('subject', 'Subject Area'),
    ('language', 'Language'),
    ('world_readiness', 'World Readiness Standards'),
    ('21st_century_skills', '21st Century Skills'),
    ('instructional_context', 'Instructional Context'),
    ('language_proficiency', 'Language Proficiency'),
)

METADATA_TYPES = (
    ('subject', 'Subject Area(s)'), 
    ('language', 'Language(s)'), 
    ('ic_heritage_learners', 'Heritage Learners'), 
    ('ic_target_audience_description', 'Target Audience Description'), 
    ('ic_target_audience_role', 'Audience Role'), 
    ('ic_target_audience_location', 'Audience Location'), 
    ('ic_product_description', 'Product Description'), 
    ('ic_product_target_culture', 'Product Target Culture'), 
    ('lp_actfl_scale', 'ACTFL Scale'), 
    ('lp_ilr_scale_listening', 'ILR Scale Listening'), 
    ('lp_ilr_scale_reading', 'ILR Scale Reading'), 
    ('lp_ilr_scale_speaking', 'ILR Scale Speaking'), 
    ('lp_ilr_scale_writing', 'ILR Scale Writing'), 
    ('wr_goal_area_communication', 'Communication'), 
    ('wr_goal_area_cultures', 'Cultures'), 
    ('wr_goal_area_connections', 'Connections'), 
    ('wr_goal_area_comparisons', 'Comparisons'), 
    ('wr_goal_area_communities', 'Communities'), 
    ('cs_interdisciplinary_themes', 'Interdisciplinary Themes'), 
    ('cs_info_media_technology_skills', 'Information, Media, and Technology Skills'), 
    ('cs_like_career_skills', 'Life and Career Skills'),
)

METADATA_TYPES_TO_CATEGORIES = {
    'subject': 'subject',
    'language': 'language',
    'ic_heritage_learners': 'instructional_context',
    'ic_target_audience_description': 'instructional_context',
    'ic_target_audience_role': 'instructional_context',
    'ic_target_audience_location': 'instructional_context',
    'ic_product_description': 'instructional_context',
    'ic_product_target_culture': 'instructional_context',
    'lp_actfl_scale': 'language_proficiency',
    'lp_ilr_scale_listening': 'language_proficiency',
    'lp_ilr_scale_reading': 'language_proficiency',
    'lp_ilr_scale_speaking': 'language_proficiency',
    'lp_ilr_scale_writing': 'language_proficiency',
    'wr_goal_area_communication': 'world_readiness',
    'wr_goal_area_cultures': 'world_readiness',
    'wr_goal_area_connections': 'world_readiness',
    'wr_goal_area_comparisons': 'world_readiness',
    'wr_goal_area_communities': 'world_readiness',
    'cs_interdisciplinary_themes': '21st_century_skills',
    'cs_info_media_technology_skills': '21st_century_skills',
    'cs_like_career_skills': '21st_century_skills', 
}


"""
CONTROLLED VOCABULARLY FOR BASE AND EXTENDED DESCRIPTORS
--------
"""

SUBJECT_AREAS = (
    ('architecture', 'architecture'),
    ('beauty', 'beauty'),
    ('communities', 'communities'),
    ('creativity', 'creativity'),
    ('design', 'design'),
    ('economy', 'economy'),
    ('education', 'education'),
    ('emigration/immigration', 'emigration/immigration'),
    ('entertainment', 'entertainment'),
    ('ethics', 'ethics'),
    ('ethnic identity', 'ethnic identity'),
    ('family', 'family'),
    ('fashion', 'fashion'),
    ('food', 'food'),
    ('friendship', 'friendship'),
    ('geography', 'geography'),
    ('global challenges', 'global challenges'),
    ('health', 'health'),
    ('heroes', 'heroes'),
    ('history', 'history'),
    ('language and literature', 'language and literature'),
    ('lifestyles', 'lifestyles'),
    ('national identity', 'national identity'),
    ('nature', 'nature'),
    ('philosophy', 'philosophy'),
    ('psychology', 'psychology'),
    ('restaurant', 'restaurant'),
    ('science', 'science'),
    ('social networks', 'social networks'),
    ('society', 'society'),
    ('sustainability', 'sustainability'),
    ('technology', 'technology'),
    ('the environment', 'the environment'),
    ('theater', 'theater'),
    ('traditions', 'traditions'),
    ('travel', 'travel'),
    ('values', 'values'),
    ('visual arts', 'visual arts')
)

COPYRIGHT_TYPES = (
    ('http://creativecommons.org/', 'Creative Commons'),
)

WR_GOAL_AREA = {
    'communication': (
        ('Interpersonal', 'Interpersonal'),
        ('Interpretive', 'Interpretive'),
        ('Presentational', 'Presentational')
    ),

    'cultures': (
        ('Relating Cultural Practices to Perspectives',
         'Relating Cultural Practices to Perspectives'),
        ('Relating Cultural Products to Perspectives',
         'Relating Cultural Products to Perspectives')
    ),

    'connections': (
        ('Making Connections', 'Making Connections'),
        ('Acquiring Information and Diverse Perspectives',
         'Acquiring Information and Diverse Perspectives')
    ),

    'comparisons': (
        ('Language comparisons', 'Language comparisons'),
        ('Cultural comparisons', 'Cultural comparisons')
    ),

    'communities': (
        ('School and Global', 'School and Global'),
        ('Lifelong Learning', 'Lifelong Learning')
    )
}

CENTURY_SKILLS = {
    'interdisciplinary-themes': (
        ('Global Awareness', 'Global Awareness'),
        ('Civic Literacy', 'Civic Literacy'),
        ('Health Literacy', 'Health Literacy'),
        ('Financial, Economic, Business and Entrepreneurial Literacy',
         'Financial, Economic, Business and Entrepreneurial Literacy')
    ),

    'information-media-technology-skills': (
        ('Communication', 'Communication'),
        ('Collaboration', 'Collaboration'),
        ('Creativity and Innovation', 'Creativity and Innovation'),
        ('Information Literacy', 'Information Literacy'),
        ('Media Literacy', 'Media Literacy'),
        ('Technology Literacy', 'Technology Literacy'),
    ),

    'like-career-skills': (
        ('Flexibility and adaptability', 'Flexibility and adaptability'),
        ('Initiative and Self-Direction', 'Initiative and Self-Direction'),
        ('Social and Cross Cultural Skills',
         'Social and Cross Cultural Skills'),
        ('Productivity and Accountability', 'Productivity and Accountability'),
        ('Leadership and responsibility', 'Leadership and responsibility'),
    )
}

INSTRUCTIONAL_CONTEXTS = {
    'heritage-learners': (
        ('yes', 'Yes'),
        ('mixed', 'Mixed'),
        ('no', 'No')
    )
}

LANGUAGE_PROFICIENCY = {
    'actfl': (
        ('1', 'Novice Low'),
        ('2', 'Novice Mid'),
        ('3', 'Novice High'),
        ('4', 'Intermediate Low'),
        ('5', 'Intermediate Mid'),
        ('6', 'Intermediate High'),
        ('7', 'Advanced Low'),
        ('8', 'Advanced Mid'),
        ('9', 'Advanced High'),
        ('10', 'Superior')
    ),

    'ilr-reading': (
        ('0', 'Reading 0'),
        ('1', 'Reading 1'),
        ('2', 'Reading 2'),
        ('3', 'Reading 3'),
        ('4', 'Reading 4'),
        ('5', 'Reading 5')
    ),

    'ilr-listening': (
        ('0', 'Listening 0'),
        ('1', 'Listening 1'),
        ('2', 'Listening 2'),
        ('3', 'Listening 3'),
        ('4', 'Listening 4'),
        ('5', 'Listening 5')
    ),

    'ilr-speaking': (
        ('0', 'Speaking 0'),
        ('1', 'Speaking 1'),
        ('2', 'Speaking 2'),
        ('3', 'Speaking 3'),
        ('4', 'Speaking 4'),
        ('5', 'Speaking 5')
    ),

    'ilr-writing': (
        ('0', 'Writing 0'),
        ('1', 'Writing 1'),
        ('2', 'Writing 2'),
        ('3', 'Writing 3'),
        ('4', 'Writing 4'),
        ('5', 'Writing 5')
    )
}

LANGUAGES_NISO = [(u'Achinese', u'Achinese'), (u'Acoli', u'Acoli'), (u'Adangme', u'Adangme'), (u'Afro-Asiatic (Other)', u'Afro-Asiatic (Other)'), (u'Afrihili (Artificial language)', u'Afrihili (Artificial language)'), (u'Afrikaans', u'Afrikaans'), (u'Aljamia', u'Aljamia'), (u'Akkadian', u'Akkadian'), (u'Albanian', u'Albanian'), (u'Aleut', u'Aleut'), (u'Algonquian languages', u'Algonquian languages'), (u'Amharic', u'Amharic'), (u'English', u'English'), (u'Apache languages', u'Apache languages'), (u'Arabic', u'Arabic'), (u'Aramaic', u'Aramaic'), (u'Armenian', u'Armenian'), (u'Araucanian', u'Araucanian'), (u'Arapaho', u'Arapaho'), (u'Artificial (Other)', u'Artificial (Other)'), (u'Arawak', u'Arawak'), (u'Assamese', u'Assamese'), (u'Athapascan languages', u'Athapascan languages'), (u'Avaric', u'Avaric'), (u'Avestan', u'Avestan'), (u'Awadhi', u'Awadhi'), (u'Aymara', u'Aymara'), (u'Azerbaijani', u'Azerbaijani'), (u'Banda', u'Banda'), (u'Bamileke languages', u'Bamileke languages'), (u'Bashkir', u'Bashkir'), (u'Baluchi', u'Baluchi'), (u'Bambara', u'Bambara'), (u'Balinese', u'Balinese'), (u'Basque', u'Basque'), (u'Basa', u'Basa'), (u'Baltic (Other)', u'Baltic (Other)'), (u'Beja', u'Beja'), (u'Byelorussian', u'Byelorussian'), (u'Bemba', u'Bemba'), (u'Bengali', u'Bengali'), (u'Berber languages', u'Berber languages'), (u'Bhojpuri', u'Bhojpuri'), (u'Bikol', u'Bikol'), (u'Bini', u'Bini'), (u'Siksika', u'Siksika'), (u'Braj', u'Braj'), (u'Breton', u'Breton'), (u'Buginese', u'Buginese'), (u'Bulgarian', u'Bulgarian'), (u'Burmese', u'Burmese'), (u'Caddo', u'Caddo'), (u'Central American Indian (Other)', u'Central American Indian (Other)'), (u'Khmer', u'Khmer'), (u'Carib', u'Carib'), (u'Catalan', u'Catalan'), (u'Caucasian (Other)', u'Caucasian (Other)'), (u'Cebuano', u'Cebuano'), (u'Celtic languages', u'Celtic languages'), (u'Chamorro', u'Chamorro'), (u'Chibcha', u'Chibcha'), (u'Chechen', u'Chechen'), (u'Chagatai', u'Chagatai'), (u'Chinese', u'Chinese'), (u'Chinook jargon', u'Chinook jargon'), (u'Choctaw', u'Choctaw'), (u'Cherokee', u'Cherokee'), (u'Church Slavic', u'Church Slavic'), (u'Chuvash', u'Chuvash'), (u'Cheyenne', u'Cheyenne'), (u'Coptic', u'Coptic'), (u'Cornish', u'Cornish'), (u'Creoles and Pidgins', u'Creoles and Pidgins'), (u'Cree', u'Cree'), (u'Creoles and Pidgins (Other)', u'Creoles and Pidgins (Other)'), (u'Cushitic (Other)', u'Cushitic (Other)'), (u'Czech', u'Czech'), (u'Dakota', u'Dakota'), (u'Danish', u'Danish'), (u'Delaware', u'Delaware'), (u'Dinka', u'Dinka'), (u'Dogri', u'Dogri'), (u'Dravidian (Other)', u'Dravidian (Other)'), (u'Duala', u'Duala'), (u'Dutch', u'Dutch'), (u'Dyula', u'Dyula'), (u'Efik', u'Efik'), (u'Egyptian', u'Egyptian'), (u'Ekajuk', u'Ekajuk'), (u'Elamite', u'Elamite'), (u'Eskimo', u'Eskimo'), (u'Esperanto', u'Esperanto'), (u'Estonian', u'Estonian'), (u'Ethiopic', u'Ethiopic'), (u'Ewe', u'Ewe'), (u'Ewondo', u'Ewondo'), (u'Fang', u'Fang'), (u'Faroese', u'Faroese'), (u'Fanti', u'Fanti'), (u'Fijian', u'Fijian'), (u'Finnish', u'Finnish'), (u'Finno-Ugrian (Other)', u'Finno-Ugrian (Other)'), (u'Fon', u'Fon'), (u'French', u'French'), (u'Friesian', u'Friesian'), (u'Fula', u'Fula'), (u'G\xfe', u'G\xfe'), (u'Gaelic (Scots)', u'Gaelic (Scots)'), (u'Gallegan', u'Gallegan'), (u'Oromo', u'Oromo'), (u'Gayo', u'Gayo'), (u'Germanic (Other)', u'Germanic (Other)'), (u'Georgian', u'Georgian'), (u'German', u'German'), (u'Gilbertese', u'Gilbertese'), (u'Gondi', u'Gondi'), (u'Gothic', u'Gothic'), (u'Grebo', u'Grebo'), (u'Greek', u'Greek'), (u'Guarani', u'Guarani'), (u'Gujarati', u'Gujarati'), (u'Haida', u'Haida'), (u'Hausa', u'Hausa'), (u'Hawaiian', u'Hawaiian'), (u'Hebrew', u'Hebrew'), (u'Herero', u'Herero'), (u'Hiligaynon', u'Hiligaynon'), (u'Himachali', u'Himachali'), (u'Hindi', u'Hindi'), (u'Hiri Motu', u'Hiri Motu'), (u'Hungarian', u'Hungarian'), (u'Hupa', u'Hupa'), (u'Iban', u'Iban'), (u'Igbo', u'Igbo'), (u'Icelandic', u'Icelandic'), (u'Ijo', u'Ijo'), (u'Iloko', u'Iloko'), (u'Indic (Other)', u'Indic (Other)'), (u'Indonesian', u'Indonesian'), (u'Indo-European (Other)', u'Indo-European (Other)'), (u'Interlingua (International Auxiliary Language Association)', u'Interlingua (International Auxiliary Language Association)'), (u'Iranian (Other)', u'Iranian (Other)'), (u'Irish', u'Irish'), (u'Iroquoian languages', u'Iroquoian languages'), (u'Italian', u'Italian'), (u'Javanese', u'Javanese'), (u'Japanese', u'Japanese'), (u'Judeo-Persian', u'Judeo-Persian'), (u'Judeo-Arabic', u'Judeo-Arabic'), (u'Kara-Kalpak', u'Kara-Kalpak'), (u'Kabyle', u'Kabyle'), (u'Kachin', u'Kachin'), (u'Kamba', u'Kamba'), (u'Kannada', u'Kannada'), (u'Karen', u'Karen'), (u'Kashmiri', u'Kashmiri'), (u'Kanuri', u'Kanuri'), (u'Kawi', u'Kawi'), (u'Kazakh', u'Kazakh'), (u'Khasi', u'Khasi'), (u'Khoisan (Other)', u'Khoisan (Other)'), (u'Khotanese', u'Khotanese'), (u'Kikuyu', u'Kikuyu'), (u'Kinyarwanda', u'Kinyarwanda'), (u'Kirghiz', u'Kirghiz'), (u'Konkani', u'Konkani'), (u'Kongo', u'Kongo'), (u'Korean', u'Korean'), (u'Kpelle', u'Kpelle'), (u'Kru', u'Kru'), (u'Kurukh', u'Kurukh'), (u'Kuanyama', u'Kuanyama'), (u'Kurdish', u'Kurdish'), (u'Kusaie', u'Kusaie'), (u'Kutenai', u'Kutenai'), (u'Ladino', u'Ladino'), (u'Lahnd', u'Lahnd'), (u'Lamba', u'Lamba'), (u"Langue d'oc (post-1500)", u"Langue d'oc (post-1500)"), (u'Lao', u'Lao'), (u'Lapp', u'Lapp'), (u'Latin', u'Latin'), (u'Latvian', u'Latvian'), (u'Lingala', u'Lingala'), (u'Lithuanian', u'Lithuanian'), (u'Mongo', u'Mongo'), (u'Lozi', u'Lozi'), (u'Luba-Katanga', u'Luba-Katanga'), (u'Ganda', u'Ganda'), (u'Luiseno', u'Luiseno'), (u'Lunda', u'Lunda'), (u'Luo (Kenya and Tanzania)', u'Luo (Kenya and Tanzania)'), (u'Macedonian', u'Macedonian'), (u'Madurese', u'Madurese'), (u'Magahi', u'Magahi'), (u'Marshall', u'Marshall'), (u'Maithili', u'Maithili'), (u'Makasar', u'Makasar'), (u'Malayalam', u'Malayalam'), (u'Mandingo', u'Mandingo'), (u'Maori', u'Maori'), (u'Austronesian (Other)', u'Austronesian (Other)'), (u'Marathi', u'Marathi'), (u'Masai', u'Masai'), (u'Manx', u'Manx'), (u'Malay', u'Malay'), (u'Mende', u'Mende'), (u'Micmac', u'Micmac'), (u'Minangkabau', u'Minangkabau'), (u'Miscellaneous (Other)', u'Miscellaneous (Other)'), (u'Mon-Khmer (Other)', u'Mon-Khmer (Other)'), (u'Malagasy', u'Malagasy'), (u'Maltese', u'Maltese'), (u'Manipuri', u'Manipuri'), (u'Manobo languages', u'Manobo languages'), (u'Mohawk', u'Mohawk'), (u'Moldavian', u'Moldavian'), (u'Mongolian', u'Mongolian'), (u'Mossi', u'Mossi'), (u'Multiple languages', u'Multiple languages'), (u'Munda (Other)', u'Munda (Other)'), (u'Creek', u'Creek'), (u'Marwari', u'Marwari'), (u'Mayan languages', u'Mayan languages'), (u'Aztec', u'Aztec'), (u'North American Indian (Other)', u'North American Indian (Other)'), (u'Navajo', u'Navajo'), (u'Ndebele (Zimbabwe)', u'Ndebele (Zimbabwe)'), (u'Ndonga', u'Ndonga'), (u'Nepali', u'Nepali'), (u'Newari', u'Newari'), (u'Niger-Kordofanian (Other)', u'Niger-Kordofanian (Other)'), (u'Niuean', u'Niuean'), (u'Norwegian', u'Norwegian'), (u'Northern Sotho', u'Northern Sotho'), (u'Nubian languages', u'Nubian languages'), (u'Nyanja', u'Nyanja'), (u'Nyamwezi', u'Nyamwezi'), (u'Nyankole', u'Nyankole'), (u'Nyoro', u'Nyoro'), (u'Nzima', u'Nzima'), (u'Ojibwa', u'Ojibwa'), (u'Oriya', u'Oriya'), (u'Osage', u'Osage'), (u'Ossetic', u'Ossetic'), (u'Turkish', u'Turkish'), (u'Otomian languages', u'Otomian languages'), (u'Papuan-Australian (Other)', u'Papuan-Australian (Other)'), (u'Pangasinan', u'Pangasinan'), (u'Pahlavi', u'Pahlavi'), (u'Pampanga', u'Pampanga'), (u'Panjabi', u'Panjabi'), (u'Papiamento', u'Papiamento'), (u'Palauan', u'Palauan'), (u'Old Persian (ca. 600-400 B.C.)', u'Old Persian (ca. 600-400 B.C.)'), (u'Persian', u'Persian'), (u'Pali', u'Pali'), (u'Polish', u'Polish'), (u'Ponape', u'Ponape'), (u'Portuguese', u'Portuguese'), (u'Prakrit languages', u'Prakrit languages'), (u'Provencal', u'Provencal'), (u'Pushto', u'Pushto'), (u'Quechua', u'Quechua'), (u'Rajasthani', u'Rajasthani'), (u'Rarotongan', u'Rarotongan'), (u'Romance (Other)', u'Romance (Other)'), (u'Raeto-Romance', u'Raeto-Romance'), (u'Romany', u'Romany'), (u'Romanian', u'Romanian'), (u'Rundi', u'Rundi'), (u'Russian', u'Russian'), (u'Sandawe', u'Sandawe'), (u'Sango', u'Sango'), (u'South American Indian (Other)', u'South American Indian (Other)'), (u'Salishan languages', u'Salishan languages'), (u'Samaritan Aramaic', u'Samaritan Aramaic'), (u'Sanskrit', u'Sanskrit'), (u'Samoan', u'Samoan'), (u'Serbo-Croatian (Cyrillic)', u'Serbo-Croatian (Cyrillic)'), (u'Scots', u'Scots'), (u'Serbo-Croatian (Roman)', u'Serbo-Croatian (Roman)'), (u'Selkup', u'Selkup'), (u'Semitic (Other)', u'Semitic (Other)'), (u'Shan', u'Shan'), (u'Shona', u'Shona'), (u'Sidamo', u'Sidamo'), (u'Siouan languages', u'Siouan languages'), (u'Sino-Tibetan (Other)', u'Sino-Tibetan (Other)'), (u'Slavic (Other)', u'Slavic (Other)'), (u'Slovak', u'Slovak'), (u'Slovenian', u'Slovenian'), (u'Sindhi', u'Sindhi'), (u'Sinhalese', u'Sinhalese'), (u'Somali', u'Somali'), (u'Songhai', u'Songhai'), (u'Spanish', u'Spanish'), (u'Serer', u'Serer'), (u'Sotho', u'Sotho'), (u'Sukuma', u'Sukuma'), (u'Sundanese', u'Sundanese'), (u'Susu', u'Susu'), (u'Sumerian', u'Sumerian'), (u'Swahili', u'Swahili'), (u'Swazi', u'Swazi'), (u'Syriac', u'Syriac'), (u'Tagalog', u'Tagalog'), (u'Tahitian', u'Tahitian'), (u'Tajik', u'Tajik'), (u'Tamil', u'Tamil'), (u'Tatar', u'Tatar'), (u'Telugu', u'Telugu'), (u'Timne', u'Timne'), (u'Tereno', u'Tereno'), (u'Thai', u'Thai'), (u'Tibetan', u'Tibetan'), (u'Tigre', u'Tigre'), (u'Tigrinya', u'Tigrinya'), (u'Tivi', u'Tivi'), (u'Tlingit', u'Tlingit'), (u'Tonga (Nyasa)', u'Tonga (Nyasa)'), (u'Tonga (Tonga Islands)', u'Tonga (Tonga Islands)'), (u'Truk', u'Truk'), (u'Tsimshian', u'Tsimshian'), (u'Tsonga', u'Tsonga'), (u'Tswana', u'Tswana'), (u'Turkmen', u'Turkmen'), (u'Tumbuka', u'Tumbuka'), (u'Altaic (Other)', u'Altaic (Other)'), (u'Twi', u'Twi'), (u'Ugaritic', u'Ugaritic'), (u'Uighur', u'Uighur'), (u'Ukrainian', u'Ukrainian'), (u'Umbundu', u'Umbundu'), (u'Undetermined', u'Undetermined'), (u'Urdu', u'Urdu'), (u'Uzbek', u'Uzbek'), (u'Vai', u'Vai'), (u'Venda', u'Venda'), (u'Vietnamese', u'Vietnamese'), (u'Votic', u'Votic'), (u'Wakashan languages', u'Wakashan languages'), (u'Walamo', u'Walamo'), (u'Waray', u'Waray'), (u'Washo', u'Washo'), (u'Welsh', u'Welsh'), (u'Sorbian languages', u'Sorbian languages'), (u'Wolof', u'Wolof'), (u'Xhosa', u'Xhosa'), (u'Yao', u'Yao'), (u'Yap', u'Yap'), (u'Yiddish', u'Yiddish'), (u'Yoruba', u'Yoruba'), (u'Zapotec', u'Zapotec'), (u'Zenaga', u'Zenaga'), (u'Zulu', u'Zulu'), (u'Zuni', u'Zuni')]


"""
PrototypeMetadataForm is designed to define form fields used in ProjectPrototype forms. See reposite.forms to understand
how these fields are used.

Note that the form fields defined below are based on the metadata schema illustrated above (and its related choices
or 'vocabulary'). If there are additions, deletions, or modifications to the
schema above, they need to be reflected and/or edited in the relevant form field definitions defined here.

Alert: the category attribute is required for each form widget. This should reflect one of the items in METADATA_CATEGORIES above.
"""

from django import forms


class PrototypeMetadataForm(forms.Form):
    default_input_size = '60'

    subject = forms.MultipleChoiceField(
        choices=SUBJECT_AREAS,
        label='Subject Area',
        label_suffix='Subject Area(s)',
        help_text='(Check all that apply)',
        widget=forms.CheckboxSelectMultiple(attrs={}),
        required=True,
        )
    language = forms.MultipleChoiceField(
        choices=LANGUAGES_NISO,
        label='Language',
        label_suffix='Language(s)',
        help_text='(Check all that apply)',
        widget=forms.CheckboxSelectMultiple(attrs={}),
        required=False)

    ic_heritage_learners = forms.ChoiceField(
        choices=INSTRUCTIONAL_CONTEXTS['heritage-learners'],
        label='Instructional Context',
        label_suffix='Heritage Learners',
        widget=forms.RadioSelect(attrs={'class': ''}),
        required=False)
    ic_target_audience_description = forms.CharField(
        label='Instructional Context',
        label_suffix='Target Audience Description',
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        required=False)
    ic_target_audience_role = forms.CharField(
        label='Instructional Context',
        label_suffix='Audience Role',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False)
    ic_target_audience_location = forms.CharField(
        label='Instructional Context',
        label_suffix='Audience Location',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False)
    ic_product_description = forms.CharField(
        label='Instructional Context',
        label_suffix='Product Description',
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        required=False)
    ic_product_target_culture = forms.CharField(
        label='Instructional Context',
        label_suffix='Product Target Culture',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False)

    lp_actfl_scale = forms.MultipleChoiceField(
        choices=LANGUAGE_PROFICIENCY['actfl'],
        label='Language Proficiency',
        label_suffix='ACTFL Scale',
        help_text='(Check all that apply)',
        widget=forms.CheckboxSelectMultiple(attrs={'class': ''}),
        required=False)
    lp_ilr_scale_listening = forms.MultipleChoiceField(
        choices=LANGUAGE_PROFICIENCY['ilr-listening'],
        widget=forms.CheckboxSelectMultiple(attrs={'class': ''}),
        label='Language Proficiency',
        label_suffix='ILR Scale Listening',
        help_text='(Check all that apply)',
        required=False)
    lp_ilr_scale_reading = forms.MultipleChoiceField(
        choices=LANGUAGE_PROFICIENCY['ilr-reading'],
        widget=forms.CheckboxSelectMultiple(attrs={'class': ''}),
        label='Language Proficiency',
        label_suffix='ILR Scale Reading',
        help_text='(Check all that apply)',
        required=False)
    lp_ilr_scale_speaking = forms.MultipleChoiceField(
        choices=LANGUAGE_PROFICIENCY['ilr-speaking'],
        widget=forms.CheckboxSelectMultiple(attrs={'class': ''}),
        label='Language Proficiency',
        label_suffix='ILR Scale Speaking',
        help_text='(Check all that apply)',
        required=False)
    lp_ilr_scale_writing = forms.MultipleChoiceField(
        choices=LANGUAGE_PROFICIENCY['ilr-writing'],
        widget=forms.CheckboxSelectMultiple(attrs={'class': ''}),
        label='Language Proficiency',
        label_suffix='ILR Scale Writing',
        help_text='(Check all that apply)',
        required=False)

    wr_goal_area_communication = forms.MultipleChoiceField(
        choices=WR_GOAL_AREA['communication'],
        widget=forms.CheckboxSelectMultiple(attrs={'class': ''}),
        label='World Readiness Standards',
        label_suffix='Communication',
        help_text='(Check all that apply)',
        required=False)
    wr_goal_area_cultures = forms.MultipleChoiceField(
        choices=WR_GOAL_AREA['cultures'],
        widget=forms.CheckboxSelectMultiple(attrs={'class': ''}),
        label='World Readiness Standards',
        label_suffix='Cultures',
        help_text='(Check all that apply)',
        required=False)
    wr_goal_area_connections = forms.MultipleChoiceField(
        choices=WR_GOAL_AREA['connections'],
        widget=forms.CheckboxSelectMultiple(attrs={'class': ''}),
        label='World Readiness Standards',
        label_suffix='Connections',
        help_text='(Check all that apply)',
        required=False)
    wr_goal_area_comparisons = forms.MultipleChoiceField(
        choices=WR_GOAL_AREA['comparisons'],
        widget=forms.CheckboxSelectMultiple(attrs={'class': ''}),
        label='World Readiness Standards',
        label_suffix='Comparisons',
        help_text='(Check all that apply)',
        required=False)
    wr_goal_area_communities = forms.MultipleChoiceField(
        choices=WR_GOAL_AREA['communities'],
        widget=forms.CheckboxSelectMultiple(attrs={'class': ''}),
        label='World Readiness Standards',
        label_suffix='Communities',
        help_text='(Check all that apply)',
        required=False)

    cs_interdisciplinary_themes = forms.MultipleChoiceField(
        choices=CENTURY_SKILLS['interdisciplinary-themes'],
        widget=forms.CheckboxSelectMultiple(attrs={'class': ''}),
        label='21st Century Skills',
        label_suffix='Interdisciplinary Themes',
        help_text='(Check all that apply)',
        required=False)
    cs_info_media_technology_skills = forms.MultipleChoiceField(
        choices=CENTURY_SKILLS['information-media-technology-skills'],
        widget=forms.CheckboxSelectMultiple(attrs={'class': ''}),
        label='21st Century Skills',
        label_suffix='Information, Media, and Technology Skills',
        help_text='(Check all that apply)',
        required=False)
    cs_like_career_skills = forms.MultipleChoiceField(
        choices=CENTURY_SKILLS['like-career-skills'],
        widget=forms.CheckboxSelectMultiple(attrs={'class': ''}),
        label='21st Century Skills',
        label_suffix='Life and Career Skills',
        help_text='(Check all that apply)',
        required=False)

    def multiple_choice_fields(self):
        return [field_name for field_name, field_type in self.fields.items() if type(field_type) == forms.MultipleChoiceField]

    
    def display_order_fields(self):
        """ Returns the definition order of the field names. """
        return self.fields.keys()


