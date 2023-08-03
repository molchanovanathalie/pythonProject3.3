#2. В большой текстовой строке
# подсчитать количество встречаемых слов и вернуть 10
# самых частых. Не учитывать знаки препинания и регистр
# символов. За основу возьмите любую статью из википедии
# или из документации к языку.

import itertools


text =('Ещё в 1912 году стало очевидно, что планы на будущее Э. Хьюитта и С. Морли принципиально не совпадают. Судя по дневнику и переписке, 29-летний учёный вынашивал амбициозный проект раскопок и реставрации руин Чичен-Ицы, и нуждался в серьёзном покровителе в столице. Бюджет этого предприятия он оценивал в 10 000 долларов ежегодно на срок, по крайней мере, десять лет. К тому времени Институт Карнеги, преимущественно разрабатывавший фундаментальную естественнонаучную тематику, был близок к включению археологической тематики в свой план и штатное расписание. Лоббистами кандидатуры Морли выступили Смитсоновский институт и его Национальный музей. Попечительский совет одобрил проект Морли в декабре 1912 года, но встреча с президентом Института Вудвордом[en] прошла крайне неудачно: физик-администратор считал археологов гробокопателями и полагал, что их работу отлично выполняют музеи[25]. 9 мая 1913 года Сильванус Морли подал заявку в правительство Мексики о выделении концессии на раскопки Чичен-Ицы, которая так и осталась без ответа. Летом 1913 года, из-за того, что альтернативные кандидаты так и не появились на заседании правления, Вудворд одобрил назначение Морли куратором археологического направления и научным сотрудником Института. Он должен был получать жалованье 1053 доллара в год, не считая оплаты дорожных расходов (этнограф Риверс получал жалованье в 1500 долларов в год); тогда же произошло знакомство Вэя с инженером Парсонсом[en], который добивался открытия археологического отдела Института Карнеги ещё с 1907 года. Тот разъяснил молодому учёному искусство написания отчётов, которые бы нравились руководству и помогали выделению денег. Морли представил крайне эффектную презентацию и бизнес-план, в котором предусмотрел все мелочи, вплоть до платы индейским подёнщикам[26]. Окончательное решение вопроса о проекте Морли рассматривалось на заседании попечительского совета Института Карнеги 15 января 1914 года. Решение было положительным, но сам проект раскопок был отставлен, так как в Мексике шла революция и неизбежной была интервенция США в эту страну. Это привело к конфликту с Хьюиттом, который прямо задал Морли вопрос, на кого тот работает. В ожидании новостей Морли за собственный счёт поехал в экспедицию в Петен[27]. Экспедиция длилась пять месяцев, затронув Тикаль, Яшчилан, Пьедрас-Неграс и Киригуа. Также Морли на моторной лодке отправился в Британский Гондурас, где поработал в Наранхо с Гербертом Спинденом[en], с которым был давно знаком')
register_text = text.lower()

# текст под нижний регистр
words = register_text.split()
set_words = set(words)

global_dict = {}
for i in set_words:
    quantity = 0
    for j in words:
        if i == j:
            quantity += 1

# создаем общий словарь из сгенерированных коротких словарей
    global_dict[i] =quantity

# сортируем словарь по значению по убыванию
sort_dict = sorted(global_dict.items(), key=lambda x: x[1], reverse=True)
sort_global_dict = dict(sort_dict)

# выводим отсортированный словарь и обрезаем все кроме первых 10 элементов
print(dict(itertools.islice(sort_global_dict.items(), 10)))

