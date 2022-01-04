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

class ManimCreator(Scene):
    def construct(self):
        manimTitle = Text('Grant Sanderson', font_size = 30).shift(UP * 3)
        
        manimDefinition = Text('Graduado em Matemática pela Universidade de Stanford', font_size = 25).next_to(manimTitle, DOWN).shift(LEFT * 2.5, DOWN)
        manimCreation = Text('Trabalhou na Khan Academy de 2015 a 2016', font_size = 25).next_to(manimDefinition, DOWN).shift(LEFT * 0.8)
        manimObjective = Text('Fundou o canal 3Blue1Brown', font_size = 25).next_to(manimCreation, DOWN).shift(LEFT)
        manimOSpecifics = Text('Criou o Manim como projeto pessoal', font_size = 25).next_to(manimObjective, DOWN).shift(RIGHT * 0.5)
        threeBlue = Text('Acumulou 4 milhões de inscritos e utiliza o Manim em suas produções', font_size = 25).next_to(manimOSpecifics, DOWN).shift(RIGHT * 2.3)
        
        self.play(Write(manimTitle))
        self.play(Write(manimDefinition))
        self.play(Write(manimCreation))
        self.play(Write(manimObjective))
        self.play(Write(manimOSpecifics))
        self.play(Write(threeBlue))

class WhoManim(Scene):
    def construct(self):
        manimTitle = Text('Cenários de utilização', font_size = 30).shift(UP * 3)
        
        manimDefinition = Text('· Animações matemáticas', font_size = 25).next_to(manimTitle, DOWN).shift(LEFT * 2.5, DOWN)
        manimCreation = Text('· Trabalhos precisos', font_size = 25).next_to(manimDefinition, DOWN).shift(LEFT * 0.4)
        manimObjective = Text('· Desenhos explanativos', font_size = 25).next_to(manimCreation, DOWN).shift(RIGHT * 0.3)
        manimOSpecifics = Text('· Aumentar engajamento do público', font_size = 25).next_to(manimObjective, DOWN).shift(RIGHT * 0.8)
        
        self.play(Write(manimTitle))
        self.play(Write(manimDefinition))
        self.play(Write(manimCreation))
        self.play(Write(manimObjective))
        self.play(Write(manimOSpecifics))

class ManimDiferentials(Scene):
    def construct(self):
        manimTitle = Text('Diferenciais do Manim', font_size = 30).shift(UP * 3)

        vertices = (
            (-2, 1, 0),
            (-1, 2, 0),
            (1, 2, 0),
            (2, 1, 0),
            (0, -2, 0)
        )

        mob = Dot(radius=2.0) 
        mob.set_color_by_gradient([PINK, BLUE]).shift(LEFT * 2)

        polygon = Polygon(*vertices).next_to(mob, RIGHT)

        self.play(Write(manimTitle))
        self.play(Write(mob))
        self.play(Write(polygon))

class ManimDiferentials2(Scene):
    def construct(self):
        manimTitle = Text('Diferenciais do Manim', font_size = 30).shift(UP * 3)

        line1 = Line( ORIGIN, RIGHT ).shift(LEFT * 3)
        line2 = Line( ORIGIN, UP ).shift(LEFT * 3)
        mob = RightAngle(line1, line2, color=YELLOW, stroke_width=7)
        
        line3 = Line((LEFT+(1/3)*UP)*0.1, RIGHT+(1/3)*DOWN).shift(RIGHT * 3)
        line4 = Line((DOWN+(1/3)*RIGHT)*0.1, UP+(1/3)*LEFT).shift(RIGHT * 3)
        angle = Angle(line3, line4, radius=0.3)        

        self.add(manimTitle)
        self.play(Write(line1))
        self.play(Write(line2))
        self.play(Write(mob))

        self.play(Write(line3))
        self.play(Write(line4))
        self.play(Write(angle))

class ManimDiferentials3(Scene):
    def construct(self):
        manimTitle = Text('Diferenciais do Manim', font_size = 30).shift(UP * 3)

        logo_green = '#87c2a5'
        logo_blue = '#525893'
        logo_red = '#e07a5f'
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT, DOWN)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP, DOWN)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT, DOWN)
        logo = VGroup(triangle, square, circle).scale(1.3)
              

        self.add(manimTitle)
        self.play(Write(logo))

class Thanks(Scene):
    def construct(self):
        thanks = Text('Obrigado!', font_size = 30)
        
        doubts = Text('Dúvidas?', font_size = 15).next_to(thanks, DOWN)

        
        self.play(Write(thanks))
        self.play(Write(doubts))