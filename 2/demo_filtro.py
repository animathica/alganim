# -*- coding: utf-8 -*-
from manim import *
#####################################################################################
######################  Norma inducida y bases ortonormales  ########################
#####################################################################################


#####################################################################################
###############################  Cuarta escena  #####################################
###############################  versión: Manim Community v0.8.0   ##################
#####################################################################################

ROJO = '#FF0000'
AZUL = '#0087FF'
NARANJA = '#FF7700'
VERDE = '#1FFF00'
MAGENTA = '#FF00FF'
AMARILLO = "#FFFF00"
GRIS = "#505050"
MAGENTA_CLARO = "#FF67FF"
AZUL_CLARO = "#9CDCEB"
AZUL_OSCURO = "#1C758A"
TEAL_A = "#ACEAD7"
TEAL_E = "#49A88F"
MOSTAZA_OSCURO = "#FFD025"
MOSTAZA_CLARO = "#FFE072"
RADIOGRAFIA = "#00FFFF"


class Subescena_1(Scene):
    config.background_color = BLACK
    def construct(self):
        plane = NumberPlane()
        vect = Arrow(start=np.array([1, 1, 0]), end=np.array([4, -3, 0]), color=VERDE, buff=0,
                     stroke_width=7, max_tip_length_to_length_ratio=0.4
                     )

        def apunta_hacia_arriba(vector) -> bool:
            '''
            Función para determinar si un vector apunta hacia "arriba" (coordenada angular en
            el intervalo [0,pi]), o hacia "abajo" (coordenada angular (pi, 2pi))
            '''
            if vector.get_end()[1] > vector.get_start()[1]:
                return True
            else:
                return False

        def filtro_radiografia(vector):
            # Rectángulo que hace las veces de filtro de radiografía
            rectangle = Polygon([-8, 5, 0], [-8, 5, 0], [8, 5, 0],
                                [8, 5, 0], fill_color=RADIOGRAFIA, fill_opacity=0.2)
            # Se agraga al canvas
            self.add(
                rectangle
            )
            vect_col = vector.get_color()

            # Value tracker para el desplazamiento vertical del filtro
            t1 = ValueTracker(rectangle.get_bottom()[1])
            # Objeto auxiliar que se convertirá en el vector filtrado (blanco)
            aux_dot = Dot(vector.get_end(), radius=0)
            self.add(aux_dot)
            white_copy = vector.copy().set_color(WHITE)

            #Updater para el filtro de radiografía
            def rectangle_updater(rectangle):
                bottom = t1.get_value()
                new_rectangle = Polygon([-8, bottom, 0], [-8, 5, 0], [8, 5, 0],
                                        [8, bottom, 0], fill_color=RADIOGRAFIA, fill_opacity=0.2)
                rectangle.become(new_rectangle)

            def vector_hacia_abajo_updater(vector):
                if rectangle.get_bottom()[1] > vector.get_start()[1]:
                    pass
                elif vector.get_end()[1] <= rectangle.get_bottom()[1] <= vector.get_start()[1]:
                    vector.become(white_copy)
                    self.add_foreground_mobject(vector)
                else:
                    pass

            def vector_filtrado_updater(dot_auxiliar):
                # ---- Extremos del vector
                # Posición de la cola
                x1, y1 = vector.get_start()[0], vector.get_start()[1]
                # Posición de la punta
                x2, y2 = vector.get_end()[0], vector.get_end()[1]
                # Coordenada y del extremo inferior del plano
                y = rectangle.get_bottom()[1]
                # Proyección horizontal de la intersección
                # entre el borde inferior del filtro y la flecha

                x = x1+(x2-x1)*(y-y1)/(y2-y1) if y1 != y2 else x1

                if apunta_hacia_arriba(vector):
                    # Se mantiene el color original del vector y se va rellenando
                    # con un vector que va de la intersección del filtro con el vector a
                    # la punta del vector
                    vect_ = Arrow(start=np.array([x, y, 0]), end=vector.get_end(), color=WHITE, buff=0,
                                  stroke_width=7, max_tip_length_to_length_ratio=0.4
                                  )
                    if y > y2:
                        pass
                    elif y1 <= y <= y2:
                        dot_auxiliar.become(vect_)
                    else:
                        pass
                else:
                    # Se cambia el color original del vector a blanco con el updater 'vector_hacia_abajo_updater'
                    # y se va rellenando con un vector del color original que va de la intersección del filtro con
                    # el vector a la punta del vector
                    vect_ = Arrow(start=np.array([x, y, 0]), end=vector.get_end(), color=vect_col, buff=0,
                                  stroke_width=7, max_tip_length_to_length_ratio=0.4
                                  )
                    if y > y1:
                        pass
                    elif y2 <= y <= y1:
                        dot_auxiliar.become(vect_)
                        self.add_foreground_mobject(dot_auxiliar)
                    else:
                        pass

            rectangle.add_updater(rectangle_updater)
            aux_dot.add_updater(vector_filtrado_updater)
            if not apunta_hacia_arriba(vector):
                vector.add_updater(vector_hacia_abajo_updater)

            self.play(
                t1.animate.set_value(-5),
                run_time=10
            )

            rectangle.remove_updater(rectangle_updater)
            aux_dot.remove_updater(vector_filtrado_updater)
            if not apunta_hacia_arriba(vector):
                vector.remove_updater(vector_hacia_abajo_updater)

        #self.play(
        #    Write(plane)
        #)
        self.play(
            Write(vect)
        )
        filtro_radiografia(vect)
