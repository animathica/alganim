from manim import *
#####################################################################################
######################  Norma inducida y bases ortonormales  ########################
#####################################################################################

#####################################################################################
###############################  Tercera escena  ####################################
######################  versión: Manim Community v0.17.2   ##########################
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

class E3(Scene):
    def construct(self):

       texto1 = MathTex(r"(V,K)").shift(3*LEFT+ 2*UP).scale(0.6)
       texto1.to_edge(RIGHT)
       texto2 = MathTex(r" \langle \cdot , \cdot \rangle : V\times V\to K \ \text{es un producto escalar en} \ V ").scale(.6)

       texto_1=VGroup(texto1, texto2).arrange(direction=DOWN, center=False, aligned_edge=RIGHT)

       texto3=MathTex(r"||\vec{v}||:=\sqrt{\langle \vec{v} , \vec{v} \rangle} \quad \forall \ \vec{v}\in V").scale(.6).shift(0.5*UP)
       texto4=MathTex(r"||\cdot||:V \to K").scale(.6)
       texto5=MathTex(r"\forall \ \vec{v}\in V,", r" \forall \ a \in K,").scale(.6)
       texto6=MathTex(r"||a\vec{u}|| = \sqrt{\langle a\vec{u} , a\vec{u} \rangle}", r"= \sqrt{ a\overline{a}\langle \vec{u} , \vec{u} \rangle}", r" = \sqrt{a\overline{a}}", r"\sqrt{\langle \vec{u} , \vec{u} \rangle}", r" = |a| \ ||\vec{u}||").scale(.6)
       texto7=MathTex(r"|| \vec{u} ||= 0", r" \Longleftrightarrow" r"\sqrt{\langle \vec{u} , \vec{u} \rangle}", r" = 0", r"\Longleftrightarrow", r" \langle \vec{u} , \vec{u} \rangle = 0", r" \Longleftrightarrow ",  r"\vec{u} = \vec{0}").scale(.6)

       texto_2=VGroup(texto3, texto4, texto5,  texto6, texto7).arrange(direction=DOWN, center=False, aligned_edge=RIGHT)

       self.wait()

       for element in texto_1:
         self.play(Write(element), run_time=2)

       for element in texto_2:
         self.play(Write(element), run_time=2)
