from manim import *
#####################################################################################
######################  Norma inducida y bases ortonormales  #######################
#####################################################################################


#####################################################################################
###############################  Segunda escena  ####################################
###############################  versión: Manim Community v0.14.0   ##################
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

class Subescena2(MovingCameraScene):


     def bortonormal(self):

       texto1 = MathTex(r"\text{N}=\{\vec{n}_1,...,\vec{n}_k\}\subseteq V \ \text{es \emph{ortonormal}}").scale(.5)
       texto1_2 = MathTex(r" \text{ si} \ \langle \vec{n}_i , \vec{n}_j \rangle =").scale(.5)
       texto1_3 = MathTex(r"0 \text{ para } i\neq j \text{ con } 1\le i,j\le k",r"\text{ y }", r"||" , r"\vec{n}_i" , r"||", r"=1" , r"\text{ para } 1\le i\le k.").scale(.5)

       texto_1=VGroup(texto1, texto1_2, texto1_3).arrange(direction=RIGHT, center=True)
       texto1_2.next_to(texto1, RIGHT)
       texto1_3.next_to(texto1_2, RIGHT)
       texto_1.move_to(3*UP)

       texto2_3 = MathTex(r"0 \text{ para } i\neq j \text{ con } 1\le i,j\le k",r"\text{ y }", r" \langle " , r"\vec{n}_i" , r", \vec{n}_i \rangle", r"=1" , r"\text{ para } 1\le i\le k.").scale(.5)
       texto2_3.next_to(texto1_2, RIGHT)

       texto3_3 = MathTex(r" \begin{cases} 1 &\text{si } i=j \\ 0 &\text{si } i\neq j \end{cases} \text{ para } 1\le i,j\le k.").scale(.5)
       texto3_3.next_to(texto1_2, RIGHT)



       texto3 = MathTex(r"N=\{\vec{n}_1,...,\vec{n}_k\}" ).scale(.5)
       texto4 = MathTex(r"\text{ es base \emph{ortonormal} de } V \text{ si}").scale(.5)
       texto5 = MathTex(r"\text{dim}(V)=k.").scale(.5)
       texto5_c1 = Tex("$\\langle \\vec{n}_i, \\vec{n}_i\\rangle = 1 \\ $~", "si~","$i = j$").scale(.6)
       texto5_c2 = Tex("$0 \\ $~", " si~", " $i \\neq j,$").scale(.6)
       for i, item in enumerate(texto5_c2):
          item.align_to(texto5_c1[i], LEFT)
       texto5_c1g = VGroup(*texto5_c1)
       texto5_c2g = VGroup(*texto5_c2)
       texto5_c2g.next_to(texto5_c1g, DOWN)
       texto5_g = VGroup(texto5_c1g, texto5_c2g)
       b3 = Brace(texto5_g, .1*LEFT)
       P_ij = b3.get_text("$\\langle \\vec{n}_i, \\vec{n}_j\\rangle$ =").scale(.6)
       nj_ni = VGroup(P_ij, b3, texto5_g).arrange(direction=RIGHT, buff=.15)

       N_ort = VGroup(nj_ni, texto5).arrange(direction=RIGHT, buff=0.75, center=True)

       texto3.move_to(1.75*UP, aligned_edge=RIGHT)
       texto4.move_to(3*UP)
       texto4.next_to(texto3, direction=RIGHT)

       self.wait()
       self.play(self.camera.frame.animate.move_to(1.5*UP))

       for element in texto_1:
         self.play(Write(element), run_time=2)

       self.wait(2)
       self.play(ReplacementTransform(texto1_3, texto2_3))

       self.wait(2)
       self.play(FadeOut(texto2_3))
       self.play(Write(texto3_3))

       self.wait(2)
       self.play(Write(texto3))

       self.play(Write(texto4))
       self.wait(2)
       N_ort[0].move_to(2*LEFT)


       self.play(Write(N_ort[0]))
       self.play(Write(N_ort[1]))

     def construct(self):
      self.bortonormal()
