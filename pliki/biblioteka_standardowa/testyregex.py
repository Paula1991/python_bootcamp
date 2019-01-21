#[^a] wszystko poza a
#[0-9]+ - wystapienia po sobie
# [a-z] wszystko w przedziale
# . wszystko
# \s wszystkie biale znaki
# \d liczby
# \D wszystko poza liczbami
#[t]{2,3} wystapienia t , 2-3 to po sobie
#[A-Z][a-z]* -mix liter
#api/costam* wywowla wszystko od tego momentu do konca
import re

regex = re.compile("\d+")
wynik = regex.findall("asgdagagasdferf112st2220e220stsgatsrfesersrsrtest")


print(wynik1)
print(wynik2)
print(wynik3)


with open("info1.txt","w", encoding='utf-8') as f:
    tekst file.read()

kodpocztowy=re.compile("\d{2}-\d{3}")
wynik1=kodpocztowy.findall("12-12323242-2312-123")
adresemail=re.compile("\w+@\w+.\w{3}")
wynik2=adresemail.findall("email@gmail.comabc@o2.com")

data=re.compile("\d{2}\s\[A-Z][a-z]{3}\s\d{4}")
wynik3=data.findall("12 Jan 195411 Feb 2011")
