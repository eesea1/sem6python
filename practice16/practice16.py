import logging
import os
from pdf2docx import Converter
from docx2pdf import convert
from PIL import Image
import PySimpleGUI as sg


def delFiles(key, substr, values):
    if key == 1:
        for i in getFiles():
            if i.startswith(substr):
                os.remove(values["-FOLDER-"]+f"/{i}")
                print(f"Файл: {i} успешно удалён!")
    if key == 2:
        for i in getFiles():
            if i.split(".")[0].endswith(substr):
                os.remove(values["-FOLDER-"]+f"/{i}")
                print(f"Файл: {i} успешно удалён!")
    if key == 3:
        for i in getFiles():
            if i.count(substr) != 0:
                os.remove(values["-FOLDER-"]+f"/{i}")
                print(f"Файл: {i} успешно удалён!")
    if key == 4:
        for i in getFiles():
            if i.endswith(substr):
                os.remove(values["-FOLDER-"]+f"/{i}")
                print(f"Файл: {i} успешно удалён!")


def createLayout():
    cur_path = os.getcwd()
    files = []
    for file in os.listdir(cur_path):
        files.append(file)
    file_list_column = [
        [
            sg.Text("Folder"),
            sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
            sg.FolderBrowse()
        ],
        [
            sg.Listbox(
                values=files, enable_events=True, size=(40, 20), key="-FILE LIST-"
            )
        ],
    ]
    actions_column = [
        [sg.Text(size=(40, 4), key="-TOUT-")],
        [sg.Button(button_text="Choose file to action", key="-ACTS-")],
        [sg.Text(key="-HELP-", size=(40, 1))],
        [sg.Text(text="Шкала сжатия картинки", key="-HELP-", size=(40, 1))],
        [sg.Input(key="SCALE", size=(40, 1))],
        [sg.Button(button_text="Удалить файлы с определенным началом", key="STARTDEL")],
        [sg.Button(button_text="Удалить файлы, содержащие подстроку", key="CONDEL")],
        [sg.Button(button_text="Удалить файлы с определенным концом", key="ENDDEL")],
        [sg.Button(button_text="Удалить файлы с определенным типом", key="TYPEDEL")],
        [sg.Input(default_text="Подстрока удаления", key="SUBSTR")]
    ]
    layout = [
        [
            sg.Column(file_list_column),
            sg.VSeparator(),
            sg.Column(actions_column),
        ]
    ]
    return layout


def getFiles():
    folder = values["-FOLDER-"]
    try:
        file_list = os.listdir(folder)
    except:
        file_list = []
    fnames = [
        f
        for f in file_list
        if os.path.isfile(os.path.join(folder, f))
    ]
    return fnames


if __name__ == '__main__':
    window = sg.Window("Практическая 16", createLayout())
    act = -1
    while True:
        event, values = window.read()
        #Выбор папки
        if event == "-FOLDER-":
            window["-FILE LIST-"].update(getFiles())
        #Выбор файла из списка
        elif event == "-FILE LIST-":
            try:
                filename = os.path.join(
                    values["-FOLDER-"], values["-FILE LIST-"][0]
                )
                if filename.endswith(".docx") or filename.endswith(".doc"):
                    window["-ACTS-"].update("Преобразовать docx в pdf")
                    window["-TOUT-"].update(f"Вы выбрали {filename}")
                    act = 1

                if filename.endswith(".pdf"):
                    window["-ACTS-"].update("Преобразовать pdf в docx")
                    window["-TOUT-"].update(f"Вы выбрали {filename}")
                    act = 2

                if filename.endswith(".jpeg") or filename.endswith(".jpg"):
                    window["-ACTS-"].update("Сжать изображение")
                    window["-TOUT-"].update(f"Вы выбрали {filename}")
                    act = 3
            except:
                pass
        if event == "STARTDEL":
            delFiles(1, values["SUBSTR"], values)
            window["-FILE LIST-"].update(getFiles())
        if event == "CONDEL":
            delFiles(2, values["SUBSTR"], values)
            window["-FILE LIST-"].update(getFiles())
        if event == "ENDDEL":
            delFiles(3, values["SUBSTR"], values)
            window["-FILE LIST-"].update(getFiles())
        if event == "TYPEDEL":
            delFiles(4, values["SUBSTR"], values)
            window["-FILE LIST-"].update(getFiles())
        if event == "-ACTS-":
            folder = values["-FOLDER-"]
            window["-HELP-"].update(f"Хотите преобразовать {filename} в {folder} newpdf.pdf")
            if act == 1:
                convert(filename, filename[:-5] + ".pdf")
                window["-FILE LIST-"].update(getFiles())
            elif act == 2:
                cv = Converter(filename)
                cv.convert(filename[:-4] + ".docx")
                cv.close()
                window["-FILE LIST-"].update(getFiles())
            elif act == 3:
                scale = values["SCALE"]
                try:
                    scale = int(scale)
                    if 0 <= scale <= 100:
                        image = Image.open(filename)
                        image.save(filename[:-4]+".jpg", quality=scale)
                        window["-FILE LIST-"].update(getFiles())
                    else:
                        sg.popup("Введите корректное значение сжатия")
                except:
                    sg.popup("Введите значение сжатия")
        if event == sg.WIN_CLOSED:
            break
    window.close()

