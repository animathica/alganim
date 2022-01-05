from manim import *

#####################################################################################
#####################  Producto escalar y bases ortogonales  ########################
#####################################################################################


#####################################################################################
###############################  Tercera escena  ####################################
###############################  Subescena 2  #######################################
###############################  versión: Manim Community v0.8.0   ##################
#####################################################################################



# Constantes de los colores usados.
ROJO = '#FF0000'
ROSA = '#E95771'
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

class Escena4(ThreeDScene):

    grid = NumberPlane()

    def Signo(self):

        # Función para producto punto de vectores.
        def producto_punto(a,b):
            return (a.get_end()[0]-a.get_start()[0])*(b.get_end()[0]-b.get_start()[0]) \
                 + (a.get_end()[1]-a.get_start()[1])*(b.get_end()[1]-b.get_start()[1])

        # Vectores con los que se trabaja en el video
        A1, A2, B1, B2 = 1, 3, 4, 2
        VecA = Arrow((0,0,0), (A1,A2,0), color = AZUL, buff = 0)
        VecB = Arrow((0,0,0), (B1,B2,0), color = ROJO, buff = 0)

        # Texto para mostrar el producto de VecA y VecB, sin resultado
        Texto_Producto = Tex(''' $ A \\cdot B =  $ ''').move_to(DOWN*2+0.5*LEFT)

        # Resultado del producto de los vectores.
        Resultado = DecimalNumber(producto_punto(VecA,VecB))
        Resultado.next_to(Texto_Producto, RIGHT, buff = 0.2, aligned_edge=Resultado.get_bottom())
        #Resultado.add_updater( lambda x: x.set_value(producto_punto(VecA,VecB)) )
        Espacio_vacio = Tex(''' - - ''').set_color(BLACK)
        Espacio_vacio.next_to(Resultado, RIGHT, buff = 0, aligned_edge=Espacio_vacio.get_bottom())
        Texto_Producto_bg = SurroundingRectangle(VGroup(Texto_Producto,Resultado,Espacio_vacio), \
            color = WHITE, fill_color = BLACK, fill_opacity = 1)
        Texto_Producto_group = VGroup(Texto_Producto_bg,Texto_Producto,Resultado)

        # Texto para coordenadas de los vectores
        Coma_2 = Tex(''',l''').move_to(DOWN*2+RIGHT*1)
        Coma_2[0][1].set_color(BLACK)
        Texto_Coord_B_1 = DecimalNumber(VecB.get_end()[0]).next_to(Coma_2,LEFT,buff=0.4)
        Texto_Coord_B_2 = DecimalNumber(VecB.get_end()[1]).next_to(Coma_2,RIGHT,buff=0.1)
        Parentesis_Derecho_2 = Tex(''')''').next_to(Texto_Coord_B_2,RIGHT,buff=0.4)
        Aprox = Tex('''$\\approx$''').next_to(Parentesis_Derecho_2,RIGHT,buff=0.1)
        Parentesis_Izquierdo_2 = Tex('''(''').next_to(Texto_Coord_B_1,LEFT,buff=0.1)
        Operador = Tex('''$\\cdot$''').next_to(Parentesis_Izquierdo_2,LEFT,buff=0.1)
        Resultado_2 = DecimalNumber(producto_punto(VecA,VecB)).next_to(Parentesis_Derecho_2,RIGHT, buff=0.7)
        Parentesis_Derecho_1 = Tex(''')''').next_to(Operador,LEFT,buff=0.1)
        Texto_Coord_A_2 = DecimalNumber(VecA.get_end()[1]).next_to(Parentesis_Derecho_1,LEFT,buff=0.4)
        Coma_1 = Tex(''',l''').next_to(Texto_Coord_A_2,LEFT,buff=0)
        Coma_1[0][1].set_color(BLACK)
        Texto_Coord_A_1 = DecimalNumber(VecA.get_end()[0]).next_to(Coma_1,LEFT,buff=0.4)
        Parentesis_Izquierdo_1 = Tex('''(''').next_to(Texto_Coord_A_1,LEFT,buff=0.1)
        Resultado_2.add_updater( lambda x: x.set_value(producto_punto(VecA,VecB)) )
        Texto_Coord_A_1.add_updater( lambda x: x.set_value(VecA.get_end()[0]) )
        Texto_Coord_A_2.add_updater( lambda x: x.set_value(VecA.get_end()[1]) )
        Texto_Coord_B_1.add_updater( lambda x: x.set_value(VecB.get_end()[0]) )
        Texto_Coord_B_2.add_updater( lambda x: x.set_value(VecB.get_end()[1]) )
        Espacio_vacio_2 = Tex(''' - - - - ''').set_color(BLACK)
        Espacio_vacio_2.next_to(Resultado_2, RIGHT, buff = 0, aligned_edge=Espacio_vacio_2.get_bottom())
        Texto_Coordenadas_A = VGroup(Parentesis_Izquierdo_1, Texto_Coord_A_1 \
            , Coma_1, Texto_Coord_A_2, Parentesis_Derecho_1)
        Texto_Coordenadas_B = VGroup(Parentesis_Izquierdo_2, Texto_Coord_B_1 \
            , Coma_2, Texto_Coord_B_2, Parentesis_Derecho_2)
        Texto_Coordenadas_bg = SurroundingRectangle(VGroup(Parentesis_Izquierdo_1 \
            , Parentesis_Izquierdo_2,Texto_Coord_A_1,Texto_Coord_A_2,Operador,Texto_Coord_B_1 \
                , Texto_Coord_B_2,Parentesis_Derecho_1, Parentesis_Derecho_2, Resultado_2 \
                , Coma_1, Coma_2, Espacio_vacio_2), color = WHITE, fill_color = BLACK, fill_opacity = 1)
        Texto_Coordenadas = VGroup(Texto_Coordenadas_bg, Texto_Coordenadas_A \
            , Texto_Coordenadas_B, Operador, Aprox, Resultado_2)

        # ValueTrackers para los reescalamientos.
        VT_A = ValueTracker(1)
        VT_B = ValueTracker(1)

        # Funciones para reescalamiento.
        def upd_for_vecA(obj):
                t = VT_A.get_value()
                NewVec = Arrow((0,0,0),(t*A1,t*A2,0),buff=0, color = obj.get_color())
                obj.become(NewVec)

        def upd_for_vecB(obj):
                t = VT_B.get_value()
                NewVec = Arrow((0,0,0),(t*B1,t*B2,0),buff=0, color = obj.get_color())
                obj.become(NewVec)

        # ValueTrackers para los desplazamientos.
        VT_A_2 = ValueTracker(0)
        VT_B_2 = ValueTracker(0)

        # Funciones para los desplazamientos.
        def upd_for_vecA_2(obj):
            a1, a2 = VecA.get_end()[0], VecA.get_end()[1]
            p1, p2 = proyeccion(VecA,VecB)
            t = VT_A_2.get_value()
            nv1 = a1 - (t*(a1 - p1))
            nv2 = a2 - (t*(a2 - p2))
            NewVec = Arrow((0,0,0),(nv1,nv2,0),buff = 0, color = obj.get_color())
            obj.become(NewVec)

        def upd_for_vecB_2(obj):
            b1, b2 = VecB.get_end()[0], VecB.get_end()[1]
            p1, p2 = proyeccion(VecB,VecA)
            t = VT_B_2.get_value()
            nv1 = b1 - (t*(b1 - p1))
            nv2 = b2 - (t*(b2 - p2))
            NewVec = Arrow((0,0,0),(nv1,nv2,0),buff = 0, color = obj.get_color())
            obj.become(NewVec)

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
                rayo = DashedLine( [i[0]+x2o,i[1]+y2o,0], [i[0],i[1],0] \
                    , stroke_width=5 , buff = 0.05).set_color(AMARILLO)
                rays.append(rayo)
            # Se hace un VGroup con los rayos.
            grupo = VGroup()
            for i in rays:
                grupo.add(i)
            return(grupo)

        def light_2(x1,y1,x2,y2,n = 10):
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
                #r1 = x1 + i*((x2-x1)/n)
                #r2 = y1 + i*((y2-y1)/n)
                r1 = x2 + 1.2*i*(p1-x2)/n
                r2 = y2 + 1.2*i*(p2-y2)/n
                #nr = np.sqrt(r1**2 + r2**2)
                if r1 > 0 and r1 < p1:
                    inter = line_intersection(((0,0),(x1,y1)),((r1,r2),(r1 + x2o,r2 + y2o)))
                    rayc.append([inter[0],inter[1]])                
                else:
                    rayc.append([r1,r2])
            # Se genera cada rayo.
            for i in rayc:
                rayo = DashedLine( [i[0]-2*x2o,i[1]-2*y2o,0], [i[0],i[1],0] \
                    , stroke_width=5 , buff = 0.05).set_color(AMARILLO)
                rays.append(rayo)
            # Se hace un VGroup con los rayos.
            grupo = VGroup()
            for i in rays:
                grupo.add(i)
            return(grupo)

        def light_3(x1,y1,x2,y2,n = 10):
            # Coordenadas de un vector ortogonal a (x2,y2)
            x2o = y2
            y2o = -x2
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
                r1 = 0 + i*((x2/n)*1.3)
                r2 = 0 + i*((y2/n)*1.3)
                nr = np.sqrt(r1**2 + r2**2)
                if nr < norma_proy:
                    inter = line_intersection(((0,0),(x1,y1)),((r1,r2),(r1 + x2o,r2 + y2o)))
                    rayc.append([inter[0],inter[1]])                
                else:
                    rayc.append([r1,r2])
            # Se genera cada rayo.
            for i in rayc:
                rayo = DashedLine( [i[0]+15*x2o,i[1]+15*y2o,0], [i[0],i[1],0] \
                    , stroke_width=5 , buff = 0.05).set_color(AMARILLO)
                rays.append(rayo)
            # Se hace un VGroup con los rayos.
            grupo = VGroup()
            for i in rays:
                grupo.add(i)
            return(grupo)

        ProyeccionAB_1 = light(A1,A2,B1,B2,25)
        ProyeccionAB_2 = light_2(A1,A2,-B1,-B2,35)
        ProyeccionBA_1 = light_3(B1,B2,A1,A2,35)

        # Función para obtener las coordenadas de la proyección de A sobre B.
        # Los argumentos son objetos Arrow.
        # Regresa las coordenadas de la proyección.
        def proyeccion(VecA,VecB):
            b1, b2 = VecB.get_end()[0], VecB.get_end()[1]
            c1 = (producto_punto(VecA, VecB) / (b1**2 + b2**2) ) * b1
            c2 = (producto_punto(VecA, VecB) / (b1**2 + b2**2) ) * b2
            return c1, c2

        # Vectores de las proyecciones de A sobre B y B sobre A, respectivamente.
        VecSombra_1 = Arrow((0,0,0), (proyeccion(VecA,VecB)[0] \
            ,proyeccion(VecA,VecB)[1],0), color = AMARILLO, buff = 0)
        VecSombra_2 = Arrow((0,0,0), (proyeccion(VecB,VecA)[0] \
            ,proyeccion(VecB,VecA)[1],0), color = AMARILLO, buff = 0)

        # Función para el reescalamiento del vector de proyección.
        def upd_for_sombra(obj):
            if ( np.sqrt(proyeccion(VecA,VecB)[0]**2 + proyeccion(VecA,VecB)[1]**2) ) > 0.05:
                NewVec = Arrow((0,0,0), (proyeccion(VecA,VecB)[0] \
                    ,proyeccion(VecA,VecB)[1],0), color = AMARILLO, buff = 0)
            else:
                NewVec = obj
            obj.become(NewVec)

        # Linea punteada que actúa como "piso" para proyectar sobre el otro lado del vector B.
        Piso_B = DashedLine( [B1*10,B2*10,0], [-B1*10,-B2*10,0] \
            , stroke_width=5 , buff = 0.05).set_color(GRIS)

        # Rayo que delimita el desplazamiento del vector A sin que cambie el producto escalar.
        Rayo_extremo_1 = DashedLine((proyeccion(VecA,VecB)[0],proyeccion(VecA,VecB)[1],0)\
            ,(A1-10*B2,A2+10*B1,0)\
                , stroke_width=5 , buff = 0.05).set_color(AMARILLO)

        # Rayo que delimita el desplazamiento del vector B sin que cambie el producto escalar.
        Rayo_extremo_2 = DashedLine((proyeccion(VecB,VecA)[0],proyeccion(VecB,VecA)[1],0)\
            ,(B1+10*A2,B2-10*A1,0)\
                , stroke_width=5 , buff = 0.05).set_color(AMARILLO)

        # ValueTracker usado para girar el vector A.
        VT_A_3 = ValueTracker(np.arctan(A2/A1))

        # Updater usado para girar el vector A.
        def upd_for_VecA_3(obj):
            t = VT_A_3.get_value()
            norma = np.linalg.norm((A1,A2))
            nv1 = norma * np.cos(t) * ( 1 + np.abs( np.sin(t-np.arctan(A2/A1) ) ) )
            nv2 = norma * np.sin(t) * ( 1 + np.abs( np.sin(t-np.arctan(A2/A1) ) ) )
            NewVec = Arrow((0,0,0),(nv1,nv2,0),buff = 0, color = obj.get_color())
            obj.become(NewVec)

        # Updater para que reescalamiento de vector corte a los rayos.
        def upd_for_rayo(obj):
            # Se aplica el updater a cada rayo de la proyección individualmente.
            # En este caso el vector A es el que corta.
            # El rayo parte de la proyección de A en B.
            # Puntos iniciales y finales del rayo.
            RI_1, RI_2 = obj.get_start()[0], obj.get_start()[1]
            RF_1, RF_2 = obj.get_end()[0], obj.get_end()[1]
            # Puntos finales de los vectores.
            a1, a2 = VecA.get_end()[0], VecA.get_end()[1]
            b1, b2 = VecB.get_end()[0], VecB.get_end()[1]
            # Norma de A.
            normaVecA = np.sqrt(a1**2 + a2**2)
            # Intersección del vector A y el rayo, (o donde se intersecaría).
            l = line_intersection(((0,0),(a1,a2)),((RI_1,RI_2),(RF_1,RF_2)))
            # Norma del vector que va a la intersección.
            normaInt = np.sqrt(l[0]**2 + l[1]**2)
            # Intersección de rayo y vector B (sobre el que se proyecta).
            IntB = line_intersection(((0,0),(b1,b2)),((RI_1,RI_2),(RF_1,RF_2)))
            # Intersección de rayo y linea de salida, para encontrar punto inicial.
            # Se usa esta linea de salida para que no se modifique el tamaño de los rayos.
            Base = line_intersection(((0+10,0+10),(b1+10,b2+10)),((RI_1,RI_2),(RF_1,RF_2)))
            # Se compara la norma de la intersección con la del vector que corta, para ver si hay cambios.
            if normaVecA < normaInt:
                # Si es menor el vector que corta, el rayo llega hasta el vector B.
                NewRayo = DashedLine( [Base[0],Base[1],0], [IntB[0],IntB[1],0], \
                     stroke_width=5 , buff = 0.05).set_color(AMARILLO)
            elif normaVecA >= normaInt:
                # Si es mayor el vector que corta, el rayo se detiene en donde se intersecan.
                NewRayo = DashedLine( [Base[0],Base[1],0], [l[0],l[1],0], \
                     stroke_width=5 , buff = 0.05).set_color(AMARILLO)
            # Se actualiza el rayo.
            obj.become(NewRayo)
            # Se manda al fondo el rayo.
            self.bring_to_back(obj)

        # Rayo que une proyección y vector A durante rotación.
        Rayo_union = DashedLine( VecA.get_end(),VecSombra_1.get_end()\
            , stroke_width=5 , buff = 0.05).set_color(AMARILLO)

        # Updater para unión entre proyección y vector A.
        def upd_for_union(obj):
            # No se grafica si está cerca de 0 la norma de la proyección.
            if np.abs(producto_punto(VecA,VecSombra_1)) > 0.1:
                NewRayo = DashedLine( VecA.get_end(),VecSombra_1.get_end()\
                , stroke_width=5 , buff = 0.05).set_color(AMARILLO)
                obj.become(NewRayo)
            else:
                NewRayo = DashedLine( VecA.get_end(),VecSombra_1.get_end()\
                , stroke_width=5 , buff = 0.05).set_color(AMARILLO).set_opacity(0)
                obj.become(NewRayo)


        # Animaciones de la escena.
        self.play(Create(VGroup(VecA,VecB)))
        self.wait()
        self.play(Write(Texto_Producto_group))
        self.bring_to_back(ProyeccionAB_1)
        self.play(Create(ProyeccionAB_1))
        self.wait()
        self.play(Create(VecSombra_1))
        self.wait()
        self.play(FadeOut(VGroup(ProyeccionAB_1,VecSombra_1)))
        self.wait()
        self.bring_to_back(ProyeccionBA_1)
        self.play(Create(ProyeccionBA_1))
        self.wait()
        self.play(Create(VecSombra_2))
        self.wait()
        self.play(FadeOut(VGroup(ProyeccionBA_1,VecSombra_2)))
        self.play(Create(VecSombra_1),Create(ProyeccionAB_1))
        for i in ProyeccionAB_1:
            i.add_updater(upd_for_rayo)
        self.add_foreground_mobjects(VecA)
        VecSombra_1.add_updater(upd_for_sombra)
        VecA.add_updater(upd_for_vecA)
        VecB.add_updater(upd_for_vecB)
        self.add_foreground_mobject(Texto_Producto)
        self.play(ReplacementTransform(Texto_Producto_bg,Texto_Coordenadas_bg))
        self.remove_foreground_mobject(Texto_Producto)
        self.play(ReplacementTransform( Texto_Producto[0][0], Texto_Coordenadas_A ) \
            , ReplacementTransform( Texto_Producto[0][2], Texto_Coordenadas_B ) \
                , ReplacementTransform(Texto_Producto[0][1], Operador) \
                    , ReplacementTransform(Texto_Producto[0][3], Aprox) \
                        , ReplacementTransform(Resultado, Resultado_2))
        self.add_foreground_mobjects(Texto_Coordenadas)
        self.add_foreground_mobjects(Texto_Coordenadas_A \
            , Texto_Coordenadas_B, Operador, Aprox, Resultado_2)
        self.play(VT_A.animate.set_value(1.3),run_time=2)
        self.play(VT_A.animate.set_value(0.2),run_time=2)
        self.play(VT_A.animate.set_value(1),run_time=2)
        for i in ProyeccionAB_1:
            i.remove_updater(upd_for_rayo)
        self.play(FadeOut(ProyeccionAB_1))
        self.remove_foreground_mobjects(VecA)
        self.wait()
        self.play(VT_B.animate.set_value(1.7),run_time=2)
        self.play(VT_B.animate.set_value(0.15),run_time=2)
        self.play(VT_B.animate.set_value(1),run_time=2)
        self.wait()
        self.play(VT_B.animate.set_value(-1),run_time=2)
        self.wait()
        self.bring_to_back(Piso_B)
        self.play(Create(Piso_B))
        self.wait()
        self.bring_to_back(ProyeccionAB_2)
        self.play(Create(ProyeccionAB_2))
        self.wait()
        self.play(FadeOut(ProyeccionAB_2))
        self.wait()
        self.play(FadeOut(Piso_B))
        self.wait()
        self.play(VT_A.animate.set_value(-1),run_time=2)
        self.wait()
        self.play(VT_B.animate.set_value(1),run_time=2)
        self.wait()
        self.play(VT_A.animate.set_value(1),run_time=2)
        self.wait()
        self.play(Create(Rayo_extremo_1))
        self.wait()
        VecA.add_updater(upd_for_vecA_2)
        self.wait()
        self.play(VT_A_2.animate.set_value(1),run_time=2)
        self.play(VT_A_2.animate.set_value(0),run_time=2)
        self.wait()
        self.play(FadeOut(Rayo_extremo_1))
        self.wait()
        self.play(FadeOut(VecSombra_1))
        self.wait()
        self.play(Create(Rayo_extremo_2))
        self.wait()
        VecB.add_updater(upd_for_vecB_2)
        self.play(VT_B_2.animate.set_value(1),run_time=2)
        self.play(VT_B_2.animate.set_value(0),run_time=2)
        self.play(FadeOut(Rayo_extremo_2))
        self.wait()
        self.play(Create(VecSombra_1))
        self.wait()
        self.play(Create(Rayo_union))
        self.wait()
        VecA.add_updater(upd_for_VecA_3)
        Rayo_union.add_updater(upd_for_union)
        for _ in range(4):
            self.play(VT_A_3.animate.increment_value(np.pi/2),run_time=2)
        self.wait()
        VecA.remove_updater(upd_for_VecA_3)

        self.wait(2)

    def construct(self):
        self.play(Write(self.grid))
        self.Signo()

#if __name__ == '__main__':
#    import os
#    os.system('manim -pql Lineal/E3SE2.py')
