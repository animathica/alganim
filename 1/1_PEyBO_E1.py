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
VERDE = '#1FFF00'
MAGENTA = '#FF00FF'
AMARILLO = "#FFFF00"
GRIS = "#888888"
MAGENTA_CLARO = "#FF67FF"
AZUL_CLARO = "#9CDCEB"
AZUL_OSCURO = "#1C758A"
TEAL_A = "#ACEAD7"
TEAL_E = "#49A88F"
MOSTAZA_OSCURO = "#FFD025"
MOSTAZA_CLARO = "#FFE072"


'''
Esta primera escena consta de tres partes:
INTRODUCCIÓN
ESCENA GEOMÉTRICA EN R^2
PLANTEAMIENTO DEL PROBLEMA EN GENERAL Y SEGÚN LA DIMENSIÓN QUE SE CONSIDERE
'''

class Subescena_1(Scene):
    def parte_1(self):
        #----------------------------------- ESPACIO V EN GENERAL
        dim_V = MathTex("\\text{dim}\\left(V\\right)=k<\\infty").scale(0.8).to_edge(UP)
        base_beta = Tex(
            "$\\beta = \\{\\vec{b}_1,..., \\vec{b}_k\\}$", #0
            " base de ", #1
            "$V$" #2
        ).move_to(UP)

        base_propiedades = Tex(
            "$\\langle \\beta\\rangle = V$",
            "$,\\,\\beta$ es l.i."
        )
        combination_0 = MathTex("\\vec{v}") #0
        combination_1 = MathTex("=") #1
        combination_2 = MathTex("c_1") #2
        combination_3 = MathTex("\\vec{b}_1") #3
        combination_4 = MathTex("+") #4
        combination_5 = MathTex("\\cdots") #5
        combination_6 = MathTex("+") #6
        combination_7 = MathTex("c_k") #7
        combination_8 = MathTex("\\vec{b}_k") #8

        combination = VGroup(combination_0, combination_1, combination_2, combination_3, combination_4,\
                        combination_5, combination_6, combination_7, combination_8).arrange(direction=RIGHT, buff=0.15, center=False)
        coeficientes_c = Tex("¿",
                            r"$c_1, ..., c_k$",
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
        def EncontrarEscalares(Vec1,VecObj1, text_A, Vec2, VecObj2, text_B, vecobjetivo, text_vecobjetivo):
            #Colores para los vectores escalados
            col1 = VecObj1.get_color()
            col2 = VecObj2.get_color()
            col3 = VERDE
            #Recta numérica a lo largo de la cual se desplazan los escalares
            real_numbers = MathTex("\\mathbb{R}").set_color(MAGENTA_CLARO).scale(0.8)
            number_line = NumberLine(color = MAGENTA_CLARO, rotation = PI/2, include_numbers = True, label_direction = RIGHT, x_range=[-3, 3, 1]).move_to(np.array([5.5,-1.8,0])).scale(0.5)
            real_numbers.next_to(number_line, 0.3*UP)
            pointerVec_1 = Vector(RIGHT).scale(0.4)
            label_1 = MathTex("c_1").add_updater(lambda m: m.next_to(pointerVec_1, 0.3*LEFT))
            pointerVec_2 = Vector(LEFT).scale(0.4)
            label_2 = MathTex("c_2").add_updater(lambda m: m.next_to(pointerVec_2, 0.3*RIGHT))
            # ValueTrackers para vector 1 y vector 2, respectivamente
            t1 = ValueTracker(1)
            t2 = ValueTracker(1)
            #Updaters para los sliders sobre la recta real 
            pointerVec_1.add_updater(
                lambda m: m.next_to(
                            number_line.n2p(t1.get_value()),
                            0.5*LEFT
                )
            )
            pointerVec_2.add_updater(
                lambda m: m.next_to(
                            number_line.n2p(t2.get_value()),
                            1.7*RIGHT
                )
            )
            slidersBox = SurroundingRectangle(VGroup(real_numbers, number_line,\
                                                    ), color=WHITE, fill_color=BLACK, fill_opacity = 1, buff = 0.5)
            Sliders = VGroup(slidersBox, real_numbers, number_line, label_1, pointerVec_1, label_2, pointerVec_2)
            #Escalares
            label1 = MathTex("c_1")
            label2 = MathTex("c_2")
            #vector suma
            Vec1plusVec2 = Vec1+Vec2
            Vec_AplusB = Arrow((0, 0, 0), Vec1plusVec2, buff=0, color = col3)
            #distancias de separación entre puntas de vectores y texto
            dist_1 = 0.4*Vec1/(np.linalg.norm(Vec1))
            dist_2 = 0.4*Vec2/(np.linalg.norm(Vec2))
            dist_3 = 0.4*Vec1plusVec2/(np.linalg.norm(Vec1plusVec2))
            #Etiqueta de la suma
            plus_sign = MathTex("+").move_to(Vec_AplusB.get_end()+dist_3)
            label_sum1 = MathTex("c_2").next_to(plus_sign, 0.5*RIGHT)
            label_sum2 = text_B.copy().next_to(label_sum1, 0.5*RIGHT)
            label_sum3 = text_A.copy().next_to(plus_sign, 0.5*LEFT)
            label_sum4 = MathTex("c_1").next_to(label_sum3, 0.5*LEFT)
            label3 = VGroup(plus_sign, label_sum1, label_sum2, label_sum3, label_sum4).move_to(Vec_AplusB.get_end()+dist_3)
            #Otros símbolos utilizados
            equal_sign = MathTex("=")

            def upd_for_vec1(obj):
                NewVec = Arrow((0,0,0), t1.get_value()*Vec1, buff=0, color = col1)
                obj.become(NewVec)

            def upd_for_vec2(obj):
                NewVec = Arrow((0,0,0), t2.get_value()*Vec2, buff=0, color = col2)
                obj.become(NewVec)

            def upd_for_vec3(obj):
                NewVec = Arrow((0,0,0), t1.get_value()*Vec1+t2.get_value()*Vec2, buff=0, color = col3)
                obj.become(NewVec)

            def upd_for_text1(obj):
                obj.move_to(VecObj1.get_end()+dist_1)
                
            def upd_for_text2(obj):
                obj.move_to(VecObj2.get_end()+dist_2)
            
            def upd_for_text3(obj):
                obj.move_to(Vec_AplusB.get_end()+dist_3)

            def upd_for_label1(obj):
                obj.next_to(text_A, 0.5*LEFT)

            def upd_for_label2(obj):
                obj.next_to(text_B, 0.5*LEFT)

            VecObj1.add_updater(upd_for_vec1)
            label1.add_updater(upd_for_label1)
            text_A.add_updater(upd_for_text1)

            VecObj2.add_updater(upd_for_vec2)
            text_B.add_updater(upd_for_text2)
            label2.add_updater(upd_for_label2)

            Vec_AplusB.add_updater(upd_for_vec3)
            label3.add_updater(upd_for_text3)

            #Obtención de los escalares resolviendo el sistema de ecuaciones:
            A=np.array([Vec1[:2], Vec2[:2]]).T
            b=np.array(vecobjetivo[:2])
            c=np.linalg.solve(A,b)
            #Animaciones
            self.play(FadeIn(label1.next_to(text_A, 0.5*LEFT)),
            FadeIn(label2.next_to(text_B, 0.5*LEFT)),
            Write(Vec_AplusB),
            FadeIn(label3),
            run_time = 2
            )
            self.play(FadeIn(Sliders))
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
            FadeOut(text_vecobjetivo),
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
            self.play(t1.animate.set_value(c[0]), 
            t2.animate.set_value(c[1]),
            run_time = 2.0)
            self.wait(0.5)
            equal_sign.next_to(label3, 0.5*LEFT)
            text_vecobjetivo.next_to(equal_sign, 0.5*LEFT)
            #Puntos para destello
            dot1 = Dot(radius = 0, color=AMARILLO).next_to(label1, 2*UP)
            dot2 = Dot(radius = 0, color=AMARILLO).next_to(label2, 2*UP)
            self.play(Circumscribe(label1, fade_out=True), 
            Circumscribe(label2, fade_out=True),
            Flash(dot1), 
            Flash(dot2),
            FadeIn(equal_sign),
            FadeIn(text_vecobjetivo),
            run_time = 2.5)
            self.play(
            FadeOut(VecObj1),
            FadeOut(VecObj2),
            FadeOut(Vec_AplusB),
            *[FadeOut(mob) for mob in self.mobjects],
            run_time = 1)
        

        # Coordenadas del vector objetivo
        vec = np.array([5,3,0])
        # Coordenadas de vector A
        vec_A = np.array([-2,2,0])
        # Coordenadas de vector B
        vec_B = np.array([3,1,0])

        grid = NumberPlane()
        Vec = Arrow((0, 0, 0), vec, buff=0,color=NARANJA)
        VecA = Arrow((0, 0, 0), vec_A, buff=0,color=AZUL)
        VecB = Arrow((0, 0, 0), vec_B, buff=0,color=ROJO)

        text_vec = MathTex("\\vec{v}").move_to(Vec.get_end()+0.4*vec/(np.linalg.norm(vec)))
        text_A = MathTex("\\vec{b}_1").move_to(VecA.get_end()+0.4*vec_A/(np.linalg.norm(vec_A)))
        text_B = MathTex("\\vec{b}_2").move_to(VecB.get_end()+0.4*vec_B/(np.linalg.norm(vec_B)))

        generado_vecA = DashedLine(-5*vec_A, 5*vec_A, color = MAGENTA, buff = 0)
        generado_vecB = DashedLine(-5*vec_B, 5*vec_B, color = MAGENTA, buff = 0)
        Ejes_AB = VGroup(generado_vecA, generado_vecB)
        self.play(Write(grid))
        self.wait(0.5)
        self.play(FadeIn(Vec))
        self.play(Write(text_vec))
        self.play(FadeIn(VecA), Write(text_A), FadeIn(VecB), Write(text_B))
        self.wait(0.65)
        EncontrarEscalares(vec_A,VecA, text_A, vec_B,VecB, text_B, vec, text_vec)
        self.wait(0.65)
    def construct(self):
        self.parte_2()
#-------------------------------------------------------------------------------------------------------
class Subescena_3(Scene):
    def parte_3(self):
        #----------------------------------- ESPACIO V EN GENERAL
        dim_V = MathTex("\\text{dim}\\left(V\\right)=k<\\infty").scale(0.8).to_edge(UP)
        base_beta = Tex(
            "$\\beta = \\{\\vec{b}_1,..., \\vec{b}_k\\}$", #0
            " base de ", #1
            "$V$" #2
        ).move_to(UP)

        base_propiedades = Tex(
            "$\\langle \\beta\\rangle = V$",
            "$,\\,\\beta$ es l.i."
        )
        combination_0 = MathTex("\\vec{v}") #0
        combination_1 = MathTex("=") #1
        combination_2 = MathTex("c_1") #2
        combination_3 = MathTex("\\vec{b}_1") #3
        combination_4 = MathTex("+") #4
        combination_5 = MathTex("\\cdots") #5
        combination_6 = MathTex("+") #6
        combination_7 = MathTex("c_k") #7
        combination_8 = MathTex("\\vec{b}_k") #8

        combination = VGroup(combination_0, combination_1, combination_2, combination_3, combination_4,\
                        combination_5, combination_6, combination_7, combination_8).arrange(direction=RIGHT, buff=0.15, center=False)
        coeficientes_c = Tex("¿",
                            r"$c_1, ..., c_k$",
                            "?")
        group_1 = VGroup(base_beta, base_propiedades, combination, coeficientes_c).scale(0.8)
        group_1.arrange(1*DOWN, center=False, aligned_edge=LEFT)
        coeficientes_ci = Tex("¿",
                            "$c_i$",
                            "?").scale(0.8).align_to(group_1[3], LEFT).align_to(group_1[3], UP)
        combination_copy = group_1[2].copy()
        #----------------------------------- POSIBILIDADADES PARA EL VECTOR v
        #FUNCIONES
        combination_function_0 = MathTex("\\vec{v}")
        combination_function_1 = MathTex("=")
        combination_function_2 = MathTex("c_1")
        combination_function_3 = MathTex("f")
        combination_function_4 = MathTex("+")
        combination_function_5 = MathTex("\\cdots")
        combination_function_6 = MathTex("+")
        combination_function_7 = MathTex("c_k")
        combination_function_8 = MathTex("g")
        combination_function = VGroup(combination_function_0, combination_function_1, combination_function_2,\
             combination_function_3, combination_function_4, combination_function_5,\
            combination_function_6, combination_function_7, combination_function_8).scale(0.8).arrange(direction=RIGHT, buff=0.15, center=False)
        combination_function.align_to(group_1[2],LEFT)
        combination_function.shift(2*LEFT)

        #N-TUPLAS
        entries_ntup1 = [["v_{1}"], ["v_{2}"],["\\vdots"],["v_{k}"]]  
        ntup1 = Matrix(entries_ntup1,
                    left_bracket="\\big(",
                    right_bracket="\\big)")

        entries_ntup2 = [["w_{1}"], ["w_{2}"],["\\vdots"],["w_{k}"]] 
        ntup2 = Matrix(entries_ntup2,
                    left_bracket="\\big(",
                    right_bracket="\\big)")

        combination_ntup_0 = MathTex("\\vec{v}")
        combination_ntup_1 = MathTex("=")
        combination_ntup_2 = MathTex("c_1")
        combination_ntup_3 = ntup1.copy()
        combination_ntup_4 = MathTex("+")
        combination_ntup_5 = MathTex("\\cdots")
        combination_ntup_6 = MathTex("+")
        combination_ntup_7 = MathTex("c_k")
        combination_ntup_8 = ntup2.copy()
        combination_ntup = VGroup(combination_ntup_0, combination_ntup_1, combination_ntup_2, combination_ntup_3,\
            combination_ntup_4, combination_ntup_5,\
            combination_ntup_6, combination_ntup_7, combination_ntup_8).scale(0.8).arrange(direction=RIGHT, buff=0.15, center=False)
        combination_ntup.align_to(group_1[2],LEFT)
        combination_ntup.shift(2*LEFT)

        #MATRIX
        entries1 = [["a_{11}", "\\cdots","a_{12}"],\
            ["\\vdots", "\\ddots","\\vdots"],\
            ["a_{1n}", "\\cdots","a_{nn}"],\
            ]
                
        m1 = Matrix(entries1,
                    left_bracket="\\big(",
                    right_bracket="\\big)")
        entries2 = [["z_{11}", "\\cdots","z_{12}"],\
            ["\\vdots", "\\ddots","\\vdots"],\
            ["z_{1n}", "\\cdots","z_{nn}"],\
            ]
        m2 = Matrix(entries2,
                    left_bracket="\\big(",
                    right_bracket="\\big)")

        combination_matrix_0 = MathTex("\\vec{v}")
        combination_matrix_1 = MathTex("=")
        combination_matrix_2 = MathTex("c_1")
        combination_matrix_3 = m1.copy()
        combination_matrix_4 = MathTex("+")
        combination_matrix_5 = MathTex("\\cdots")
        combination_matrix_6 = MathTex("+")
        combination_matrix_7 = MathTex("c_k")
        combination_matrix_8 = m2.copy()
        combination_matrix = VGroup(combination_matrix_0, combination_matrix_1, combination_matrix_2, combination_matrix_3,\
            combination_matrix_4, combination_matrix_5,\
            combination_matrix_6, combination_matrix_7, combination_matrix_8).scale(0.8).arrange(direction=RIGHT, buff=0.15, center=False)
        combination_matrix.align_to(group_1[2],LEFT)
        combination_matrix.shift(2*LEFT)
        #----------------------------------- SISTEMA DE ECUACIONES y RUN TIME COMPLEXITY O(n^3)
        v = MathTex(r"\vec{v} = ").scale(0.8).move_to(5*LEFT)
        #entradas posibles vectores

        v_posib_ent = [[["v_{1}"], ["v_{2}"]]]
        v_possib_mat = [Matrix(v_posib_ent[0],left_bracket="\\big(",right_bracket="\\big)").set_color(AZUL).scale(0.8).next_to(v)]

        #Se crean listas de las posibilidades
        for i in range(1, 6):
            v_posib_ent_aux = v_posib_ent[i-1].copy()
            v_posib_ent_aux.append(["v_{:}".format(i+2)])
            v_posib_ent.append(v_posib_ent_aux)
            v_possib_mat.append(Matrix(v_posib_ent_aux,left_bracket="\\big(",right_bracket="\\big)").set_color(AZUL).scale(0.8).next_to(v))
        #Para convertir la última n-tupla en una n-tupla en abstracto
        v_possib_mat_last = Matrix([["v_{1}"], ["v_{2}"],["\\vdots"],["v_{k}"]],
                    left_bracket="\\big(",
                    right_bracket="\\big)").scale(0.8).next_to(v).set_color(AZUL)
        #Sistema de ecuaciones
        sis_row1 = MathTex(r"v_1", " = ","c_1","v_{11}","+","c_2","v_{21}", "+", "c_3","v_{31}","+", "c_4","v_{41}",\
                            "+", "c_5","v_{51}","+", "c_6","v_{61}","+", "c_7","v_{71}")
        sis_row2 = MathTex(r"v_2", " = ","c_1","v_{12}","+","c_2","v_{22}", "+", "c_3","v_{32}","+", "c_4","v_{42}",\
                            "+", "c_5","v_{52}","+", "c_6","v_{62}","+", "c_7","v_{72}")
        sis_row3 = MathTex(r"v_3", " = ","c_1","v_{13}","+","c_2","v_{23}", "+", "c_3","v_{33}","+", "c_4","v_{43}",\
                            "+", "c_5","v_{53}","+", "c_6","v_{63}","+", "c_7","v_{73}")
        sis_row4 = MathTex(r"v_4", " = ","c_1","v_{14}","+","c_2","v_{24}", "+", "c_3","v_{34}","+", "c_4","v_{44}",\
                            "+", "c_5","v_{54}","+", "c_6","v_{64}","+", "c_7","v_{74}")
        sis_row5 = MathTex(r"v_5"," = ","c_1","v_{15}","+","c_2","v_{25}", "+", "c_3","v_{35}","+", "c_4","v_{45}",\
                            "+", "c_5","v_{55}","+", "c_6","v_{65}","+", "c_7","v_{75}")
        sis_row6 = MathTex(r"v_6", " = ","c_1","v_{16}","+","c_2","v_{26}", "+", "c_3","v_{36}","+", "c_4","v_{46}",\
                            "+", "c_5","v_{56}","+", "c_6","v_{66}","+", "c_7","v_{76}")
        sis_row7 = MathTex(r"v_7", " = ","c_1","v_{17}","+","c_2","v_{27}", "+", "c_3","v_{37}","+", "c_4","v_{47}",\
                            "+", "c_5","v_{57}","+", "c_6","v_{67}","+", "c_7","v_{77}")
        sist_group = VGroup(sis_row1, sis_row2, sis_row3, sis_row4, sis_row5, sis_row6, sis_row7).scale(0.6).move_to(2*RIGHT+3*UP)
        sist_group.arrange(0.7*DOWN, center=False, aligned_edge=LEFT)
        
        #2, 5, 8, 11, 14, 17, 20 --------> color de las constantes
        for i in range(len(sist_group)):
            sist_group[i][0].set_color(AZUL)
            for j in range(2, 21, 3):
                sist_group[i][j].set_color(ROJO)
        #Sistema en abstracto:
        s1 = MathTex(r"v_1"," = ","c_1", "v_{11}","+","c_2", "v_{21}", "+", "\cdots","+","c_k", "v_{k1}")
        s2 = MathTex(r"v_2"," = ","c_1", "v_{12}","+","c_2", "v_{22}", "+", "\cdots","+","c_k", "v_{k2}")
        s3 = MathTex(r"v_2"," = ","c_1v_{12}","+","c_2v_{22}", "+", "..", r"\vdots","..","+","c_kv_{k2}")
        s4 = MathTex(r"v_k"," = ","c_1", "v_{1k}","+","c_2", "v_{2k}", "+", "\cdots","+","c_k", "v_{kk}")

        s_group = VGroup(s1, s2, s3, s4).scale(0.6).move_to(2*RIGHT+UP)
        s_group.arrange(0.7*DOWN, center=False, aligned_edge=LEFT)

        for i in range(4):
            s_group[i][0].set_color(AZUL)
        for i in range(len(s_group)):
            if i != 2:
                s_group[i][2].set_color(ROJO)
                s_group[i][5].set_color(ROJO)
                s_group[i][10].set_color(ROJO)

        s_group[2][:2].set_opacity(0)
        s_group[2][2].set_opacity(0)
        s_group[2][4].set_opacity(0)
        s_group[2][6].set_opacity(0)
        s_group[2][8].set_opacity(0)
        s_group[2][10].set_opacity(0)

        brace_s = Brace(s_group[:], LEFT)

        list_braces = []
        list_braces.append(Brace(sist_group[:2], LEFT))

        for i in range(3, 8):
            list_braces.append(Brace(sist_group[:i], LEFT))
        
        #Complejidad tracker
        big_o = MathTex(r"\mathcal{O}",r"\left(", r"2^3",r"\right)").move_to(2*DOWN)
        sust_3 = MathTex(r"\mathcal{O}",r"\left(", r"3^3",r"\right)").move_to(2*DOWN)
        sust_4 = MathTex(r"\mathcal{O}",r"\left(", r"4^3",r"\right)").move_to(2*DOWN)
        sust_5 = MathTex(r"\mathcal{O}",r"\left(", r"5^3",r"\right)").move_to(2*DOWN)
        sust_6 = MathTex(r"\mathcal{O}",r"\left(", r"6^3",r"\right)").move_to(2*DOWN)
        sust_7 = MathTex(r"\mathcal{O}",r"\left(", r"7^3",r"\right)").move_to(2*DOWN)
        sust_k = MathTex(r"\mathcal{O}",r"\left(", r"k^3",r"\right)").move_to(2*DOWN)

        #----------------------------------Animaciones
        self.play(FadeIn(group_1), run_time = 2)
        self.play(FadeOut(group_1[:2]),
        FadeOut(group_1[3]),
        run_time = 2 
        )
        self.play(group_1[2][:].animate.shift(2*LEFT))
        self.play(Transform(group_1[2][:], combination_function[:]),
        run_time = 3)
        self.play(Transform(group_1[2][:], combination_ntup[:]),
        run_time = 3)
        self.play(Transform(group_1[2][:], combination_matrix[:]),
        run_time = 3)
        self.play(Transform(group_1[2][:], combination_copy),
        run_time = 3)
        self.play(
            FadeOut(group_1[2][:]),
            run_time = 1
        )
        #--------------------------------
        self.play(
                FadeIn(v),
                FadeIn(v_possib_mat[0]),
                FadeIn(list_braces[0]),
                FadeIn(sist_group[0][:7]),
                FadeIn(sist_group[1][:7]),
                Write(big_o),
                run_time = 2
        )
        self.wait(1)
        self.play(
                ReplacementTransform(v_possib_mat[0], v_possib_mat[1]),
                ReplacementTransform(list_braces[0], list_braces[1]),
                FadeIn(sist_group[2][:10]),
                FadeIn(sist_group[0][7:10]),
                FadeIn(sist_group[1][7:10]),
                Transform(big_o, sust_3),
                run_time = 2
        )

        self.wait(1)
        self.play(
                ReplacementTransform(v_possib_mat[1], v_possib_mat[2]),
                ReplacementTransform(list_braces[1], list_braces[2]),
                FadeIn(sist_group[3][:13]),
                FadeIn(sist_group[1][10:13]),
                FadeIn(sist_group[0][10:13]),
                FadeIn(sist_group[2][10:13]),
                Transform(big_o, sust_4),
                run_time = 2
        )
        self.wait(1)
        self.play(
                ReplacementTransform(v_possib_mat[2], v_possib_mat[3]),
                ReplacementTransform(list_braces[2], list_braces[3]),
                FadeIn(sist_group[4][:16]),
                FadeIn(sist_group[0][13:16]),
                FadeIn(sist_group[1][13:16]),
                FadeIn(sist_group[2][13:16]),
                FadeIn(sist_group[3][13:16]),
                Transform(big_o, sust_5),
                run_time = 2
        )

        self.wait(1)
        self.play(
                ReplacementTransform(v_possib_mat[3], v_possib_mat[4]),
                ReplacementTransform(list_braces[3], list_braces[4]),
                FadeIn(sist_group[5][:19]),
                FadeIn(sist_group[0][16:19]),
                FadeIn(sist_group[1][16:19]),
                FadeIn(sist_group[2][16:19]),
                FadeIn(sist_group[3][16:19]),
                FadeIn(sist_group[4][16:19]),
                Transform(big_o, sust_6),
                run_time = 2
        )
        self.play(
                ReplacementTransform(v_possib_mat[4], v_possib_mat[5]),
                ReplacementTransform(list_braces[4], list_braces[5]),
                FadeIn(sist_group[6][:22]),
                FadeIn(sist_group[0][19:22]),
                FadeIn(sist_group[1][19:22]),
                FadeIn(sist_group[2][19:22]),
                FadeIn(sist_group[3][19:22]),
                FadeIn(sist_group[4][19:22]),
                FadeIn(sist_group[5][19:22]),
                Transform(big_o, sust_7),
                run_time = 2
        )
        self.play(
                ReplacementTransform(v_possib_mat[-1], v_possib_mat_last),
                ReplacementTransform(sist_group, s_group),
                ReplacementTransform(list_braces[5], brace_s),
                Transform(big_o, sust_k),
            )
        self.wait(1.5)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time = 1)
    def construct(self):
        self.parte_3()