# -*- coding: utf-8 -*-

import random
import matplotlib.pyplot as plt
import numpy as np

"""
def hashpass(haslo, alfabet):


  A = [5, 5]
  B = [1, 1]
  prosta = [(A[1]-B[1])/(A[0]-B[0]), A[1]-(A[1]-B[1])/(A[0]-B[0])*A[0]]
  punkty = [A,B]
  for i in range(len(haslo)-2):
    x = random.random()*200-100
    punkty.append([x, prosta[0]*x+prosta[1]])
  punkty_nowe = []
  for i in range(len(punkty)):
    punkty[i][1] -= alfabet[haslo[i]] 
    punkty_nowe.append([punkty[i],haslo[i]])
  y0 = prosta[1]
  return punkty_nowe, y0

"""


def transform(linia):
    if linia.startswith("ALFABET"):
        linia = linia[7:]
        linia = "{" + linia.replace(' ', "'") + "} "
        i = 0
        last = 0
        linia2 = ""
        for j in range(len(linia)):
            if linia[j] == "'":
                i += 1
            if i == 2:
                linia2 = linia2 + linia[last + 2:j + 1] + ":" + linia[j + 1] + ","
                last = j
                i = 0
        linia2 = eval("{'" + linia2[:len(linia2) - 1] + '}')
        return linia2
    if linia.startswith("SPRAWDZ"):
        linia = linia[8:]
        j = 0
        while j < len(linia):
            if linia[j] == ' ':
                id = linia[:j]
                linia = linia[j + 1:]
                j = len(linia) + 1
            j += 1

        j = 0
        while j < len(linia):
            if linia[j] == ' ':
                y0 = linia[:j]
                linia = linia[j + 1:]
                j = len(linia) + 1
            j += 1

        j = 0
        while j < len(linia):
            if linia[j] == ')' and linia[j + 2] != "(":
                punkty = linia[:j + 1]
                linia = linia[j + 1:]
                j = len(linia) + 1
            j += 1
        punkty = punkty.replace('(', '[')
        punkty = punkty.replace(')', ']')
        punkty = eval('[' + punkty.replace(' ', ',') + ']')

        linia = "{" + linia.replace(' ', "'") + "} "
        i = 0
        last = 0
        linia2 = ""
        for j in range(len(linia)):
            if linia[j] == "'":
                i += 1
            if i == 2:
                linia2 = linia2 + linia[last + 2:j + 1] + ":" + linia[j + 1] + ","
                last = j
                i = 0
        wpisane = eval("{'" + linia2[:len(linia2) - 1] + '}')

        return id, y0, punkty, wpisane


def checkpass(wpisane, y0, punkty, alfabet, id):
    punkty_nowe = []
    i = 0
    for key in wpisane:
        punkty_nowe.append(punkty[wpisane[key] - 1])
        wpisane[key] = i
        i += 1

    for key in wpisane:
        punkty_nowe[(wpisane[key])][1] += alfabet[key]

    A = punkty_nowe[0]
    B = punkty_nowe[1]
    prosta = [(A[1] - B[1]) / (A[0] - B[0]), A[1] - (A[1] - B[1]) / (A[0] - B[0]) * A[0]]
    for i in range(len(punkty_nowe)):
        if abs(punkty_nowe[i][0] * prosta[0] + prosta[1] - punkty_nowe[i][1]) > 0.000001:
            return (id + " NotOk")
    if abs(prosta[1] - y0) > 0.000001:
        return (id + " NotOk")
    return (id + " Ok")


# FOR TEST "ALFABET A 1 B 2 C 5 D 8"

# FOR TEST "SPRAWDZ user123 0 (5,4) (1,-1) (-70.74487662683563,-75.74487662683563) (-81.78068361015112,-89.78068361015112) B 2 C 3 D 4"

linia = "NIC"
while linia != "KONIEC":
    try:
        linia = input("Wprowadz dane")
        if linia.startswith("ALFABET"):
            alfabet = transform(linia)
        if linia.startswith("SPRAWDZ"):
            id, y0, punkty, wpisane = transform(linia)
            print(checkpass(wpisane, float(y0), punkty, alfabet, id))
    except:
        print("BLAD")
