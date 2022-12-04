import tkinter
from tkinter import *

class Graphics2_2:
    def __init__(self, start_board_list):
        self.board_list = start_board_list.copy()
        # make 0 be a blank string

        # set variables
        self.text_font = "Laksaman 18"
        self.background_color = "#FEFCFB"
        self.rectangle_color = "#FEFCFB"
        self.line_color = "#0A1128"
        self.text_color = "#0A1128"

        self.total_width = 1000
        self.total_height = 1000
        self.board_width = 700
        self.board_height = 800

        # initialize canvas
        self.window = tkinter.Tk()
        self.window.configure(background=self.background_color)
        self.canvas = tkinter.Canvas(self.window, width=600, height=60000, bg=self.background_color,scrollregion=(0,0,600,60000))
        hbar=Scrollbar(self.window,orient=HORIZONTAL)
        hbar.pack(side=BOTTOM,fill=X)
        hbar.config(command=self.canvas.xview)
        vbar=Scrollbar(self.window,orient=VERTICAL)
        vbar.pack(side=RIGHT,fill=Y)
        vbar.config(command=self.canvas.yview)
        #self.canvas.config(width=600,height=6000000)
        self.canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canvas.pack(side=LEFT,expand=True,fill=BOTH)
        self.canvas.pack()
        self.draw_board(self.board_list, 10, 10, self.board_width, self.board_height)

    def draw_board(self, board_list, x, y, width, height):
        self.canvas.create_rectangle(x, y, x + width, y + height, fill=self.rectangle_color)

        self.canvas.create_line(x + (width / 4), y, x + (width / 4), y + height, fill=self.line_color)
        self.canvas.create_line(x + (width / 4 * 2), y, x + (width / 4 * 2), y + height, fill=self.line_color)
        self.canvas.create_line(x + (width / 4 * 3), y, x + (width / 4 * 3), y + height, fill=self.line_color)
        self.canvas.create_line(x, y + (height / 4), x + width, y + (height / 4), fill=self.line_color)
        self.canvas.create_line(x, y + (height / 4 * 2), x + width, y + (height / 4 * 2), fill=self.line_color)
        self.canvas.create_line(x, y + (height / 4 * 3), x + width, y + (height / 4 * 3), fill=self.line_color)


        self.canvas.create_text(x + (width / 8), y + (width / 8), text=board_list[0], font=self.text_font, fill=self.text_color)
        self.canvas.create_text(x + (width / 2.74), y + (width / 8), text=board_list[1], font=self.text_font, fill=self.text_color)
        self.canvas.create_text(x + (width / 1.64), y + (width / 8), text=board_list[2], font=self.text_font, fill=self.text_color)
        self.canvas.create_text(x + (width / 1.14), y + (width / 8), text=board_list[3], font=self.text_font,fill=self.text_color)

        self.canvas.create_text(x + (width / 8), y + (width / 2.68), text=board_list[4], font=self.text_font,fill=self.text_color)
        self.canvas.create_text(x + (width / 2.74), y + (width / 2.68), text=board_list[5], font=self.text_font,fill=self.text_color)
        self.canvas.create_text(x + (width / 1.64), y + (width / 2.68), text=board_list[6], font=self.text_font,fill=self.text_color)
        self.canvas.create_text(x + (width / 1.14), y + (width / 2.68), text=board_list[7], font=self.text_font,fill=self.text_color)

        self.canvas.create_text(x + (width / 8), y + (width / 1.65), text=board_list[8], font=self.text_font,fill=self.text_color)
        self.canvas.create_text(x + (width / 2.74), y + (width / 1.65), text=board_list[9], font=self.text_font,fill=self.text_color)
        self.canvas.create_text(x + (width / 1.64), y + (width / 1.65), text=board_list[10], font=self.text_font,fill=self.text_color)
        self.canvas.create_text(x + (width / 1.14), y + (width / 1.65), text=board_list[11], font=self.text_font,fill=self.text_color)

        self.canvas.create_text(x + (width / 8), y + (width / 1.15), text=board_list[12], font=self.text_font,fill=self.text_color)
        self.canvas.create_text(x + (width / 2.74), y + (width / 1.15), text=board_list[13], font=self.text_font,fill=self.text_color)
        self.canvas.create_text(x + (width / 1.64), y + (width / 1.15), text=board_list[14], font=self.text_font,fill=self.text_color)
        self.canvas.create_text(x + (width / 1.14), y + (width / 1.15), text=board_list[15], font=self.text_font,fill=self.text_color)

    def show_solution(self, path_to_solution):
        
        boxes_per_row = 7
        padding = 10
        w = self.total_width / boxes_per_row - padding
        h = self.total_height / boxes_per_row - padding
        padding = 10
        self.canvas.delete("all")
        rows = 0
        count = 0
        
        for item in path_to_solution:
            item = item.tolist()
            
            item[item.index(0)] = " "
            #print("in the iteration:",item.board.board_list)
            self.draw_board(item, (count * padding + padding) + (count * w), (rows * padding + padding) + (rows * h), w, h)
            count += 1
            if count > boxes_per_row - 1:
                rows += 1
                count = 0

        self.window.mainloop()
