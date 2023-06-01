from manim import *
#####################################################################################
######################  Norma inducida y bases ortonormales  ########################
#####################################################################################

#####################################################################################
###############################  Primera escena  ####################################
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
CARTÓN = "#CD9F61"
CARTÓN_BORDE = "#C08F4F"


class SE1(Scene):
    def construct(self):
        plano = NumberPlane()
        caja = Square(fill_opacity=1, fill_color=CARTÓN, stroke_color=CARTÓN_BORDE, stroke_width=8, side_length=1)
        vec_u = Arrow(start=ORIGIN, end=3*UP, color=AZUL, buff=0)
        label_u = MathTex("\\vec{u}", color=AZUL).next_to(vec_u, 0.8*LEFT)
        vec_v = Arrow(start=ORIGIN, end=5*RIGHT, color=ROJO, buff=0)
        label_v = MathTex("\\vec{v}", color=ROJO).next_to(vec_v, 0.75*DOWN)

        vec_u_fantasma = Arrow(start=vec_v.get_end(), end=vec_v.get_end()+vec_u.get_end(), color=AZUL, buff=0)
        label_u_fantasma = MathTex("\\vec{u}", color=AZUL).next_to(vec_u_fantasma, 0.8*RIGHT)
        vec_v_fantasma = Arrow(start=vec_u.get_end(), end=vec_v.get_end()+vec_u.get_end(), color=ROJO, buff=0)
        label_v_fantasma = MathTex("\\vec{v}", color=ROJO).next_to(vec_v_fantasma, 0.75*UP)
        desplazamiento = Arrow(start=ORIGIN, end=vec_v.get_end()+vec_u.get_end(), color=MAGENTA, buff=0)
        label_desplazamiento_1 = MathTex("\\vec{u}+\\vec{v}").move_to(4*RIGHT+1.5*UP)
        label_desplazamiento_1[0][0:2].set_color(AZUL)
        label_desplazamiento_1[0][3:].set_color(ROJO)
        label_desplazamiento_1_box = SurroundingRectangle(label_desplazamiento_1, color=BLACK, fill_opacity=1)
        label_desplazamiento_2 = MathTex("\\vec{v}+\\vec{u}").move_to(RIGHT+1.5*UP)
        label_desplazamiento_2[0][0:2].set_color(ROJO)
        label_desplazamiento_2[0][3:].set_color(AZUL)
        label_desplazamiento_2_box = SurroundingRectangle(label_desplazamiento_2, color=BLACK, fill_opacity=1)
        igual = MathTex("=").move_to(3*DOWN)
        igual_box = SurroundingRectangle(igual, color=BLACK, fill_opacity=1, buff=0.25)

        #Empujando la caja
        self.next_section()
        self.play(Create(plano))
        self.wait()
        self.play(FadeIn(caja))
        self.wait()
        self.play(caja.animate.shift(3*UP), Create(vec_u)) #¡Arreglar sincronización con rate functions!
        self.play(FadeIn(label_u))
        self.wait()
        self.play(caja.animate.shift(5*RIGHT), Create(vec_v_fantasma))
        self.play(FadeIn(label_v_fantasma))
        self.wait()
        self.play(FadeIn(desplazamiento, label_desplazamiento_1_box))
        self.play(FadeIn(label_desplazamiento_1[0][0:2]))
        self.play(FadeIn(label_desplazamiento_1[0][2]), run_time=0.5)
        self.play(FadeIn(label_desplazamiento_1[0][3:]))
        self.wait()
        self.play(FadeOut(vec_u, label_u, vec_v_fantasma, label_v_fantasma, desplazamiento, label_desplazamiento_1_box, label_desplazamiento_1))
        self.play(caja.animate.shift(3*DOWN+5*LEFT))
        self.wait()
        self.play(caja.animate.shift(5*RIGHT), Create(vec_v))
        self.play(FadeIn(label_v))
        self.wait()
        self.play(caja.animate.shift(3*UP), Create(vec_u_fantasma))
        self.play(FadeIn(label_u_fantasma))
        self.next_section(skip_animations=True)
        self.wait()
        self.play(FadeIn(desplazamiento, label_desplazamiento_2_box))
        self.wait()
        self.play(FadeIn(label_desplazamiento_2[0][0:2]), run_time=0.5)
        self.play(FadeIn(label_desplazamiento_2[0][2]), run_time=0.5)
        self.play(FadeIn(label_desplazamiento_2[0][3:]))
        self.wait()
        self.play(FadeIn(vec_u, label_u, vec_v_fantasma, label_v_fantasma, label_desplazamiento_1_box, label_desplazamiento_1))
        self.wait()
        self.play(label_desplazamiento_1.animate.move_to(LEFT+3*DOWN), label_desplazamiento_1_box.animate.move_to(LEFT+3*DOWN), run_time=0.5)
        self.play(FadeIn(igual_box, igual), run_time=0.5)
        self.play(label_desplazamiento_2.animate.move_to(RIGHT+3*DOWN), label_desplazamiento_2_box.animate.move_to(RIGHT+3*DOWN), run_time=0.5)
        self.play(igual.animate.set_color(MAGENTA))
        self.wait()

        #Ley del Paralelogramo
        forall = MathTex("x \\ \\forall \\ \\vec{u}, \\vec{v} \\in \\mathbb{R}^2").move_to(1.6*RIGHT+3*DOWN)
        forall[0][0].set_color(BLACK)
        forall[0][2:4].set_color(AZUL)
        forall[0][5:7].set_color(ROJO)
        V = MathTex("V").set(center=forall[0][7].get_center())
        forall_box = SurroundingRectangle(forall, color=BLACK, fill_opacity=1)
        u_scale_VT = ValueTracker(0)
        v_scale_VT = ValueTracker(0)
        equation = VGroup(label_desplazamiento_1_box, igual_box, label_desplazamiento_2_box, label_desplazamiento_1, igual,  label_desplazamiento_2)
        def upd_for_vec_u_fantasma(obj):
            obj.become(Arrow(start=vec_v.get_end(), end=vec_v.get_end()+vec_u.get_end(), color=AZUL, buff=0))
        def upd_for_vec_v_fantasma(obj):
            obj.become(Arrow(start=vec_u.get_end(), end=vec_v.get_end()+vec_u.get_end(), color=ROJO, buff=0))
        def upd_for_desplazamiento(obj):
            obj.become(Arrow(start=ORIGIN, end=vec_v.get_end()+vec_u.get_end(), color=MAGENTA, buff=0))
        vec_u_fantasma.add_updater(upd_for_vec_u_fantasma)
        vec_v_fantasma.add_updater(upd_for_vec_v_fantasma)
        desplazamiento.add_updater(upd_for_desplazamiento)

        self.next_section(skip_animations=True)
        self.play(equation.animate.shift(1.5*LEFT), run_time=0.5)
        self.play(FadeIn(forall_box, forall))
        self.wait()
        self.play(FadeOut(caja, label_u, label_v, label_u_fantasma, label_v_fantasma)) #¡Arreglar GLITCH!
        self.play(Rotate(vec_u, angle=PI/5, about_point=vec_u.get_start()), Rotate(vec_v, angle=-4*PI/5, about_point=vec_v.get_start()))
        self.wait()


        #Axioma de conmutatividad
        self.next_section(skip_animations=True)
        #self.play(FadeIn(Rectangle(color=WHITE, width=3.5, height=0.7).move_to(DOWN*3)), run_time=0.5)


        #Magnitud
        self.next_section()


class SE2(Scene):
    def propiedades(self):
        t0 = Tex("Norma")
        t1 = MathTex("||\\cdot||:V \\to \\mathbb{R}_{\geq0}").scale(0.6)

        p1 = MathTex("\\forall \ \\vec{u},\\vec{v}\\in V, \ \\forall \ a\\in K,").scale(0.6)
        p2 = MathTex("||a\\vec{u}||", "=", "|a| \ ||\\vec{u}||").scale(0.6).move_to(2*LEFT)
        p3 = MathTex("||\\vec{u}|| = 0 ", " \\Longleftrightarrow", " \\vec{u} = \\vec{0}").scale(0.6).next_to(p2, 2*DOWN)
        p4 = MathTex("||\\vec{u}+\\vec{v}|| ", "\\le", " ||\\vec{u}|| + ||\\vec{v}||").scale(0.6).next_to(p3, 2*DOWN)

        pe2 = p2.get_part_by_tex("=")
        pe3 = p3.get_part_by_tex("\\Longleftrightarrow").align_to(pe2, LEFT)
        pe4 = p4.get_part_by_tex("\\le").align_to(pe3, LEFT)
        p2.get_part_by_tex("||a\\vec{u}||").next_to(pe2, LEFT)
        p2.get_part_by_tex("|a| \ ||\\vec{u}||").next_to(pe2, RIGHT)
        p3.get_part_by_tex("||\\vec{u}|| = 0 ").next_to(pe3, LEFT)
        p3.get_part_by_tex(" \\vec{u} = \\vec{0}").next_to(pe3, RIGHT)
        p4.get_part_by_tex("||\\vec{u}+\\vec{v}|| ").next_to(pe4, LEFT)
        p4.get_part_by_tex(" ||\\vec{u}|| + ||\\vec{v}||").next_to(pe4, RIGHT)

        tinv = Tex("aaaa", color = BLACK).scale(0.6).next_to(p3, RIGHT)
        t2 = Tex("Escalabilidad \\emph{absoluta}").scale(0.6)
        t3 = Tex("Distinción del vector nulo").scale(0.6)
        t4 = Tex("Desigualdad del triángulo").scale(0.6)

        g = VGroup(t2,t3,t4).arrange(direction=2.5*DOWN, aligned_edge=LEFT)
        g.next_to(tinv, RIGHT)
        t0.move_to(2.5*UP)
        self.play(Write(t0))
        t1.move_to(2*UP)
        p1.move_to(0.8*UP+2*LEFT)
        p3.shift(0.15*LEFT)

        #Animaciones
        self.play(Write(t1))
        self.play(Write(p1))

        self.play(Write(p2))
        self.play(Write(p3))
        self.play(Write(p4))
        self.play(Write(t2))
        self.play(Write(t3))
        self.play(Write(t4))

    def construct(self):
        self.propiedades()
