# -*- coding: utf-8 -*-

from manim import *
#####################################################################################
######################  Producto escalar y bases ortogonales  #######################
#####################################################################################


#####################################################################################
###############################  Segunda escena  ####################################
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

class Subescena1(Scene):
    #-------------------------------------------------------Propiedades del producto escalar en un campo K
     def propiedades(self):
         t1 = MathTex("\langle\cdot, \cdot\\rangle:V\\times V\\to K ")
         p1 = MathTex("(1) \\forall \ \\vec{u}, \\vec{v}, \\vec{w}&\in V, \ \\forall \ a\in K\\").scale(.5)
         p2 = MathTex(" (2) \langle\\vec{u}+\\vec{w},\\vec{v}\\rangle &= \langle \\vec{u} , \\vec{v} \\rangle + \langle \\vec{w} , \\vec{v} \\rangle \\").scale(.5)
         p3 = MathTex(" (3) \langle a\\vec{u} , \\vec{v} \\rangle &= a \langle \\vec{u} , \\vec{v} \\rangle\\").scale(.5)
         p4 = MathTex(" (4) \langle \\vec{u} , \\vec{v} \\rangle &= \overline{ \langle \\vec{v} , \\vec{u} \\rangle}\\").scale(.5)
         p5 = MathTex(" (5) \langle \\vec{u}, \\vec{u} \\rangle > 0 \ &\ \\text{si} \ \ \\vec{u}\\neq\\vec{0}").scale(.5)
         text_10_bg = VGroup(p1, p2, p3, p4, p5, color=WHITE, fill_color=BLACK, fill_opacity=1).arrange(direction=DOWN, buff=0.15)
         g1 =VGroup(p1, p2, p3, color=WHITE, fill_color=BLACK, fill_opacity=1)
         b1 = Brace(g1, direction=RIGHT).scale(1.3)
         t2 = MathTex("\langle a\\vec{u}+\\vec{w} , \\vec{v} \\rangle = a \langle \\vec{u} , \\vec{v} \\rangle + \langle \\vec{w} , \\vec{v} \\rangle\ ").scale(.5)
         g2 = VGroup(g1, p4, color=WHITE, fill_color=BLACK, fill_opacity=1).arrange(direction=DOWN, buff=0.1)
         b2 = Brace(g2, direction=LEFT)
         #-----------------------------------------------------------Producto escalar en el campo de los Reales 
         t3 = MathTex("K =\mathbb R").scale(2)
         t4 = MathTex("\langle\cdot, \cdot\\rangle:V\\times V\\to \mathbb R").scale(.9)
         


         #ANIMACIONES# 
         t1.move_to(2*UP)
         self.wait(2)
         self.play(Write(t1))
         self.wait(3)
         self.play(FadeOut(t1))
         self.play(FadeIn(text_10_bg))
         self.wait(5)
         self.play(FadeOut(text_10_bg))
         self.play(FadeIn(g1))
         self.play(Write(b1))
         t2.next_to(b1, direction=RIGHT)
         self.play(FadeIn(t2))
         self.wait(3)
         self.play(FadeIn(g2))
         self.play(Write(b2))
         self.play(FadeOut(b1, b2, t2))
         self.play(Write(p5))
         self.wait(4)
         self.play(FocusOn(p5))
         self.wait(5)
         self.play(FadeOut(text_10_bg, p5))
         #Animaciones-Reales#
         self.play(Write(t3))
         self.wait(3)
         t4.move_to(2*UP)
         self.play(ReplacementTransform(t3, t4))
         

         

        def construct(self):
            self.propiedades()

#-------------------------------------------Definición de ortogonalidad
class Subescena2(Scene):
 

     def ortogonalidad(self):


      def construct(self):
            self.ortogonalidad()

            

# MathTex(r"\alpha") -> Código en LaTeX
# Tex("blabla") -> texto normal
# SurroundingRectangle(self, mobject, color=YELLOW, buff=SMALL_BUFF, **kwargs)
# VGroup(mobjects)
# Line(start=LEFT, end=RIGHT, buff=0, path_arc=None, **kwargs)
# 

class Subescena_3(Scene):
    '''
    La escena esta organizada de la siguiente forma: se definen cuatro funciones, cada una de ellas
    incluye la prueba de una de las propiedades. Al ejecutar cada una de estas funciones se anima la
    demostración de dicha propiedad en el lado derecho de la pantalla, sin afectar a los objetos
    que ya están definidos en el lado izquierdo.
    '''
    
    def demo_1(self):
        '''
        Función que contiene todos los objetos y animaciones para mostrar en pantalla la demostración
        de la primer propiedad del producto punto
        '''
        #----------- OBJETOS
        entries_v = [["v_{1}"], ["v_{2}"]] 
        vec_v = Matrix(entries_v,
                    left_bracket="\\big(",
                    right_bracket="\\big)").shift(LEFT)
        vec_v_label = MathTex(r"\vec{v} = ").next_to(vec_v, LEFT)

        entries_w = [["w_{1}"], ["w_{2}"]] 
        vec_w = Matrix(entries_w,
                    left_bracket="\\big(",
                    right_bracket="\\big)").shift(2*RIGHT)
        vec_w_label = MathTex(r"\vec{w} = ").next_to(vec_w, LEFT)
        entries_u = [["u_{1}"], ["u_{2}"]] 
        vec_u = Matrix(entries_u,
                    left_bracket="\\big(",
                    right_bracket="\\big)").shift(4*LEFT)
        vec_u_label = MathTex(r"\vec{u} = ").next_to(vec_u, LEFT)                    

        tresvecs = VGroup(vec_u, vec_u_label, vec_v, vec_v_label, vec_w, vec_w_label).scale(0.7).shift(4*RIGHT + UP) # SE QUEDA
        
        recordemos = Text("Recordemos que:").next_to(tresvecs,DOWN).scale(0.5)

        # Recordando la suma de vectores
        umw_entries = [["u_{1} + w_{1}"], ["u_{2} + w_{2}"]] 
        vec_umw = Matrix(umw_entries,
                    left_bracket="\\big(",
                    right_bracket="\\big)").next_to(recordemos,DOWN).shift(RIGHT)
        vec_umw_label = MathTex(r"\vec{u} + \vec{w} = ").next_to(vec_umw, LEFT)  
        umw = VGroup(vec_umw_label, vec_umw).scale(0.7)     
        
        # Demostración: S
        obj_1 = MathTex(r"  \langle\vec{u}+\vec{w},\vec{v}\rangle ").scale(0.8).shift(UP)
        obj_2 = MathTex(r" &= (\vec{u}+\vec{w})\cdot \vec{v} ").next_to(obj_1,RIGHT).scale(0.8)
        obj_3 = MathTex(r" &= (u_1+w_1)v_1 + (u_2+w_2)v_2 ").next_to(obj_2,DOWN).scale(0.8)
        obj_4 = MathTex(r" &= u_1v_1 + w_1v_1 + u_2v_2 + w_2v_2").next_to(obj_2,DOWN).scale(0.8)
        obj_5 = MathTex(r" &= u_1v_1 + u_2v_2 + w_1v_1 + w_2v_2").next_to(obj_2,DOWN).scale(0.8)
        obj_5 = MathTex(r" &= u_1v_1 + u_2v_2 + w_1v_1 + w_2v_2").next_to(obj_2,DOWN).scale(0.8)
        obj_6 = MathTex(r" &= (u_1v_1 + u_2v_2) + (w_1v_1 + w_2v_2)").next_to(obj_2,DOWN).scale(0.8)
        obj_7 = MathTex(r" &= \vec{u}\cdot \vec{v} + \vec{w}\cdot \vec{v} ").next_to(obj_3,DOWN).scale(0.8)
        obj_8 = MathTex(r" &= \langle \vec{u} , \vec{v} \rangle + \langle \vec{w} , \vec{v} \rangle ").next_to(obj_7,DOWN).scale(0.8)
        
        objs = VGroup(obj_1, obj_2, obj_6, obj_7, obj_8)

        final  = MathTex(r"\langle\vec{u}+\vec{w},\vec{v}\rangle &= \langle \vec{u} , \vec{v} \rangle + \langle \vec{w} , \vec{v} \rangle ").shift(UP)
        final.scale(0.8).move_to(obj_8)
        asi = Text("Así,").next_to(final, UP).scale(0.5)
        g_final = VGroup(asi, final).shift(UP)

        #####################
        ## ANIMACIONES DEMO 1 ###
        #####################
        self.play(Write(tresvecs))
        self.wait(1)
        self.play(Write(recordemos))
        self.play(Write(umw))

        self.play(FadeOut(tresvecs),FadeOut(recordemos), FadeOut(umw))

        # Animación de la demostración. Se quedan fijos los pasos que pasan del P.E. al P.P.
        # los pasos algebráicos se animan con transformaciones.
        self.play(Write(obj_1))
        self.play(Write(obj_2))
        self.play(Write(obj_3))
        self.wait(1)
        self.play(ReplacementTransform(obj_3, obj_4))
        self.wait(1)
        self.play(ReplacementTransform(obj_4, obj_5))
        self.wait(1)
        self.play(ReplacementTransform(obj_5, obj_6))
        self.wait(1)
        self.play(Write(obj_7))
        self.play(Write(obj_8))
        self.wait(1)
        self.play(FadeOut(objs))
        self.play(Write(g_final))
        self.wait(1)
        self.play(FadeOut(g_final))


    def demo_2(self):
        '''
        Función que contiene todos los objetos y animaciones para mostrar en pantalla la demostración
        de la segunda propiedad del producto punto
        '''
        #----------- OBJETOS
        entries_v = [["v_{1}"], ["v_{2}"]] 
        vec_v = Matrix(entries_v,
                    left_bracket="\\big(",
                    right_bracket="\\big)").shift(LEFT)
        vec_v_label = MathTex(r"\vec{v} = ").next_to(vec_v, LEFT)
        entries_u = [["u_{1}"], ["u_{2}"]] 
        vec_u = Matrix(entries_u,
                    left_bracket="\\big(",
                    right_bracket="\\big)").shift(4*LEFT)
        vec_u_label = MathTex(r"\vec{u} = ").next_to(vec_u, LEFT)          
               

        dosvecs = VGroup(vec_u, vec_u_label, vec_v, vec_v_label).scale(0.7).shift(4*RIGHT + UP)
        scalar_a = MathTex(r",\ a \in \mathbb{R}").next_to(dosvecs,RIGHT).scale(0.7)  # SE QUEDA

        # Recordamos multiplicación por un escalar
        recordemos = Text("Recordemos que:").next_to(dosvecs,1.5*DOWN).scale(0.5)

        au_entries = [["a\ u_1"], ["a\ u_2"]] 
        vec_au = Matrix(au_entries,
                    left_bracket="\\big(",
                    right_bracket="\\big)").next_to(recordemos,DOWN).shift(2*RIGHT)
        vec_au_label = MathTex(r"a\vec{u} = ").next_to(vec_au, LEFT)  
        au = VGroup(vec_au_label, vec_au).scale(0.7)     
        
        # Objetos para la demostración
        obj_1 = MathTex(r"  \langle a\vec{u}},\vec{v}\rangle ").scale(0.8).shift(UP)
        obj_2 = MathTex(r" &= (a\vec{u})\cdot \vec{v} ").next_to(obj_1,RIGHT).scale(0.8)
        obj_3 = MathTex(r" &= (au_1)v_1 + (au_2)v_2 ").next_to(obj_2,DOWN).scale(0.8)
        obj_4 = MathTex(r" &= a(u_1v_1) + a(u_2v_2)").next_to(obj_2,DOWN).scale(0.8)
        obj_5 = MathTex(r" &= a(u_1v_1 + u_2v_2)").next_to(obj_2,DOWN).scale(0.8)
        obj_6 = MathTex(r" &= a(\vec{u}\cdot \vec{v})").next_to(obj_3,DOWN).scale(0.8)
        obj_7 = MathTex(r" &= a \langle \vec{u} , \vec{v} \rangle").next_to(obj_6,DOWN).scale(0.8)
        
        objs = VGroup(obj_1, obj_2, obj_5, obj_6, obj_7)

        final  = MathTex(r"\langle a\vec{u}},\vec{v}\rangle &= a \langle \vec{u} , \vec{v} \rangle")
        final.scale(0.8).move_to(obj_7)
        asi = Text("Así,").next_to(final, 1.5*UP).scale(0.5)
        g_final = VGroup(asi, final)
        
        #####################
        ## ANIMACIONES DEMO 2 ###
        #####################
        self.play(Write(dosvecs))
        self.play(Write(scalar_a))
        self.wait(1)
        self.play(Write(recordemos))
        self.play(Write(au))

        self.play(FadeOut(dosvecs),FadeOut(recordemos), FadeOut(au), FadeOut(scalar_a))
        
        # Animación de la demostración
        self.play(Write(obj_1))
        self.play(Write(obj_2))
        self.play(Write(obj_3))
        self.wait(1)
        self.play(ReplacementTransform(obj_3, obj_4))
        self.wait(1)
        self.play(ReplacementTransform(obj_4, obj_5))
        self.wait(1)
        self.play(Write(obj_6))
        self.play(Write(obj_7))
        self.wait(1)
        self.play(FadeOut(objs))
        self.play(Write(g_final))
        self.wait(1)
        self.play(FadeOut(g_final))


    def demo_3(self):
        '''
        Función que contiene todos los objetos y animaciones para mostrar en pantalla la demostración
        de la tercer propiedad del producto punto
        '''
        #----------- OBJETOS
        entries_v = [["v_{1}"], ["v_{2}"]] 
        vec_v = Matrix(entries_v,
                    left_bracket="\\big(",
                    right_bracket="\\big)").shift(LEFT)
        vec_v_label = MathTex(r"\vec{v} = ").next_to(vec_v, LEFT)
        entries_u = [["u_{1}"], ["u_{2}"]] 
        vec_u = Matrix(entries_u,
                    left_bracket="\\big(",
                    right_bracket="\\big)").shift(4*LEFT)
        vec_u_label = MathTex(r"\vec{u} = ").next_to(vec_u, LEFT)          
               

        dosvecs = VGroup(vec_u, vec_u_label, vec_v, vec_v_label).scale(0.7).shift(4*RIGHT + UP)
        scalar_a = MathTex(r",\ a \in \mathbb{R}").next_to(dosvecs,RIGHT).scale(0.7)  # SE QUEDA

        # Recordamos multiplicación por un escalar
        recordemos = Text("Recordemos que:").next_to(dosvecs,1.5*DOWN).scale(0.5)

        au_entries = [["a\ u_1"], ["a\ u_2"]] 
        vec_au = Matrix(au_entries,
                    left_bracket="\\big(",
                    right_bracket="\\big)").next_to(recordemos,DOWN).shift(2*RIGHT)
        vec_au_label = MathTex(r"a\vec{u} = ").next_to(vec_au, LEFT)  
        au = VGroup(vec_au_label, vec_au).scale(0.7)     
        
        # Objetos para la demostración
        obj_1 = MathTex(r"  \langle a\vec{u}},\vec{v}\rangle ").scale(0.8).shift(UP)
        obj_2 = MathTex(r" &= (a\vec{u})\cdot \vec{v} ").next_to(obj_1,RIGHT).scale(0.8)
        obj_3 = MathTex(r" &= (au_1)v_1 + (au_2)v_2 ").next_to(obj_2,DOWN).scale(0.8)
        obj_4 = MathTex(r" &= a(u_1v_1) + a(u_2v_2)").next_to(obj_2,DOWN).scale(0.8)
        obj_5 = MathTex(r" &= a(u_1v_1 + u_2v_2)").next_to(obj_2,DOWN).scale(0.8)
        obj_6 = MathTex(r" &= a(\vec{u}\cdot \vec{v})").next_to(obj_3,DOWN).scale(0.8)
        obj_7 = MathTex(r" &= a \langle \vec{u} , \vec{v} \rangle").next_to(obj_6,DOWN).scale(0.8)
        
        objs = VGroup(obj_1, obj_2, obj_5, obj_6, obj_7)

        final  = MathTex(r"\langle a\vec{u}},\vec{v}\rangle &= a \langle \vec{u} , \vec{v} \rangle")
        final.scale(0.8).move_to(obj_7)
        asi = Text("Así,").next_to(final, 1.5*UP).scale(0.5)
        g_final = VGroup(asi, final)
        
        #####################
        ## ANIMACIONES DEMO 2 ###
        #####################
        self.play(Write(dosvecs))
        self.play(Write(scalar_a))
        self.wait(1)
        self.play(Write(recordemos))
        self.play(Write(au))

        self.play(FadeOut(dosvecs),FadeOut(recordemos), FadeOut(au), FadeOut(scalar_a))
        
        # Animación de la demostración
        self.play(Write(obj_1))
        self.play(Write(obj_2))
        self.play(Write(obj_3))
        self.wait(1)
        self.play(ReplacementTransform(obj_3, obj_4))
        self.wait(1)
        self.play(ReplacementTransform(obj_4, obj_5))
        self.wait(1)
        self.play(Write(obj_6))
        self.play(Write(obj_7))
        self.wait(1)
        self.play(FadeOut(objs))
        self.play(Write(g_final))
        self.wait(1)
        self.play(FadeOut(g_final))

    def demo_4(self):
        '''
        Función que contiene todos los objetos y animaciones para mostrar en pantalla la demostración
        de la cuarta propiedad del producto punto
        '''
        #----------- OBJETOS
        entries_v = [["v_{1}"], ["v_{2}"]] 
        vec_v = Matrix(entries_v,
                    left_bracket="\\big(",
                    right_bracket="\\big)").shift(LEFT)
        vec_v_label = MathTex(r"\vec{v} = ").next_to(vec_v, LEFT)
        entries_u = [["u_{1}"], ["u_{2}"]] 
        vec_u = Matrix(entries_u,
                    left_bracket="\\big(",
                    right_bracket="\\big)").shift(4*LEFT)
        vec_u_label = MathTex(r"\vec{u} = ").next_to(vec_u, LEFT)          
               

        dosvecs = VGroup(vec_u, vec_u_label, vec_v, vec_v_label).scale(0.7).shift(4*RIGHT + UP)
        scalar_a = MathTex(r",\ a \in \mathbb{R}").next_to(dosvecs,RIGHT).scale(0.7)  # SE QUEDA

        # Recordamos multiplicación por un escalar
        recordemos = Text("Recordemos que:").next_to(dosvecs,1.5*DOWN).scale(0.5)

        au_entries = [["a\ u_1"], ["a\ u_2"]] 
        vec_au = Matrix(au_entries,
                    left_bracket="\\big(",
                    right_bracket="\\big)").next_to(recordemos,DOWN).shift(2*RIGHT)
        vec_au_label = MathTex(r"a\vec{u} = ").next_to(vec_au, LEFT)  
        au = VGroup(vec_au_label, vec_au).scale(0.7)     
        
        # Objetos para la demostración
        obj_1 = MathTex(r"  \langle a\vec{u}},\vec{v}\rangle ").scale(0.8).shift(UP)
        obj_2 = MathTex(r" &= (a\vec{u})\cdot \vec{v} ").next_to(obj_1,RIGHT).scale(0.8)
        obj_3 = MathTex(r" &= (au_1)v_1 + (au_2)v_2 ").next_to(obj_2,DOWN).scale(0.8)
        obj_4 = MathTex(r" &= a(u_1v_1) + a(u_2v_2)").next_to(obj_2,DOWN).scale(0.8)
        obj_5 = MathTex(r" &= a(u_1v_1 + u_2v_2)").next_to(obj_2,DOWN).scale(0.8)
        obj_6 = MathTex(r" &= a(\vec{u}\cdot \vec{v})").next_to(obj_3,DOWN).scale(0.8)
        obj_7 = MathTex(r" &= a \langle \vec{u} , \vec{v} \rangle").next_to(obj_6,DOWN).scale(0.8)
        
        objs = VGroup(obj_1, obj_2, obj_5, obj_6, obj_7)

        final  = MathTex(r"\langle a\vec{u}},\vec{v}\rangle &= a \langle \vec{u} , \vec{v} \rangle")
        final.scale(0.8).move_to(obj_7)
        asi = Text("Así,").next_to(final, 1.5*UP).scale(0.5)
        g_final = VGroup(asi, final)
        
        #####################
        ## ANIMACIONES DEMO 2 ###
        #####################
        self.play(Write(dosvecs))
        self.play(Write(scalar_a))
        self.wait(1)
        self.play(Write(recordemos))
        self.play(Write(au))

        self.play(FadeOut(dosvecs),FadeOut(recordemos), FadeOut(au), FadeOut(scalar_a))
        
        # Animación de la demostración
        self.play(Write(obj_1))
        self.play(Write(obj_2))
        self.play(Write(obj_3))
        self.wait(1)
        self.play(ReplacementTransform(obj_3, obj_4))
        self.wait(1)
        self.play(ReplacementTransform(obj_4, obj_5))
        self.wait(1)
        self.play(Write(obj_6))
        self.play(Write(obj_7))
        self.wait(1)
        self.play(FadeOut(objs))
        self.play(Write(g_final))
        self.wait(1)
        self.play(FadeOut(g_final))
    

    def construct(self): # Cambiar a construct
        '''
        Aquí se definen objetos y animaciones que estarán a lo largo de toda la subescena, por lo que
        se definen en el método principal (construct). Siempre que queramos ver/omitir una de las pruebas
        podemos descomentar/comentar la línea donde se invoca la función.
        '''
        #-------------- DEFINICIÓN DEL PP EN ABSTRACTO: OPERACION Y PROPS (OBJETOS)
        pe_def = MathTex(r" \langle\cdot,\cdot\rangle:",r"V", r"\times ", r"V",r"\to ",r"K").shift(2*UP)
        pe_def_1 = MathTex(r" \forall \ \vec{u}, \vec{v}, \vec{w}&\in V, \ \forall \ a\in K ").next_to(pe_def, 1.1*DOWN)
        pe_def_2 = MathTex(r"  \langle\vec{u}+\vec{w},\vec{v}\rangle &= \langle \vec{u} , \vec{v} \rangle + \langle \vec{w} , \vec{v} \rangle ").next_to(pe_def_1, 1.1*DOWN)
        pe_def_3 = MathTex(r"  \langle a\vec{u} , \vec{v} \rangle &= a \langle \vec{u} , \vec{v} \rangle ").next_to(pe_def_2, 1.1*DOWN)
        pe_def_4 = MathTex(r"  \langle \vec{u} , \vec{v} \rangle &= \overline{ \langle \vec{v} , \vec{u} \rangle} ").next_to(pe_def_3, 1.1*DOWN)
        pe_def_5 = MathTex(r" \langle \vec{u}, \vec{u} \rangle > 0 \ &\ \text{si} \ \ \vec{u}\neq\vec{0} ").next_to(pe_def_4, 1.1*DOWN)

        #VGroup que contiene las propiedades que debe satisfacer el P.E. en abstracto
        pe_group_2 = VGroup(pe_def_1, pe_def_2, pe_def_3, pe_def_4, pe_def_5).scale(0.8).shift(0.5*DOWN)
        
        #---------------- PASANDO DE LO ABSRTACTO AL CASO PARTICULAR en R2 (OJETOS)
        pp_def = MathTex(r" \langle\cdot,\cdot\rangle:",r"\mathbb{R}^2", r"\times ", r"\mathbb{R}^2",r"\to ",r"\mathbb{R}").shift(2*UP) # SE QUEDA
        pp_def[1].set_color(AMARILLO)
        pp_def[3].set_color(AMARILLO)
        pp_def[5].set_color(AZUL_CLARO)
        entries_v = [["v_{1}"], ["v_{2}"]]  
        vec_v = Matrix(entries_v,
                    left_bracket="\\big(",
                    right_bracket="\\big)").shift(LEFT)
        vec_v_label = MathTex(r"v = ").next_to(vec_v, LEFT)

        entries_w = [["w_{1}"], ["w_{2}"]] 
        vec_w = Matrix(entries_w,
                    left_bracket="\\big(",
                    right_bracket="\\big)").shift(2*RIGHT)
        vec_w_label = MathTex(r"w = ").next_to(vec_w, LEFT)                    

        vecs_enR2 = VGroup(vec_v_label, vec_v, vec_w_label, vec_w).scale(0.9).shift(0.4*UP) # SE QUEDA
        pp_oper = MathTex(r"\langle \vec{v},\vec{w}\rangle  = \vec{v}\cdot\vec{w} = v_1w_1 + v_2w_2" ).shift(DOWN) #SE QUEDA

        #------------- REACOMODO DE LAS COSAS EN LA PANTALLA, DIBUJAMOS LÍNEAS (OBJETOS)
        
        linea_1 = Line(start = 7*LEFT + 0.5*UP, end = LEFT + 0.5*UP, buff= 0.5)
        linea_2 = Line(start = 4*UP + 1.5*LEFT, end = 4*DOWN + 1.5*LEFT, buff= 0.5)


    #####################
    ## ANIMACIONES   ###
    #####################

        # INTRODUCCION, PLANTEAMIENTO DEL CASO PARTICULAR Y DEFINICIÓN DEL PP 
        self.play(Write(pe_def))
        self.wait()
        self.play(Write(pe_group_2), runtime = 2)
        self.wait()
        self.play(pe_group_2.animate.set_opacity(0))
        self.play(ReplacementTransform(pe_def,pp_def))
        self.play(Write(vecs_enR2))
        self.wait(0.5)
        self.play(Write(pp_oper))

        #------ REACOMODO DE LOS OBJETOS Y DIBUJO DE LÍNEAS 
        self.play(pp_def.animate.shift(4*LEFT+1*UP).scale(0.7))
        self.play(vecs_enR2.animate.shift(4*LEFT+1.6*UP).scale(0.7))
        self.play(pp_oper.animate.shift(4*LEFT+2*UP).scale(0.7))
        self.play(Write(linea_1))
        self.play(Write(linea_2))

        
        self.play(pe_def_1.animate.shift(4*LEFT+0.5*DOWN).scale(0.6))
        self.play(pe_def_1.animate.set_opacity(1))
        self.play(pe_def_2.animate.shift(4*LEFT+0.8*DOWN).scale(0.8))
        self.play(pe_def_2.animate.set_opacity(1))
        self.play(pe_def_3.animate.shift(4*LEFT+0.8*DOWN).scale(0.8))
        self.play(pe_def_3.animate.set_opacity(1))
        self.play(pe_def_4.animate.shift(4*LEFT+0.8*DOWN).scale(0.8))
        self.play(pe_def_4.animate.set_opacity(1))
        self.play(pe_def_5.animate.shift(4*LEFT+0.8*DOWN).scale(0.8))
        self.play(pe_def_5.animate.set_opacity(1))

        #######################
        # ANIM PREVIAS A DEM 1 #
        #######################

        self.play(pe_def_3.animate.set_opacity(0.3), pe_def_4.animate.set_opacity(0.3),
        pe_def_4.animate.set_opacity(0.3), pe_def_5.animate.set_opacity(0.3))
        self.play(pe_def_2.animate.scale(1.2))

        self.demo_1() # Llamamos a la animación completa de la primer demostración

        #######################
        # ANIM PREVIAS A DEM 2 #
        #######################

        self.play(pe_def_2.animate.scale(1/1.2).set_opacity(0.3))
        self.play(pe_def_3.animate.set_opacity(1).scale(1.2))

        self.demo_2() # Llamamos a la animación completa de la segunda demostración

        #######################
        # ANIM PREVIAS A DEM 3 #
        #######################

        self.play(pe_def_3.animate.scale(1/1.2).set_opacity(0.3))
        self.play(pe_def_4.animate.set_opacity(1).scale(1.2))

        self.demo_3() # Llamamos a la animación completa de la tercera demostración

        #######################
        # ANIM PREVIAS A DEM 4 #
        #######################

        self.play(pe_def_4.animate.scale(1/1.2).set_opacity(0.3))
        self.play(pe_def_5.animate.set_opacity(1).scale(1.2))

        self.demo_4() # Llamamos a la animación completa de la cuarta demostración

        #####################
        # ANIMACIONES FINALES
        #####################
        self.play(pe_def_5.animate.scale(1/1.2))

        self.play(pe_def_2.animate.set_opacity(1))
        self.play(pe_def_3.animate.set_opacity(1))
        self.play(pe_def_4.animate.set_opacity(1))
