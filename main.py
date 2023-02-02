import tkinter

from dictionary import Dictionary
from widget_ER import Widget_ER


class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # Создать две рамки: одну для виджетов Radiobutton
        # и еще одну для обычных виджетов Button.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Создать объект IntVar для использования
        # с виджетами Radiobutton.
        self.radio_var = tkinter.IntVar()

        # Назначить объекту IntVar значение 1.
        self.radio_var.set(1)

        # Создать виджеты Radiobutton в рамке top_frame.
        self.rb1 = tkinter.Radiobutton(self.top_frame,
                                       text='С английского на русский',
                                       variable=self.radio_var,
                                       value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame,
                                       text='С русского на английский',
                                       variable=self.radio_var,
                                       value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame,
                                       text='Редактировать словарь',
                                       variable=self.radio_var,
                                       value=3)

        # Упаковать виджеты Radiobutton.
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # Создать кнопку 'ОК' и кнопку 'Выйти'.
        self.ok_button = tkinter.Button(self.bottom_frame,
                                        text='OK',
                                        command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Выйти',
                                          command=self.main_window.destroy)
        # Упаковать виджеты Button.
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Упаковать рамки.
        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def show_choice(self):
        choice = self.radio_var.get()

        if choice == 1:
            Widget_ER()
        elif choice == 2:
            pass
        elif choice == 3:
            Dictionary()

if __name__ == '__main__':
    GUI()
