# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

from quizzes.models import Question as QuestionModel
from quizzes.models import Option as OptionModel


QUESTION_DATA = [
    {
        "text": "Which song by Burna Boy features the line, \"i dey port harcourt when dem kill soboma\"?",
        "options": [
            "Last last",
            "Gbona",
            "Anybody",
        ],
        "answer": "Last last",
    },
    {
        "text": "In what year did Burna Boy win his first Grammy Award?",
        "options": [
            "2020",
            "2021",
            "2022",
        ],
        "answer": "2021",
    },
    {
        "text": "Which city was Burna Boy born in?",
        "options": [
            "Lagos",
            "Abuja",
            "Port Harcourt",
        ],
        "answer": "Port Harcourt",
    },
    {
        "text": "Burna Boy has often cited this legendary Nigerian artist as his greatest influence. Who is it?",
        "options": [
            "Sunny Ade",
            "Fela Kuti",
            "King Wasiu Ayinde Marshal",
        ],
        "answer": "Fela Kuti",
    },
    {
        "text": "What did Burna Boy controversially claim during an interview in 2023?",
        "options": [
            "Afrobeats is a global phenomenon",
            "Afrobeats lacks real-life substance",
            "Afrobeats is purely Nigerian music",
        ],
        "answer": "Afrobeats lacks real-life substance",
    },
    {
        "text": "Which Davido song includes the line, \"My money, my body, na your own\"?",
        "options": [
            "If",
            "Fall",
            "Assurance",
        ],
        "answer": "If",
    },
    {
        "text": "In which year did Davido win the BET Award for Best International Act?",
        "options": [
            "2018",
            "2019",
            "2020",
        ],
        "answer": "2018",
    },
    {
        "text": "Davido was born in which U.S. city?",
        "options": [
            "Los Angeles",
            "Atlanta",
            "Miami",
        ],
        "answer": "Atlanta",
    },
    {
        "text": "What is the name of Davido’s debut studio album?",
        "options": [
            "A Better Time",
            "Omo Baba Olowo",
            "Omo Baba Olowo: The Genesis",
        ],
        "answer": "Omo Baba Olowo: The Genesis",
    },
    {
        "text": "In a 2021 interview, Davido claimed that which aspect of his life sets him apart from other Afrobeats artists?",
        "options": [
            "His diverse upbringing",
            "His vocal style",
            "His family tree",
        ],
        "answer": "His diverse upbringing",
    },
    {
        "text": "Which Rema song features the lyrics, \"I'm in love with plenty women, I no mind marry all of them\"?",
        "options": [
            "Bounce",
            "Dumebi",
            "Woman",
        ],
        "answer": "Woman",
    },
    {
        "text": "In what year did Rema release his debut single, \"Dumebi\"?",
        "options": [
            "2018",
            "2019",
            "2020",
        ],
        "answer": "2019",
    },
    {
        "text": "Rema was born in which Nigerian city?",
        "options": [
            "Lagos",
            "Benin City",
            "Abuja",
        ],
        "answer": "Benin City",
    },
    {
        "text": "Rema is often associated with a unique genre he calls \"Afrorave.\" Which genre is this heavily influenced by?",
        "options": [
            "Dancehall",
            "Trap",
            "Highlife",
        ],
        "answer": "Trap",
    },
    {
        "text": "In a 2022 interview, Rema mentioned that which artist played a major role in shaping his musical style?",
        "options": [
            "Burna Boy",
            "Wizkid",
            "Drake",
        ],
        "answer": "Drake",
    },
    {
        "text": "Which Asake song features the lyrics, \"Dem dey carry me dey go where I no know\"?",
        "options": [
            "Omo Ope",
            "Peace Be Unto You (PBUY)",
            "Terminator",
        ],
        "answer": "Peace Be Unto You (PBUY)",
    },
    {
        "text": "In what year did Asake release his breakout single, \"Mr. Money\"?",
        "options": [
            "2020",
            "2021",
            "2022",
        ],
        "answer": "2021",
    },
    {
        "text": "Asake was born in which Nigerian state?",
        "options": [
            "Lagos State",
            "Ogun State",
            "Osun State",
        ],
        "answer": "Lagos State",
    },
    {
        "text": "Before his breakthrough in music, Asake was primarily involved in which artistic field?",
        "options": [
            "Acting",
            "Dancing",
            "Modeling",
        ],
        "answer": "Dancing",
    },
    {
        "text": "In an interview, Asake mentioned that which famous Nigerian artist had a significant influence on his decision to pursue music?",
        "options": [
            "2Baba",
            "Olamide",
            "Wizkid",
        ],
        "answer": "Olamide",
    },
    {
        "text": "Which J. Cole song features the lyrics, \"I'm on some Marvin Gaye, I get my chill on\"?",
        "options": [
            "Lights Please",
            "Can't Get Enough",
            "Work Out",
        ],
        "answer": "Work Out",
    },
    {
        "text": "In what year did J. Cole release his debut studio album, Cole World: The Sideline Story?",
        "options": [
            "2010",
            "2011",
            "2012",
        ],
        "answer": "2011",
    },
    {
        "text": "J. Cole was born on a U.S. military base in which country?",
        "options": [
            "Germany",
            "South Korea",
            "Japan",
        ],
        "answer": "Germany",
    },
    {
        "text": "Which university did J. Cole graduate from before pursuing his music career full-time?",
        "options": [
            "University of North Carolina",
            "St. John's University",
            "Duke University",
        ],
        "answer": "St. John's University",
    },
    {
        "text": "In an interview, J. Cole once mentioned that which book profoundly impacted his perspective on life?",
        "options": [
            "\"The Alchemist\" by Paulo Coelho",
            "The Autobiography of Malcolm X",
            "\"1984\" by George Orwell",
        ],
        "answer": "The Autobiography of Malcolm X",
    },
    {
        "text": "Which Doja Cat song includes the lyrics, \"I want you, I need you, I’ll see you, see you, I’ll see you later\"?",
        "options": [
            "Say So",
            "Agora Hills",
            "Kiss Me More",
        ],
        "answer": "Agora Hills",
    },
    {
        "text": "In what year did Doja Cat release her viral breakout single, \"Mooo!\"?",
        "options": [
            "2018",
            "2019",
            "2020",
        ],
        "answer": "2018",
    },
    {
        "text": "Doja Cat was born in which U.S. city?",
        "options": [
            "Los Angeles",
            "New York City",
            "Atlanta",
        ],
        "answer": "Los Angeles",
    },
    {
        "text": "Before rising to fame, Doja Cat was active on which online platform, where she built an early fanbase?",
        "options": [
            "SoundCloud",
            "TikTok",
            "Vine",
        ],
        "answer": "TikTok",
    },
    {
        "text": "In a 2021 interview, Doja Cat mentioned which artist greatly influenced her eclectic style and genre-blending approach?",
        "options": [
            "Nicki Minaj",
            "Rihanna",
            "Missy Elliott",
        ],
        "answer": "Nicki Minaj",
    },
    {
        "text": "Which Ayra Starr song contains the lyrics, \"I don’t care if you’re bad for me, you’re bad for me\"?",
        "options": [
            "Away",
            "Bloody Samaritan",
            "Fashion Killer",
        ],
        "answer": "Away",
    },
    {
        "text": "In what year did Ayra Starr release her debut self-titled EP?",
        "options": [
            "2021",
            "2020",
            "2019",
        ],
        "answer": "2021",
    },
    {
        "text": "Ayra Starr was born in which West African country?",
        "options": [
            "Nigeria",
            "Benin Republic",
            "Ghana",
        ],
        "answer": "Benin Republic",
    },
    {
        "text": "Ayra Starr was signed to which record label before her debut EP was released?",
        "options": [
            "Chocolate City",
            "Mavin Records",
            "YBNL Nation",
        ],
        "answer": "Mavin Records",
    },
    {
        "text": "In a 2022 interview, Ayra Starr stated that which of these artists is one of her biggest influences?",
        "options": [
            "Rihanna",
            "Beyoncé",
            "Tiwa Savage",
        ],
        "answer": "Rihanna",
    },
    {
        "text": "Which song by The Weeknd features the lyrics, \"When I'm faded, I forget, forget what you mean to me\"?",
        "options": [
            "Coming Down",
            "The Hills",
            "Call Out My Name",
        ],
        "answer": "Coming Down",
    },
    {
        "text": "In what year did The Weeknd win his first Grammy Award?",
        "options": [
            "2015",
            "2016",
            "2017",
        ],
        "answer": "2015",
    },
    {
        "text": "The Weeknd was born in which Canadian city?",
        "options": [
            "Toronto",
            "Montreal",
            "Vancouver",
        ],
        "answer": "Toronto",
    },
    {
        "text": "What is The Weeknd's real first name?",
        "options": [
            "Abel",
            "Allen",
            "Khalid",
        ],
        "answer": "Abel",
    },
    {
        "text": "In a 2021 interview, The Weeknd stated that which film greatly influenced his music video for \"Blinding Lights\"?",
        "options": [
            "Uncut Gems",
            "Drive",
            "Joker",
        ],
        "answer": "Uncut Gems",
    },
    {
        "text": "Which Central Cee song features the lyrics, \"I grew up in Streatham, teachers was givin' man tests\"?",
        "options": [
            "Streatham",
            "Not a Central Cee song",
            "Obsessed With You",
        ],
        "answer": "Not a Central Cee song",
    },
    {
        "text": "In which year did Central Cee release his debut mixtape, *Wild West*?",
        "options": [
            "2020",
            "2021",
            "2022",
        ],
        "answer": "2021",
    },
    {
        "text": "Central Cee’s heritage includes which of the following nationalities?",
        "options": [
            "Guyanese",
            "Jamaican",
            "Ghanaian",
        ],
        "answer": "Guyanese",
    },
    {
        "text": "What is Central Cee's real first name?",
        "options": [
            "Oakley",
            "Curtis",
            "Jason",
        ],
        "answer": "Oakley",
    },
    {
        "text": "",
        "options": [
            "Reggae",
            "Grime",
            "House",
        ],
        "answer": "Grime",
    },
    {
        "text": "In what year did Buju release his first major hit, \"Lenu\"?",
        "options": [
            "2019",
            "2020",
            "2021",
        ],
        "answer": "2019",
    },
    {
        "text": "Before adopting the name Buju, what was the original meaning of his stage name BNXN?",
        "options": [
            "Beyond Noise Zenith Nation",
            "Big Name Xtra Nice",
            "Benson",
        ],
        "answer": "Benson",
    },
    {
        "text": "Which Nigerian state is Buju originally from?",
        "options": [
            "Lagos",
            "Akwa Ibom",
            "Edo",
        ],
        "answer": "Akwa Ibom",
    },
    {
        "text": "In a 2022 interview, Buju stated that what motivates him most in creating music?",
        "options": [
            "Fame and recognition",
            "A desire to express his emotions",
            "Competing with other artists",
        ],
        "answer": "A desire to express his emotions",
    },
    {
        "text": "Which of these artists hasn’t been featured by Ckay?",
        "options": [
            "Blaqbonez",
            "Ayra Starr",
            "Teni",
        ],
        "answer": "Teni",
    },
    {
        "text": "In what year did CKay release the original version of his global hit \"Love Nwantiti\"?",
        "options": [
            "2019",
            "2020",
            "2021",
        ],
        "answer": "2019",
    },
    {
        "text": "CKay was born in which Nigerian state?",
        "options": [
            "Lagos State",
            "Kaduna State",
            "Anambra State",
        ],
        "answer": "Kaduna State",
    },
    {
        "text": "Before his solo career took off, CKay was signed to which record label?",
        "options": [
            "Chocolate City",
            "Mavin Records",
            "YBNL Nation",
        ],
        "answer": "Chocolate City",
    },
    {
        "text": "In an interview, CKay revealed that which of these musical genres has the most significant influence on his sound?",
        "options": [
            "Highlife",
            "Afrobeat",
            "Dancehall",
        ],
        "answer": "Afrobeat",
    },
    {
        "text": "Which Jorja Smith song includes the lyrics, \"You were the topic of my lunch times\"?",
        "options": [
            "Blue Lights",
            "Teenage Fantasy",
            "On My Mind",
        ],
        "answer": "Teenage Fantasy",
    },
    {
        "text": "In what year did Jorja Smith release her debut album, *Lost & Found*?",
        "options": [
            "2017",
            "2018",
            "2019",
        ],
        "answer": "2018",
    },
    {
        "text": "Jorja Smith was born in which English town?",
        "options": [
            "Walsall",
            "Birmingham",
            "Manchester",
        ],
        "answer": "Walsall",
    },
    {
        "text": "Jorja Smith collaborated with which American rapper on the song \"Get It Together\"?",
        "options": [
            "Kendrick Lamar",
            "Drake",
            "J. Cole",
        ],
        "answer": "Drake",
    },
    {
        "text": "In an interview, Jorja Smith mentioned that which of these artists had a significant impact on her vocal style?",
        "options": [
            "Erykah Badu",
            "Amy Winehouse",
            "Lauryn Hill",
        ],
        "answer": "Amy Winehouse",
    },
    {
        "text": "In what year did Teni win the Headies Award for Best New Artist?",
        "options": [
            "2018",
            "2019",
            "2020",
        ],
        "answer": "2018",
    },
    {
        "text": "Teni was born in which Nigerian state?",
        "options": [
            "Lagos State",
            "Ondo State",
            "Ogun State",
        ],
        "answer": "Ondo State",
    },
    {
        "text": "Teni is the younger sister of which popular Nigerian singer?",
        "options": [
            "Niniola",
            "Simi",
            "Tiwa Savage",
        ],
        "answer": "Niniola",
    },
    {
        "text": "In a 2019 interview, Teni revealed that she was inspired to pursue music after listening to which legendary musician?",
        "options": [
            "King Sunny Ade",
            "Ebenezer Obey",
            "Fela Kuti",
        ],
        "answer": "Ebenezer Obey",
    },
    {
        "text": "Which Fireboy DML song features the lyrics, \"Carry me dey go, carry overload\"?",
        "options": [
            "Tattoo",
            "Vibration",
            "Need You",
        ],
        "answer": "Vibration",
    },
    {
        "text": "In what year did Fireboy DML release his debut album, *Laughter, Tears & Goosebumps*?",
        "options": [
            "2018",
            "2019",
            "2020",
        ],
        "answer": "2019",
    },
    {
        "text": "Fireboy DML hails from which Nigerian state?",
        "options": [
            "Lagos State",
            "Ogun State",
            "Ondo State",
        ],
        "answer": "Ogun State",
    },
    {
        "text": "Before signing with YBNL Nation, Fireboy DML was studying which academic discipline?",
        "options": [
            "Law",
            "Medicine",
            "English Language",
        ],
        "answer": "English Language",
    },
    {
        "text": "In a 2021 interview, Fireboy DML cited which of these artists as a major influence on his music style?",
        "options": [
            "Wande Coal",
            "2Baba",
            "Wizkid",
        ],
        "answer": "Wande Coal",
    },
    {
        "text": "Which J Hus song includes the lyrics, \"I don't wanna make friends, I don't wanna break the ice\"?",
        "options": [
            "Did You See",
            "Deeper than rap",
            "Bouff Daddy",
        ],
        "answer": "Deeper than rap",
    },
    {
        "text": "In what year did J Hus release his debut studio album, *Common Sense*?",
        "options": [
            "2016",
            "2017",
            "2018",
        ],
        "answer": "2017",
    },
    {
        "text": "J Hus was born in which London borough?",
        "options": [
            "Hackney",
            "Newham",
            "Southwark",
        ],
        "answer": "Newham",
    },
    {
        "text": "J Hus has cited which of these genres as a major influence on his music style?",
        "options": [
            "Reggae",
            "Afrobeats",
            "Grime",
        ],
        "answer": "Afrobeats",
    },
    {
        "text": "In a 2020 interview, J Hus mentioned that his album *Big Conspiracy* was heavily influenced by which of these topics?",
        "options": [
            "Love and Relationships",
            "Politics and Social Issues",
            "Spirituality and Faith",
        ],
        "answer": "Politics and Social Issues",
    },
    {
        "text": "In what year did Joeboy release his debut EP, *Love & Light*?",
        "options": [
            "2018",
            "2019",
            "2020",
        ],
        "answer": "2019",
    },
    {
        "text": "Joeboy was born in which Nigerian state?",
        "options": [
            "Lagos State",
            "Ogun State",
            "Oyo State",
        ],
        "answer": "Lagos State",
    },
    {
        "text": "Joeboy was discovered by which popular Nigerian artist?",
        "options": [
            "Burna Boy",
            "Mr Eazi",
            "Wizkid",
        ],
        "answer": "Mr Eazi",
    },
    {
        "text": "In a 2020 interview, Joeboy mentioned that which of these genres played a significant role in shaping his sound?",
        "options": [
            "Highlife",
            "Afrobeats",
            "Afropop",
        ],
        "answer": "Afropop",
    },
    {
        "text": "Which Chris Brown song includes the lyrics, \"I get what you get in ten years, in two days\"?",
        "options": [
            "Look at me now",
            "Loyal",
            "Say Goodbye",
        ],
        "answer": "Look at me now",
    },
    {
        "text": "In what year did Chris Brown release his debut single, \"Run It!\"?",
        "options": [
            "2004",
            "2005",
            "2006",
        ],
        "answer": "2005",
    },
    {
        "text": "Chris Brown was born in which U.S. state?",
        "options": [
            "Virginia",
            "Georgia",
            "North Carolina",
        ],
        "answer": "Virginia",
    },
    {
        "text": "Chris Brown won his first Grammy Award in which category?",
        "options": [
            "Best New Artist",
            "Best R&B Album",
            "Best Male R&B Vocal Performance",
        ],
        "answer": "Best R&B Album",
    },
    {
        "text": "In a 2017 interview, Chris Brown revealed which legendary artist had the most significant impact on his career and style?",
        "options": [
            "Michael Jackson",
            "Usher",
            "Prince",
        ],
        "answer": "Michael Jackson",
    },
    {
        "text": "Which Mohbad song features the lyrics, \"Music no need permission to enter your spirit\"?",
        "options": [
            "Egwu",
            "Ponmo Sweet",
            "Feel Good",
        ],
        "answer": "Egwu",
    },
    {
        "text": "In what year did Mohbad release his debut EP, Light?",
        "options": [
            "2020",
            "2019",
            "2021",
        ],
        "answer": "2020",
    },
    {
        "text": "What nickname did Mohbad give himself that was a jab at Naira Marley?",
        "options": [
            "Finnest",
            "Omoba",
            "Imole",
        ],
        "answer": "Imole",
    },
    {
        "text": "Mohbad was formally signed to which Nigerian record label?",
        "options": [
            "YBNL Nation",
            "Mavin Records",
            "Marlian Music",
        ],
        "answer": "Marlian Music",
    },
    {
        "text": "Why did people suspect Naira Marley's gang in the death of Mohbad?",
        "options": [
            "Refused to sign new contract",
            "Legal dispute over unpaid royalties",
            "Refused to record new music",
        ],
        "answer": "Legal dispute over unpaid royalties",
    },
    {
        "text": "What song did Travis say “Bout to sign this deal and throw it all away”?",
        "options": [
            "Stargazing",
            "Stargazing",
            "Upper Echelon",
        ],
        "answer": "Stargazing",
    },
    {
        "text": "What song did Kanye West hear that made him call Travis the next big thing?",
        "options": [
            "Owl pharaoh",
            "Rodeo",
            "Astroworld",
        ],
        "answer": "Owl pharaoh",
    },
    {
        "text": "In what year did Travis Scott release his debut studio album, Rodeo?",
        "options": [
            "2015",
            "2016",
            "2017",
        ],
        "answer": "2015",
    },
    {
        "text": "During the Astroworld investigation, it was revealed that Travis Scott had previously faced criticism for what behaviors at his concerts?",
        "options": [
            "Encouraging drug use",
            "Inciting the crowd to act recklessly",
            "Performing with unsafe stage setups",
        ],
        "answer": "Inciting the crowd to act recklessly",
    },
    {
        "text": "In various interviews, Travis Scott has openly discussed his use of which drug, frequently referencing it in his music?",
        "options": [
            "Lean",
            "Cocaine",
            "Ecstasy",
        ],
        "answer": "Lean",
    },
    {
        "text": "In 2019, Summer Walker made headlines for abruptly ending her “First and Last Tour” due to what reason?",
        "options": [
            "Social anxiety",
            "Health issues",
            "Creative differences",
        ],
        "answer": "Social anxiety",
    },
    {
        "text": "Summer Walker faced backlash after she posted about which controversial topic on her social media in 2020?",
        "options": [
            "Anti-vaccination views",
            "Political opinions",
            "Veganism",
        ],
        "answer": "Anti-vaccination views",
    },
    {
        "text": "In a 2021 interview, Summer Walker was criticized for her comments regarding what parenting practice?",
        "options": [
            "Feeding her child a diet based primarily on raw foods",
            "Homeschooling",
            "Anti-vaccine stance",
        ],
        "answer": "Feeding her child a diet based primarily on raw foods",
    },
    {
        "text": "Summer Walker has frequently been criticized for her unconventional approach to which aspect of her live performances?",
        "options": [
            "Lack of stage presence",
            "Refusing to perform hits",
            "Overly elaborate staging",
        ],
        "answer": "Lack of stage presence",
    },
    {
        "text": "In 2020, Summer Walker found herself in a controversy for publicly criticizing which prominent figure or entity?",
        "options": [
            "The music industry",
            "A fellow artist",
            "A government official",
        ],
        "answer": "The music industry",
    },
]


def create_question_data(apps, schema_editor):
    Question: QuestionModel = apps.get_model("quizzes", "Question")
    Option: OptionModel = apps.get_model("quizzes", "Option")

    for data in QUESTION_DATA:
        question = Question.objects.create(text=data.get("text"))
        for option in data.get("options"):
            is_correct = option == data.get("answer")
            Option.objects.create(
                text=option,
                question=question,
                is_correct=is_correct,
            )



class Migration(migrations.Migration):
    dependencies = [
        ("quizzes", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_question_data),
    ]
