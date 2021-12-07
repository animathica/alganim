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

class Escena3_2(ThreeDScene):

    grid = NumberPlane()

    def E3_SE2(self):

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
        Resultado.add_updater( lambda x: x.set_value(producto_punto(VecA,VecB)) )
        Espacio_vacio = Tex(''' - - ''').set_color(BLACK)
        Espacio_vacio.next_to(Resultado, RIGHT, buff = 0, aligned_edge=Espacio_vacio.get_bottom())
        Texto_Producto_bg = SurroundingRectangle(VGroup(Texto_Producto,Resultado,Espacio_vacio), \
            color = WHITE, fill_color = BLACK, fill_opacity = 1)
        Texto_Producto_group = VGroup(Texto_Producto_bg,Texto_Producto,Resultado)

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
                rayo = DashedLine( [i[0]+x2o,i[1]+y2o,0], [i[0],i[1],0], width=5, stroke_width=5 , buff = 0.05).set_color(AMARILLO)
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
                rayo = DashedLine( [i[0]-2*x2o,i[1]-2*y2o,0], [i[0],i[1],0], width=5, stroke_width=5 , buff = 0.05).set_color(AMARILLO)
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
                rayo = DashedLine( [i[0]+15*x2o,i[1]+15*y2o,0], [i[0],i[1],0], width=5, stroke_width=5 , buff = 0.05).set_color(AMARILLO)
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
        VecSombra_1 = Arrow((0,0,0), (proyeccion(VecA,VecB)[0],proyeccion(VecA,VecB)[1],0), color = AMARILLO, buff = 0)
        VecSombra_2 = Arrow((0,0,0), (proyeccion(VecB,VecA)[0],proyeccion(VecB,VecA)[1],0), color = AMARILLO, buff = 0)

        # Función para el reescalamiento del vector de proyección.
        def upd_for_sombra(obj):
            NewVec = Arrow((0,0,0), (proyeccion(VecA,VecB)[0],proyeccion(VecA,VecB)[1],0), color = AMARILLO, buff = 0)
            obj.become(NewVec)

        # Linea punteada que actúa como "piso" para proyectar sobre el otro lado del vector B.
        Piso_B = DashedLine( [B1*10,B2*10,0], [-B1*10,-B2*10,0], width=5, stroke_width=5 , buff = 0.05).set_color(GRIS)

        # Rayo que delimita el desplazamiento del vector A sin que cambie el producto escalar.
        Rayo_extremo_1 = DashedLine((proyeccion(VecA,VecB)[0],proyeccion(VecA,VecB)[1],0)\
            ,(A1-10*B2,A2+10*B1,0)\
                , width=5, stroke_width=5 , buff = 0.05).set_color(AMARILLO)

        # Rayo que delimita el desplazamiento del vector B sin que cambie el producto escalar.
        Rayo_extremo_2 = DashedLine((proyeccion(VecB,VecA)[0],proyeccion(VecB,VecA)[1],0)\
            ,(B1+10*A2,B2-10*A1,0)\
                , width=5, stroke_width=5 , buff = 0.05).set_color(AMARILLO)

        # ValueTracker usado para girar el vector A.
        VT_A_3 = ValueTracker(np.arctan(A2/A1))

        # Updater usado para girar el vector A.
        def upd_for_VecA_3(obj):
            t = VT_A_3.get_value()
            norma = np.linalg.norm((A1,A2))
            nv1 = norma * np.cos(t)
            nv2 = norma * np.sin(t)
            NewVec = Arrow((0,0,0),(nv1,nv2,0),buff = 0, color = obj.get_color())
            obj.become(NewVec)

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
        self.play(Create(ProyeccionBA_1))
        self.wait()
        self.play(Create(VecSombra_2))
        self.wait()
        self.play(FadeOut(VGroup(ProyeccionBA_1,VecSombra_2)))
        self.play(Create(VecSombra_1))
        VecSombra_1.add_updater(upd_for_sombra)
        VecA.add_updater(upd_for_vecA)
        VecB.add_updater(upd_for_vecB)
        self.play(VT_A.animate.set_value(1.3),run_time=2)
        self.play(VT_A.animate.set_value(0.2),run_time=2)
        self.play(VT_A.animate.set_value(1),run_time=2)
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
        self.play(FadeOut(VecSombra_1))
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
        self.play(Create(Rayo_extremo_2))
        self.wait()
        VecB.add_updater(upd_for_vecB_2)
        self.play(VT_B_2.animate.set_value(1),run_time=2)
        self.play(VT_B_2.animate.set_value(0),run_time=2)
        self.play(FadeOut(Rayo_extremo_2))
        self.wait()
        self.play(Create(VecSombra_1))
        self.wait()
        VecA.add_updater(upd_for_VecA_3)
        self.play(VT_A_3.animate.set_value(np.arctan(A2/A1)+(2*np.pi)),run_time=8, rate_func=linear)
        self.wait()
        VecA.remove_updater(upd_for_VecA_3)

        self.wait(2)

    def construct(self):

        self.play(Write(self.grid))
        self.E3_SE2()