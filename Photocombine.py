import tkinter.filedialog as fl
import tkinter as tk
import tkinter.messagebox as mb
import pandas as pd
import cv2
import glob
import numpy as np
import os
from tkinter import ttk
from tkinter import *


PROJECT_DIR = os.getcwd()


def selectfile():
    global path                  #globalとして宣言
    #フォルダのパスを選択
    path = fl.askdirectory(initialdir = PROJECT_DIR, title = "select file")
    
    entry1.set(path)


def hconcat():
    try:
        #フォルダ内写真を結合
        files = glob.glob(path + "/*.png")
        # 空のリストを準備
        img_list = []
        #リストのインデックスと要素を取得し、画像を読み込む
        for i, figures in enumerate(files):
            img = cv2.imread(figures)
            img = np.asarray(img)
            img_list.append(img)

        #hconcat によって img_list内の画像を結合
        combined = cv2.hconcat(img_list)

        #結果をウィンドウに出力
        cv2.imshow(entry_title.get(), combined)
        

        #ファイルの書き出し
        cv2.imwrite(entry_title.get() + ".png", combined)
        cv2.waitKey(0)
        mb.showinfo("完了",  PROJECT_DIR + "に画像を保存しました。")

    except:
        mb.showinfo("エラー", "エラー。設定を確認してください")

def vconcat():
    try:
        #フォルダ内写真を結合
        files = glob.glob(path + "/*.png")
        # 空のリストを準備
        img_list = []
        #リストのインデックスと要素を取得し、画像を読み込む
        for i, figures in enumerate(files):
            img = cv2.imread(figures)
            img = np.asarray(img)
            img_list.append(img)

        #hconcat によって img_list内の画像を結合
        combined = cv2.vconcat(img_list)

        #結果をウィンドウに出力
        cv2.imshow(entry_title.get(), combined)
        

        #ファイルの書き出し
        cv2.imwrite(entry_title.get() + ".png", combined)
        cv2.waitKey(0)
        mb.showinfo("完了",  PROJECT_DIR + "ディレクトリに画像を保存しました。")

    except:
        mb.showinfo("エラー", "エラー。設定を確認してください")


if __name__ == "__main__":
    root = tk.Tk()
    root.title('PhotoCombine')
    root.resizable(False,False)
    frame1 = tk.LabelFrame(root, text = "png画像の結合", foreground = "green")
    frame1.grid(row = 0, sticky = tk.W)

    #タイトル入力  ラベルの作成
    titleLabel = ttk.Label(frame1, text = "タイトルを入力＞＞", padding = (5, 2))
    titleLabel.grid(row = 0, column = 0)


    #タイトル入力　エントリーの作成
    entry_title = tk.Entry(frame1, width = 30)
    entry_title.insert(tk.END, "file_name")
    entry_title.grid(row = 0, column = 1, padx = 5)


    #フォルダ参照　エントリーの作成
    entry1 = StringVar()
    IDirEntry = ttk.Entry(frame1, textvariable=entry1, width=30)
    IDirEntry.grid(row = 1, column = 0)
    #フォルダ参照　ボタンの作成
    button_select = tk.Button(frame1, text = "フォルダを参照", width = 10, command = selectfile)
    button_select.grid(row = 1, column = 1) 

    #横方向結合ボタンの作成
    button_exe = tk.Button(frame1, text = "横方向に結合", width = 10, command = hconcat)
    button_exe.grid(row = 1, column = 2)

    #縦方向結合ボタンの作成
    button_exe = tk.Button(frame1, text = "縦方向に結合", width = 10, command = vconcat)
    button_exe.grid(row = 1, column = 3)

    root.mainloop()

###画像は作業ディレクトリに保存されるので注意###