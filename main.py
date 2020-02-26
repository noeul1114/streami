import tkinter

window = tkinter.Tk()

window.title("Control Panel")
window.geometry("800x600")
# Width x Height + X Pos + Y Pos
window.resizable(False, False)
# 상하 크기 조절, 좌우 크기 조절

window.mainloop()