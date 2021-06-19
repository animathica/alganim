from manimlib.imports import *


#####################################################################################
######################  Ortogonalización y ortonormalización  #######################
#####################################################################################


#####################################################################################
#################################  Tercera escena  ##################################
###############################  versión manimlib  ##################################
#####################################################################################

class CodeWindow(VGroup):
    '''
    Code Window es escencialmente un objeto del tipo SurroundingRectangle con
    formato de ventana de código, que enumera las líneas de texto.
    INPUT: text, parámetros de surrounding rectangle.
            text ---->  VGroup con un cierto número de líneas. Para escribir espacios se recomienda
            usar lineas de texto que nunca serán escritas o añadidas a la pantalla.
    '''
    # PARA EL EQUIPO DE DOCUMENTACIÓN:
    # Mejorar la recepción de parámetros con **kwargs, si se puede, para escribir mejor la clase.
    # Implementar mejor control sobre el formato de la enumeración.

    def __init__(self, text, buff, color, fill_color, stroke_width, fill_opacity):
        rect = SurroundingRectangle(text,
                                    buff = buff,
                                    color = color,
                                    fill_color = fill_color,
                                    stroke_width = stroke_width,
                                    fill_opacity = fill_opacity)
        
        red_button = Dot(radius=0.1, stroke_width=0, color='#ff5f56')
        red_button.shift(LEFT * 0.1 * 3)
        yellow_button = Dot(radius=0.1, stroke_width=0, color='#ffbd2e')
        green_button = Dot(radius=0.1, stroke_width=0, color='#27c93f')
        green_button.shift(RIGHT * 0.1 * 3)
        buttons = VGroup(red_button, yellow_button, green_button)
        buttons.move_to(rect.get_corner(UL))
        buttons.shift(0.2*DOWN+0.5*RIGHT)

        number_line = [TextMobject(str(i+1)) for i in range(len(text))]
        number_line_mob = VGroup(*number_line).scale(0.5)
        number_line_mob.arrange(0.6*DOWN, aligned_edge=RIGHT)
        number_line_mob.next_to(text,0.4*LEFT)

        for i in range(len(number_line)):
            number_line_mob[i].set_color("#8A8A8A")
            number_line_mob[i].align_to(text[i], UP)

        self.canvas = VGroup(rect, buttons, number_line_mob)
        self.canvas.shift(0.3*LEFT)

class TerceraEscena(GraphScene, Scene):
    def setup(self):
        Scene.setup(self)
        GraphScene.setup(self)
    def FadeOutWrite(self,objeto1,objeto2):
        self.play(FadeOut(objeto1))
        self.play(Write(objeto2))            
    CONFIG = {
        "x_min": -0.25,
        "x_max": 1,
        "x_axis_width": 5,
        "x_tick_frequency": 10,
        "x_leftmost_tick": None,  # Change if different from x_min
        "x_labeled_nums": [],
        "x_axis_label": "$x$",
        "y_min": -1.5,
        "y_max": 1.5,
        "y_axis_height": 3*1.5,
        "y_tick_frequency": 0.5,
        "y_bottom_tick": None,  # Change if different from y_min
        "y_labeled_nums": [-1,1],
        "y_axis_label": "$y$",
        "axes_color": BLUE,
        "graph_origin": 4.5*LEFT+0.7*DOWN,
        "exclude_zero_label": True,
        "default_graph_colors": [BLUE, GREEN, YELLOW],
        "default_derivative_color": GREEN,
        "default_input_color": YELLOW,
        "default_riemann_start_color": BLUE,
        "default_riemann_end_color": GREEN,
        "area_opacity": 0.8,
        "num_rects": 50,
        "num_graph_anchor_points": 15000
    }


    def parte_1(self):
        #------------------------------------------------------------------- GRAM-SCHMIDT normal
        seaL = (TextMobject('''Sea $I$ un conjunto l.i.''').scale(0.7)).to_edge(1*UP)
        global left_corner 
        left_corner = 3.2*LEFT

        proceso_GM = TextMobject('''\\textbf{Proceso de Gram-Schmidt}''').scale(0.6)
        proceso_GM.set_color('#0087FF')
        
        algoritmo_left_1_1 = TextMobject('''\\texttt{1.- Tomar a un vector de $I$ y}''').scale(0.6)
        algoritmo_left_1_2 = TextMobject('''\\texttt{agregarlo a un nuevo conjunto }''',
                                            '''\\texttt{$\\Gamma$}''', '''.''').scale(0.6)
        algoritmo_left_1_2[1].set_color('#0087FF')                                

        algoritmo_left_2_1 = TextMobject('''\\texttt{2.- Tomar a otro de los vectores}''').scale(0.6)
        algoritmo_left_2_2 = TextMobject('''\\texttt{de $I$, restarle sus proyecciones}''').scale(0.6)
        algoritmo_left_2_3 = TextMobject('''\\texttt{sobre todos los vectores de }''', '''\\texttt{$\\Gamma$}''').scale(0.6)
        algoritmo_left_2_3[1].set_color('#0087FF')

        algoritmo_left_2_4 = TextMobject('''\\texttt{y después agregarlo a }''','''\\texttt{$\\Gamma$}''','''.''').scale(0.6)
        algoritmo_left_2_4[1].set_color('#0087FF')

        algoritmo_left_3_1 = TextMobject('''\\texttt{3.- Repetir el paso 2 hasta}''').scale(0.6)
        algoritmo_left_3_2 = TextMobject('''\\texttt{que }''','''\\texttt{$\\Gamma$}''','''\\texttt{ tenga tantos vectores}''').scale(0.6)
        algoritmo_left_3_2[1].set_color('#0087FF')
        algoritmo_left_3_3 = TextMobject('''\\texttt{como $I$.}''').scale(0.6)

        espacio = TextMobject('''\\texttt{espacio, espacio, espacio}''').scale(0.6).set_color("#303030")

        algo_left = VGroup(
                            proceso_GM, #0
                            algoritmo_left_1_1, #1
                            algoritmo_left_1_2, #2
                            espacio, #3
                            espacio.copy(), #4
                            algoritmo_left_2_1, #5
                            algoritmo_left_2_2, #6
                            algoritmo_left_2_3, #7
                            algoritmo_left_2_4, #8
                            espacio.copy(), #9
                            espacio.copy(), #10
                            algoritmo_left_3_1, #11
                            algoritmo_left_3_2, #12
                            algoritmo_left_3_3, #13
        ).arrange(0.4*DOWN, aligned_edge=LEFT).move_to(left_corner)

        canvas_GM = CodeWindow(text = algo_left, buff = 0.6, color = "#303030", fill_color = "#303030", stroke_width=0, fill_opacity = 0.5).canvas

        linea = Line((0,2.5,0),(0,-2,0))

        #------------------------------------------------------------------- GRAM-SCHMIDT modificado

        global right_corner
        right_corner = 3.7*RIGHT
        proceso_GMM = TextMobject('''\\textbf{Gram-Schmidt \\textit{modificado}}''').scale(0.6)
        proceso_GMM.set_color('#4FFF00')

        algoritmo_right_1_1 = TextMobject('''\\texttt{1.- Tomar a un vector de $I$,}''').scale(0.6)
        algoritmo_right_1_2 = TextMobject('''\\texttt{\\textit{normalizarlo} }''', '''\\texttt{y agregarlo a}''').scale(0.6)
        algoritmo_right_1_2[0].set_color('#4FFF00')
        algoritmo_right_1_3 = TextMobject('''\\texttt{un nuevo conjunto }''','''\\texttt{$N$}.''').scale(0.6)
        algoritmo_right_1_3[1].set_color('#4FFF00')

        algoritmo_right_2_1 = TextMobject('''\\texttt{2.- Tomar a otro de los vectores}''').scale(0.6)
        algoritmo_right_2_2 = TextMobject('''\\texttt{de $I$, restarle sus proyecciones}''').scale(0.6)
        algoritmo_right_2_3 = TextMobject('''\\texttt{sobre todos los vectores de }''','''\\texttt{$N$}''',''',''').scale(0.6)
        algoritmo_right_2_3[1].set_color('#4FFF00')
        algoritmo_right_2_4 = TextMobject('''\\texttt{\\textit{normalizarlo}''', '''\\texttt{, y después}''').scale(0.6)
        algoritmo_right_2_4[0].set_color('#4FFF00')
        algoritmo_right_2_5 = TextMobject('''\\texttt{agregarlo a }''','''\\texttt{$N$}''','''.''').scale(0.6)
        algoritmo_right_2_5[1].set_color('#4FFF00')

        algoritmo_right_3_1 = TextMobject('''\\texttt{3.- Repetir el paso 2 hasta}''').scale(0.6)
        algoritmo_right_3_2 = TextMobject('''\\texttt{que }''','''\\texttt{$N$}''', '''\\texttt{ tenga tantos vectores}''').scale(0.6)
        algoritmo_right_3_2[1].set_color('#4FFF00')
        algoritmo_right_3_3 = TextMobject('''\\texttt{como $I$.}''').scale(0.6)

        algo_right = VGroup(
                            proceso_GMM, #0
                            algoritmo_right_1_1, #1
                            algoritmo_right_1_2, #2
                            algoritmo_right_1_3, #3
                            espacio.copy(), #4
                            algoritmo_right_2_1, #5
                            algoritmo_right_2_2, #6
                            algoritmo_right_2_3, #7
                            algoritmo_right_2_4, #8
                            algoritmo_right_2_5, #9
                            espacio.copy(), #10
                            algoritmo_right_3_1, #11
                            algoritmo_right_3_2, #12
                            algoritmo_right_3_3, #13
        ).arrange(0.4*DOWN, aligned_edge=LEFT).move_to(right_corner)

        canvas_GMM = CodeWindow(text = algo_right, buff = 0.6, color = "#303030", fill_color = "#303030", stroke_width=0, fill_opacity = 0.5).canvas

        conclusiones = (TextMobject(
            "\\quad¡", #0
            "$\\Gamma$",#1
            " es ", #2
            "ortogonal", #3
            "!", #4
            "\\quad\\quad\\quad", #5
            "$\\langle$", #6
            "$\\Gamma$", #7
            "$\\rangle$", #8
            "$ = \\langle I\\rangle = \\langle$",#9
            "$N$",#10
            "$\\rangle$", #11
            "\\quad\\quad\\quad", #12
            "¡",#13
            "$N$",#14
            " es ", #15
            "ortonormal", #16
            "!"#17
        ).scale(0.7)).next_to(linea, 5*DOWN)
        conclusiones[1].set_color('#0087FF')
        conclusiones[3].set_color('#0087FF')
        conclusiones[7].set_color('#0087FF')
        conclusiones[10].set_color('#4FFF00')
        conclusiones[14].set_color('#4FFF00')
        conclusiones[16].set_color('#4FFF00')

        self.play(Write(seaL))
        self.play(ShowCreation(canvas_GM[0]), run_time = 2)
        self.play(ShowCreation(canvas_GM[1]), run_time = 1)
        self.play(ShowCreation(canvas_GM[2]), run_time = 1)
        self.play(Write(algo_left[0]))
        self.play(Write(algo_left[1:3]))
        self.wait(2)
        self.play(Write(algo_left[5:9]))
        self.wait(2)
        self.play(Write(algo_left[11:]))
        self.wait(2)
        #self.play(ShowCreation(linea))

        self.play(ShowCreation(canvas_GMM[0]), run_time = 2)
        self.play(ShowCreation(canvas_GMM[1]), run_time = 1)
        self.play(ShowCreation(canvas_GMM[2]), run_time = 1)
        self.play(Write(algo_right[0]))
        self.play(Write(algo_right[1:4]))
        self.wait(2)
        self.play(Write(algo_right[5:10]))
        self.wait(2)
        self.play(Write(algo_right[11:]))
        self.wait(2)

        self.play(
            FadeIn(conclusiones[6:12]),
            run_time = 2
        )
        self.play(
            FadeIn(conclusiones[:5]),
            run_time = 2
        )
        self.play(
            FadeIn(conclusiones[13:]),
            run_time = 2
        )

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )


    def parte_2(self):
        #------------------------------------------------------------------- Teorema de Gram-Schmidt
        tex_8 = TextMobject("Teorema de Gram-Schmidt").scale(0.9).to_edge(UP)
        tex_1 = TexMobject("\\text{dim}(V)=k<\\infty").scale(0.6).next_to(tex_8, DOWN)

        tex_4_1 = TexMobject("\\Gamma", #0
                            " = \\{\\vec{g}_1,..., \\vec{g}_k\\}" #1
                            ).scale(0.6).next_to(tex_1,DOWN)
        tex_4_2 = TextMobject("$\\Gamma$", #0
                                " es l.i." #1
                                ).scale(0.6).next_to(tex_4_1,DOWN)
        tex_4 = VGroup(tex_4_1, tex_4_2)
        tex_4[0][0].set_color('#0087FF')
        tex_4[1][0].set_color('#0087FF')
        tex_4.arrange(0.4*DOWN, center=False, aligned_edge=LEFT)
        tex_4.align_to(tex_1,LEFT)

        tex_2_1 = TexMobject("I= \\{\\vec{v}_1,..., \\vec{v}_k\\},\\,k<\\infty").scale(0.6).next_to(tex_4[0],10*LEFT)
        tex_2_2 = TextMobject("$I$ es l.i.").scale(0.6).next_to(tex_2_1,DOWN)
        tex_2 = VGroup(tex_2_1, tex_2_2)
        tex_2.arrange(0.4*DOWN, center=False, aligned_edge=LEFT)

        
        tex_6_1 = TexMobject("N",
                            " = \\{\\hat{n}_1,..., \\hat{n}_k\\}"
                            ).scale(0.6).next_to(tex_4[0], 10*RIGHT)
        tex_6_2 = TextMobject("$N$",
                            " es l.i."
                            ).scale(0.6).next_to(tex_6_1,DOWN)
        tex_6 = VGroup(tex_6_1, tex_6_2)
        tex_6[0][0].set_color('#4FFF00')
        tex_6[1][0].set_color('#4FFF00')
        tex_6.arrange(0.4*DOWN, center=False, aligned_edge=LEFT)

        tex_3_1 = TexMobject("\\vec{g}_1:=\\vec{v}_1").scale(0.6).next_to(tex_4,2.5*DOWN)
        tex_3_2 = TexMobject("""\\vec{g}_j:=
                        \\vec{v}_j
                        -
                        \\displaystyle\\sum_{i=1}^{j-1}
                        \\dfrac{\\langle\\vec{v}_j, \\vec{g}_i\\rangle}
                        {\\left\\Vert\\vec{g}_i\\right\\Vert}
                        \\hat{g}_i
                        """).scale(0.6).next_to(tex_3_1,2.5*DOWN)
        tex_3 = VGroup(tex_3_1, tex_3_2)
        tex_3.arrange(5*DOWN, center=False, aligned_edge=LEFT)
        tex_3.align_to(tex_4,LEFT)

        tex_5_1 = TexMobject("\\hat{n}_1:=\\dfrac{\\vec{v}_1}{\\left\\Vert\\vec{v}_1\\right\\Vert}").scale(0.6).next_to(tex_6,1.5*DOWN)
        tex_5_2 = TexMobject("""\\hat{n}_j:=
                        \\dfrac{
                        \\vec{v}_j
                        -
                        \\displaystyle\\sum_{i=1}^{j-1}
                        \\langle\\vec{v}_j, \\hat{n}_i\\rangle
                        \\hat{n}_i
                        }
                        {
                        \\left\\Vert
                        \\vec{v}_j
                        -
                        \\displaystyle\\sum_{i=1}^{j-1}
                        \\langle\\vec{v}_j, \\hat{n}_i\\rangle
                        \\hat{n}_i
                        \\right\\Vert
                        }
                        """).scale(0.6).next_to(tex_5_1,1.5*DOWN)
        tex_5 = VGroup(tex_5_1, tex_5_2)
        tex_5.arrange(1*DOWN, center=False, aligned_edge=LEFT)
        tex_5.align_to(tex_6,LEFT)
        tex_5[1].shift(0.3*DOWN)

        intervalo_j = TexMobject("1<j\\leq k").scale(0.6).next_to(tex_5, LEFT)
        intervalo_j.align_to(tex_2,LEFT)
        intervalo_j.shift(0.7*DOWN)


        tex_7_0 = TextMobject("$\\langle$", #0
            "$\\Gamma$", #1
            "$\\rangle$", #2
            "$ = \\langle I\\rangle = \\langle$",#3
            "$N$",#4
            "$\\rangle$", #5
            )
        tex_7_1 = TextMobject("$\\Gamma$",
                                " es un conjunto ",
                                "ortogonal",
                                ", "
                            ).next_to(tex_7_0)
        tex_7_2 = TextMobject("$N$",
                                " es un conjunto ",
                                "ortonormal"
                            ).next_to(tex_7_1,RIGHT)

        tex_7_0[1].set_color('#0087FF')
        tex_7_0[4].set_color('#4FFF00')

        tex_7_1[0].set_color('#0087FF')
        tex_7_1[2].set_color('#0087FF')

        tex_7_2[0].set_color('#4FFF00')
        tex_7_2[2].set_color('#4FFF00')
                            
        tex_7_1_2 = VGroup(tex_7_1, tex_7_2)

        tex_7_1_2.next_to(tex_7_0, 4*DOWN)

        tex_7 = VGroup(tex_7_0, tex_7_1_2[0], tex_7_1_2[1]).scale(0.6).move_to(3*DOWN)


        #self.play(Write(tex_1))
        self.wait(2)
        self.play(FadeIn(tex_2), run_time = 2)
        self.wait(2)
        self.play(Write(tex_3[0]))
        self.wait(2)
        self.play(Write(tex_3[1]))
        self.wait(2)
        self.play(FadeIn(intervalo_j))
        self.wait(1)
        self.play(FadeIn(tex_4), run_time = 2)
        for _ in range(2):
            self.play(
                ApplyMethod(tex_3[1].set_color, '#0087FF', rate_func=there_and_back),
                ApplyMethod(intervalo_j.set_color, '#0087FF', rate_func=there_and_back),
                run_time = 2
            )
        self.wait(2)
        self.play(Write(tex_5[0]))
        self.wait(2)
        self.play(Write(tex_5[1]))
        self.wait(2)
        self.play(FadeIn(tex_6), run_time = 2)
        self.wait(2)
        for _ in range(2):
            self.play(
                ApplyMethod(tex_5[1].set_color, '#4FFF00', rate_func=there_and_back),
                ApplyMethod(intervalo_j.set_color, '#4FFF00', rate_func=there_and_back),
                run_time = 2
            )
        self.play(GrowFromCenter(tex_7[0]),
                run_time = 2)
        self.wait(2)
        self.play(Write(tex_7[1]))
        self.wait(2)
        self.play(Write(tex_7[2]))
        self.wait(2)
        self.play(Write(tex_8))
        self.wait(2)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

    def parte_3(self):
        #------------------------------------------------------------------- Pregunta y ejercicios
        seaV = TextMobject("Sea $V$ un espacio vectorial con producto escalar").scale(0.7).move_to(3.4*UP)
        ejercicio_1_1 = TextMobject("Ejercicio 2.1. ","Demuestra que").scale(0.7)
        ejercicio_1_2_1 = TexMobject("""\\Bigg\\langle
                                \\qty\\Bigg{
                                \\vec{u},\\vec{v}-\\dfrac{\\langle\\vec{v}, \\vec{u}\\rangle}
                                {\\left\\Vert\\vec{u}\\right\\Vert}\\hat{u}
                                """).scale(0.7)
        ejercicio_1_2_2 = TexMobject(
                                """
                                \\Bigg\\rangle 
                                = 
                                \\langle
                                \\{\\vec{u},\\vec{v}\\}
                                \\rangle
                                """).scale(0.7).next_to(ejercicio_1_2_1,0.3*RIGHT)
        ejercicio_1_2 = VGroup(ejercicio_1_2_1, ejercicio_1_2_2)
        ejercicio_1_3 = TextMobject("para $\\vec{u},\\vec{v}\\in V$ con $\\vec{u},\\vec{v}\\neq\\vec{0}$ y dibuja un ejemplo en $\\mathbb{R}^2$.").scale(0.7)
        ejercicio_1_1[0].set_color('#0087FF')
        ejercicioG_1 = VGroup(ejercicio_1_1, ejercicio_1_2, ejercicio_1_3)
        ejercicioG_1.arrange(0.5*DOWN, center=False, aligned_edge=LEFT)
        ejercicioG_1.move_to(2*UP)
        ejercicioG_1[1].shift(2*RIGHT)

        ejercicio_2_1 = TextMobject("Ejercicio 2.2. ","Supongamos que $V$ tiene dimensión finita. \n").scale(0.7)
        ejercicio_2_2 = TextMobject("Demuestra que, para $1\\leq k\\leq \\text{dim}(V)$, cualquier conjunto\n").scale(0.7)
        ejercicio_2_3 = TextMobject("ortogonal de $k$ vectores es linealmente independiente.\n").scale(0.7)
        ejercicio_2_1[0].set_color('#0087FF')
        ejercicioG_2 = VGroup(ejercicio_2_1, ejercicio_2_2, ejercicio_2_3)
        ejercicioG_2.arrange(0.5*DOWN, center=False, aligned_edge=LEFT)
        ejercicioG_2.align_to(ejercicioG_1, LEFT)

        pregunta_1 = TextMobject("Pregunta: ",'''¿Qué sucedería si aplicáramos el proceso de\n''').scale(0.7)
        pregunta_2 = TextMobject("Gram-Schmidt a un conjunto linealmente \\textit{dependiente}\n").scale(0.7)
        pregunta_3 = TextMobject("de $k$ vectores?").scale(0.7)
        pregunta_1[0].set_color('#FF0000')
        preguntaG = VGroup(pregunta_1, pregunta_2, pregunta_3)
        preguntaG.arrange(0.5*DOWN, center=False, aligned_edge=LEFT)
        preguntaG.align_to(ejercicioG_2, LEFT)
        preguntaG.move_to(2.5*DOWN)
    #--------------------------------
        self.play(Write(seaV))
        self.play(Write(ejercicioG_1))
        self.wait(2)
        self.play(Write(ejercicioG_2))
        self.wait(2)
        self.play(Write(preguntaG))
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

    #animaciones
    def construct(self):
        self.parte_1()
        self.parte_2()
        self.parte_3()
