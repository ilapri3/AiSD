numbers = {}
numbers['ноль'],numbers['0'] = 0, 'ноль'
numbers['один'],numbers['1'] = 1, 'один'
numbers['два'], numbers['2'] = 2, 'два'
numbers['три'], numbers['3'] = 3, 'три'
numbers['четыре'], numbers['4'] = 4, 'четыре'
numbers['пять'], numbers['5'] = 5, 'пять'
numbers['шесть'], numbers['6'] = 6, 'шесть'
numbers['семь'], numbers['7'] = 7, 'семь'
numbers['восемь'], numbers['8'] = 8, 'восемь'
numbers['девять'], numbers['9'] = 9, 'девять'
numbers['десять'], numbers['10'] = 10, 'десять'
numbers['одиннадцать'], numbers['11'] = 11, 'одиннадцать'
numbers['двенадцать'], numbers['12'] = 12, 'двенадцать'
numbers['тринадцать'], numbers['13'] = 13, 'тринадцать'
numbers['четырнадцать'], numbers['14'] = 14, 'четырнадцать'
numbers['пятнадцать'], numbers['15'] = 15, 'пятнадцать'
numbers['шестнадцать'], numbers['16'] = 16, 'шестнадцать'
numbers['семнадцать'], numbers['17'] = 17, 'семнадцать'
numbers['восемнадцать'], numbers['18'] = 18, 'восемнадцать'
numbers['девятнадцать'], numbers['19'] = 19, 'девятнадцать'
numbers['двадцать'], numbers['20'] = 20, 'двацать'
numbers['тридцать'], numbers['30'] = 30, 'тридцать'
numbers['сорок'], numbers['40'] = 40, 'сорок'
numbers['пятьдесят'], numbers['50'] = 50, 'пятьдесят'
numbers['шестьдесят'], numbers['60'] = 60, 'шестьдесят'
numbers['семьдесят'], numbers['70'] = 70, 'семьдесят'
numbers['восемьдесят'], numbers['80'] = 80, 'восемьдесят'
numbers['девяносто'], numbers['90'] = 90, 'девяносто'
numbers['сто'], numbers['100'] = 100, 'сто'
numbers['двести'], numbers['200'] = 200, 'двести'
numbers['триста'], numbers['300'] = 300, 'триста'
numbers['четыреста'], numbers['400'] = 400, 'четыреста'
numbers['пятьсот'], numbers['500'] = 500, 'пятьсот'
numbers['шестьсот'], numbers['600'] = 600, 'шестьсот'
numbers['семьсот'], numbers['700'] = 700, 'семьсот'
numbers['восемьсот'], numbers['800'] = 800, 'восемьсот'
numbers['девятьсот'], numbers['900'] = 900, 'девятьсот'

def to_text(x):
    if 0 <= num <= 20:
        return numbers[str(num)]
    elif num > 20 and num%10 == 0:
        return numbers[str(num)]
    elif num%10 != 0 and num > 20 and num < 100:
        return numbers[str((num//10)*10)]+ ' ' + numbers[str(num%10)]
    else:
        return numbers[str((num//100)*100)]+ ' ' + numbers[str((num//10)%10*10)] + ' ' + numbers[str(num%10)]

num = input()

print(to_text(num))