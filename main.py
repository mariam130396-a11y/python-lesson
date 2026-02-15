print( """Ladies and gentlemen, I'm 78 years old and I finally got 15 minutes of fame once in a lifetime
and I guess that this is mine.

People have also told me to make these next few minutes excruciatingly embarrassing
and to take vengeance of my enemies. Neither will happen.

More than 3 years ago I moved to Novo-Novsk, but worked on new Magnetic Storage for last 40.
When I was 8...
""" ) 
from transliterate import translit
print (translit( "Lorem ipsum dolor sit amet", 'hy'))
print (translit ("Lorem ipsum dolor sit amet" , 'el'))
print (translit ( "Lorem ipsum dolor sit amet", 'uk'))

from transliterate import translit
print (translit ("""Ladies and gentlemen, I'm 78 years old and I finally got 15 minutes of fame once in a lifetime
and I guess that this is mine. People have also told me to make these next few minutes
excruciatingly embarrassing and to take vengeance of my enemies. Neither will happen.
More than 3 years ago I moved to Novo-Novsk, but worked on new Magnetic Storage for last 40.
When I was 8...""", 'ru'))

from num2words import num2words

print(num2words(42))
print(num2words(42, to='ordinal'))
print(num2words(42, lang='fr'))

from transliterate import translit

print(translit( """Ladies and gentlemen, I'm 78 years old and I finally got 15 minutes of fame once in a lifetime
and I guess that this is mine.

People have also told me to make these next few minutes excruciatingly embarrassing
and to take vengeance of my enemies. Neither will happen.

More than 3 years ago I moved to Novo-Novsk, but worked on new Magnetic Storage for last 40.
When I was 8...
""", 'ru' )) 
import re
from num2words import num2words

speech = """
Ладиес анд гентлемен, ИЬм 78 ыеарс олд анд И финаллы гот 15 минутес оф фаме онце ин а лифетиме
анд И гуесс тхат тхис ис мине. Пеопле хаве алсо толд ме то маке тхесе неxт феw минутес
еxцруциатинглы ембаррассинг анд то таке венгеанце оф мы енемиес. Неитхер wилл хаппен.
Море тхан 3 ыеарс аго И мовед то Ново-Новск, бут wоркед он неw Магнетиц Стораге фор ласт 40.
Wхен И wас 8...
"""

# найти все числа
numbers = re.findall(r'\d+', speech)

# вывести число и слово
for number in numbers:
    print(number, "-", num2words(int(number)))

import re
from num2words import num2words
from transliterate import translit

speech = """
Ладиес анд гентлемен, ИЬм 78 ыеарс олд анд И финаллы гот 15 минутес
Море тхан 3 ыеарс аго... ласт 40. Wхен И wас 8...
"""

# найти все числа
numbers = re.findall(r'\d+', speech)

# вывести число + слово + кириллица
for number in numbers:
    word_en = num2words(int(number))
    word_ru = translit(word_en, 'ru')
    print(number, "-", word_en, "-", word_ru)


