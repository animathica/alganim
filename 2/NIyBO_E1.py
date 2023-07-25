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


class SE2(MovingCameraScene):
    def propiedades(self):

        #Texto
        t0 = Tex("Norma")
        t1 = MathTex("||\\cdot||:V \\to", "\\mathbb{R}^{\\geq0}").scale(0.7)

        p1 = MathTex("\\forall \ \\vec{u},\\vec{v}\\in V, \ \\forall \ a\\in K,").scale(0.6)
        p1_C = MathTex("\\forall \ \\vec{u},\\vec{v}\\in V, \ \\forall \ a\\in \\mathbb{C},").scale(0.6).shift(0.725*UP+0.02*LEFT)
        p1_copy = p1.copy().shift(0.725*UP+0.02*LEFT)
        p2 = MathTex("||a\\vec{u}||", "=", "|a| \ ||\\vec{u}||").scale(0.6).move_to(1.5*LEFT).shift(0.25*DOWN)
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
        t5 = Tex("*", "Ver la ", "Pregunta 2.5 ", "al final del video.").scale(.55).to_edge(DOWN).shift(0.25*DOWN)
        t5[0].set_color(AMARILLO)
        t5[2].set_color(ROJO)
        t6 = Tex("*", "Ver el ", "Ejercicio 2.1", ".").scale(.55).to_edge(DOWN).shift(0.25*DOWN)
        t6[0].set_color(AMARILLO)
        t6[2].set_color(AZUL)

        g = VGroup(t2,t3,t4).arrange(direction=2.5*DOWN, aligned_edge=LEFT)
        g.next_to(tinv, RIGHT).shift(0.25*LEFT)
        t0.move_to(2*UP)
        t1.move_to(1.4*UP)
        p1.move_to(0.75*UP)
        p3.shift(0.15*LEFT)

        #Geometría
        grid = NumberPlane(x_range=[-3.25, 3.25, 1], y_range=[-3.25, 3.25, 1],
                           background_line_style={
                               "stroke_width": 1, "stroke_opacity": 0.5}
                           ).shift(6.75*LEFT)

        u1, u2, v1, v2 = ValueTracker(1.5), ValueTracker(-1), ValueTracker(0.5), ValueTracker(2.5) #Coordenadas de los vectores u y v

        vt_u = ValueTracker(1)
        vec_u = Vector(direction = [u1.get_value(), u2.get_value(), 0], color=AZUL).shift(6.75*LEFT)
        vec_u.add_updater(lambda v:
                          ( vec_u.become( (Vector([value*u1.get_value(), value*u2.get_value(), 0], buff=0, color=AZUL).shift(6.75*LEFT)) ) ) if ((value := vt_u.get_value()) != 0)
                          else vec_u.become(Circle(radius=0.025, color=AZUL).set_opacity(1).shift(6.75*LEFT))
                          )
        norm_u = MathTex(r"||\vec{u}||").scale(0.6)
        norm_u[0][2:4].set_color(AZUL)
        brace_u = BraceBetweenPoints(ORIGIN, [u1.get_value(), u2.get_value(), 0]).shift(6.75*LEFT)
        brace_u.put_at_tip(norm_u, buff=0)
        brace_u.add_updater(lambda v:
                            brace_u.become( BraceBetweenPoints(ORIGIN, [value*u1.get_value(), value*u2.get_value(), 0]).shift(6.75*LEFT) ) if ((value := vt_u.get_value()) > 0)
                            else ( ( brace_u.become( BraceBetweenPoints([value*u1.get_value(), value*u2.get_value(), 0], ORIGIN).shift(6.75*LEFT) ) ) if (value < 0) else ( brace_u.become( Line(start=6.75*LEFT - [0.175, 0.175, 0], end=6.75*LEFT - [0.35, 0.35, 0])) )
                                  )
                          )
        norm_u.add_updater(lambda n: (brace_u.put_at_tip(n, buff=0)) if (vt_u.get_value() != 0)
                           else n.set_opacity(1).move_to(7.345*LEFT+0.5*DOWN)
                           )
        geq0 = MathTex(r"0\leq").scale(0.6).next_to(norm_u, LEFT, buff=0.1)
        geq0.add_updater(lambda n: n.next_to(norm_u, LEFT, buff=0.1))

        vec_u_2 = Vector(direction = [u1.get_value(), u2.get_value(), 0], color=AZUL).shift(6.75*LEFT)
        norm_u_2 = MathTex(r"||\vec{u}||").scale(0.6)
        norm_u_2[0][2:4].set_color(AZUL)
        brace_u_2 = BraceBetweenPoints(ORIGIN, [u1.get_value(), u2.get_value(), 0]).shift(6.75*LEFT).shift([u1.get_value(), u2.get_value(), 0])
        brace_u_2.put_at_tip(norm_u_2, buff=0)

        vt_2u = ValueTracker(1)
        vec_2u = Vector(direction = [u1.get_value(), u2.get_value(), 0], color=AZUL).shift(6.75*LEFT)
        vec_2u.add_updater(lambda v:
                          vec_u.become( Vector([vt_2u.get_value()*u1.get_value(), vt_2u.get_value()*u2.get_value(), 0], buff=0, color=AZUL).shift(6.75*LEFT) )
                          )
        norm_2u = MathTex(r"||2\vec{u}||").scale(0.6)
        norm_2u[0][3:5].set_color(AZUL)
        brace_2u = BraceBetweenPoints([u1.get_value(), u2.get_value(), 0], ORIGIN).shift(6.75*LEFT).put_at_tip(norm_2u, buff=0.1)
        brace_2u.put_at_tip(norm_2u, buff=0)
        brace_2u.add_updater(lambda v:
                            brace_2u.become( BraceBetweenPoints([value*u1.get_value(), value*u2.get_value(), 0], ORIGIN).shift(6.75*LEFT) ) if ((value := vt_2u.get_value()) > 0)
                            else brace_2u.become( BraceBetweenPoints(ORIGIN, [value*u1.get_value(), value*u2.get_value(), 0]).shift(6.75*LEFT) )
                            )
        norm_2u.add_updater(lambda n: brace_2u.put_at_tip(n, buff=0))
        norm_m2u = MathTex(r"||-2\vec{u}||").scale(0.6)
        norm_m2u[0][4:6].set_color(AZUL)
        norm_m2u.add_updater(lambda n: brace_2u.put_at_tip(n, buff=0))

        norm_u_copy = MathTex(r"||\vec{u}||").scale(0.6)
        norm_u_copy[0][2:4].set_color(AZUL)
        brace_u_copy = BraceBetweenPoints(ORIGIN, [u1.get_value(), u2.get_value(), 0]).shift(6.75*LEFT)
        brace_u_copy.put_at_tip(norm_u_copy, buff=0)
        norm_u_copy_2 = MathTex(r"||\vec{u}||").scale(0.6)
        norm_u_copy_2[0][2:4].set_color(AZUL)
        brace_u_copy_2 = BraceBetweenPoints(ORIGIN, [u1.get_value(), u2.get_value(), 0]).shift(6.75*LEFT)
        brace_u_copy_2.put_at_tip(norm_u_copy_2, buff=0)

        vt_v = ValueTracker(0)
        vec_v = Arrow(start = ORIGIN, end = [v1.get_value(), v2.get_value(), 0], buff=0, color=ROJO).shift(6.75*LEFT)
        vec_v.add_updater(lambda v:
                          vec_v.become( Arrow(start = [vt_v.get_value()*u1.get_value(), vt_v.get_value()*u2.get_value(), 0], end = [v1.get_value()+vt_v.get_value()*u1.get_value(), v2.get_value()+vt_v.get_value()*u2.get_value(), 0], buff=0, color=ROJO).shift(6.75*LEFT) )
                          )
        norm_v = MathTex(r"||\vec{v}||").scale(0.6)
        norm_v[0][2:4].set_color(ROJO)
        brace_v = BraceBetweenPoints(ORIGIN, [v1.get_value(), v2.get_value(), 0]).shift(6.75*LEFT).put_at_tip(norm_v, buff=0)
        brace_v.add_updater(lambda v:
                          brace_v.become( BraceBetweenPoints([vt_v.get_value()*u1.get_value(), vt_v.get_value()*u2.get_value(), 0], [v1.get_value()+vt_v.get_value()*u1.get_value(), v2.get_value()+vt_v.get_value()*u2.get_value(), 0]).shift(6.75*LEFT) )
                          )
        norm_v.add_updater(lambda n: brace_v.put_at_tip(norm_v, buff=0))

        vec_upv = Vector(direction = [u1.get_value()+v1.get_value(), u2.get_value()+v2.get_value(), 0], buff=0, color=MAGENTA).shift(6.75*LEFT)
        vec_upv.add_updater(lambda v:
                          vec_upv.become( Vector(direction = [u1.get_value()+v1.get_value(), u2.get_value()+v2.get_value(), 0], buff=0, color=MAGENTA).shift(6.75*LEFT) )
                          )
        brace_upv = BraceBetweenPoints([u1.get_value()+v1.get_value(), u2.get_value()+v2.get_value(), 0], ORIGIN).shift(6.75*LEFT)
        norm_upv = MathTex(r"||\vec{u}+\vec{v}||").scale(0.6)
        norm_upv[0][2:7].set_color(MAGENTA)
        brace_upv.put_at_tip(norm_upv, buff=0)
        brace_upv.add_updater(lambda v:
                          brace_upv.become( BraceBetweenPoints([u1.get_value()+v1.get_value(), u2.get_value()+v2.get_value(), 0], ORIGIN).shift(6.75*LEFT) )
                          )
        norm_upv.add_updater(lambda n: brace_upv.put_at_tip(norm_upv, buff=0))

        #ANIMACIONES

        grid.shift(3.75*LEFT)
        vec_u.shift(3.75*LEFT)
        self.play(Write(t0))
        self.play(Write(t1[0]))
        self.wait()

        self.add(grid, vec_u)
        self.play(self.camera.frame.animate.move_to(3*LEFT), grid.animate.shift(3.75*RIGHT), vec_u.animate.shift(3.75*RIGHT))
        self.wait()
        self.play(Write(brace_u))
        self.play(Write(norm_u), reverse=True)
        self.wait()

        self.play(Write(geq0), reverse=True)
        self.wait(0.5)
        self.play(vt_u.animate.set_value(1.5))
        self.play(vt_u.animate.set_value(-1.5))
        self.play(vt_u.animate.set_value(1))
        self.play(Write(t1[1]))
        self.play(Unwrite(geq0))
        self.wait()

        vec_u_2.set_opacity(0)
        vec_2u.set_opacity(0)
        self.add(vec_u_2, vec_2u)
        self.play(vec_u_2.animate.set_opacity(1), vec_2u.animate.set_opacity(1))
        self.play(vec_u_2.animate.shift([u1.get_value(), u2.get_value(), 0]), run_time = 0.5)
        self.play(FadeIn(brace_u_2, norm_u_2), run_time = 0.5)
        self.wait()
        self.play(Write(brace_2u))
        self.play(vt_2u.animate.set_value(2))
        self.wait()
        self.play(Write(norm_2u))
        self.wait()
        self.play(Unwrite(norm_2u))
        self.wait()
        self.play(vt_2u.animate.set_value(1), FadeOut(vec_u_2, brace_u_2, norm_u_2))
        self.wait()
        self.play(vt_2u.animate.set_value(-2))
        self.play(Write(norm_m2u))
        self.wait()
        self.add(norm_u_copy, brace_u_copy, norm_u_copy_2, brace_u_copy_2)
        self.play(FadeOut(brace_u, norm_u),
                  brace_u_copy.animate.shift([-u1.get_value(), -u2.get_value(), 0]),
                  norm_u_copy.animate.shift([-u1.get_value(), -u2.get_value(), 0]))
        self.play(brace_u_copy_2.animate.shift([-2*u1.get_value(), -2*u2.get_value(), 0]),
                  norm_u_copy_2.animate.shift([-2*u1.get_value(), -2*u2.get_value(), 0])
                  )
        self.wait()
        self.play(Write(p1))
        self.wait()
        self.play(Write(p2[0][2:5]), reverse=True)
        self.wait()
        self.play(Write(p2[0][0:2]), Write(p2[0][5:7]))
        self.play(Write(p2[1]))
        self.play(Write(p2[2][3:]), run_time=1.5)
        self.play(Write(p2[2][:3]))
        self.wait()
        self.play(Write(t5), Transform(p1[0][12], p1_C[0][12]))
        self.wait()
        self.play(FadeOut(t5), Transform(p1[0][12], p1_copy[0][12]), run_time=0.5)
        self.wait()
        self.play(vt_2u.animate.set_value(0), FadeOut(brace_2u, norm_m2u, brace_u_copy, norm_u_copy, brace_u_copy_2, norm_u_copy_2, vec_2u)) # Arreglar el FadeOut de vec_2u
        self.wait()
        self.play(Write(t2))
        self.wait()

        self.play(FadeIn(brace_u, norm_u))
        self.wait()
        self.play(vt_u.animate.set_value(0), run_time=0.75)
        self.wait()
        cero = MathTex("=0").scale(0.6).next_to(norm_u, buff=0.1)
        self.play(Write(cero))
        self.wait()
        self.play(Write(p3[0]))
        self.play(Write(p3[1]))
        self.play(Write(p3[2]))
        self.wait()
        self.play(Write(t3))
        self.wait()
        self.play(Unwrite(cero))
        self.play(vt_u.animate.set_value(1), run_time=0.75)
        self.wait()
        self.play(FadeIn(vec_v, brace_v, norm_v))
        self.wait()
        self.play(vt_v.animate.set_value(1))
        self.play(FadeIn(vec_upv, brace_upv, norm_upv))
        self.wait()
        self.play(Write(p4[0]), Indicate(norm_upv, color=MAGENTA))
        self.play(Write(p4[1]))
        self.play(Write(p4[2]), Indicate(norm_u, color=AZUL), Indicate(norm_v, color=ROJO))
        self.wait()
        self.play(u1.animate.set_value(0.5), run_time=0.5)
        self.play(u2.animate.set_value(-2), run_time=0.5)
        self.play(v1.animate.set_value(2),  run_time=0.5)
        self.play(u1.animate.set_value(2.5),
                  u2.animate.set_value(0.5),
                  v1.animate.set_value(-3), 
                  v2.animate.set_value(2),
                  run_time=0.5
                  )
        self.play(u1.animate.set_value(1.5),
                  u2.animate.set_value(-1),
                  v1.animate.set_value(0.5), 
                  v2.animate.set_value(2.5),
                  run_time=0.5
                  )
        self.wait()
        self.play(Write(t4))
        self.wait()
        self.play(Write(t6))
        self.wait()
        self.play(FadeOut(t6), run_time=0.5)
        self.wait()

        self.play(self.camera.frame.animate.move_to(ORIGIN),
                  FadeOut(grid, vec_u, brace_u, norm_u, vec_v, brace_v, norm_v, vec_upv, brace_upv, norm_upv)
                  )
        self.wait()

    def construct(self):
        self.propiedades()
