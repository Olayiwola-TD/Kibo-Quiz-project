import random
import time
import sys
from string import ascii_lowercase
print("\n                                    ..................................")
print("                                    :⭐ HEADIES AWARD WINNERS QUIZ ⭐:")
print("                                    ..................................\n")
name = input("What is your name? ")
name = name.capitalize()
# Introduce a delay of 1 seconds
time.sleep(1)
while True:
    guest = input(f"Hey {name}, did you attend the Headies Award Event?(yes/no) ").lower()
    # Introduce a delay of 1 seconds
    time.sleep(1)
    if guest == "yes":
        print("Okay great, let's Refresh your memory on the list of winners.")
        break
    elif guest == "no":
        print("We're sorry to hear that you missed the Headies award event.")
        while True:
            missed_event = input("\nWill you still like to participate in the Award Winners Quiz?(yes/no) ").lower()
            # Introduce a delay of 3 seconds
            time.sleep(1)
            if missed_event == "yes":
                print("Okay great, Let's go!")
                break
            elif missed_event == "no":
                print("Goodbye!, thanks for your time.")
                sys.exit()
            else:
                print("Invalid input.  Please enter 'yes' or 'no'.")
        break
    else:
        print("Invalid input.  Please enter 'yes' or 'no'.")

print(f"\nWelcome to Headies award winners quiz, {name}. Let's test your knowledge on the recent Headies award event.")
while text := input("Enter the word 'start' to begin today quiz: ").lower() != "start":
    print(f"You have enter an invalid input, please try again.\n")
# number of questions in the quiz
NUM_QUESTION_PER_QUIZ = 28

# These are the question and answers of the quiz
# These quiz is about 2023 Headies award winners

# Here is the question and answer of the quiz
QUESTIONS = {
    "Who won the BEST RECORDING OF THE YEAR": [
         "“Soweto” – Victony and Tempoe",
         "“Alone” – Burna Boy",
         "“I’m a Mess” – Omah Lay",
         "“Ku lo sa” –  Oxlade",
         "“Stand Strong” – Davido",
         "“No Woman, No Cry” – Tems"
         ],
    "Who won the PRODUCER OF THE YEAR ": [
         "Rexxie – “Abracadabra”",
         "Magicstickz – “Sungba Remix”",
         "Pheelz – “Electricity”",
         "Andrevibez & London – “Calm Down”",
         "Tempoe – “Soweto”",
         "Kel-P – “Kpe Paso”",
         ],
    "Who won the SONGWRITER OF THE YEAR": [
        "“Loyal” – Simi",
        "“I’m a Mess” – Omah Lay",
        "“Lift Me Up” – Tems",
        "“Alone” – Burna Boy",
        "“In My Mind” – BNXN",
        "“Earth Song” – Wizard Chan"
    ],
    "Who won the Best R&B Single  ": [
        "“For My Hand” – Burna Boy ft ED Sheeran",
        "“Just 4 u” – Dami Oniru",
        "“Mmadu” – CKay",
        "“Red Wine” – Preye",
        "“Hard to Find” – Chike ft Flavour",
        "“Loyal” – Simi ft Fave"
    ],
    "Who won the Best Rap Single": [
        "“Declan Rice” – Odumodublvck",
        ''"“Hustle” – Reminisce ft BNXN",
        "“Back in Uni” – Blaq Bonez",
        "“Bando Diaries” – Psycho YP ft Odumodublvck",
        "“My Bro” – Jeriq the Hussla ft Phyno",
    ],
    "Who won the Best Vocal Performance (Female) ": [
        "“In Between” – Waje",
        "“Loyal” – Simi",
        "“Memories” – Niniola",
        "“Adua Remix” – Liya",
        "“Red Wine” – Preye Itams",
        "“Just 4 U” – Dami Oniru",
    ],
    "Who won the Best Vocal Performance (Male) ": [
        "“Kpe Paso” Wande Coal",
        "“My Only Baby” Ric Hassani",
        "“Love Don’t Cost a Dime” Magixx",
        "“Reckless” Praiz",
        "“Red Wine” – Preye Itams",
    ],
    "Who won the Best Alternative Song ": [
        "“Earth Song” – Wizard Chan",
        "“Final Champion” – Cruel Santino",
        "“The Traveller” – Basketmouth and The Cavemen",
        "“In a Loop” By BOJ – Mellissa",
        "“Game Changer” – Flavour",
        "“Tinko Tinko” – Obongjayar",
    ],
    "Who won the Best Music Video ": [
        "“Calm Down (Remix)” – Director K",
        "“Back in Uni” –Blaqbonez Perliks",
        "“Spell (Remix)” –  Director Pink",
        "“Common Person” – Director K",
        "“Bandana” by TG Omori",
    ],
    "Who won the Best Collaboration ": [
        "Spyro ft. Tiwa Savage – “Who’s Your Guy Remix”",
        "Bnxn ft. Kizz Daniel & Seyi Vibes – “Gwagwalada”",
        "Pheelz ft Bnxn – “Finesse”",
        "Pheelz ft Davido– “Electricity”",
        "Wande Coal ft. Olamide– “Kpe Paso”",
    ],
    "Who won the Best Street-Hop Artiste ": [
        "Seyi Vibez – “Chance (Na Ham)”",
        "Rexxie Ft. Naira Marley & Skiibii – “Abracadabra”",
        "Asake – “Joha”",
        "Zlatan Ft. Young Jonn – “Astalavista”",
        "Poco Lee & Hotkid – “Otilo”",
        "Mohbad – “Peace”",
    ],
    "Who won the Afro-beats Single Of The Year ": [
        "“Last Last” – Burna Boy",
        "“Rush” – Ayra Starr",
        "“Buga” – Kizz Daniel & Tekno",
        "“Finesse” – Pheelz ft Bnxn",
        "“Who’s Your Guy?” – Spyro",
        "“Asiwaju” – Ruger",
    ],
    "Who won the Headies’ Viewers’ Choice ": [
        "Victony & Tempoe – “Soweto”",
        "Ruger – “Asiwaju”",
        "Fireboy Dml & Asake – “Bandana”",
        "Ayra Star – “Rush”",
        "Asake – “Terminator”",
        "Crayon – “Ijo (Laba Laba)”",
        "Oxlade – “Ku Lo Sa”",
        "Kizz Daniel & Tekno – “Buga”",
        "Pheelz & Davido – “Electricity”",
    ],
    "Who won the Best West African Artiste Of The Year ": [
        "Black Sherif (Ghana)",
        "Gyakie (Ghana)",
        "The Therapist (Liberia)",
        "Camidoh (Ghana)",
    ],
    "Who won the Best East African Artiste Of The Year ": [
        "Diamond Platinumz",
        "Zuchu",
        "Rayvanny",
        "Eddy Kenzo",
        "Hewan Gebreworld",
    ],
    "Who won the Best North African Artiste Of The Year ": [
        "El Grande Toto – Morocco",
        "Marwa Loud – Morocco",
        "Wegz – Egypt",
        "Soolking – Algeria",
    ],
    "Who won the Best Southern African Artiste Of The Year ": [
        "Focalistic – South Africa",
        "Aka (South Africa)",
        "Nasty C – South Africa",
        "Costa Titch – South Africa",
        "Uncle Waffles – South Africa",
        "Dj Tarico – Mozambique",
    ],
    "Who won the Best Central African Artiste Of The Year ": [
        "Libianca – Cameroon",
        "Fally Ipupa – Democratic Republic Of Congo",
        "Gaz Mawete – Democratic Republic Of Congo",
        "Matias Damasio – Angola",
        "Emma’a – Gabon",
    ],
    "Who won the Best R&B Album ": [
        "The Brother’s Keeper – Chike",
        "Home – Johnny Drille",
        "Reckless – Praiz",
        "Waje 2.0 – Waje",
        "Matter Of Time – Dami Oniru",
        "To Be Honest (Tbh) – Simi",
    ],
    "Who won the Best Alternative Album": [
        "Gbagada Express – Boj",
        "Horoscopes – Basketmouth",
        "Some Nights I Dream Of Doors – Obongjayar",
        "Subaru Boys: Final Heaven – Cruel Santino",
        "Heart Of The Heavenly Undeniable – Somadina",
        "Native World – Native Sound System",
    ],
    "Who won the Best Rap Album ": [
        "Young Preacher – Blaqbonez",
        "Fly Talk Only – Payper Corleone",
        "Palmwine Music Vol 3 – Show Dem Camp",
        "Ypszn3 – Psychoyp",
        "Teslim: The Energy Still Lives In Me – Vector",
        "Billion Dollar Dream – Jeriq",
    ],
    "Who won the Album Of The Year ": [
        "Mr Money With The Vibe – Asake",
        "Love, Damini – Burna Boy",
        "Rave And Roses – Rema",
        "Boy Alone – Omah Lay",
        "Outlaw – Victony",
        "Timeless – Davido",
    ],
    "Who won the Song Of The Year ": [
        "Love, Damini – Burna Boy",
        "Mr Money With The Vibe – Asake",
        "Rave And Roses – Rema",
        "Boy Alone – Omah Lay",
        "Outlaw – Victony",
        "Timeless – Davido",
    ],
    "Who won the Best Female Artiste ": [
        "Ayra Starr",
        "Tems",
        "Simi",
        "Tiwa Savage",
    ],
    "Who won the Best Male Artiste ": [
        "Rema",
        "Asake",
        "Kizz Daniel",
        "Ruger",
        "Omah Lay",
        "Burna Boy",
    ],
    "Who won the Next Rated Artiste ": [
        "Asake",
        "Young Jonn",
        "Seyi Vibez",
        "Victony",
        "Spyro",
    ],
    "Who won the Rookie of the Year ": [
        "Odumodu Blvck",
        "Bloody Civilian",
        "Bayyani",
        "Guchi",
        "Eltee Skillz",
        "Khaid",
    ],
    "Who won the African Artiste Of The Year ": [
        "Rema (Nigeria)",
        "Burna Boy (Nigeria)",
        "Marwa Loud (Morocco)",
        "Black Sherif (Ghana)",
        "Diamond Platnumz (Tanzania)",
    ],
    "Who won the Lyricist On The Roll ": [
        "Payper Corleone – “Fly Talk Only”",
        "Ladipoe – “Clowns”",
        "Vector – “Clowns”",
        "Alpha Ojini – “Vigilante Bop”",
        "A-Q – “Family First”",
        "Tec (Sdc) – “Live Life”",
    ],
    "Who was the International Artiste Recognition ": [
        "Sean ‘love’ Combs",
        "Youssou N’dour",
        "Burna Boy",
        "Ayra Starr",
        "Omah Lay",
    ],
    "Who was the Hall Of Fame ": [
        "Youssou N’dour",
        "Burna Boy",
        "Ayra Starr",
        "Rema",
    ],
    "Who won the Best Inspirational Single ": [
        "“Eze Ebube” – Neon Adejo",
        "“Stand Strong” – Davido Ft Sunday Service Choir",
        "“Jireh (My Provider)” – Limoblaze, Lecrae & Happi Music",
        "“This Year” – Victor Thompson & Ehis ‘d’ Greatest",
        "“Tobechukwu” – Nathaniel Bassey And Mercy Chinwo",
        "“I Get Backing” – Victoria Orenze",
    ],
    "Who won the Digital Artiste Of The Year ": [
        "Rema",
        "Burna Boy",
        "Ayra Starr",
        "Omah Lay",
        "Kizz Daniel",
        "Asake",
    ],
    "Who won the International Artist Of The Year ": [
        "Selena Gomez",
        "Drake",
        "Future",
        "Don Toliver",
        "Ed Sheeran",
    ],
    "Who was the Special Recognition Act ": [
        "Sound Sultan",
        "Omah Lay",
        "Future",
        "Selena Gomez",
        "Kizz Daniel",
    ]
}

# RANDOMIZING THE QUESTIONS AND ALTERNATIVES, AND HOW THEY ARE ASKED/SHOW UP
num_question = min(NUM_QUESTION_PER_QUIZ, len(QUESTIONS))
questions = random.sample(list(QUESTIONS.items()), k=num_question)
num_correct = 0

# Introduce a delay of 3 seconds
time.sleep(2)
# Writing the loop code to get the question and alternatives answer
for num, (question, alternatives) in enumerate(questions, start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    corrected_answer = alternatives[0]
    labeled_alternatives = dict(zip(ascii_lowercase, random.sample(alternatives, k=len(alternatives))))
    for label, alternative in labeled_alternatives.items():
        print(f"({label}) {alternative}")
    # Introduce a delay of 0.4 seconds
    time.sleep(0.4)
    while (answer_label := input("\nChoose your answer? ")) not in labeled_alternatives:
        # Introduce a delay of 0.4 seconds
        time.sleep(0.4)
        print(f"Please answer one of {',' .join(labeled_alternatives)}")
# conditional statement to check if the answer picked by user is the same as the correct answer
    # Introduce a delay of 0.4 seconds
    time.sleep(0.4)
    answer = labeled_alternatives.get(answer_label)
    if answer == corrected_answer:
        num_correct += 1
        print("⭐ Correct! ⭐")
    else:
        print(f"The answer is {corrected_answer!r}, not {answer!r}.")
    # Introduce a delay of 1.8 seconds
    time.sleep(1.8)
# to show the user the score and their percentage
print(f"\nYou get {num_correct} questions correctly out of {num} questions.")
percentage = int(num_correct) * 100
percentage = percentage/len(questions)
print(f"You get {percentage: .2f}% of the questions correctly.")
