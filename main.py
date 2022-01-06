from manim import *

class MainTitleScene(Scene):
    def construct(self):
        courseTitle = Text('Comunicação técnica e científica', font_size = 30).shift(RIGHT * 3, DOWN * 1.5)
        mainTitle = Text('Uma introdução ao Manim', font_size = 60).next_to(courseTitle, DOWN).shift(LEFT * 1.7)
        group = Text('Dante Escame, Gabriel Tetzlaf, Gustavo Manarin e Pedro Potenza', font_size = 20).next_to(mainTitle, DOWN).shift(RIGHT * 0.8)
        
        self.play(Write(courseTitle))
        self.play(Write(mainTitle))
        self.play(Write(group))

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

class Community(Scene):
    def construct(self):
        manimTitle = Text('Atenção da comunidade', font_size = 30).shift(UP * 3)
        
        manimDefinition = Text('Manim atraiu desenvolvedores e produtores de vídeo', font_size = 25).next_to(manimTitle, DOWN).shift(LEFT * 2.5, DOWN)
        manimCreation = Text('Surge necessidade de novas funções', font_size = 25).next_to(manimDefinition, DOWN).shift(LEFT * 1.2, DOWN * 0.5)
        manimObjective = Text('Em 2020 surge a versão Community', font_size = 25).next_to(manimCreation, DOWN).shift(RIGHT * 0.05, DOWN * 0.5)
        
        self.play(Write(manimTitle))
        self.play(Write(manimDefinition))
        self.play(Write(manimCreation))
        self.play(Write(manimObjective))

class Installation(Scene):
    def construct(self):
        manimTitle = Text('Como utilizar o Manim', font_size = 30).shift(UP * 3)
        
        manimDefinition = Text('· Instalar Python', font_size = 25).next_to(manimTitle, DOWN).shift(LEFT * 2.5, DOWN)
        manimCreation = Text('· Instalar LaTeX', font_size = 25).next_to(manimDefinition, DOWN).shift(DOWN * 0.5)
        manimObjective = Text('· Instalar Manim utilizando pip', font_size = 25).next_to(manimCreation, DOWN).shift(RIGHT, DOWN * 0.5)
        
        self.play(Write(manimTitle))
        self.play(Write(manimDefinition))
        self.play(Write(manimCreation))
        self.play(Write(manimObjective))

class BooleanOperations(Scene):
    def construct(self):
        ellipse1 = Ellipse(
            width=4.0, height=5.0, fill_opacity=0.5, color=BLUE, stroke_width=10
        ).move_to(LEFT)
        ellipse2 = ellipse1.copy().set_color(color=RED).move_to(RIGHT)
        bool_ops_text = Text('Rompendo barreiras com o Manim', font_size = 30).next_to(ellipse1, UP * 3)
        ellipse_group = Group(bool_ops_text, ellipse1, ellipse2).move_to(LEFT * 3)
        self.play(FadeIn(ellipse_group))

        i = Intersection(ellipse1, ellipse2, color=GREEN, fill_opacity=0.5)
        self.play(i.animate.scale(0.25).move_to(RIGHT * 5 + UP * 2.5))
        intersection_text = Text("Intersection", font_size=23).next_to(i, UP)
        self.play(FadeIn(intersection_text))

        u = Union(ellipse1, ellipse2, color=ORANGE, fill_opacity=0.5)
        union_text = Text("Union", font_size=23)
        self.play(u.animate.scale(0.3).next_to(i, DOWN, buff=union_text.height * 3))
        union_text.next_to(u, UP)
        self.play(FadeIn(union_text))

        e = Exclusion(ellipse1, ellipse2, color=YELLOW, fill_opacity=0.5)
        exclusion_text = Text("Exclusion", font_size=23)
        self.play(e.animate.scale(0.3).next_to(u, DOWN, buff=exclusion_text.height * 3.5))
        exclusion_text.next_to(e, UP)
        self.play(FadeIn(exclusion_text))

        d = Difference(ellipse1, ellipse2, color=PINK, fill_opacity=0.5)
        difference_text = Text("Difference", font_size=23)
        self.play(d.animate.scale(0.3).next_to(u, LEFT, buff=difference_text.height * 3.5))
        difference_text.next_to(d, UP)
        self.play(FadeIn(difference_text))

class FollowingGraphCamera(MovingCameraScene):
    def construct(self):
        manimTitle = Text('Rompendo barreiras com o Manim', font_size = 30).shift(UP * 3)
        self.play(Write(manimTitle))
        self.camera.frame.save_state()

        # create the axes and the curve
        ax = Axes(x_range=[-1, 10], y_range=[-1, 10])
        graph = ax.plot(lambda x: np.sin(x), color=BLUE, x_range=[0, 3 * PI])

        # create dots based on the graph
        moving_dot = Dot(ax.i2gp(graph.t_min, graph), color=ORANGE)
        dot_1 = Dot(ax.i2gp(graph.t_min, graph))
        dot_2 = Dot(ax.i2gp(graph.t_max, graph))

        self.add(ax, graph, dot_1, dot_2, moving_dot)
        self.play(self.camera.frame.animate.scale(0.5).move_to(moving_dot))

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.add_updater(update_curve)
        self.play(MoveAlongPath(moving_dot, graph, rate_func=linear))
        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))

class ThreeDCameraIllusionRotation(ThreeDScene):
    def construct(self):
        manimTitle = Text('Rompendo barreiras com o Manim', font_size = 30).shift(UP * 6.5)

        axes = ThreeDAxes()
        circle=Circle()
        circle2=Circle().scale(2)
        self.set_camera_orientation(phi = 10 * DEGREES, theta = 100 * DEGREES)
        self.add(circle, circle2, axes)
        self.begin_3dillusion_camera_rotation(rate = 2)
        self.play(Write(manimTitle))
        self.wait(PI)
        self.stop_3dillusion_camera_rotation()

class Production(Scene):
    def construct(self):
        groupTitle = Text('Produções com Manim', font_size = 30).shift(UP * 3)
        
        danteImage = ImageMobject("images/Video1.png").next_to(groupTitle, DOWN).shift(LEFT * 4.8, DOWN * 1.5)
        tetzImage = ImageMobject("images/Video2.png").next_to(danteImage, RIGHT)
        manarinImage = ImageMobject("images/Video3.png").next_to(tetzImage, RIGHT)
        pedroImage = ImageMobject("images/Video4.png").next_to(manarinImage, RIGHT)

        self.play(Write(groupTitle))

        self.play(FadeIn(danteImage))
        self.play(FadeIn(tetzImage))
        self.play(FadeIn(manarinImage))
        self.play(FadeIn(pedroImage))

class Thanks(Scene):
    def construct(self):
        thanks = Text('Obrigado!', font_size = 30)
        
        doubts = Text('Dúvidas?', font_size = 15).next_to(thanks, DOWN)

        
        self.play(Write(thanks))
        self.play(Write(doubts))