import re

mytext = "heloo456 , ..FFFFama3456.asdf a;lFFFFsdkfjadkfj"\
    "helloll heloo 79mama"\
    "hello "
"""
\d = any digit 0-9
\D = any non digit
\w = any alphabet symbol [a-z , A-Z]
\W = any non Alphabet symbol
\s = breakspase
\S = non breakspace

[0-9] {3} від нудя до 0 по три цифри
[A-z][a-z]+
\w+\.\w+
"""




textlookfor = r"\w+\.\w+" # шукаємо якндекс
allresults = re.findall(textlookfor, mytext)
#всі результати рівняються знайти всі в тексіті

print(allresults)
