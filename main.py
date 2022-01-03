from manim import *
class MainTitleScene(Scene):
    def construct(self):
        courseTitle = Text('Comunicação técnica e científica', font_size = 30).shift(RIGHT * 3, DOWN * 1.5)
        mainTitle = Text('Manim: da história até agora', font_size = 60).next_to(courseTitle, DOWN).shift(LEFT * 2)
        
        self.play(Write(courseTitle))
        self.play(Write(mainTitle))

class GroupScene(Scene):
    def construct(self):
        groupTitle = Text('Grupo', font_size = 30).shift(UP * 3)
        
        danteImage = ImageMobject("images/Dante.png").scale(0.3).next_to(groupTitle, DOWN).shift(LEFT * 4.5, DOWN * 1)
        tetzImage = ImageMobject("images/Tetz2.png").scale(0.3).next_to(danteImage, RIGHT)
        manarinImage = ImageMobject("images/Manarin.png").scale(0.3).next_to(tetzImage, RIGHT)
        pedroImage = ImageMobject("images/Pedro.png").scale(0.3).next_to(manarinImage, RIGHT)

        danteTitle = Text('Dante Escame', font_size = 20).next_to(danteImage, DOWN)
        tetzTitle = Text('Gabriel Tetzlaf', font_size = 20).next_to(tetzImage, DOWN)
        manarinTitle = Text('Gustavo Manarin', font_size = 20).next_to(manarinImage, DOWN)
        pedroTitle = Text('Pedro Potenza', font_size = 20).next_to(pedroImage, DOWN)

        self.play(Write(groupTitle))

        self.play(FadeIn(danteImage))
        self.play(FadeIn(tetzImage))
        self.play(FadeIn(manarinImage))
        self.play(FadeIn(pedroImage))

        self.play(Write(danteTitle))
        self.play(Write(tetzTitle))
        self.play(Write(manarinTitle))
        self.play(Write(pedroTitle))

class WhatIsManim(Scene):
    def construct(self):
        manimTitle = Text('O que é o Manim?', font_size = 30).shift(UP * 3)
        
        manimDefinition = Text('Biblioteca python', font_size = 25).next_to(manimTitle, DOWN).shift(LEFT * 3.5, DOWN)
        manimCreation = Text('· Criado como projeto pessoal de Grant Sanderson', font_size = 25).next_to(manimDefinition, DOWN).shift(RIGHT * 3)
        manimObjective = Text('· Tem como objetivo criar animações matemáticas', font_size = 25).next_to(manimCreation, DOWN)
        manimOSpecifics = Text('· Animações precisam ser precisas e explanativas', font_size = 25).next_to(manimObjective, DOWN)
        
        self.play(Write(manimTitle))
        self.play(Write(manimDefinition))
        self.play(Write(manimCreation))
        self.play(Write(manimObjective))
        self.play(Write(manimOSpecifics))