
from manimlib.imports import *


#####################################################################################
######################  Ortogonalización y ortonormalización  #######################
#####################################################################################

#####################################################################################
#################################  Primera escena  ##################################
#####################################################################################

class OO1(ThreeDScene):

    def acomodar_textos(self,objeto):
        self.add_fixed_in_frame_mobjects(objeto)
        self.play(Write(objeto))

    def construct(self):

        # Texto de prodcto escalar y su rectángulo.
        Text1 = TextMobject('''$ \\langle \\vec{a},\\vec{b} \\rangle \\ \\ \\neq \\vec{0} $''').move_to(2*UP + 4*LEFT)
        Text1.bg = SurroundingRectangle(Text1,color=WHITE,fill_color=BLACK,fill_opacity=1)
        Text1.group = VGroup(Text1.bg,Text1)
        Text1_1 = VGroup()
        for i in range(0,7):
            Text1_1.add(Text1[0][i])
        Text1_2 = VGroup(Text1[0][-1],Text1[0][-2],Text1[0][-3],Text1[0][-4])

        # Texto de proyección y su rectángulo.
        Text2 = TextMobject('''$ \\frac{ \\langle \\vec{a} , \\vec{b} \\rangle} { \\norm{ \\vec{b} } ^2} \\vec{b} \\neq \\vec{0} $''').move_to(2*UP + 4*LEFT).scale(1.2)
        Text2.bg = SurroundingRectangle(Text2,color=WHITE,fill_color=BLACK,fill_opacity=1)
        Text2.group = VGroup(Text2.bg,Text2)
        Text2_1 = VGroup()
        for i in range(0,7):
            Text2_1.add(Text2[0][i])
        Text2_2 = VGroup()
        for i in range(7,15):
            Text2_2.add(Text2[0][i])

        # Texto de conjunto inicial y su rectángulo.
        Cto = TextMobject('''$ S = \\{ \\vec{a}, \\vec{b} \\} $''').move_to(1.5*DOWN + 3.5*RIGHT)
        Cto.bg = SurroundingRectangle(Cto,color=WHITE,fill_color=BLACK,fill_opacity=1)
        Cto.group = VGroup(Cto.bg,Cto)
        Cto_1 = VGroup(Cto[0][6].copy(),Cto[0][7].copy())

        # Texto de conjunto ortogonal y su rectángulo, con las variaciones usadas.
        CtoO = TextMobject('''$ S' = \\{ \\vec{b} \\} $''').move_to(2.5*DOWN + 3.5*RIGHT)
        CtoO[0][4].set_color(BLACK)
        CtoO[0][5].set_color(BLACK)
        CtoO.bg = SurroundingRectangle(CtoO,color=WHITE,fill_color=BLACK,fill_opacity=1)
        CtoO.group = VGroup(CtoO.bg,CtoO)
        CtoO_1 = VGroup(CtoO[0][4],CtoO[0][5])
        CtoO_1_1 = TextMobject('''$ S' = \\{ \\vec{b} \\} $''').move_to(2.5*DOWN + 3.5*RIGHT)
        CtoO_2 = TextMobject('''$ S' = \\{ \\vec{b} , \\vec{c} \\} $''').move_to(2.5*DOWN + 3.5*RIGHT)
        for i in range(6,9):
            CtoO_2[0][i].set_color(BLACK)
        CtoO_2_1 = TextMobject('''$ S' = \\{ \\vec{b} , \\vec{c} \\} $''').move_to(2.5*DOWN + 3.5*RIGHT)
        CtoO_3 = VGroup(CtoO_2[0][6],CtoO_2[0][7],CtoO_2[0][8])
        CtoO_2.bg = SurroundingRectangle(CtoO_2,color=WHITE,fill_color=BLACK,fill_opacity=1)

        # Textos para vector normalizado y sus rectángulos.
        Text3 = TextMobject(''' $ (x_b,y_b) $ ''').move_to(2*DOWN + 4*LEFT)
        Text3.bg = SurroundingRectangle(Text3,color=WHITE,fill_color=BLACK,fill_opacity=1)
        Text3_1 = TextMobject(''' $ \\norm{ \\left( \\frac{x_b}{\\norm{\\vec{b}}},\\frac{y_b}{\\norm{\\vec{b}}} \\right) } = 1 $ ''').move_to(2*DOWN + 4*LEFT)
        for i in range(0,4):
            Text3_1[0][i].set_color(BLACK)
        for i in range(1,7):
            Text3_1[0][-i].set_color(BLACK)
        Text3_2 = TextMobject(''' $ \\norm{ \\left( \\frac{x_b}{\\norm{\\vec{b}}},\\frac{y_b}{\\norm{\\vec{b}}} \\right) } = 1 $ ''').move_to(2*DOWN + 4*LEFT)
        Text3_3 = TextMobject(''' $ \\norm{\\vec{b}'} = 1 $ ''').move_to(2*DOWN + 4*LEFT)
        Text3_1.bg = SurroundingRectangle(Text3_2,color=WHITE,fill_color=BLACK,fill_opacity=1)
        Text3.group = VGroup(Text3.bg, Text3)
        Text3_3.bg = SurroundingRectangle(Text3_3,color=WHITE,fill_color=BLACK,fill_opacity=1)

        # Textos para proyección con normalizado y sus rectángulos.
        Text4 = TextMobject('''$ \\frac{ \\langle \\vec{a} , \\vec{b}' \\rangle} { \\norm{ \\vec{b}' } ^2} \\vec{b}' \\neq \\vec{0} $''').move_to(2*UP + 4*LEFT).scale(1.2)
        Text4.bg = SurroundingRectangle(Text4,color=WHITE,fill_color=BLACK,fill_opacity=1)
        #for i in range(1,5):
        #    Text4[0][-i].set_color(BLACK)
        Text4_b = VGroup()
        for i in range(9,14):
            Text4_b.add(Text4[0][i])
        Text4_1 = TextMobject('''$ \\frac{ \\langle \\vec{a} , \\vec{b}' \\rangle} { 1 } \\vec{b}' \\neq \\vec{0} $''').move_to(2*UP + 4*LEFT).scale(1.2)
        Text4_2 = TextMobject('''$  \\langle \\vec{a} , \\vec{b}' \\rangle \\vec{b}' \\neq \\vec{0} $''').move_to(2*UP + 4*LEFT)

        grid = NumberPlane()

        # Coordenadas de vector A
        a_1 = 1
        a_2 = 3
        
        # Coordenadas de vector B
        b_1 = 5
        b_2 = 2

        # Vectores A y B, con sus etiquetas.
        VecA = Arrow((0, 0, 0), a_1 * RIGHT + a_2*UP, buff=0,color=BLUE)
        VecB = Arrow((0, 0, 0),b_1 * RIGHT + b_2*UP, buff=0,color=RED)
        VecALab=TexMobject("\\vec{a}").move_to(VecA.get_end()+0.5*LEFT)
        VecBLab=TexMobject("\\vec{b}").move_to(VecB.get_end()+0.5*RIGHT)

        # Texto para los vectores, con su rectángulo correspondiente.
        Text_B = TextMobject('''$\\vec{b} = (5,2)$''').move_to(3*DOWN + 4*LEFT)
        Text_A = TextMobject('''$\\vec{a} = (1,3)$''').next_to(Text_B, UP)
        Text_Vec = VGroup(Text_B,Text_A)
        VecBox = SurroundingRectangle(Text_Vec,color=WHITE,fill_color=BLACK,fill_opacity=1)
        VecBox.group = VGroup(VecBox,Text_Vec)

        # Función para calcular intersección entre rectas.
        def line_intersection(line1, line2):
            xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
            ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

            def det(a, b):
                return a[0] * b[1] - a[1] * b[0]

            div = det(xdiff, ydiff)

            d = (det(*line1), det(*line2))
            x = det(d, xdiff) / div
            y = det(d, ydiff) / div
            return([x, y])

        # Función para la luz usada para la proyección.
        # (x1,y1) es el vector proyectado, (x2,y2) es sobre el que se proyecta.
        # n es la cantidad de líneas que se generan para colorear la zona iluminada.
        def light(x1,y1,x2,y2,n = 10):
            # Coordenadas de un vector ortogonal a (x2,y2)
            x2o = -y2
            y2o = x2
            # Lista donde se guarda cada "rayo" de luz.
            rays = []
            # Lista donde se guardan las coordenadas de cada rayo:
            rayc = []
            # Se calcula la proyección.
            p1 = ((x1*x2 + y1*y2)/(x2**2 + y2**2)) * x2
            p2 = ((x1*x2 + y1*y2)/(x2**2 + y2**2)) * y2
            proy = [p1,p2]
            norma_proy = np.sqrt(p1**2 + p2**2)
            # Se generan las coordenadas de cada rayo y se agregan a la lista.
            for i in range(0,n+1):
                r1 = 0 + i*(x2/n)
                r2 = 0 + i*(y2/n)
                nr = np.sqrt(r1**2 + r2**2)
                if nr < norma_proy:
                    inter = line_intersection(((0,0),(x1,y1)),((r1,r2),(r1 + x2o,r2 + y2o)))
                    rayc.append([inter[0],inter[1]])                
                else:
                    rayc.append([r1,r2])
            # Se genera cada rayo.
            for i in rayc:
                rayo = Line( [i[0]+x2o,i[1]+y2o,0], [i[0],i[1],0], width=5, stroke_width=5 , buff = 0.05).set_color(WHITE).set_color(color=[WHITE,"#8f8f8f"])
                #rayo = Line( [i[0]+x2o,i[1]+y2o,0], [i[0],i[1],0], width=5, stroke_width=5 , buff = 0.05).set_color(WHITE)
                rays.append(rayo)
            # Se hace un VGroup con los rayos.
            grupo = VGroup()
            for i in rays:
                grupo.add(i)
            return(grupo)

        # Objeto usado para la luz.
        luz = light(a_1,a_2,b_1,b_2,200)

        # Flecha de la proyección.
        p1 = ((a_1*b_1 + a_2*b_2)/(b_1**2 + b_2**2)) * b_1
        p2 = ((a_1*b_1 + a_2*b_2)/(b_1**2 + b_2**2)) * b_2
        VecP = Arrow((0, 0, 0),(p1,p2,0), color = GREEN_D, buff = 0)
                
        # Copia de proyección usada para la resta.
        VecPC = Arrow((a_1,a_2,0),(a_1-p1,a_2-p2,0), color = GREEN_D, buff = 0)

        # Vector resultante de la resta y su etiqueta.
        VecR = Arrow((0, 0, 0),(a_1-p1,a_2-p2,0), color = YELLOW, buff = 0)
        VecRLab = TextMobject('''$ \\vec{c} $''').move_to(VecR.get_end()+0.5*LEFT)

        # Eje para normalizar vector.
        Eje = DashedLine((0-5*b_1, 0-5*b_2, 0),(5*b_1,5*b_2,0), color = PURPLE, buff = 0)

        # Se normaliza vector B.
        # Norma de vector B.
        NorB = np.sqrt(b_1**2 + b_2**2)
        # Coordenadas de B normalizado.
        nb_1 = b_1/NorB
        nb_2 = b_2/NorB
        #Vector B normalizado y su etiqueta.
        VecBN = Arrow((0,0,0),(nb_1,nb_2,0), color = BLUE, buff = 0)
        VecBNLab = TextMobject(''' $ \\vec{b}' $ ''').move_to(VecB.get_end()+0.5*UP)

        # Arco para mostrar distancia r=1.
        # El ángulo hasta el que llega el arco.
        slope = (b_2/b_1)
        ang = np.arctan(slope)
        # Un ValueTracker para la longitud del arco.
        theta = ValueTracker(0)
        # El arco.
        arco = Arc(radius=1,angle=theta.get_value())
        # La función para cambiar el tamaño del arco.
        def upd_for_arc(arc):
            th = theta.get_value()
            new_arc = Arc(radius=1, angle=th)
            arc.become(new_arc)
        # Punto al final del arco.
        punto = Dot((np.cos(theta.get_value()),np.sin(theta.get_value()),0))
        # Función para posición del punto.
        def upd_for_dot(obj):
            th = theta.get_value()
            new_punto = Dot((np.cos(th),np.sin(th),0))
            punto.become(new_punto)


        ######################
        ####### Escena #######
        ######################

        self.play(Write(grid))
        self.wait(0.5)
        self.play(Write(VecBox),Write(Text_A))
        self.play(ShowCreation(VecA),Write(VecALab))
        self.wait()
        self.play(Write(Text_B))
        self.play(ShowCreation(VecB),Write(VecBLab))
        self.wait()
        self.play(Write(Cto.group))
        self.wait()
        self.play(Write(CtoO.group))
        self.wait()
        self.play(ReplacementTransform(CtoO,CtoO_1_1))
        #self.play(ReplacementTransform(Cto_1,CtoO_1),ReplacementTransform(CtoO,CtoO_1_1))
        self.wait()
        self.play(Write(Text1.group))
        self.add_foreground_mobject(Text1)
        self.wait()
        self.play(ReplacementTransform(Text1.bg,Text2.bg), runtime = 0.5)
        self.remove_foreground_mobject(Text1)
        self.play(ReplacementTransform(Text1_1,Text2_1),Write(Text2_2))
        self.wait()
        self.play(ShowCreation(luz))
        self.wait()
        self.play(ShowCreation(VecP), runtime=2)
        self.wait()
        self.play(FadeOut(luz))
        self.wait()
        self.play(ReplacementTransform(VecP,VecPC))
        self.wait()
        self.play(ShowCreation(VecR),Write(VecRLab))
        self.play(FadeOut(VGroup(VecPC,VecA,VecALab,VecBox.group)))
        self.wait()
        self.add_foreground_mobject(CtoO_1_1)
        self.play(ReplacementTransform(CtoO.bg,CtoO_2.bg))
        self.remove_foreground_mobject(CtoO_1_1)
        self.play(ReplacementTransform(CtoO_1_1,CtoO_2))
        self.wait()
        self.play(ReplacementTransform(CtoO_2,CtoO_2_1))
        #self.play(ReplacementTransform(VecRLab.copy(),CtoO_3),ReplacementTransform(CtoO_2,CtoO_2_1))
        self.wait()
        self.play(Write(Text3.group))
        self.wait()
        self.add_foreground_mobject(Text3)
        self.play(ReplacementTransform(Text3.bg,Text3_1.bg))
        self.remove_foreground_mobject(Text3)
        self.play(ReplacementTransform(Text3,Text3_1))
        self.wait()
        self.play(ReplacementTransform(Text3_1,Text3_2))
        self.wait()
        self.play(ReplacementTransform(Text3_2,Text3_3))
        self.wait()
        self.add_foreground_mobject(Text3_3)
        self.play(ReplacementTransform(Text3_1.bg,Text3_3.bg))
        self.wait()
        self.add_foreground_mobjects(Text3_3.bg,Text3_3)
        self.play(ShowCreation(Eje))
        self.wait()
        self.play(ShowCreation(arco),ShowCreation(punto))
        arco.add_updater(upd_for_arc)
        punto.add_updater(upd_for_dot)
        self.play(theta.set_value,ang,rate_func=linear)
        self.wait()
        self.play(ShowCreation(VecBN))
        self.wait()
        self.play(FadeOut(VGroup(Eje,arco,punto)))
        self.remove_foreground_mobjects(Text3_3.bg,Text3_3)
        self.wait()
        self.play(ReplacementTransform(Text2.bg,Text4.bg))
        self.play(ReplacementTransform(VGroup(Text2_1,Text2_2,Text1_2),Text4))
        self.wait()
        self.play(ReplacementTransform(Text4,Text4_1))
        self.wait()
        self.play(ReplacementTransform(Text4_1,Text4_2))
        self.wait()
        
	
#####################################################################################
#################################  Segunda escena  ##################################
#####################################################################################


def projection_of_a_along_b(vector_a, vector_b):
            vector_b_norm = np.sqrt(sum(vector_b**2))
            return (np.dot(vector_a, vector_b)/vector_b_norm**2)*vector_b

class segundaescena(ThreeDScene):
                
    def construct(self):
        axis_config = {
            "y_max" : 5,
            "y_min" : 0,
            "x_max" : 4,
            "x_min" : 0,
            "z_max" : 3,
            "z_min" : 0,
        }
        axes = ThreeDAxes(**axis_config)

        
        text1 = TexMobject(r"\langle \ \vec{b}, \vec{a} \ \rangle \neq 0").move_to(2*DOWN+4*RIGHT)
        text1_bg=VGroup(SurroundingRectangle(text1, color=WHITE, fill_color=BLACK, fill_opacity=1), text1)
        text2 = TexMobject(r"\vec{a}").move_to(DOWN+6*LEFT).scale(1.5)
        text2[0].set_color(AZUL)
        text3 = TexMobject(r"\vec{b}").next_to(text2, DOWN).scale(1.5)
        text3[0].set_color(ROJO)
        text4 = TexMobject(r"\vec{c}").next_to(text3, DOWN).scale(1.5)
        text4[0].set_color(NARANJA)
        text_group = VGroup(text2, text3, text4)
        text_bg=SurroundingRectangle(text_group, color=WHITE, fill_color=BLACK, fill_opacity=1) 
        text5 = TexMobject(r" \langle \ \vec{c}, \vec{a} \ \rangle  \neq 0").next_to(text1, DOWN)
        text5_bg=VGroup(SurroundingRectangle(text5, color=WHITE, fill_color=BLACK, fill_opacity=1), text5)
        text6 = TexMobject(r'''S = \qty\Big{\vec{a}, \vec{b} -  \frac{\langle \ \vec{b}, \vec{a} \ \rangle}{||\vec{a}||^2}\vec{a}, \hspace{.5cm}} ''').move_to(2.5*DOWN)
        text6[0][6:8].set_color(ROJO)
        text6[0][9:26].set_color(VERDE)
        text6_bg=SurroundingRectangle(text6, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text6_group = VGroup(text6, text6_bg)
        text7 = TexMobject(r"S = \qty\Big{  \vec{a},   \vec{b}'  , \vec{c} -  \frac{\langle \ \vec{c}, \vec{a} \ \rangle}{||\vec{a}||^2}\vec{a} - \frac{\langle \ \vec{c}, \vec{b} \ \rangle}{||\vec{b}||^2}\vec{b} } ").move_to(2.5*DOWN)
        text7[0][6:9].set_color(VERDE)
        text7[0][10:12].set_color(NARANJA)
        text7[0][13:-1].set_color(MAGENTA)
        text7_bg = SurroundingRectangle(text7, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text8 = TexMobject(r"S = \qty\Big{ \vec{a}, \ \vec{b}', \ \vec{c}' } ").move_to(2*DOWN+2.9*RIGHT)
        text8[0][6:9].set_color(VERDE)
        text8[0][10:-1].set_color(MAGENTA)
        text8_bg = SurroundingRectangle(text8, color=WHITE, fill_color=BLACK, fill_opacity=1)
        text9 = TexMobject(r"S = \qty\Big{ ", r"\vec{a}, \ ", r"\vec{b}'" , r", \ \vec{c}' ", r"} ").move_to(2*DOWN+4*RIGHT)
        text9[2].set_color(VERDE)
        text9[3].set_color(GOLD_C)
        text9_bg = VGroup(SurroundingRectangle(text9, color=WHITE, fill_color=BLACK, fill_opacity=1), text9)

        a = np.array([0.5, 2.6, 3.5])
        b = np.array([3, 0, 2])
        c = np.array([2, 2, 1])
        a_vec = Vector(direction = a, color = AZUL)
        b_vec = Vector(direction = b, color = ROJO)
        c_vec = Vector(direction = c, color = NARANJA)

        #PROYECCION DE B SOBRE A 
        a_pro = projection_of_a_along_b(b, a)
        a_vec_pro = Vector(direction = a_pro, color = YELLOW)
        line_a = DashedLine(ORIGIN, a_pro, width=5, buff = 0.1)
        line_a_perp = DashedLine(b, a_pro, width=5, buff=0.1)
        a_ort = Vector(direction = b-a_pro, color = VERDE)
        suma_a = Arrow(start = b, end = b-a_pro, color = YELLOW)

        #PROYECCION DE C SOBRE A 
        c_pro = projection_of_a_along_b(c, a)
        c_vec_pro = Vector(direction = c_pro, color = YELLOW)
        line_c = DashedLine(ORIGIN, c_pro, width=5, buff = 0.1)
        line_c_perp = DashedLine(c, c_pro, width=5, buff=0.1)
        c_ort = Vector(direction = c-c_pro, color = MAGENTA)
        suma_c = Arrow(start = c, end = c-c_pro, color = YELLOW)

        #PROYECCION DE C SOBRE B
        b_pro = projection_of_a_along_b(c, b)
        b_vec_pro = Vector(direction = b_pro, color = YELLOW)
        line_b = DashedLine(ORIGIN, b_pro, width=5, buff = 0.1)
        line_b_perp = DashedLine(c, b_pro, width=5, buff=0.1)
        b_ort = Vector(direction = c-b_pro, color = MAGENTA)
        suma_b = Arrow(start = c, end = c-b_pro, color = YELLOW)
        cb_ort = Vector(direction = c-c_pro-b_pro, color = MAGENTA)
        suma_cb = Arrow(start = c-c_pro, end = c-c_pro-b_pro, color = MAGENTA)

        self.set_camera_orientation(phi=80 * DEGREES, theta=30*DEGREES)
        self.play(ShowCreation(axes))
        self.wait()
        self.add_fixed_in_frame_mobjects(text_bg)
        self.play(Write(text_bg))
        self.play(GrowArrow(a_vec))
        self.wait()
        self.add_fixed_in_frame_mobjects(text2)
        self.play(Write(text2))
        self.wait()
        self.play(GrowArrow(b_vec))
        self.wait()
        self.add_fixed_in_frame_mobjects(text3)
        self.play(Write(text3))
        self.wait()
        self.play(GrowArrow(c_vec))
        self.wait()
        self.add_fixed_in_frame_mobjects(text4)
        self.play(Write(text4))
        self.wait()
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(12)
        self.move_camera(phi=90 * DEGREES, run_time=3)
        self.stop_ambient_camera_rotation()
        self.add_fixed_in_frame_mobjects(text1_bg)
        self.play(Write(text1_bg))
        self.play(c_vec.set_opacity, 0)
        self.play(FadeOut(text1_bg))
        
        #PROYECCION DE B SOBRE A
        self.play(Write(line_a))
        self.wait()
        self.play(Write(line_a_perp))
        self.wait()
        self.play(GrowArrow(a_vec_pro))
        self.wait(2)
        self.play(FadeOut(line_a), FadeOut(line_a_perp))
        self.add_fixed_in_frame_mobjects(text6_bg)
        self.play(Write(text6_bg))
        self.add_fixed_in_frame_mobjects(text6[0][:8])
        self.play(Write(text6[0][:8]))
        self.wait()
        self.play(Transform(a_vec_pro, suma_a), run_time=3)
        self.add_fixed_in_frame_mobjects(text6[0][8:])
        self.play(Write(text6[0][8:]))
        self.wait()
        self.play(GrowArrow(a_ort))
        self.wait()
        self.play(FadeOut(a_vec_pro))
        self.wait()
        self.move_camera(phi=80 * DEGREES, theta=30*DEGREES, run_time=3)
        self.play(FadeOut(text6), FadeOut(text6_bg))
        self.add_fixed_in_frame_mobjects(text7_bg)
        self.add_fixed_in_frame_mobjects(text7[0][:10])
        self.play(Write(text7_bg), Write(text7[0][:10]))
        self.wait()

        #PROYECCION DE C SOBRE A
        self.play(c_vec.set_opacity, 1, b_vec.set_opacity, 0)
        self.play(Write(line_c))
        self.wait()
        self.play(Write(line_c_perp))
        self.wait()
        self.play(GrowArrow(c_vec_pro))
        self.wait(2)
        self.play(FadeOut(line_c), FadeOut(line_c_perp))
        self.add_fixed_in_frame_mobjects(text7[0][9:12])
        self.play(Write(text7[0][9:12]))
        self.wait()
        self.play(Transform(c_vec_pro, suma_c), run_time=3)
        self.add_fixed_in_frame_mobjects(text7[0][12:31])
        self.play(Write(text7[0][12:31]))
        self.wait()
        self.play(GrowArrow(c_ort))
        self.wait()
        self.play(FadeOut(c_vec_pro))
        self.wait()

        #PROYECCION DE C SOBRE B
        self.play(b_vec.set_opacity, 1, a_vec.set_opacity, 0)
        self.play(Write(line_b))
        self.wait()
        self.play(Write(line_b_perp))
        self.wait()
        self.play(GrowArrow(b_vec_pro))
        self.wait(2)
        self.play(FadeOut(line_b), FadeOut(line_b_perp))
        self.wait()
        self.play(Transform(b_vec_pro, suma_b), run_time=3)
        self.add_fixed_in_frame_mobjects(text7[0][31:])
        self.play(Write(text7[0][31:]))
        self.wait()
        self.play(GrowArrow(b_ort))
        self.wait()
        self.play(FadeOut(b_vec_pro))
        self.play(b_vec.set_opacity, 0, c_vec.set_opacity, 0, a_vec.set_opacity, 1, run_time=3)
        self.wait()
        self.play(FadeOut(text7), FadeOut(text7_bg))
        self.play(Transform(b_ort, suma_cb))
        self.play(GrowArrow(cb_ort))
        self.play(FadeOut(b_ort), FadeOut(c_ort))
        self.add_fixed_in_frame_mobjects(text8_bg)
        self.add_fixed_in_frame_mobjects(text8)
        self.play(Write(text8_bg), Write(text8))
        self.wait()
	
	
######################################################
##### Tercera escena ########################
######################################################

class TerceraEscena(GraphScene,Scene):
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
        "num_graph_anchor_points": 3000
    }
    def construct(self):
        #------------------------------------------------------------------- GRAM-SCHMIDT normal
        seaL = (TextMobject('''Sea $L$ un conjunto l.i.''').scale(0.7)).to_edge(1*UP)
        left_corner = 3*LEFT+2.8*UP
        proceso_GM = (TextMobject('''\\textbf{Proceso de Gram-Schmidt}''').scale(0.7)).move_to(left_corner+LEFT)
        algoritmo_left_1_1 = (TextMobject('''\\texttt{1.- Tomar a un vector de $L$ y}''').scale(0.7)).move_to(left_corner+0.5*DOWN+1*LEFT)
        algoritmo_left_1_2 = TextMobject('''\\texttt{agragarlo a un nuevo conjunto $\\Gamma$}.''').scale(0.7)
        algoritmo_paso_1 = VGroup(algoritmo_left_1_1, algoritmo_left_1_2)
        algoritmo_paso_1.arrange(0.08*DOWN, center=False, aligned_edge=LEFT)

        algoritmo_left_2_1 = (TextMobject('''\\texttt{2.- Tomar a otro de los vectores}''').scale(0.7)).next_to(algoritmo_paso_1, 2*DOWN)
        algoritmo_left_2_2 = TextMobject('''\\texttt{de $L$, restarle sus proyecciones}''').scale(0.7)
        algoritmo_left_2_3 = TextMobject('''\\texttt{sobre todos los vectores de $\\Gamma$}''').scale(0.7)
        algoritmo_left_2_4 = TextMobject('''\\texttt{y después agragarlo a $\\Gamma$}.''').scale(0.7)
        algoritmo_paso_2 = VGroup(algoritmo_left_2_1, algoritmo_left_2_2, algoritmo_left_2_3, algoritmo_left_2_4)
        algoritmo_paso_2.arrange(0.15*DOWN, center=False, aligned_edge=LEFT)
        algoritmo_paso_2.align_to(algoritmo_paso_1, LEFT)

        algoritmo_left_3_1 = (TextMobject('''\\texttt{3.- Repetir el paso 2 hasta}''').scale(0.7)).next_to(algoritmo_paso_2, 2*DOWN)
        algoritmo_left_3_2 = TextMobject('''\\texttt{que $\\Gamma$ tenga tantos vectores}''').scale(0.7)
        algoritmo_left_3_3 = TextMobject('''\\texttt{como $L$.}''').scale(0.7)
        algoritmo_paso_3 = VGroup(algoritmo_left_3_1, algoritmo_left_3_2, algoritmo_left_3_3)
        algoritmo_paso_3.arrange(0.08*DOWN, center=False, aligned_edge=LEFT)
        algoritmo_paso_3.align_to(algoritmo_paso_2, LEFT)

        linea = Line((0,2.5,0),(0,-2,0))

        #------------------------------------------------------------------- GRAM-SCHMIDT modificado

        right_corner = 3*RIGHT+2.8*UP
        proceso_GMM = (TextMobject('''\\textbf{Gram-Schmidt \\textit{modificado}}''').scale(0.7)).move_to(right_corner)
        algoritmo_right_1_1 = (TextMobject('''\\texttt{1.- Tomar a un vector de $L$,}''').scale(0.7)).move_to(right_corner+0.5*DOWN)
        algoritmo_right_1_2 = TextMobject('''\\texttt{\\textit{normalizarlo} y agragarlo a}''').scale(0.7)
        algoritmo_right_1_3 = TextMobject('''\\texttt{un nuevo conjunto $N$}.''').scale(0.7)
        algoritmor_paso_1 = VGroup(algoritmo_right_1_1, algoritmo_right_1_2, algoritmo_right_1_3)
        algoritmor_paso_1.arrange(0.08*DOWN, center=False, aligned_edge=LEFT)

        algoritmo_right_2_1 = (TextMobject('''\\texttt{2.- Tomar otro de los vectores}''').scale(0.7)).next_to(algoritmor_paso_1, 2*DOWN)
        algoritmo_right_2_2 = TextMobject('''\\texttt{de $L$, restarle sus proyecciones}''').scale(0.7)
        algoritmo_right_2_3 = TextMobject('''\\texttt{sobre todos los vectores de $N$, }''').scale(0.7)
        algoritmo_right_2_4 = TextMobject('''\\texttt{\\textit{normaliarlo}, y después}.''').scale(0.7)
        algoritmo_right_2_5 = TextMobject('''\\texttt{agragarlo a $N$}.''').scale(0.7)
        algoritmor_paso_2 = VGroup(algoritmo_right_2_1, algoritmo_right_2_2, algoritmo_right_2_3, algoritmo_right_2_4, algoritmo_right_2_5)
        algoritmor_paso_2.arrange(0.08*DOWN, center=False, aligned_edge=LEFT)
        algoritmor_paso_2.align_to(algoritmor_paso_1, LEFT)

        algoritmo_right_3_1 = (TextMobject('''\\texttt{3.- Repetir el paso 2 hasta}''').scale(0.7)).next_to(algoritmor_paso_2, 2*DOWN)
        algoritmo_right_3_2 = TextMobject('''\\texttt{que $N$ tenga tantos vectores}''').scale(0.7)
        algoritmo_right_3_3 = TextMobject('''\\texttt{como $L$.}''').scale(0.7)
        algoritmor_paso_3 = VGroup(algoritmo_right_3_1, algoritmo_right_3_2, algoritmo_right_3_3)
        algoritmor_paso_3.arrange(0.08*DOWN, center=False, aligned_edge=LEFT)
        algoritmor_paso_3.align_to(algoritmor_paso_2, LEFT)
        
        resultado_2 = (TextMobject('''¡$N$ es ortonormal!''').scale(0.7)).next_to(algoritmor_paso_3, 2*DOWN)
        resultado_1 = (TextMobject('''¡$\\Gamma$ es ortogonal!''').scale(0.7)).next_to(algoritmo_paso_3, 2*DOWN)
        resultado_1.align_to(resultado_2, UP)

        #------------------------------------------------------------------- Enunciado del Teorema
        texto1 = TextMobject("""Teorema de Gram-Schmidt:""").to_edge(UP+LEFT)
        teorema_1 = (TextMobject('''Sea $V$ sobre $K$ un espacio vectorial y ''').scale(0.8)).move_to(1.0*UP)
        subconjunto_S_li = (TexMobject("S", #0
                                    "=", #1
                                    "\\left(", #2
                                    "\\textbf{u}_1,", #3
                                    "\\textbf{u}_2,", #4
                                    "...,", #5
                                    "\\textbf{u}_n", #6
                                    "\\right)"#7
                                    ).scale(0.8)).move_to(0.5*UP)
        teorema_2 = TextMobject("un subconjunto linealmente independiente de $V$").scale(0.8)

        teorema_3 = (TextMobject('''Si definimos al conjunto''').scale(0.8)).move_to(2.0*UP)
        subconjunto_Sp = (TexMobject("S'", #0
                                    "=", #1
                                    "(", #2
                                    "\\textbf{v}_1,", #3
                                    "\\textbf{v}_2,", #4
                                    "...,", #5
                                    "\\textbf{v}_n", #6
                                    ")"#7
                                    ).scale(0.8)).move_to(1.5*UP)
        teorema_4 = (TextMobject("de tal forma que").scale(0.8)).move_to(1.0*UP)
        v_1 = (TexMobject("\\textbf{v}_1 = \\textbf{u}_1,").scale(0.8)).move_to(0.5*UP)
        v_k = (TexMobject("\\textbf{v}_k", #0
                            "=", #1
                            "\\textbf{u}_k", #2
                            "-\\displaystyle\\sum_{j=1}^{k-1}", #3
                            "\\dfrac{\\langle \\textbf{u}_k,\\textbf{v}_j\\rangle}{\\left\\lVert \\textbf{v}_j\\right\\rVert^2}", #4
                            "\\textbf{v}_j", #5
                            "=", #6
                            "\\textbf{u}_k", #7
                            "-\\displaystyle\\sum_{j=1}^{k-1}", #8
                            "\\dfrac{\\langle \\textbf{u}_k,\\textbf{v}_j\\rangle}{\\left\\lVert \\textbf{v}_j\\right\\rVert}", #9
                            "\\dfrac{\\textbf{v}_j}{\\left\\lVert \\textbf{v}_j\\right\\rVert}", #10
                            ).scale(0.8)).move_to(0.5*DOWN+1*LEFT)
        teorema_5 = (TextMobject("para $2\\leq k\\leq n.$").scale(0.8)).next_to(v_k)
        teorema_6 = TextMobject("""entonces $S$ es un subconjunto ortogonal \n
                                  de $V$ tal que $\\langle S'\\rangle = \\langle S\\rangle$""").scale(0.8)
        projection_uk_vj = TexMobject("P_{\\textbf{v}_j}\\left(\\textbf{u}_k\\right)").scale(0.8)



        pregunta = TextMobject("Pregunta: ",'''¿Qué sucedería si aplicáramos el\n
         proceso de Gram-Schmidt a un conjunto\n
         linealmente dependiente?''').scale(0.7)
        pregunta[0].set_color('FF0000')
        ejercicio = TextMobject("Ejercicio: ","""Sea $V$ un espacio vectorial de dimensión finita $n$ con \n
                                    producto escalar. Demuestra que, para toda $k$ entre $1$ y $n$, \n
                                    cualquier conjunto ortogonal de $k$ vectores no nulos es un \n
                                    conjunto linealmente independiente. En particular, demuestra \n
                                    que cualquier conjunto ortogonal de $n$ vectores no nulos es \n
                                     una base ortogonal de $V$.""").scale(0.7)
        ejercicio[0].set_color('#0087FF')
        
        
        
        
        ###ANIMACIONES
        #--------------------------------
        '''
        Tercera escena: 
        Este mismo proceso para obtener un conjunto ortogonal a partir de un conjunto de vectores linealmente
        independientes puede ser generalizado para espacios vectoriales dendimensiones, y se conoce como el
        proceso de Gram-Schmidt.
        '''
        #--------------------------------
        self.play(Write(seaL))
        self.play(Write(proceso_GM))
        self.play(Write(algoritmo_paso_1))
        self.wait(1)
        self.play(Write(algoritmo_paso_2))
        self.wait(1)
        self.play(Write(algoritmo_paso_3))
        self.wait(1)
        self.play(ShowCreation(linea))

        self.play(Write(proceso_GMM))
        self.wait(1)
        self.play(Write(algoritmor_paso_1))
        self.wait(1)
        self.play(Write(algoritmor_paso_2))
        self.wait(1)
        self.play(Write(algoritmor_paso_3))

        self.play(
            FadeIn(resultado_1),
            FadeIn(resultado_2),
            run_time = 1
        )

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

        self.play(Write(texto1))
        self.play(Write(teorema_1))
        self.play(Write(subconjunto_S_li[:]))
        self.play(Write(teorema_2))
        self.play(
            *[FadeOut(mob) for mob in [teorema_1, teorema_2]]
        )
        self.play(
            subconjunto_S_li[:].shift,
            3*DOWN+3.5*RIGHT, 
            run_time = 2
        )
        self.wait(3)


        self.play(Write(teorema_3))
        self.play(Write(subconjunto_Sp[:]))
        self.play(Write(teorema_4))
        self.play(Write(v_1))
        self.play(Write(v_k[:6]))
        self.play(
            *[FadeOut(mob) for mob in [teorema_3, teorema_4, v_1]]
        )
        self.play(
            subconjunto_Sp[:].shift,
            3.5*DOWN+3.5*RIGHT, 
            run_time = 2
        )
        self.play(
            ReplacementTransform(v_k[1].copy(),v_k[6]),
			ReplacementTransform(v_k[2].copy(),v_k[7]),
			ReplacementTransform(v_k[3].copy(),v_k[8]),
			run_time=2
			)
        self.play(
			FadeIn(v_k[9]),
            FadeIn(v_k[10]),
            Write(teorema_5),
			run_time=2
			)
        self.play(
            *[FadeOut(mob) for mob in [v_k, teorema_5]]
        )
        self.play(Write(teorema_6))        
        self.wait(3)

        #--------------------------------
        '''
        Pregunta y ejercicios
        '''
        #--------------------------------
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.play(Write(pregunta))
        self.play(
            pregunta.shift, 
            2*UP+3*LEFT,
            run_time = 2
        )
        self.wait(3)
        self.play(Write(ejercicio))
        self.play(
            ejercicio.shift,
            1.5*DOWN+1.5*RIGHT, 
            run_time = 2
        )
        self.wait(5)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
