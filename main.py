from manim import *
class MainTitleScene(Scene):
    def construct(self):
        dir_str = [ 'UP', 'DOWN', 'LEFT', 'RIGHT']
        dir_list = [ UP, DOWN, LEFT, RIGHT]

        courseTitle = Text('Comunicação técnica e científica', font_size = 30).shift(RIGHT * 3, DOWN * 1.5)
        mainTitle = Text('Manim: da história até agora', font_size = 60).next_to(courseTitle, DOWN).shift(LEFT * 2)
        
        self.play(Write(courseTitle))
        self.play(Write(mainTitle))
