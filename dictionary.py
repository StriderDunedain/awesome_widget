import tkinter as tk

from functions import conn, cur, delete_record, get_all, insert_word, logger


class Dictionary:
 
    def __init__(self):
        self.window = tk.Tk()
        # Создать 4 рамки.
        self.answer_frame = tk.Frame(self.window)
        self.quit_frame = tk.Frame(self.window)
        self.top_frame = tk.Frame(self.window)
        self.mid_frame = tk.Frame(self.window)
        self.bottom_frame = tk.Frame(self.window)
        
        # Создать кнопку выхода.
        self.quit = tk.Button(self.quit_frame,
                              text = 'Выход',
                              command = self.window.destroy)
        self.quit.pack(side = 'right')
        
        # Заполнение 1-ой рамки.
        self.text_1 = tk.Label(self.top_frame,
                              text = '''Слово
        на английском''')
        self.text_1.pack(side = 'left')
        self.text_2 = tk.Label(self.top_frame,
                              text = '''Слово
        на русском''')
        self.text_2.pack(side = 'right')
        
        # Заполнение 2-ой рамки.
        self.r_word = tk.Entry(self.answer_frame,
                                width = 10)
        self.r_word.pack(side = 'right')

        self.n = tk.Label(self.answer_frame,
                          text = '------')
        self.n.pack(side = 'right')
        
        self.e_word = tk.Entry(self.answer_frame,
                                width = 10)
        self.e_word.pack(side = 'right')
        
        # Заполнение 3-ей рамки.
        self.button_1 = tk.Button(self.mid_frame,
                                  text = 'Сохранить',
                                  command = self.save_words)
        self.button_1.pack(side = 'left')
        self.button_2 = tk.Button(self.mid_frame,
                                  text = 'Удалить',
                                  command = self.delete_words)
        self.button_2.pack(side = 'right')
        
        # Заполнение 4-ой рамки.
        self.button_4 = tk.Button(self.bottom_frame,
                                  text = 'Показать словарь',
                                  command = self.show_dictionary)
        self.button_4.pack(side = 'right')
        
        self.quit_frame.pack(ipadx = 6, ipady = 5)
        self.answer_frame.pack()
        self.top_frame.pack()
        self.mid_frame.pack(ipadx = 15, ipady = 8)
        self.bottom_frame.pack()

        tk.mainloop()

    def save_words(self):
        insert_word(eng_word=self.e_word.get(), rus_word=self.r_word.get())
        conn.commit()

    def delete_words(self):
        delete_record(self.e_word.get())
        conn.commit()

    def show_dictionary(self):
        self.main_window = tk.Tk()
        self.listbox = tk.Listbox(self.main_window)
        self.listbox.pack(padx=10, pady=10)
        for word_tuple in get_all():
            index = word_tuple[0]
            words = word_tuple[1], ':', word_tuple[2]
            self.listbox.insert(index, words)
        tk.mainloop()


if __name__ == '__main__':
    Dictionary()

    conn.commit()
    logger.info('Connection closed successfully...')
    cur.close()
