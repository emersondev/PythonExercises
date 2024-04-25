"""
Faça um programa em python que abra e reproduza o áudio de um arquivo MP3
"""
import pygame as pg
mx = pg.mixer
mus = mx.music

# inicia o pygame
mx.init()

# carrego a música (que está no mesmo diretório)
mus.load('kevin-macleod-crusade.mp3')

# toco a música carregada
mus.play()

# espera tocar a música
input()
pg.event.wait()