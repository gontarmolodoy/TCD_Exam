import os
from tkinter import *
from tkinter.ttk import *
from tkinter import Toplevel, Label, mainloop
import plotly.express as px
import pandas as pd
from PIL import Image, ImageTk
import requests
import shutil



#Строим графики для наших игроков

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

if not os.path.exists("images"):
    os.mkdir("images")
fig_panarin.write_image("images/Panarintotal.png")

#По очкам
data1 = {
    'Сезон': ['2020-2021', '2021-2022', '2022-2023', '2023-2024', '2024-2025'],
    'Среднее количество очков за игру': [1.38, 1.28, 1.12, 1.46, 1.01],
}

# Преобразуем данные в DataFrame
df1 = pd.DataFrame(data1)

# Строим график для среднего количества очков за игру
fig_panarinp = px.line(df1, x='Сезон', y='Среднее количество очков за игру', title='Среднее количество очков за игру за последние 5 сезонов')
fig_panarinp.write_image("images/Panarinaverage.png")

#Адам Фокс
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
fig_fox.write_image("images/Foxtotal.png")

#График для очков в среднем
data = {
    'Сезон': ['2020-2021', '2021-2022', '2022-2023', '2023-2024', '2024-2025'],
    'Среднее количество очков за игру': [0.85, 0.94, 0.87, 1.01, 0.77],
}

# Преобразуем данные в DataFrame
df = pd.DataFrame(data)

# Строим график для среднего количества очков за игру
fig_foxp = px.line(df, x='Сезон', y='Среднее количество очков за игру', title='Среднее количество очков за игру за последние 5 сезонов')
fig_foxp.write_image("images/Foxaverage.png")

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
fig_trochek.write_image("images/Trochektotal.png")

# Строим график для среднего количества очков за игру
data = {
    'Сезон': ['2020-2021', '2021-2022', '2022-2023', '2023-2024', '2024-2025'],
    'Среднее количество очков за игру': [0.91, 0.63, 0.78, 0.94, 0.67],
}

# Преобразуем данные в DataFrame
df = pd.DataFrame(data)

# Строим график для среднего количества очков за игру
fig_trochekp = px.line(df, x='Сезон', y='Среднее количество очков за игру', title='Cреднее количество очков за игру за последние 5 сезонов')
fig_trochekp.write_image("images/Trochekaverage.png")

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
fig_ziba.write_image("images/Zibatotal.png")

data = {
    'Сезон': ['2020-2021', '2021-2022', '2022-2023', '2023-2024', '2024-2025'],
    'Среднее количество очков за игру': [0.89, 1, 1.1, 0.89, 0.63],
}

# Преобразуем данные в DataFrame
df = pd.DataFrame(data)

# Строим график для среднего количества очков за игру
fig_zibap = px.line(df, x='Сезон', y='Среднее количество очков за игру', title='Cреднее количество очков за игру за последние 5 сезонов')
fig_zibap.write_image("images/Zibaaverage.png")

#Лафреньер
# Пример данных
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
fig_lafi.write_image("images/Lafitotal.png")

#Среднее кол-во очков
data = {
    'Сезон': ['2020-2021', '2021-2022', '2022-2023', '2023-2024', '2024-2025'],
    'Среднее количество очков за игру': [0.37, 0.39, 0.48, 0.7, 0.56],
}

# Преобразуем данные в DataFrame
df = pd.DataFrame(data)

# Строим график для среднего количества очков за игру
fig_lafip = px.line(df, x='Сезон', y='Среднее количество очков за игру', title='Cреднее количество очков за игру за последние 5 сезонов')
fig_lafip.write_image("images/Lafiaverage.png")

#Уилл Кайлли
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
fig_cul.write_image("images/Cullyetotal.png")

#Среднее кол-во очков за игру
data = {
    'Сезон': ['2020-2021', '2021-2022', '2022-2023', '2023-2024', '2024-2025'],
    'Среднее количество очков за игру': [0, 0, 0, 0.26, 0.56],
}

# Преобразуем данные в DataFrame
df = pd.DataFrame(data)

# Строим график для среднего количества очков за игру
fig_culp = px.line(df, x='Сезон', y='Среднее количество очков за игру', title='Cреднее количество очков за игру за последние 5 сезонов')
fig_culp.write_image("images/Cullyeaverage.png")





#Раздел для выгрузки фотографий по api
photo = requests.get('https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3891952.png&w=350&h=254', stream=True) #достаём рандомное изображение собаки

if photo.status_code == 200:
    with open('images/Panarin.png','wb') as f:
        shutil.copyfileobj(photo.raw, f)

photo1 = requests.get('https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4197146.png&w=350&h=254', stream=True)
if photo1.status_code == 200:
    with open('images/Fox.png','wb') as f:
        shutil.copyfileobj(photo1.raw, f)

photo2 = requests.get('https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2563036.png&w=350&h=254', stream=True)
if photo2.status_code == 200:
    with open('images/Trochek.png','wb') as f:
        shutil.copyfileobj(photo2.raw, f)

photo3 = requests.get('https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2562637.png&w=350&h=254',
                          stream=True)
if photo3.status_code == 200:
    with open('images/Ziba.png', 'wb') as f:
        shutil.copyfileobj(photo3.raw, f)

photo4 = requests.get('https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4697382.png&w=350&h=254',
                          stream=True)
if photo4.status_code == 200:
    with open('images/Lafi.png', 'wb') as f:
        shutil.copyfileobj(photo4.raw, f)

photo3 = requests.get('https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4697468.png&w=350&h=254',
                          stream=True)
if photo3.status_code == 200:
    with open('images/Cuylle.png', 'wb') as f:
        shutil.copyfileobj(photo3.raw, f)










#Пишем функцию для вычисления
def wouldscore(matches, label_f, coefficient1, coefficient2, coefficient3):
    matches.insert(0, "0")
    match = int(matches.get())
    points = coefficient1 * match
    goals = coefficient2 * match
    assists = coefficient3 * match

    if match < 5:
        label_f.configure(text='Мало матчей, введи ещё')
    elif points > 2857 and goals > 894:
        label_f.configure(
            text=f'За {match} матчей\nигрок наберет {round(points)} очков\nзабьет {round(goals)} шайб\nсделает {round(assists)} ассистов\nПобил рекорд Гретцки по очкам и голам!')
    elif points > 2857 and assists > 1963:
        label_f.configure(text = f'За {match} матчей\nигрок наберет {round(points)} очков\nзабьет {round(goals)} шайб\nсделает {round(assists)} ассистов\nПобил рекорд Гретцки по очкам и ассистам!')
    elif points > 2857 and goals > 894 and assists > 1963:
        label_f.configure(text = f'За {match} матчей\nигрок наберет {round(points)} очков\nзабьет {round(goals)} шайб\nсделает {round(assists)} ассистов\nПобил все рекорды Гретцки!')
    else:
        label_f.configure(text=f'За {match} матчей\nигрок наберет {round(points)} очков\nзабьет {round(goals)} шайб\nсделает {round(assists)} ассистов')

def get_back(root):
    root.focus_set()
#Создаем класс новых окон, которые будут открываться по запросу из меню
class PlayerWindow(Toplevel):
    def __init__(self, back, content, content_avg, content3, name, a, b, c, base = None):
        super().__init__(base = base)
        self.focus_set()
        self.title(name)
        self.geometry('1000x800')
        label = Label(self, text= name)
        label.pack()

        #Первый график
        img = Image.open(content)
        img = img.resize((350, 300))
        new_img =ImageTk.PhotoImage(img)
        self.graph = Label(self, image=new_img)
        self.graph.image = new_img
        self.graph.place(x=10, y=10)
        self.graph.pack(side=LEFT)
        #Второй график
        img_av = Image.open(content_avg)
        img_av = img_av.resize((350, 300))
        new_img_av = ImageTk.PhotoImage(img_av)
        self.graph = Label(self, image=new_img_av)
        self.graph.image = new_img_av
        self.graph.place(x=10, y=510)
        self.graph.pack(side=RIGHT)

        #Фотография игрока
        face = Image.open(content3)
        face = face.resize((150, 150))
        new_face = ImageTk.PhotoImage(face)
        self.photo = Label(self, image=new_face)
        self.photo.image = new_face
        self.photo.place(x=700, y=110)
        self.button_back = Button(self, text='Назад к меню', command=lambda: get_back(back))
        self.photo.pack(side=TOP)
        self.button_back.pack(side=TOP)

        # Приложение для подсчёта матчей
        #Поле для ввода
        self.support = Label(self, text='Введи количество матчей',width=20, height=10)
        self.num_match = Entry(self)
        self.num_match.place(x=500, y=220, width=100, height=30)

        #Поле для вывода
        self.label_f = Label(self, text="Здесь будет результат", width=60, height=30)
        self.label_f.config(font=("Times New Roman", 10))
        self.label_f.place(x=500, y=20, width=300, height=30)

        self.button = Button(self, text='Сколько очков наберет за n матчей?', command=lambda: wouldscore(self.num_match, self.label_f, a, b, c))
        self.label_f.pack(side=BOTTOM)
        self.button.pack(side=BOTTOM)
        self.num_match.pack(side=BOTTOM)
        self.support.pack(side=BOTTOM)

        #кнопка назад






base = Tk()
base.title('Нью-Йорк Рейнджерс')
base.geometry('400x400')

label = Label(base,
              text="Лучшие игроки Нью-Йорк Рейнджерс в сезоне 24/25")

label.pack(pady=10)

# a button widget which will open a

#Кнопка для Панарина
btn = Button(base,
             text="Артемий Панарин")
btn.bind("<Button>", lambda e: PlayerWindow(base, 'images/Panarintotal.png', 'images/Panarinaverage.png', 'images/Panarin.png','Артемий Панарин', 1.11, 0.45, 0.66))
btn.pack(pady=10)

#Кнопка для Фокса
btn1 = Button(base, text='Адам Фокс')
btn1.bind("<Button>", lambda e: PlayerWindow(base, 'images/Foxtotal.png', 'images/Foxaverage.png','images/Fox.png' ,'Адам Фокс', 0.77, 0.05, 0.72))
btn1.pack(pady=10)

#Кнопка для Фокса
btn2 = Button(base, text='Винсент Трочек')
btn2.bind("<Button>", lambda e: PlayerWindow(base,'images/Trochektotal.png', 'images/Trochekaverage.png','images/Trochek.png' ,'Винсент Трочек', 0.65, 0.31, 0.34))
btn2.pack(pady=10)

#Кнопка для Зибанежада
btn3 = Button(base, text='Мика Зибанежад')
btn3.bind("<Button>", lambda e: PlayerWindow(base,'images/Zibatotal.png', 'images/Zibaaverage.png', 'images/Ziba.png' ,'Мика Зибанежад', 0.61, 0.18, 0.43))
btn3.pack(pady=10)

#Кнопка для Лафика
btn4 = Button(base, text='Алексис Лафренье')
btn4.bind("<Button>", lambda e: PlayerWindow(base,'images/Lafitotal.png', 'images/Lafiaverage.png', 'images/Lafi.png','Алексис Лафренье', 0.56, 0.25, 0.31))
btn4.pack(pady=10)

#Кнопка для Кайлле
btn5 = Button(base, text='Уилл Кайлле')
btn5.bind("<Button>", lambda e: PlayerWindow(base,'images/Cullyetotal.png', 'images/Cullyeaverage.png', 'images/Cuylle.png','Уилл Кайлле', 0.54, 0.25, 0.29))
btn5.pack(pady=10)

mainloop()
