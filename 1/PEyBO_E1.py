from manim import *
#####################################################################################
######################  Producto escalar y bases ortogonales  #######################
#####################################################################################


#####################################################################################
###############################  Primera escena  ####################################
###############################  versión: Manim Community v0.8.0   ##################
#####################################################################################
ROJO = '#FF0000'
AZUL = '#0087FF'
NARANJA = '#FF7700'
VERDE = '#4FFF00'
MAGENTA = '#FF00FF'
AMARILLO = "#FFFF00"
GRIS = "#505050"

'''
Esta primera escena consta de tres partes:
    Introducción
    Escena geométrica
    Planteamiento del problema en general 
'''

class Subescena_1(Scene):
    def parte_1(self):
        #----------------------------------- ESPACIO V EN GENERAL
        dim_V = MathTex("\\text{dim}\\left(V\\right)=k<\\infty").scale(0.8).to_edge(UP)
        base_beta = Tex(
                        "$\\beta$",
                        "$ = $", 
                        "$\\{$",
                        "$\\vec{b}_1$",
                        "$,\\dots,$",
                        "$\\vec{b}_k$",
                        "$\\}$", #0
                        " base de ", #1
                        "$V$" #2
                    ).move_to(UP)

        base_propiedades = Tex(
                            "$\\langle \\beta\\rangle = V$",
                            "$,\\,\\beta$ es l.i."
                            )
        combination = MathTex(
                            "\\vec{v}", #0
                            "=", #1
                            "c_1", #2
                            "\\vec{b}_1", #3
                            "+", #4
                            "\\cdots", #5
                            "+", #6
                            "c_k", #7
                            "\\vec{b}_k" #8
                        )
        coeficientes_c = Tex("¿",
                            "$c_1, \\dots, c_k$",
                            "?")
        group_1 = VGroup(base_beta, base_propiedades, combination, coeficientes_c).scale(0.8)
        group_1.arrange(1*DOWN, center=False, aligned_edge=LEFT)
        coeficientes_ci = Tex("¿",
                            "$c_i$",
                            "?").scale(0.8).align_to(group_1[3], LEFT).align_to(group_1[3], UP)
        combination_copy = group_1[2].copy()

        self.play(FadeIn(dim_V))
        self.wait(2)
        self.play(Write(group_1[0][:]))
        self.wait(2)
        self.play(Write(group_1[1][:]))
        self.wait(1)
        self.play(Write(group_1[2][:]))
        self.wait(1)
        self.play(Write(group_1[3][:]))
        self.wait(1)
        self.play(
            Transform(group_1[3][0], coeficientes_ci[0]),
            Transform(group_1[3][1], coeficientes_ci[1]),
            Transform(group_1[3][2], coeficientes_ci[2]),
            run_time = 2
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time = 1)

    def construct(self):
        self.parte_1()
#-------------------------------------------------------------------------------------------------------  

class Subescena_2(Scene):
    #Parámetros de CONFIG como asignación de los valores 
    #de los atributos
    config.x_min = -0.25,
    config.x_max = 1,
    config.x_axis_width = 5,
    config.x_tick_frequency = 10,
    config.x_leftmost_tick = None,  # Change if different from x_min
    config.x_labeled_nums = [],
    config.x_axis_label = "$x$",
    config.y_min = -1.5,
    config.y_max = 1.5,
    config.y_axis_height = 3*1.5,
    config.y_tick_frequency = 0.5,
    config.y_bottom_tick = None,  # Change if different from y_min
    config.y_labeled_nums = [-1,1],
    config.y_axis_label = "$y$",
    config.axes_color = BLUE,
    config.graph_origin = 4.5*LEFT+0.7*DOWN,
    config.exclude_zero_label = True,
    config.default_graph_colors = [BLUE, GREEN, YELLOW],
    config.default_derivative_color = GREEN,
    config.default_input_color = YELLOW,
    config.default_riemann_start_color = BLUE,
    config.default_riemann_end_color = GREEN,
    config.area_opacity = 0.8,
    config.num_rects = 50,
    config.num_graph_anchor_points = 3000
    def parte_2(self):
        def encontrar_escalares(vec1, vec_obj1, text_A, vec2, vec_obj2, text_B, vec_objetivo, text_vec_objetivo):
            '''
            vec: numpy array
            vec_obj: VMobject
            '''
            # Colores para los vectores escalados
            col1 = vec_obj1.get_color()
            col2 = vec_obj2.get_color()
            col3 = VERDE
            # ---------------------------------------- Recta numérica a lo largo de la cual se desplazan los escalares
            number_line = NumberLine(rotation = PI/2, include_numbers = True, label_direction = RIGHT,
                                     x_range=[-3, 3, 1], numbers_to_exclude = [-3,3]).move_to(np.array([5.5,-2.0,0])).scale(0.5)
            # Paréntesis para la recta numérica
            par_sup = Tex(")").move_to(number_line.get_end()+0.04*DOWN).scale(1).rotate(np.pi/2).scale(0.8)
            par_inf = Tex(")").move_to(number_line.get_start()+0.04*UP).scale(1).rotate(-np.pi/2).scale(0.8)
            # Símbolos de infinito para la recta numérica
            inf = Tex("$ \\infty $").move_to(number_line.get_end()+0.25*UP).scale(0.6)
            minf = Tex("$ - \\infty $").move_to(number_line.get_start()+0.25*DOWN).scale(0.6)
            # Flechas que apuntan al valor de los escalares
            pointer_vec_1 = Arrow(start=ORIGIN, end=RIGHT, max_tip_length_to_length_ratio=0.4)
            label_1 = MathTex("c_1").add_updater(lambda m: m.next_to(pointer_vec_1, 0.3*LEFT))
            pointer_vec_2 = Arrow(start=ORIGIN, end=LEFT, max_tip_length_to_length_ratio=0.4)
            label_2 = MathTex("c_2").add_updater(lambda m: m.next_to(pointer_vec_2, 0.3*RIGHT))
            # ValueTrackers para vector 1 y vector 2, respectivamente. Son utilizados para modificar muchos objetos
            # simultáneamente
            t1 = ValueTracker(1)
            t2 = ValueTracker(1)
            # Updaters para los sliders sobre la recta real 
            # Flecha para c_1
            pointer_vec_1.add_updater(
                lambda m: m.next_to(
                            number_line.n2p(t1.get_value()),
                            LEFT,
                            buff = 0.1
                )
            )
            # Flecha para c_2
            pointer_vec_2.add_updater(
                lambda m: m.next_to(
                            number_line.n2p(t2.get_value()),
                            RIGHT,
                            buff = 0.4
                )
            )
            # VGroup de la recta numérica completa
            complete_number_line = VGroup(number_line, par_sup, par_inf, inf, minf, pointer_vec_1, label_1, pointer_vec_2, label_2)

            # Box que contiene a la recta numérica
            sliders_box = Rectangle(width=2.5, height=3.9, fill_color=BLACK, fill_opacity=1).move_to(np.array([5.51,-2,0]))
            sliders = VGroup(sliders_box, complete_number_line)
            # ---------------------------------------- Vectores en el plano    
            # Texto de los escalares
            label1 = MathTex("c_1")
            label2 = MathTex("c_2")
            # Vector suma en numpy array y en arrow
            vec1_plus_vec2 = vec1+vec2
            vec_AplusB = Arrow((0, 0, 0), vec1_plus_vec2, buff=0, color = col3)
            # distancias de separación entre puntas de vectores y el correspondiente texto
            dist_1 = 0.4*vec1/(np.linalg.norm(vec1))
            dist_2 = 0.4*vec2/(np.linalg.norm(vec2))
            dist_3 = 0.4*vec1_plus_vec2/(np.linalg.norm(vec1_plus_vec2))
            # Etiqueta de la suma
            plus_sign = MathTex("+").move_to(vec_AplusB.get_end()+dist_3)
            label_sum1 = MathTex("c_2").next_to(plus_sign, 0.5*RIGHT)
            label_sum2 = text_B.copy().next_to(label_sum1, 0.5*RIGHT)
            label_sum3 = text_A.copy().next_to(plus_sign, 0.5*LEFT)
            label_sum4 = MathTex("c_1").next_to(label_sum3, 0.5*LEFT)
            label3 = VGroup(plus_sign, label_sum1, label_sum2, label_sum3, label_sum4).move_to(vec_AplusB.get_end()+dist_3)
            # Otros símbolos utilizados
            equal_sign = MathTex("=")
            # Vectores fantasma para la suma
            fantasma_flecha1 = Arrow(vec2, vec1_plus_vec2, buff = 0, stroke_opacity = 1, color = col1)[-1] # Solo la punta de la flecha
            fantasma_flecha2 = Arrow(vec1, vec1_plus_vec2, buff = 0, stroke_opacity = 1, color = col2)[-1]
            vec_obj1_fantasma = DashedLine(vec2, vec1_plus_vec2, buff = 0, color = col1, stroke_opacity = 0.5)
            vec_obj2_fantasma = DashedLine(vec1, vec1_plus_vec2, buff = 0, color = col2, stroke_opacity = 0.5)

            # Updaters
            def upd_for_vec1(obj):
                new_vec = Arrow((0,0,0), t1.get_value()*vec1, buff=0, color = col1)
                obj.become(new_vec)

            def upd_for_vec2(obj):
                new_vec = Arrow((0,0,0), t2.get_value()*vec2, buff=0, color = col2)
                obj.become(new_vec)

            def upd_for_vec3(obj):
                new_vec = Arrow((0,0,0), t1.get_value()*vec1+t2.get_value()*vec2, buff=0, color = col3)
                obj.become(new_vec)

            def upd_for_text1(obj):
                obj.move_to(vec_obj1.get_end()+dist_1)
                
            def upd_for_text2(obj):
                obj.move_to(vec_obj2.get_end()+dist_2)
            
            def upd_for_text3(obj):
                obj.move_to(vec_AplusB.get_end()+dist_3)

            def upd_for_label1(obj):
                obj.next_to(text_A, 0.5*LEFT)

            def upd_for_label2(obj):
                obj.next_to(text_B, 0.5*LEFT)

            def upd_for_fantasma1(obj):
                new_vec = DashedLine(vec_obj2.get_end(), vec_AplusB.get_end(), buff = 0, color = col1, stroke_opacity = 0.5)
                obj.become(new_vec)

            def upd_for_fantasma2(obj):
                new_vec = DashedLine(vec_obj1.get_end(), vec_AplusB.get_end(), buff = 0, color = col2, stroke_opacity = 0.5)
                obj.become(new_vec)
            
            def upd_for_fantasma_flecha1(obj):
                new_vec = Arrow(vec_obj2.get_end(), vec_AplusB.get_end(), buff = 0, stroke_opacity = 1, color = col1)[-1]
                obj.become(new_vec)

            def upd_for_fantasma_flecha2(obj):
                new_vec = Arrow(vec_obj1.get_end(), vec_AplusB.get_end(), buff = 0, stroke_opacity = 1, color = col2)[-1]
                obj.become(new_vec)

            vec_obj1.add_updater(upd_for_vec1)
            label1.add_updater(upd_for_label1)
            text_A.add_updater(upd_for_text1)

            vec_obj2.add_updater(upd_for_vec2)
            text_B.add_updater(upd_for_text2)
            label2.add_updater(upd_for_label2)

            vec_AplusB.add_updater(upd_for_vec3)
            label3.add_updater(upd_for_text3)

            vec_obj1_fantasma.add_updater(upd_for_fantasma1)
            vec_obj2_fantasma.add_updater(upd_for_fantasma2)

            fantasma_flecha1.add_updater(upd_for_fantasma_flecha1)
            fantasma_flecha2.add_updater(upd_for_fantasma_flecha2)

            # Obtención de los escalares resolviendo el sistema de ecuaciones:
            # A.c = b
            A = np.array([vec1[:2], vec2[:2]]).T
            b = np.array(vec_objetivo[:2]) # Vector objetivo
            c = np.linalg.solve(A,b) #Vector de coeficientes

            # ---------------------------------------- Animaciones
            
            self.play(FadeIn(label1.next_to(text_A, 0.5*LEFT)),
            FadeIn(label2.next_to(text_B, 0.5*LEFT)),
            Write(fantasma_flecha1),
            Write(fantasma_flecha2),
            Write(vec_obj1_fantasma),
            Write(vec_obj2_fantasma),
            Write(vec_AplusB),
            FadeIn(label3),
            run_time = 2
            )
            self.play(FadeIn(sliders))
            # Moviendo solo el primer coeficiente
            self.play(t1.animate.set_value(0.5), 
            run_time = 1.5)
            self.play(t1.animate.set_value(0.9), 
            run_time = 1.5)
            # Moviendo solo el segundo coeficiente
            self.play(t2.animate.set_value(1.2), 
            run_time = 1.5)
            self.play(t2.animate.set_value(1.0), 
            run_time = 1.5)
            #Moviendo ambos coeficientes de forma simultánea
            self.play(t1.animate.set_value(1.6), 
            t2.animate.set_value(-0.8),
            run_time = 1.5)
            self.play(t1.animate.set_value(-0.5), 
            t2.animate.set_value(0.8),
            run_time = 1.5)
            self.play(t1.animate.set_value(-1), 
            t2.animate.set_value(-1.8),
            run_time = 1.5)
            self.play(t1.animate.set_value(0.5), 
            t2.animate.set_value(1.8),
            FadeOut(text_vec_objetivo),
            run_time = 1.5)
            self.play(t1.animate.set_value(0.6), 
            t2.animate.set_value(1.9),
            run_time = 1.0)
            self.play(t1.animate.set_value(0.6), 
            t2.animate.set_value(2.1),
            run_time = 1.0)
            self.play(t1.animate.set_value(0.4), 
            t2.animate.set_value(2.1),
            run_time = 1.0)
            self.play(t1.animate.set_value(0.4), 
            t2.animate.set_value(1.9),
            run_time = 1.0)
            # Valores correctos de los coeficientes
            self.play(t1.animate.set_value(c[0]), 
            t2.animate.set_value(c[1]),
            run_time = 2.0)
            self.play(
                FadeOut(fantasma_flecha1),
                FadeOut(fantasma_flecha2),
                FadeOut(vec_obj1_fantasma),
                FadeOut(vec_obj2_fantasma),
                run_time = 2
            )
            #-----------------------------------------
            self.wait(0.5)
            equal_sign.next_to(label3, 0.5*LEFT)
            text_vec_objetivo.next_to(equal_sign, 0.5*LEFT)
            #Puntos para destello
            dot1 = Dot(radius = 0, color=AMARILLO).next_to(label1, 2*UP)
            dot2 = Dot(radius = 0, color=AMARILLO).next_to(label2, 2*UP)
            self.play(Circumscribe(label1, fade_out=True), 
            Circumscribe(label2, fade_out=True),
            Flash(dot1), 
            Flash(dot2),
            FadeIn(equal_sign),
            FadeIn(text_vec_objetivo),
            run_time = 2.5)
            self.play(
            FadeOut(vec_obj1),
            FadeOut(vec_obj2),
            FadeOut(vec_AplusB),
            *[FadeOut(mob) for mob in self.mobjects],
            run_time = 2)
        

        # Coordenadas del vector objetivo
        vec = np.array([5,3,0])
        # Coordenadas de vector A
        vec_A = np.array([-2,2,0])
        # Coordenadas de vector B
        vec_B = np.array([3,1,0])

        grid = NumberPlane()
        vec_ = Arrow((0, 0, 0), vec, buff=0,color=NARANJA)
        vecA = Arrow((0, 0, 0), vec_A, buff=0,color=AZUL)
        vecB = Arrow((0, 0, 0), vec_B, buff=0,color=ROJO)

        text_vec = MathTex("\\vec{v}").move_to(vec_.get_end()+0.4*vec/(np.linalg.norm(vec)))
        text_A = MathTex("\\vec{b}_1").move_to(vecA.get_end()+0.4*vec_A/(np.linalg.norm(vec_A)))
        text_B = MathTex("\\vec{b}_2").move_to(vecB.get_end()+0.4*vec_B/(np.linalg.norm(vec_B)))

        # ---------------------------------------- Animaciones iniciales
        self.play(Write(grid))
        self.wait(0.5)
        self.play(FadeIn(vec_))
        self.play(Write(text_vec))
        self.play(FadeIn(vecA), Write(text_A), FadeIn(vecB), Write(text_B))
        self.wait(0.5)
        encontrar_escalares(vec_A, vecA, text_A, vec_B, vecB, text_B, vec, text_vec)
        self.wait(0.5)
    def construct(self):
        self.parte_2()
#-------------------------------------------------------------------------------------------------------
class Subescena_3(Scene):
    def parte_3(self):
        #----------------------------------- ESPACIO V EN GENERAL
        base_beta = Tex(
                        "$\\beta$", #0
                        "$ = $", #1
                        "$\\{$", #2
                        "$\\vec{b}_1$", #3
                        "$,\\dots,$", #4
                        "$\\vec{b}_k$", #5
                        "$\\}$", #6
                        " base de ", #7
                        "$V$" #8
                    ).move_to(UP)

        base_propiedades = Tex(
                                "$\\langle \\beta\\rangle = V$",
                                "$,\\,\\beta$ es l.i."
                            )
        combination = MathTex(
                            "\\vec{v}", #0
                            "=", #1
                            "c_1", #2
                            "\\vec{b}_1", #3
                            "+", #4
                            "\\cdots", #5
                            "+", #6
                            "c_k", #7
                            "\\vec{b}_k" #8
                        )
        coeficientes_c = Tex("¿",
                            r"$c_i$",
                            "?")
        group = VGroup(base_beta, #0
                        base_propiedades, #1
                        combination, #2
                        coeficientes_c #3
                        ).scale(0.8).shift(4*LEFT+UP)
        group.arrange(1*DOWN, center=False, aligned_edge=LEFT)
        #----------------------------------- POSIBILIDADADES PARA EL VECTOR v
        #-------------------------------------------  FUNCIONES
        base_beta_f = Tex(
                        "$\\beta$", #0
                        "$ = $", #1
                        "$\\{$", #2
                        "$f_1$", #3
                        "$,\\dots,$", #4
                        "$f_k$", #5
                        "$\\}$", #6
                        " base de ", #7
                        "$\\mathcal{C}^0\\left(\\mathbb{R}, \\mathbb{R}\\right)$" #8
                        ).move_to(UP)
        base_propiedades_f = Tex(
                                "$\\langle \\beta\\rangle = V$",
                                "$,\\,\\beta$ es l.i."
                            )
        combination_f = MathTex(
                                "v", #0
                                "=", #1
                                "c_1", #2
                                "f_1", #3
                                "+", #4
                                "\\cdots", #5
                                "+", #6
                                "c_k", #7
                                "f_k" #8
                                )
        coeficientes_c_f = Tex("¿",
                            r"$c_i$",
                            "?")
        group_funciones = VGroup(base_beta_f, #0
                                base_propiedades_f, #1
                                combination_f, #2
                                coeficientes_c_f #3
                                ).scale(0.8).shift(4*LEFT+UP)
        group_funciones.arrange(1*DOWN, center=False, aligned_edge=LEFT)
        group_funciones.align_to(group, LEFT)

        #-------------------------------------------  MATRICES
        base_beta_M = Tex(
                        "$\\beta$", #0
                        "$ = $", #1
                        "$\\{$", #2
                        "$M_1$", #3
                        "$,\\dots,$", #4
                        "$M_{k^2}$", #5
                        "$\\}$", #6
                        " base de ", #7
                        "$\\mathcal{M}_{k\\times k}\\left(\\mathcal{K}\\right)$" #8
                        ).move_to(UP)
        base_propiedades_M = Tex(
                                "$\\langle \\beta\\rangle = V$",
                                "$,\\,\\beta$ es l.i."
                            )
        combination_M = MathTex(
                                "M", #0
                                "=", #1
                                "c_1", #2
                                "M_1", #3
                                "+", #4
                                "\\cdots", #5
                                "+", #6
                                "c_{k^2}", #7
                                "M_{k^2}" #8
                                )
        coeficientes_c_M = Tex("¿",
                            r"$c_i$",
                            "?")
        group_matrices = VGroup(base_beta_M, #0
                                base_propiedades_M, #1
                                combination_M, #2
                                coeficientes_c_M #3
                                ).scale(0.8).shift(4*LEFT+UP)
        group_matrices.arrange(1*DOWN, center=False, aligned_edge=LEFT)
        group_matrices.align_to(group_funciones, LEFT)
        #-------------------------------------------  N-TUPLAS
        entries_ntup = [["v_{1}"], ["v_{2}"],["\\vdots"],["v_{k}"]]  
        ntup = Matrix(entries_ntup,
                    left_bracket="\\big(",
                    right_bracket="\\big)")
        entries_ntup1 = [["v_{1}^1"], ["v_{2}^1"],["\\vdots"],["v_{k}^1"]]  
        ntup1 = Matrix(entries_ntup1,
                    left_bracket="\\big(",
                    right_bracket="\\big)")
        entries_ntup2 = [["v_{1}^k"], ["v_{2}^k"],["\\vdots"],["v_{k}^k"]] 
        ntup2 = Matrix(entries_ntup2,
                    left_bracket="\\big(",
                    right_bracket="\\big)")
        base_beta_T_0 =  MathTex("\\beta")
        base_beta_T_1 =  MathTex("=")
        base_beta_T_3 =  ntup1.copy()
        base_beta_T_2 =  Brace(base_beta_T_3, LEFT)
        base_beta_T_4 =  MathTex(",\\dots,")
        base_beta_T_5 =  ntup2.copy()
        base_beta_T_6 =  Brace(base_beta_T_5, RIGHT)
        base_beta_T_7 =  Tex(" base de ")
        base_beta_T_8 =  MathTex("\\mathcal{K}^k")
        base_beta_T = VGroup(base_beta_T_0,
                             base_beta_T_1,
                             base_beta_T_2,
                             base_beta_T_3,
                             base_beta_T_4,
                             base_beta_T_5,
                             base_beta_T_6,
                             base_beta_T_7,
                             base_beta_T_8
                            ).arrange(direction=RIGHT, buff=0.15, center=False).move_to(UP)
        base_propiedades_T = Tex(
                                "$\\langle \\beta\\rangle = V$",
                                "$,\\,\\beta$ es l.i."
                                )
        combination_T_0 = ntup.copy()
        combination_T_1 = MathTex("=")
        combination_T_2 = MathTex("c_1")
        combination_T_3 = ntup1.copy()
        combination_T_4 = MathTex("+")
        combination_T_5 = MathTex("\\cdots")
        combination_T_6 = MathTex("+")
        combination_T_7 = MathTex("c_k")
        combination_T_8 = ntup2.copy()
        combination_T = VGroup(
                                combination_T_0,
                                combination_T_1,
                                combination_T_2,
                                combination_T_3,
                                combination_T_4,
                                combination_T_5,
                                combination_T_6,
                                combination_T_7,
                                combination_T_8
                            ).arrange(direction=RIGHT, buff=0.15, center=False)
        coeficientes_c_T = Tex("¿",
                            r"$c_i$",
                            "?")
        group_ntuplas = VGroup(base_beta_T, #0
                                base_propiedades_T, #1
                                combination_T, #2
                                coeficientes_c_T #3
                            ).scale(0.5).shift(4*LEFT+UP)
        group_ntuplas.arrange(0.7*DOWN, center=False, aligned_edge=LEFT)
        group_ntuplas.align_to(group_matrices, LEFT)

        #-------------------------------------------  N-TUPLAS k+1

        entries_ntup_kmas1 = [["v_{1}"], ["v_{2}"],["\\vdots"],["v_{k}"], ["v_{k+1}"]]  
        ntup_kmas1 = Matrix(entries_ntup_kmas1,
                    left_bracket="\\big(",
                    right_bracket="\\big)")
        entries_ntup1_kmas1 = [["v_{1}^1"], ["v_{2}^1"],["\\vdots"],["v_{k}^1"], ["v_{k+1}^1"]]  
        ntup1_kmas1 = Matrix(entries_ntup1_kmas1,
                    left_bracket="\\big(",
                    right_bracket="\\big)")
        entries_ntup2_kmas1  = [["v_{1}^k"], ["v_{2}^k"],["\\vdots"],["v_{k}^k"], ["v_{k+1}^k"]] 
        ntup2_kmas1  = Matrix(entries_ntup2_kmas1,
                    left_bracket="\\big(",
                    right_bracket="\\big)")
        entries_ntup3_kmas1  = [["v_{1}^{k+1}"], ["v_{2}^{k+1}"],["\\vdots"],["v_{k}^{k+1}"], ["v_{k+1}^{k+1}"]] 
        ntup3_kmas1  = Matrix(entries_ntup3_kmas1,
                    left_bracket="\\big(",
                    right_bracket="\\big)")
        base_beta_T_kmas1_0 = MathTex("\\beta")
        base_beta_T_kmas1_1 = MathTex("=")
        base_beta_T_kmas1_3 = ntup1_kmas1.copy()
        base_beta_T_kmas1_2 = Brace(base_beta_T_kmas1_3, LEFT)
        base_beta_T_kmas1_4 = MathTex(",\\cdots,")
        base_beta_T_kmas1_5 = ntup2_kmas1.copy()
        base_beta_T_kmas1_6 = MathTex(", ")
        base_beta_T_kmas1_7 = ntup3_kmas1.copy()
        base_beta_T_kmas1_8 = Brace(base_beta_T_kmas1_7, RIGHT)
        base_beta_T_kmas1_9 = Tex(" base de ")
        base_beta_T_kmas1_10 = MathTex("\\mathcal{K}^{k+1}")
    
        base_beta_T_kmas1 = VGroup(base_beta_T_kmas1_0,
                                    base_beta_T_kmas1_1,
                                    base_beta_T_kmas1_2,
                                    base_beta_T_kmas1_3,
                                    base_beta_T_kmas1_4,
                                    base_beta_T_kmas1_5,
                                    base_beta_T_kmas1_6,
                                    base_beta_T_kmas1_7,
                                    base_beta_T_kmas1_8,
                                    base_beta_T_kmas1_9,
                                    base_beta_T_kmas1_10
                                ).arrange(direction=RIGHT, buff=0.15, center=False).move_to(UP)
        base_propiedades_T_kmas1 = Tex(
                                    "$\\langle \\beta\\rangle = V$",
                                    "$,\\,\\beta$ es l.i."
                                    )
        combination_T_kmas1_0 = ntup_kmas1.copy()
        combination_T_kmas1_1 = MathTex("=")
        combination_T_kmas1_2 = MathTex("c_1")
        combination_T_kmas1_3 = ntup1_kmas1.copy()
        combination_T_kmas1_4 = MathTex("+")
        combination_T_kmas1_5 = MathTex("\\cdots")
        combination_T_kmas1_6 = MathTex("+")
        combination_T_kmas1_7 = MathTex("c_k")
        combination_T_kmas1_8 = ntup2_kmas1.copy()
        combination_T_kmas1_9 = MathTex("+")
        combination_T_kmas1_10 = MathTex("c_{k+1}")
        combination_T_kmas1_11 = ntup3_kmas1.copy()
        combination_T_kmas1 = VGroup(
                                    combination_T_kmas1_0,
                                    combination_T_kmas1_1,
                                    combination_T_kmas1_2,
                                    combination_T_kmas1_3,
                                    combination_T_kmas1_4,
                                    combination_T_kmas1_5,
                                    combination_T_kmas1_6,
                                    combination_T_kmas1_7,
                                    combination_T_kmas1_8,
                                    combination_T_kmas1_9,
                                    combination_T_kmas1_10,
                                    combination_T_kmas1_11
                                    ).arrange(direction=RIGHT, buff=0.15, center=False)
        coeficientes_c_T_kmas1 = Tex("¿",
                            r"$c_i$",
                            "?")
        group_ntuplas_kmas1 = VGroup(base_beta_T_kmas1, #0
                                    base_propiedades_T_kmas1, #1
                                    combination_T_kmas1, #2
                                    coeficientes_c_T_kmas1 #3
                                ).scale(0.5).shift(4*LEFT+UP)
        group_ntuplas_kmas1.arrange(0.7*DOWN, center=False, aligned_edge=LEFT)
        group_ntuplas_kmas1.align_to(group_matrices, LEFT)
        #----------------------------------- SISTEMA DE ECUACIONES y RUN TIME COMPLEXITY O(n^3)

        
        #----------------------------------Animaciones
        self.play(FadeIn(group), run_time = 2)
        self.play(FadeOut(group[1]),
        FadeOut(group[3]),
        run_time = 2 
        )
        #Transformación vector general -> funciones
        self.play(
            ReplacementTransform(group[0], group_funciones[0]),
            ReplacementTransform(group[2], group_funciones[2]),
            run_time = 2
        )
        #Transformación vector funciones -> matrices
        self.play(
            ReplacementTransform(group_funciones[0], group_matrices[0]),
            ReplacementTransform(group_funciones[2], group_matrices[2]),
            run_time = 2
        )
        #Transformación vector matrices -> ntuplas
        self.play(
            ReplacementTransform(group_matrices[0][:], group_ntuplas[0][:]),
            ReplacementTransform(group_matrices[2][:], group_ntuplas[2][:]),
            run_time = 2
        )
        #Incremento en la dimensión de las ntuplas k -> k+1
        self.play(
            #Transformación de la base
            ReplacementTransform(group_ntuplas[0][:6], group_ntuplas_kmas1[0][:6]), #Primeros elementos coincidentes
            ReplacementTransform(group_ntuplas[0][6], group_ntuplas_kmas1[0][8]), #Braces
            ReplacementTransform(group_ntuplas[0][7:], group_ntuplas_kmas1[0][9:]), # base de K**k -> base de K**k+1
            #Transformación de la combinación lineal
            ReplacementTransform(group_ntuplas[2][:], group_ntuplas_kmas1[2][:9]),
            run_time = 2
        )
        self.play(
            #Transformación de la base
            FadeIn(group_ntuplas_kmas1[0][6:8]), #Coma y nuevo elemento faltante
            #Transformación de la combinación lineal
            FadeIn(group_ntuplas_kmas1[2][9:]),
            run_time = 1
        )
        #--------------------------------
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time = 1)
    def construct(self):
        self.parte_3()