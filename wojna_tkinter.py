from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
root.configure(bg='pink')


#zmienne
talia1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
talia2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
Gracz = 'Gracz'
Komputer = 'Komputer'
punkty_Gracz = []
punkty_Komputer = []
karta1 = str(random.choice(talia1))
karta2 = str(random.choice(talia2))


def funkcja():
    try:
        karta1 = random.choice(talia1)
        karta2 = random.choice(talia2)

        Gracz_label.config(text=karta1)
        Komputer_label.config(text=karta2)



        talia1.remove(karta1)
        talia2.remove(karta2)

        global image_Gracz, image_Komputer
        image_Gracz = ImageTk.PhotoImage(
            Image.open("C:/Users/mento/OneDrive/Pulpit/python/pyt-ze1 — 2/iwona/" + str(karta1) + ".png"))
        image_Komputer = ImageTk.PhotoImage(
            Image.open("C:/Users/mento/OneDrive/Pulpit/python/pyt-ze1 — 2/iwona/" + str(karta2) + ".png"))
        Gracz_label.config(image=image_Gracz)
        Komputer_label.config(image=image_Komputer)

        # mechanika_gry:

        if karta1 > karta2:
            kto_wygral.config(text=f"Gracz wygral runde")
            punkty_Gracz.append(1)
        elif karta1 == karta2:
            kto_wygral.config(text=f"Remis w rundzie")
            punkty_Gracz.append(1)
            punkty_Komputer.append(1)
        else:
            kto_wygral.config(text=f"Komputer wygral runde")
            punkty_Komputer.append(1)



        punkty_Gracza.config(text=f'Liczba punktow:{len(punkty_Gracz)}')
        punkty_Komputera.config(text=f'Liczba punktow:{len(punkty_Komputer)}')

        root.title(f"Gra w wojne. Liczba kart: {len(talia1) + len(talia2)}")
    except:
        root.title('wojna - KONIEC GRY')
        Gracz_label.config(text='', image='')
        Komputer_label.config(text='', image='')
        my_button.destroy()

        if len(punkty_Gracz) > len(punkty_Komputer):
            kto_wygral.config(text='Gracz wygral gre')
        elif len(punkty_Gracz) == len(punkty_Komputer):
            kto_wygral.config(text='REMIS, nikt nie wygral gry')
        else:
            kto_wygral.config(text='Komputer wygral gre')







# Put cards in frames
Komputer_label = Label(root, text='', image='', bg='pink')
Komputer_label.grid(row=4, column=2)
Gracz_label = Label(root, text='', image='', bg='pink')
Gracz_label.grid(row=4, column=0, padx=3)
punkty_Gracza = Label(root, text='', bg='pink')
punkty_Gracza.grid(row=1, column=0, padx=3)
punkty_Komputera = Label(root, text='', bg='pink')
punkty_Komputera.grid(row=1, column=2)

# tekst
text_Gracz = Label(root, text="Gracz", font=10, bg='pink')
text_Gracz.grid(row=0, column=0)
text_Komputer = Label(root, text="Komputer", font=10, bg='pink')
text_Komputer.grid(row=0, column=2)
kto_wygral=Label(root, text='', font=4, bg='gold')
kto_wygral.grid(row=1,column=1)


# przycisk
my_button = Button(root, text="Wylosuj karte", command=funkcja)
my_button.grid(row=2, column=0)



root.mainloop()