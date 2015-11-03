# japaneseLoremIpsum.py

# Creates random chunks of Japanese text to be used as filler.
# NOTE:  Japanese characters do not work in all environments.

# Also note that the rules for Japanese are much more complicated than
# English where sentences start with capitalization, have spaces between
# words, and end with periods.
# Japanese has 3 alphabets to make words from, sometimes you mix one of
# the alphabets in for grammar and word modifications, you can't start
# a sentence with certain characters, and you rarely end a sentence with
# others.

# This is not precise, but if you give it a quick glance this could be
# mistaken for the real deal.


import random


# Creates a string using specified characters for a specified length.
# Basic rules are applied:  kanas cannot begin with "ん" or small
# characters (ゃゅょーっ), and strings do not end with small characters.

# Logic for kanakana and hiragana were left separate, even though they
# are roughly the same for now (may refine slight differences later)

# For characters, choose one of the following:
# 1 = katakana, 2 = hiragana, 3 = kanji

def randomJapaneseString(characters = 2, length = 5):
    characters = str(characters)
    charString = ""
    # Include or don't include katakana, hiragana, kanji
    katakana = hiragana = kanji = ""
    # 1 is katakana
    if "1" in characters:
        # ン starts at [69]
        katakana = "" +\
        "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワ" +\
        "ガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポンャュョーッァィェォ"
        for i in range(length):
            # First character: No ン or ャュョーッァィェォ
            if i == 0:
                charString += random.SystemRandom().\
                choice(katakana[:69])
            # Last character: No ャュョーッァィェォ
            elif i == (length - 1):
                charString += random.SystemRandom().\
                choice(katakana[:70])
            # Middle characters:  Anything goes, extra chance for
            # ャュョーッァィェォ, extra chance again for ーッ
            else:
                charString += random.SystemRandom().\
                choice(katakana[:] + katakana[70:] + katakana[73:75])
        return charString
    # 2 is hiragana
    elif "2" in characters:
        # ん starts at [69]
        hiragana = "" +\
        "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわ"+\
        "がぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽんゃゅょーっ"
        for i in range(length):
            # First character: No ん or ゃゅょーっ
            if i == 0:
                charString += random.SystemRandom().\
                choice(hiragana[:69])
            # Last character: No ゃゅょーっ
            elif i == (length - 1):
                charString += random.SystemRandom().\
                choice(hiragana[:70])
            # Middle characters:  Anything goes, extra chance for
            # ゃゅょーっ, extra chance again for ーっ
            else:
                charString += random.SystemRandom().\
                choice(hiragana[:] + hiragana[70:] + hiragana[73:])
        return charString
    # 3 is kanji, we took 500 of the most common newspaper kanji
    elif "3" in characters:
        kanji = "" +\
        "連労六論和話量領力例要来落利理率立流両料葉容様用与融予有由輸優約木目" +\
        "問門夜野役名命明面味民務無毎末万補報放方法訪望防北本保文聞平米別変辺" +\
        "負武部副復福物分不付夫府八発判半反番比被費非備美必百票表評病品白売南" +\
        "難二日入任認年念能脳農派配頭働動同導道得特独内土党島投東当答統藤度渡" +\
        "都張朝町調長直追通低定提的展店転点伝田電注段男談知地置着中断宅沢達担" +\
        "団代台大第題退待態体対想早争相総送増蔵造側足族続村多打組訴席石切設説" +\
        "先千川戦線選鮮前然全税政整正生声製西成世制勢性水数常情条状職食信審心" +\
        "新深申真神親身進人場初所書助女勝商小少松消渉証象賞上乗準出術述衆集住" +\
        "十重首受収州終手種守取主若社者車写自式識七失質実示視試資事字持時次治" +\
        "思指支施止死氏私四始姿子市三参山産算残仕使察策裁際在財作昨差査再最歳" +\
        "済行高合告国今佐校構港考公口向好工広後語護交五午現言限個呼経計警撃決" +\
        "結月件建検権研県見験元原減形景近金銀九区空軍係型教況業局極強境挙京供" +\
        "共協去気規記起技疑義議宮急求球究期機基間関韓含企観株官幹感環監改海界" +\
        "開外害各格核確閣革学楽額割活運営影映英衛円援演応横欧岡音下化何価加可" +\
        "家果課過画会解回安案以位委意移違医井域育一員引院"
        for i in range(length):
            # Plainly makes a string of kanji
            charString += random.SystemRandom().choice(kanji)
        return charString
    # Graceful error if 1, 2, or 3 was not entered
    else:
        print("Error: randomJapaneseString() expects 123." +\
            "  Input not found.")
        return



# Creates sentences using randomJapaneseString().
# Option for min/max katakana, hiragana, and kanji length.
# Sentence can't start or end with particles.
# Particles (and 、) will randomly be entered 50% of the time after a
# word.
# Sentence ends with random hiragana.

def randomJapaneseSentence(
        kataMin = 3, kataMax = 6, hiraMin = 4, hiraMax = 7,
        kanjiMin = 2, kanjiMax = 5, minSentence = 5, maxSentence = 20):
    words = []
    sentence = ""
    # A weighted list of particles:
    particles = "はははががにのへををやでと、、、、、"
    sentenceLength = random.randint(minSentence, maxSentence) - 1
    # Dice roll to see if we use a katakana, hiragana, or kanji word.
    for i in range(sentenceLength):
        character = random.randint(1, 10)
        if character == 1:
            words.append(randomJapaneseString(
                1, random.randint(kataMin, kataMax)))
        elif 2 <= character <= 5:
            words.append(randomJapaneseString(
                2, random.randint(hiraMin, hiraMax)))
        else:
            words.append(randomJapaneseString(
                3, random.randint(kanjiMin, kanjiMax)))
    # Puts sentence together with a 1 in 2 chance of a particle between
    # words.
    for i in words:
        sentence += i
        partChance = random.randint(1, 2)
        if partChance == 1:
            sentence += random.SystemRandom().choice(particles)
    # Ends sentence with a random 
    sentence += randomJapaneseString(
        2, random.randint(hiraMin, hiraMax)) + "。"
    return sentence


def randomJapaneseParagraph():
    paragraph = ""
    for i in range(random.randint(2,3)):
        paragraph += randomJapaneseSentence()
    return paragraph


# Demonstrate randomString()
print("5 random katakana:")
print(randomJapaneseString(1, 5))
print("")
print("")

print("5 random hiragana:")
print(randomJapaneseString(2, 5))
print("")
print("")

print("5 random kanji:")
print(randomJapaneseString(3, 5))
print("")
print("")

print("Sentence with random Japanese characters:")
print(randomJapaneseSentence())
print("")
print("")

print("Paragraph with random Japanese characters:")
print(randomJapaneseParagraph())
print("")
print("")
