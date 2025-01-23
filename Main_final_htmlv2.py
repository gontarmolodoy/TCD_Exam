#Импортируем библиотеки для наших игроков
#В этом документе мы не будем использовать загрузку графиков в наше мини-приложение не через png, потому что kaleido работает отвратительно, а с помощью html-файлов
#Это позволит нам сохранить интерактивность графиков, но выводить их мы будем отдельно по кнопке из страницы игрока
import plotly.express as px
import pandas as pd
from tkinter import *
from tkinter.ttk import *
from tkinter import Toplevel, Label, mainloop
from PIL import Image, ImageTk
import requests
import shutil
#в измененной версии мы используем webview для отражения графиков plotly в интерактивной форме в нашем мини-приложении
import webview

#В первой части мы будем создавать в plotly графики для наших визуализаций для нашего приложения
#Графики делятся на две части: показывающие абсолютные величины и показывающие относительные величины в периоде из 5 сезонов
#Строим графики для наших игроков, они будут точечными


#Артемий Панарин
data = {
    'Сезон': ['2020-2021', '2021-2022', '2022-2023', '2023-2024', '2024-2025'],
    'Голы': [17, 22, 29, 49, 17],
    'Ассисты': [41, 74, 63, 71, 45]
}
# Преобразуем данные в DataFrame
df = pd.DataFrame(data)

# Строим график с двумя линиями для голов и ассистов
fig_panarin = px.line(df, x='Сезон', y=['Голы', 'Ассисты'], title='Голы и Ассисты за последние 5 сезонов',
              labels={"value": 'Показатель в абсолютных величинах',
              "variable":"Показатели игрока"}
              )
panarin_full = fig_panarin.to_html('Panarintotal.html', full_html=False)

#По очкам в среднем
data1 = {
    'Сезон': ['2020-2021', '2021-2022', '2022-2023', '2023-2024', '2024-2025'],
    'Среднее количество очков за игру': [1.38, 1.28, 1.12, 1.46, 1.01],
}

# Преобразуем данные в DataFrame
df1 = pd.DataFrame(data1)

# Строим график для среднего количества очков за игру
fig_panarinp = px.line(df1, x='Сезон', y='Среднее количество очков за игру', title='Среднее количество очков за игру за последние 5 сезонов')
panarin_avg = fig_panarinp.to_html('Panarinaverage.html', full_html=False)

#Адам Фокс (защитник, второй по результативности в текущем сезоне)
data = {
    'Сезон': ['2020-2021', '2021-2022', '2022-2023', '2023-2024', '2024-2025'],
    'Голы': [5, 11, 12, 17, 2],
    'Ассисты': [42, 63, 60, 56, 31]
}

# Преобразуем данные в DataFrame
df = pd.DataFrame(data)

# Строим график с двумя линиями для голов и ассистов
fig_fox = px.line(df, x='Сезон', y=['Голы', 'Ассисты'], title='Голы и Ассисты за последние 5 сезонов', labels={"value": 'Показатель в абсолютных величинах',
              "variable":"Показатели игрока"})
fig_fox.write_html("Foxtotal.html")

#График для очков в среднем
data = {
    'Сезон': ['2020-2021', '2021-2022', '2022-2023', '2023-2024', '2024-2025'],
    'Среднее количество очков за игру': [0.85, 0.94, 0.87, 1.01, 0.77],
}

# Преобразуем данные в DataFrame
df = pd.DataFrame(data)

# Строим график для среднего количества очков за игру
fig_foxp = px.line(df, x='Сезон', y='Среднее количество очков за игру', title='Среднее количество очков за игру за последние 5 сезонов')
fig_foxp.write_html("Foxaverage.html")

#Винсент Трочек
data = {
    'Сезон': ['2020-2021', '2021-2022', '2022-2023', '2023-2024', '2024-2025'],
    'Голы': [17, 21, 22, 25, 14],
    'Ассисты': [26, 30, 42, 52, 15]
}

# Преобразуем данные в DataFrame
df = pd.DataFrame(data)

# Строим график с двумя линиями для голов и ассистов
fig_trochek = px.line(df, x='Сезон', y=['Голы', 'Ассисты'], title='Голы и Ассисты за последние 5 сезонов', labels={"value": 'Показатель в абсолютных величинах',
              "variable":"Показатели игрока"})
fig_trochek.write_html("Trochektotal.html")

# Строим график для среднего количества очков за игру
data = {
    'Сезон': ['2020-2021', '2021-2022', '2022-2023', '2023-2024', '2024-2025'],
    'Среднее количество очков за игру': [0.91, 0.63, 0.78, 0.94, 0.67],
}

# Преобразуем данные в DataFrame
df = pd.DataFrame(data)

# Строим график для среднего количества очков за игру
fig_trochekp = px.line(df, x='Сезон', y='Среднее количество очков за игру', title='Cреднее количество очков за игру за последние 5 сезонов')
fig_trochekp.write_html("Trochekaverage.html")

#Мика Зибанежад
data = {
    'Сезон': ['2020-2021', '2021-2022', '2022-2023', '2023-2024', '2024-2025'],
    'Голы': [24, 29, 39, 26, 8],
    'Ассисты': [26, 52, 52, 46, 19]
}

# Преобразуем данные в DataFrame
df = pd.DataFrame(data)

# Строим график с двумя линиями для голов и ассистов
fig_ziba = px.line(df, x='Сезон', y=['Голы', 'Ассисты'], title='Голы и Ассисты Мики Забанежада за последние 5 сезонов', labels={"value": 'Показатель в абсолютных величинах',
              "variable":"Показатели игрока"})
fig_ziba.write_html("Zibatotal.html")

data = {
    'Сезон': ['2020-2021', '2021-2022', '2022-2023', '2023-2024', '2024-2025'],
    'Среднее количество очков за игру': [0.89, 1, 1.1, 0.89, 0.63],
}

# Преобразуем данные в DataFrame
df = pd.DataFrame(data)

# Строим график для среднего количества очков за игру
fig_zibap = px.line(df, x='Сезон', y='Среднее количество очков за игру', title='Cреднее количество очков за игру за последние 5 сезонов')
fig_zibap.write_html("Zibaaverage.html")

#Алексис Лафреньер
data = {
    'Сезон': ['2020-2021', '2021-2022', '2022-2023', '2023-2024', '2024-2025'],
    'Голы': [12, 19, 16, 28, 11],
    'Ассисты': [9, 12, 23, 29, 13]
}

# Преобразуем данные в DataFrame
df = pd.DataFrame(data)

# Строим график с двумя линиями для голов и ассистов
fig_lafi = px.line(df, x='Сезон', y=['Голы', 'Ассисты'], title='Голы и Ассисты за последние 5 сезонов', labels={"value": 'Показатель в абсолютных величинах',
              "variable":"Показатели игрока"})
fig_lafi.write_html("Lafitotal.html")

#Среднее кол-во очков
data = {
    'Сезон': ['2020-2021', '2021-2022', '2022-2023', '2023-2024', '2024-2025'],
    'Среднее количество очков за игру': [0.37, 0.39, 0.48, 0.7, 0.56],
}

# Преобразуем данные в DataFrame
df = pd.DataFrame(data)

# Строим график для среднего количества очков за игру
fig_lafip = px.line(df, x='Сезон', y='Среднее количество очков за игру', title='Cреднее количество очков за игру за последние 5 сезонов')
fig_lafip.write_html("Lafiaverage.html")

#Уилл Кайлли (проводит только второй год в НХЛ, поэтому в первые 3 сезона мы записали ему 0
data = {
    'Сезон': ['2020-2021', '2021-2022', '2022-2023', '2023-2024', '2024-2025'],
    'Голы': [0, 0, 0, 13, 11],
    'Ассисты': [0, 0, 0, 8, 13]
}

# Преобразуем данные в DataFrame
df = pd.DataFrame(data)

# Строим график с двумя линиями для голов и ассистов
fig_cul = px.line(df, x='Сезон', y=['Голы', 'Ассисты'], title='Голы и Ассисты за последние 5 сезонов', labels={"value": 'Показатель в абсолютных величинах',
              "variable":"Показатели игрока"})
fig_cul.write_html("Cullyetotal.html")

#Среднее кол-во очков за игру
data = {
    'Сезон': ['2020-2021', '2021-2022', '2022-2023', '2023-2024', '2024-2025'],
    'Среднее количество очков за игру': [0, 0, 0, 0.26, 0.56],
}

# Преобразуем данные в DataFrame
df = pd.DataFrame(data)

# Строим график для среднего количества очков за игру
fig_culp = px.line(df, x='Сезон', y='Среднее количество очков за игру', title='Cреднее количество очков за игру за последние 5 сезонов')
fig_culp.write_html("Cullyeaverage.html")






#Раздел для выгрузки фотографий по api (с официального сайта ESPN)
photo = requests.get('https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3891952.png&w=350&h=254', stream=True) #достаём рандомное изображение собаки

#Если запрос успешный, то записываем содержимое в png
if photo.status_code == 200:
    with open('Panarin.png','wb') as f:
        shutil.copyfileobj(photo.raw, f)

photo1 = requests.get('https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4197146.png&w=350&h=254', stream=True)
if photo1.status_code == 200:
    with open('Fox.png','wb') as f:
        shutil.copyfileobj(photo1.raw, f)

photo2 = requests.get('https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2563036.png&w=350&h=254', stream=True)
if photo2.status_code == 200:
    with open('Trochek.png','wb') as f:
        shutil.copyfileobj(photo2.raw, f)

photo3 = requests.get('https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2562637.png&w=350&h=254',
                          stream=True)
if photo3.status_code == 200:
    with open('Ziba.png', 'wb') as f:
        shutil.copyfileobj(photo3.raw, f)

photo4 = requests.get('https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4697382.png&w=350&h=254',
                          stream=True)
if photo4.status_code == 200:
    with open('Lafi.png', 'wb') as f:
        shutil.copyfileobj(photo4.raw, f)

photo3 = requests.get('https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4697468.png&w=350&h=254',
                          stream=True)
if photo3.status_code == 200:
    with open('Cuylle.png', 'wb') as f:
        shutil.copyfileobj(photo3.raw, f)






#Пишем функцию для вычисления гипотетических очков, ассистов и голов
def wouldscore(matches, label_f, coefficient1, coefficient2, coefficient3):
    matches.insert(0, "0")
    match = int(matches.get())
    points = coefficient1 * match
    goals = coefficient2 * match
    assists = coefficient3 * match

    #Условия в условном цикле - показатели величайшего игрока НХЛ Уэйна Гретцки (если игрок набирает больше него, появляются соответствующие надписи
    if match < 5:
        label_f.configure(text='Мало матчей, введи ещё')
    elif points > 2857 and goals > 894 and assists > 1963:
        label_f.configure(
            text=f'За {match} матчей\nигрок наберет {round(points)} очков\nзабьет {round(goals)} шайб\nсделает {round(assists)} ассистов\nПобил рекорд Гретцки по очкам и голам!')
    elif points > 2857 and assists > 1963:
        label_f.configure(text = f'За {match} матчей\nигрок наберет {round(points)} очков\nзабьет {round(goals)} шайб\nсделает {round(assists)} ассистов\nПобил рекорд Гретцки по очкам и ассистам!')
    elif points > 2857 and goals > 894:
        label_f.configure(text = f'За {match} матчей\nигрок наберет {round(points)} очков\nзабьет {round(goals)} шайб\nсделает {round(assists)} ассистов\nПобил все рекорды Гретцки!')
    else:
        label_f.configure(text=f'За {match} матчей\nигрок наберет {round(points)} очков\nзабьет {round(goals)} шайб\nсделает {round(assists)} ассистов')

#Пишем функцию для возвращения игрока к главному меню
def get_back(root):
    root.focus_set()
    
#Пишем функцию, которая будет создавать окна с графиками в html
def open_graph(html_file):
    webview.create_window("Plotly Graph", html_file)
    webview.start()

#Создаем класс новых окон, которые будут открываться по запросу из меню
#Главный блок нашего проекта, поскольку в нём все сводится к одному
#back - главное окно; content, content_avg, content3 - два графика и фотография игрока
#name - имя игрока; a, b и c - коэффициенты для вычисления для функции wouldscore
class PlayerWindow(Toplevel):
    def __init__(self, back, content, content_avg, content3, name, a, b, c, base = None):
        super().__init__(base = base)
        self.focus_set()
        self.title(name)
        self.geometry('1000x800') #Размер окна
        label = Label(self, text= name)
        label.pack()

        #Первый график
        self.graph = Button(self, text="Голы и ассисты за последние 5 сезонов", command=lambda: open_graph(content))
        self.graph.pack(side=LEFT)

        #Второй график
        self.graph1 = Button(self, text="График 'очко за игру' за последние 5 сезонов", command=lambda: open_graph(content_avg))
        self.graph1.pack(side=RIGHT)

        #Фотография игрока
        face = Image.open(content3)
        face = face.resize((150, 150))
        new_face = ImageTk.PhotoImage(face)
        self.photo = Label(self, image=new_face)
        self.photo.image = new_face
        self.photo.place(x=700, y=110)
        #Кнопка для вызова меню
        self.button_back = Button(self, text='Назад к меню', command=lambda: get_back(back))
        self.photo.pack(side=TOP)
        self.button_back.pack(side=TOP)

        # Приложение для подсчёта матчей
        #Поле для ввода
        self.support = Label(self, text='Введи количество матчей',width=20, height=10)
        self.num_match = Entry(self)
        self.num_match.place(x=500, y=220, width=100, height=30)

        #Надпись для вывода
        self.label_f = Label(self, text="Здесь будет результат", width=60, height=30)
        self.label_f.config(font=("Times New Roman", 10))
        self.label_f.place(x=500, y=20, width=300, height=30)

        #Кнопка для запуска функции(находится рядом с полем для ввода)
        self.button = Button(self, text='Сколько очков наберет за n матчей?', command=lambda: wouldscore(self.num_match, self.label_f, a, b, c))
        self.label_f.pack(side=BOTTOM)
        self.button.pack(side=BOTTOM)
        self.num_match.pack(side=BOTTOM)
        self.support.pack(side=BOTTOM)






#cоздаем главное окно и задаем его параметры
base = Tk()
base.title('Нью-Йорк Рейнджерс')
base.geometry('400x400')

label = Label(base,
              text="Лучшие игроки Нью-Йорк Рейнджерс в сезоне 24/25")

label.pack(pady=10)



#Кнопка для вызова страницы Панарина
btn = Button(base,
             text="Артемий Панарин")
btn.bind("<Button>", lambda e: PlayerWindow(base, 'Panarintotal.html', 'Panarinaverage.html', 'images/Panarin.png', 'Артемий Панарин', 1.11, 0.45, 0.66))
btn.pack(pady=10)

#Кнопка для вызова страницы Фокса
btn1 = Button(base, text='Адам Фокс')
btn1.bind("<Button>", lambda e: PlayerWindow(base, 'Foxtotal.html', 'Foxaverage.html','images/Fox.png' ,'Адам Фокс', 0.77, 0.05, 0.72))
btn1.pack(pady=10)

#Кнопка для вызова страницы Трочека
btn2 = Button(base, text='Винсент Трочек')
btn2.bind("<Button>", lambda e: PlayerWindow(base,'Trochektotal.html', 'Trochekaverage.html','images/Trochek.png' ,'Винсент Трочек', 0.65, 0.31, 0.34))
btn2.pack(pady=10)

#Кнопка для вызова страницы Зибанежада
btn3 = Button(base, text='Мика Зибанежад')
btn3.bind("<Button>", lambda e: PlayerWindow(base,'Zibatotal.html', 'Zibaaverage.html', 'images/Ziba.png' ,'Мика Зибанежад', 0.61, 0.18, 0.43))
btn3.pack(pady=10)

#Кнопка для вызова страницы Лафреньера
btn4 = Button(base, text='Алексис Лафренье')
btn4.bind("<Button>", lambda e: PlayerWindow(base,'Lafitotal.html', 'Lafiaverage.html', 'images/Lafi.png','Алексис Лафренье', 0.56, 0.25, 0.31))
btn4.pack(pady=10)

#Кнопка для вызова страницы Кайлле
btn5 = Button(base, text='Уилл Кайлле')
btn5.bind("<Button>", lambda e: PlayerWindow(base,'Cullyetotal.html', 'Cullyeaverage.html', 'images/Cuylle.png','Уилл Кайлле', 0.54, 0.25, 0.29))
btn5.pack(pady=10)

mainloop()
