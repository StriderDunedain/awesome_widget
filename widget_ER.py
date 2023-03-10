import tkinter

from functions import get_random


class Widget_ER:
    def __init__(self):
        # Создать объект
        self.main_window = tkinter.Tk()

        # Создать три рамки.
        self.top_frame = tkinter.Frame(self.main_window)
        self.answer_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Создать и упаковать виджеты для рамки top_frame.

        self.new = tkinter.StringVar()

        self.word = tkinter.Label(self.top_frame,
                                  textvariable=self.new)

        self.answer = tkinter.Entry(self.top_frame,
                                    width=10)
        self.word.pack(side='left')
        self.answer.pack(side='left')

        # Создать запись проверки ответа.
        self.value = tkinter.StringVar()

        self.check = tkinter.Label(self.answer_frame,
                                   textvariable=self.value)
        self.check.pack(side='left')

        # Создать и упаковать кнопку для рамки mid_frame.
        self.button = tkinter.Button(self.mid_frame,
                                     text='Ответить',
                                     command=self.convert)
        self.next = tkinter.Button(self.mid_frame,
                                   text='Продолжить',
                                   command=self.set_value)

        self.button.pack(side='left')
        self.next.pack(side='left')

        # Создать кнопку для вызода.
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Назад',
                                          command=self.main_window.destroy)
        self.quit_button.pack(side='right')
        # Закрыть все рамки.
        self.top_frame.pack()
        self.answer_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()

    def convert(self):
        if self.r_word.lower() == self.answer.get().lower():
            self.value.set('Верно')
        else:
            self.value.set(self.r_word.lower())

    def set_value(self):
        for element in get_random():
            self.e_word = element[0].lower()
            self.r_word = element[1]
            self.new.set(self.e_word)
            self.value.set('')
            self.answer.delete(0, 20)

# if __name__ == '__main__':
Widget_ER()
