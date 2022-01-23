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
         
         t1 =  MathTex("\langle\cdot, \cdot\\rangle:V\\times V\\to K ").scale(.8).shift(LEFT)

         p1 =  MathTex("\\forall \ \\vec{u}, \\vec{v}, \\vec{w}&\in V, \ \\forall \ a\in K ").scale(.6)


         p2 = MathTex("  \langle\\vec{u}+\\vec{w},\\vec{v}\\rangle").scale(.6)
         p2_2 = MathTex(" = \langle \\vec{u} , \\vec{v} \\rangle + \langle \\vec{w} , \\vec{v} \\rangle \\").scale(.6)


         p3 = MathTex("  \langle a\\vec{u} , \\vec{v} \\rangle").scale(.6)
         p3_2 = MathTex("&= a \langle \\vec{u} , \\vec{v} \\rangle\\").scale(.6)


         p4 = MathTex("  \langle \\vec{u} , \\vec{v} \\rangle").scale(.6)
         p4_2= MathTex("= \overline{ \langle \\vec{v} , \\vec{u} \\rangle}\\").scale(.6)


         p5 = MathTex(" \\vec{u}\\neq \\vec{0}").scale(.6)
         p5_2= MathTex("\Rightarrow \langle \\vec{u} , \\vec{u} \\rangle > 0 ").scale(.6)

         g1 = VGroup( p2, p2_2, p3, p3_2, p4, p4_2, p5, p5_2 ).arrange(buff=.13, direction=DOWN, aligned_edge = LEFT).shift(RIGHT+0.3*DOWN)
         p2.next_to(p2_2, LEFT)
         p3.next_to(p3_2, LEFT)
         p4.next_to(p4_2, LEFT)
         p5.next_to(p5_2, LEFT)


         g3 =VGroup(p2, p2_2, p3, p3_2, color=WHITE)
         b1 = Brace(g3, direction=RIGHT)
         t2 = MathTex("\langle a\\vec{u}+\\vec{w} , \\vec{v} \\rangle = a \langle \\vec{u} , \\vec{v} \\rangle + \langle \\vec{w} , \\vec{v} \\rangle\ ").scale(.6)
         t3 = MathTex("\langle \\vec{u} , a\\vec{w}+\\vec{v} \\rangle = \overline{a} \langle \\vec{u} , \\vec{w} \\rangle + \langle \\vec{u} , \\vec{v} \\rangle \\").scale(.6)
         t4 = Tex("\\textit{Linealidad} en la entrada izquierda").scale(.56)
         t5 = Tex("\\textit{Antilinealidad} en la entrada derecha").scale(.55)
         t6 = Tex("Positivo definido").scale(.55)
         t7 = Tex("Simetria conjugada").scale(.55)
         g4 = VGroup(g3,p4, color=WHITE)
         b2 = Brace(g4, direction=LEFT)



         #ANIMACIONES#
         t1.next_to(g1, 6*UP).shift(.45*LEFT)
         self.play(Write(t1))
         p1.next_to(t1, DOWN)
         self.play(Write(p1))
         self.wait(3)
         self.wait(23)
         g1.move_to(.1*UP)
         for element in g1:
          self.play(Write(element),run_time=2.3)
         t6.next_to(p5_2, RIGHT)
         t7.next_to(p4_2, RIGHT) 
         self.play(Write(t7))
         self.play(Write(t6))
         
         b1.next_to(p2_2, RIGHT*UP).shift(1.5*RIGHT+.3*DOWN)
         self.play(Write(b1))
         self.wait()
         t2.next_to(b1, direction=RIGHT)
         self.play(FadeIn(t2))
         t4.next_to(t2, DOWN)
         self.play(Write(t4))
                          
         self.wait(28)
         self.play(FadeIn(p4))
         b2.next_to(p3, LEFT*2*UP).shift(1.2*LEFT)
         self.play(Write(b2))
         t3.next_to(b2, direction=LEFT).shift(0.2*LEFT)
         self.play(Write(t3))
         t5.next_to(t3, DOWN)
         self.play(Write(t5))
         self.wait(23)
         self.play(FadeOut(b1, b2, t2, t3,t4,t5,t6,t7))
         self.wait(18)
         self.play(FadeOut(g1))
         self.play(FadeOut(t1,p1))

     def construct(self):
            self.propiedades()


#-------------------------------------------Definición de ortogonalidad
class Subescena2(Scene):
 

     def ortogonalidad(self):
     
       o1 = MathTex("\\vec{u},\\vec{v}\in V \ \\text{son \emph{ortogonales}} \ ").scale(.5)
       o1_2 = MathTex(" (\\vec{u}\perp\\vec{v}) \ \\text{si} \ \langle \\vec{u} , \\vec{v} \\rangle = 0 \ ").scale(.5)
       o1_3 = MathTex("\\text{ó, equivalentemente,} \ \langle \\vec{v} , \\vec{u} \\rangle = 0.").scale(.5)

       go_1=VGroup(o1, o1_2, o1_3).arrange(direction=RIGHT, center=True)
       o1_2.next_to(o1, RIGHT)
       o1_3.next_to(o1_2, RIGHT)
       go_1.move_to(3*UP)


       o2 = MathTex("\\text{O=}\{\\vec{o}_1,...,\\vec{o}_k\}\subseteq V ").scale(.5)
       o2_2=MathTex("\\text{es \emph{ortogonal} si} \ \langle \\vec{o}_i , \\vec{o}_j \\rangle = 0 ").scale(.5)
       o2_3= MathTex(" \\text{para} \ i\\neq j, \ \\text{con} \ 1\le i,j\le k.").scale(.5)

       go_2 =VGroup(o2, o2_2, o2_3).arrange(direction=RIGHT, center=True)
       go_2.move_to(2*UP)


      
       o3 = MathTex("  \Gamma=\{\\vec{g}_1,...,\\vec{g}_k\}" ).scale(.5)
       o4 = Tex("base  \\textit{ortogonal} de V").scale(.5)
       o5 = MathTex(r"\langle\Gamma\rangle = V, ").scale(.5)
       o5_c1 = Tex("$\\langle \\vec{g}_i, \\vec{g}_i\\rangle$~", "si~","$j = i$").scale(.6)
       o5_c2 = Tex("$0$~", " si~", " $j \\neq i$").scale(.6)
       for i, item in enumerate(o5_c2):
          item.align_to(o5_c1[i], LEFT)
       o5_c1g = VGroup(*o5_c1)
       o5_c2g = VGroup(*o5_c2)
       o5_c2g.next_to(o5_c1g, DOWN)
       o5_g = VGroup(o5_c1g, o5_c2g)
       b3 = Brace(o5_g, .1*LEFT)
       P_ij = b3.get_text("$\\langle \\vec{g}_i, \\vec{g}_j\\rangle$ =").scale(.6)
       gj_gi = VGroup(P_ij, b3, o5_g).arrange(direction=RIGHT, buff=.15)
       
       gamma_Prop = VGroup(o5, gj_gi).arrange(direction=RIGHT, buff=0.20, center=True)
       
        
       self.wait(8)
       for element in go_1:
         self.play(Write(element), run_time=2)
        
       for element in go_2:
         self.play(Write(element), run_time=2)

       o3.move_to(1.25*UP, aligned_edge=RIGHT)
       self.play(Write(o3))
       o4.move_to(3*UP)
       o4.next_to(o3, direction=RIGHT)
       self.play(Write(o4))
       self.wait(2)
       gamma_Prop[0].move_to(2*LEFT)

       self.play(Write(gamma_Prop[0]))
       self.play(Write(gamma_Prop[1]))

     def construct(self):
      self.ortogonalidad()
 

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

        obj_1 = MathTex(r"  \langle\vec{u}+\vec{w},\vec{v}\rangle ").scale(0.7).shift(2*UP+0.2*LEFT)
        obj_1_dup = MathTex(r"  \langle\vec{u}+\vec{w},\vec{v}\rangle ").move_to(obj_1).scale(0.7).shift(1.4*RIGHT)
        obj_2 = MathTex(r" \bigg( \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} + \begin{pmatrix} w_1 \\ w_2 \end{pmatrix} \bigg)\cdot \begin{pmatrix} v_1 \\ v_2 \end{pmatrix}").move_to(obj_1).scale(0.6).\
            shift(0.5*RIGHT)

        obj_3 = MathTex(r" &= \begin{pmatrix} u_1+w_1 \\ u_2 + w_2 \end{pmatrix}\cdot \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} ").next_to(obj_2, RIGHT).scale(0.6).shift(0.9*LEFT)
        obj_4 = MathTex(r" &= (u_1+w_1) v_1 + (u_2+w_2) v_2").scale(0.7)
        obj_5 = MathTex(r" &= u_1v_1 + w_1v_1 + u_2v_2 + w_2v_2").scale(0.7)
        obj_6 = MathTex(r" &= u_1v_1 + u_2v_2 + w_1v_1 + w_2v_2").scale(0.7)
        obj_7 = MathTex(r" &= (u_1v_1 + u_2v_2) + (w_1v_1 + w_2v_2)").scale(0.65)
        obj_8 = MathTex(r" &= \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} \cdot \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} + \begin{pmatrix} w_1 \\ w_2 \end{pmatrix} \cdot \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} ").scale(0.6)

        grupo = VGroup(obj_3, obj_4, obj_5, obj_6, obj_7, obj_8).arrange(1.5*DOWN, center=False, aligned_edge=LEFT)
        obj_9 = MathTex(r" &= \langle \vec{u} , \vec{v} \rangle + \langle \vec{w} , \vec{v} \rangle ").move_to(obj_8).scale(0.7).shift(0.8*LEFT)
       

        srct_1 = SurroundingRectangle(obj_1_dup)
        srct_2 = SurroundingRectangle(obj_9)

        objs = VGroup(obj_1_dup, obj_2, obj_3, obj_4, obj_5, obj_6, obj_7, obj_8, obj_9, srct_1, srct_2)

        # PALOMA PARA ACOMPAÑAR A LA PROPIEDAD PROBADA
        p1 = Line(ORIGIN, [1,1,0], color = VERDE, buff = 2).shift(0.1*LEFT)
        p2 = Line([-0.5,0.5,0], ORIGIN, color = VERDE, buff = 2)
        
        paloma = VGroup(p1,p2).scale(0.2).set_opacity(0).shift(2*LEFT+1.4*DOWN)
        #####################
        ## ANIMACIONES DEMO 1 ###
        #####################
        self.play(Write(obj_1))
        self.wait(1)
        self.play(ReplacementTransform(obj_1,obj_2))
        self.play(Write(obj_3))
        self.play(Write(obj_4))
        self.play(Write(obj_5))
        self.play(Write(obj_6))
        self.play(Write(obj_7))
        self.play(Write(obj_8))
        self.wait(1)
        self.play(ReplacementTransform(obj_8,obj_9))
        self.wait(1)
        self.play(ReplacementTransform(obj_2, obj_1_dup))
        self.play(Write(srct_1), Write(srct_2))
        self.wait(2)
        self.play(paloma.animate.set_opacity(1))
        self.play(FadeOut(objs))


    def demo_2(self):
        '''
        Función que contiene todos los objetos y animaciones para mostrar en pantalla la demostración
        de la segunda propiedad del producto punto
        '''
        #----------- OBJETOS

        obj_1 = MathTex(r"  \langle a\vec{u}},\vec{v}\rangle ").scale(0.7).shift(1.5*UP+RIGHT)
        inter = MathTex(r"a \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} \cdot \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} ").scale(0.7).move_to(obj_1)
        inter2 = MathTex(r" \langle a\vec{u}},\vec{v}\rangle ").scale(0.7).move_to(obj_1).shift(0.5*RIGHT)
        obj_2 = MathTex(r" &= \begin{pmatrix} au_1 \\ au_2 \end{pmatrix} \cdot \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} ").scale(0.7).next_to(inter, RIGHT)
        obj_3 = MathTex(r" &= (au_1)v_1 + (au_2)v_2 ").scale(0.7)
        obj_4 = MathTex(r" &= a(u_1v_1) + a(u_2v_2)").scale(0.7)
        obj_5 = MathTex(r" &= a(u_1v_1 + u_2v_2)").scale(0.7)
        obj_6 = MathTex(r" &= a \left(\begin{pmatrix} u_1 \\ u_2 \end{pmatrix} \cdot \begin{pmatrix} v_1 \\ v_2 \end{pmatrix}\right)")\
            .scale(0.7)
        
        grupo = VGroup(obj_2, obj_3, obj_4, obj_5, obj_6).arrange(1.5*DOWN, center=False, aligned_edge=LEFT)
        obj_7 = MathTex(r" &= a \langle \vec{u} , \vec{v} \rangle").move_to(obj_6).scale(0.7).shift(0.85*LEFT)

        objs = VGroup( inter2, grupo, obj_7)

        
        srct_1 = SurroundingRectangle(inter2)
        srct_2 = SurroundingRectangle(obj_7)

        srects = VGroup(srct_1,srct_2)

        # PALOMA PARA ACOMPAÑAR A LA PROPIEDAD PROBADA
        p1 = Line(ORIGIN, [1,1,0], color = VERDE, buff = 2).shift(0.1*LEFT)
        p2 = Line([-0.5,0.5,0], ORIGIN, color = VERDE, buff = 2)
        
        paloma = VGroup(p1,p2).scale(0.2).set_opacity(0).shift(2.9*LEFT+2*DOWN)
        #####################
        ## ANIMACIONES DEMO 2 ###
        #####################
        
        # Animación de la demostración
        self.play(Write(obj_1))
        self.wait(1)        
        self.play(ReplacementTransform(obj_1,inter))
        self.play(Write(obj_2))
        self.play(Write(obj_3))
        self.play(Write(obj_4))
        self.play(Write(obj_5))
        self.play(Write(obj_6))
        self.wait(1)
        self.play(ReplacementTransform(obj_6,obj_7))
        self.wait(1)
        self.play(ReplacementTransform(inter, inter2))
        self.play(Write(srct_1), Write(srct_2))
        self.wait(2)
        self.play(paloma.animate.set_opacity(1))
        self.play(FadeOut(srects), FadeOut(objs) )


    def demo_3(self):
        '''
        Función que contiene todos los objetos y animaciones para mostrar en pantalla la demostración
        de la tercer propiedad del producto punto
        '''
        #----------- OBJETOS       
        obj_1 = MathTex(r" \overline{ \langle \vec{v} , \vec{u} \rangle}").scale(0.8).shift(1.5*UP+1*RIGHT)
        obj_2 = MathTex(r" \overline{ \bigg(\begin{pmatrix} v_1 \\ v_2 \end{pmatrix} \cdot \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} \bigg)}").scale(0.7).move_to(obj_1)
        obj_1_dup = MathTex(r" \overline{ \langle \vec{v} , \vec{u} \rangle}").scale(0.8).move_to(obj_2).shift(0.9*RIGHT)
        obj_3 = MathTex(r" &= \overline{ (v_1u_1 + v_2u_2)}").next_to(obj_2, 0.8*RIGHT).scale(0.8)
        obj_4 = MathTex(r" &= v_1u_1 + v_2u_2").scale(0.8)
        obj_5 = MathTex(r" &= u_1v_1 + u_2v_2").scale(0.8)
        obj_6 = MathTex(r" &= \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} \cdot \begin{pmatrix} v_1 \\ v_2 \end{pmatrix}").scale(0.8)

        grupo = VGroup(obj_3, obj_4, obj_5, obj_6).arrange(1.5*DOWN, center=False, aligned_edge=LEFT)
        obj_7 = MathTex(r" &= \langle \vec{u},\vec{v}\rangle ").move_to(obj_6).scale(0.8).shift(0.65*LEFT)

        srct_1 = SurroundingRectangle(obj_1_dup)
        srct_2 = SurroundingRectangle(obj_7)

        objs = VGroup(obj_1_dup, grupo, srct_1, srct_2, obj_7)
        
        # PALOMA PARA ACOMPAÑAR A LA PROPIEDAD PROBADA
        p1 = Line(ORIGIN, [0.95,1,0], color = VERDE, buff = 2).shift(0.1*LEFT)
        p2 = Line([-0.5,0.5,0], ORIGIN, color = VERDE, buff = 2)
        
        paloma = VGroup(p1,p2).scale(0.2).set_opacity(0).shift(3.1*LEFT+2.6*DOWN)

        #####################
        ## ANIMACIONES DEMO 3 ###
        #####################

        self.play(Write(obj_1))
        self.play(ReplacementTransform(obj_1, obj_2))
        self.play(Write(obj_3))
        self.play(Write(obj_4))
        self.play(obj_4.animate.scale(1.2))
        self.wait(1)
        self.play(obj_4.animate.scale(1/1.2))
        self.play(Write(obj_5))
        self.play(Write(obj_6))
        self.wait(1)
        self.play(ReplacementTransform(obj_6, obj_7))
        self.wait(2)
        self.play(ReplacementTransform(obj_2, obj_1_dup))
        self.play(Write(srct_1),Write(srct_2))
        self.wait(2)
        self.play(paloma.animate.set_opacity(1))
        self.play(FadeOut(objs))

    def demo_4(self):

        c_nonzero = MathTex(r" \forall \ c \in \mathbb{R}, c\neq0 &\Rightarrow c^2>0").shift(3*UP+3*RIGHT).scale(0.8)
        
        #----------- OBJETOS       
        obj_1 = MathTex(r" \vec{u}\neq \vec{0} ").scale(0.8).shift(1.5*UP+1*RIGHT)
        obj_2 = MathTex(r" \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} \neq \begin{pmatrix} 0 \\ 0 \end{pmatrix}").scale(0.7).move_to(obj_1)
        obj_1_dup = MathTex(r" \vec{u}\neq \vec{0}").scale(0.8).move_to(obj_2).shift(0.5*RIGHT)
        obj_3 = MathTex(r" \Rightarrow u_1 \ \text{ó} \ u_2 \neq 0").next_to(obj_2, 0.8*RIGHT).scale(0.8).shift(0.3*LEFT)
        obj_4 = MathTex(r" \Rightarrow u_1^2 + u_2^2 > 0").scale(0.8)
        obj_5 = MathTex(r" \Rightarrow u_1u_1 + u_2u_2 > 0").scale(0.8)
        obj_6 = MathTex(r" \Rightarrow \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} \cdot \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} > 0")\
            .scale(0.8)
        
        grupo = VGroup(obj_3, obj_4, obj_5, obj_6).arrange(1.5*DOWN, center=False, aligned_edge=LEFT)

        obj_7 = MathTex(r" \Rightarrow \langle \vec{u} , \vec{u} \rangle > 0 ").move_to(obj_6).scale(0.8).shift(0.65*LEFT)

        srct_1 = SurroundingRectangle(obj_1_dup)
        srct_2 = SurroundingRectangle(obj_7)

        objs = VGroup(obj_1_dup, grupo, srct_1, srct_2, obj_7, c_nonzero)

        # PALOMA PARA ACOMPAÑAR A LA PROPIEDAD PROBADA
        p1 = Line(ORIGIN, [1,1,0], color = VERDE, buff = 2).shift(0.1*LEFT)
        p2 = Line([-0.5,0.5,0], ORIGIN, color = VERDE, buff = 2)
        
        paloma = VGroup(p1,p2).scale(0.2).set_opacity(0).shift(2.5*LEFT+3.2*DOWN)

        #####################
        ## ANIMACIONES DEMO 4 ###
        #####################
        self.play(Write(c_nonzero))
        self.play(Write(obj_1))
        self.play(ReplacementTransform(obj_1, obj_2))
        self.play(Write(obj_3))
        self.play(Write(obj_4))
        self.play(Write(obj_5))
        self.play(Write(obj_6))
        self.wait(1)
        self.play(ReplacementTransform(obj_6, obj_7))
        self.wait(2)
        self.play(ReplacementTransform(obj_2, obj_1_dup))
        self.play(Write(srct_1),Write(srct_2))
        self.wait(2)
        self.play(paloma.animate.set_opacity(1))
        self.play(FadeOut(objs))

        
    def construct(self): # Cambiar a construct
        '''
        Aquí se definen objetos y animaciones que estarán a lo largo de toda la subescena, por lo que
        se definen en el método principal (construct). Siempre que queramos ver/omitir una de las pruebas
        podemos descomentar/comentar la línea donde se invoca la función.
        '''

        #-------------- DEFINICIÓN DEL PP EN ABSTRACTO: OPERACION Y PROPS (OBJETOS)
        pe_def = MathTex(r" \langle\cdot,\cdot\rangle:",r"V", r"\times ", r"V",r"\to ",r"K").shift(2*UP)
        pe_def_1 = MathTex(r" \forall \ \vec{u}, \vec{v}, \vec{w}&\in V, \ \forall \ a\in K ").next_to(pe_def, 1.1*DOWN)
        pe_def_2 = MathTex(r"  \langle\vec{u}+\vec{w},\vec{v}\rangle &= \langle \vec{u} , \vec{v} \rangle + \langle \vec{w} , \vec{v} \rangle ").next_to(pe_def_1.get_center(), 2*DOWN)\
            .shift(0.15*RIGHT)
        pe_def_3 = MathTex(r"  \langle a\vec{u} , \vec{v} \rangle &= a \langle \vec{u} , \vec{v} \rangle ").next_to(pe_def_2.get_center(), 1.5*DOWN).shift(0.45*LEFT)
        pe_def_4 = MathTex(r"  \langle \vec{u} , \vec{v} \rangle &= \overline{ \langle \vec{v} , \vec{u} \rangle} ").next_to(pe_def_3.get_center(), 1.5*DOWN)
        pe_def_5 = MathTex(r" \vec{u}\neq \vec{0} \Rightarrow \langle \vec{u} , \vec{u} \rangle > 0 ").next_to(pe_def_4.get_center(), 1.5*DOWN).shift(0.4*RIGHT)

        #VGroup que contiene las propiedades que debe satisfacer el P.E. en abstracto
        pe_group_2 = VGroup(pe_def_1, pe_def_2, pe_def_3, pe_def_4, pe_def_5).scale(0.8).shift(0.5*DOWN)
        
        #---------------- PASANDO DE LO ABSRTACTO AL CASO PARTICULAR en R2 (OJETOS)
        pp_def = MathTex(r" \langle\cdot,\cdot\rangle:",r"\mathbb{R}^2", r"\times ", r"\mathbb{R}^2",r"\to ",r"\mathbb{R}").shift(2*UP) # SE QUEDA
        pp_def[1].set_color(AMARILLO)
        pp_def[3].set_color(AMARILLO)
        pp_def[5].set_color(AZUL_CLARO)          
        pp_oper = MathTex(r"\langle \vec{v},\vec{w}\rangle = \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} \cdot \begin{pmatrix} w_1 \\ w_2 \end{pmatrix}= v_1w_1 + v_2w_2") #SE QUEDA

        #------------- REACOMODO DE LAS COSAS EN LA PANTALLA, DIBUJAMOS LÍNEAS (OBJETOS)
        
        linea_1 = Line(start = 7*LEFT + 0.5*UP, end = LEFT + 0.5*UP, buff= 0.5)
        linea_2 = Line(start = 4*UP + 1.5*LEFT, end = 4*DOWN + 1.5*LEFT, buff= 0.5)


        

    #####################
    ## ANIMACIONES   ###
    #####################

        # INTRODUCCION, PLANTEAMIENTO DEL CASO PARTICULAR Y DEFINICIÓN DEL PP 
        self.play(Write(pe_def))
        self.wait()
        self.play(Write(pe_group_2))
        self.wait()
        self.play(pe_group_2.animate.set_opacity(0))
        self.play(ReplacementTransform(pe_def,pp_def))
        self.wait(0.5)
        self.play(Write(pp_oper))

        #------ REACOMODO DE LOS OBJETOS Y DIBUJO DE LÍNEAS 
        self.play(pp_def.animate.shift(4*LEFT+1*UP).scale(0.7))
        self.play(pp_oper.animate.shift(4.1*LEFT+1.8*UP).scale(0.6))
        self.play(Write(linea_1))
        self.play(Write(linea_2))

        
        self.play(pe_def_1.animate.shift(4.2*LEFT+0.8*DOWN).scale(0.7))
        self.play(pe_def_1.animate.set_opacity(1))
        self.play(pe_def_2.animate.next_to(pe_def_1.get_center(), 1.5*DOWN).shift(0.15*RIGHT).scale(0.8))
        self.play(pe_def_2.animate.set_opacity(1))
        self.play(pe_def_3.animate.next_to(pe_def_2.get_center(), 1.5*DOWN).shift(0.27*LEFT).scale(0.8))
        self.play(pe_def_3.animate.set_opacity(1))
        self.play(pe_def_4.animate.next_to(pe_def_3.get_center(), 1.5*DOWN).scale(0.8))
        self.play(pe_def_4.animate.set_opacity(1))
        self.play(pe_def_5.animate.next_to(pe_def_4.get_center(), 1.5*DOWN).shift(0.27*RIGHT).scale(0.8))
        self.play(pe_def_5.animate.set_opacity(1))

        #######################
        # ANIM PREVIAS A DEM 1 #
        #######################

        self.play(pe_def_3.animate.set_opacity(0.3), pe_def_4.animate.set_opacity(0.3),
        pe_def_4.animate.set_opacity(0.3), pe_def_5.animate.set_opacity(0.3))
        self.play(pe_def_2.animate.scale(1.1))

        self.demo_1() # Llamamos a la animación completa de la primer demostración

        #######################
        # ANIM PREVIAS A DEM 2 #
        #######################

        self.play(pe_def_2.animate.scale(1/1.1))
        self.play(pe_def_2.animate.set_opacity(0.3))
        self.play(pe_def_3.animate.set_opacity(1).scale(1.2))

        self.demo_2() # Llamamos a la animación completa de la segunda demostración

        #######################
        # ANIM PREVIAS A DEM 3 #
        #######################

        self.play(pe_def_3.animate.scale(1/1.1))
        self.play(pe_def_3.animate.set_opacity(0.3))
        self.play(pe_def_4.animate.set_opacity(1).scale(1.1))

        self.demo_3() # Llamamos a la animación completa de la tercera demostración


        #######################
        # ANIM PREVIAS A DEM 4 #
        #######################

        self.play(pe_def_4.animate.scale(1/1.1))
        self.play(pe_def_4.animate.set_opacity(0.3))
        self.play(pe_def_5.animate.set_opacity(1).scale(1.1))

        self.demo_4() # Llamamos a la animación completa de la cuarta demostración

    

        #####################
        # ANIMACIONES FINALES
        #####################
        self.play(pe_def_5.animate.scale(1/1.1))

        self.play(pe_def_2.animate.set_opacity(1))
        self.play(pe_def_3.animate.set_opacity(1))
        self.play(pe_def_4.animate.set_opacity(1))
        
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time = 1)
