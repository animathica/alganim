
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