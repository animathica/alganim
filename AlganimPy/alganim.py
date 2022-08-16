from manim import *
from manim.mobject.geometry.tips import ArrowTriangleFilledTip
import warnings

class DashedArrow(DashedLine):
    """An arrow.

    Parameters
    ----------
    args : Any
        Arguments to be passed to :class:`Line`.
    stroke_width : :class:`float`, optional
        The thickness of the arrow. Influenced by :attr:`max_stroke_width_to_length_ratio`.
    buff : :class:`float`, optional
        The distance of the arrow from its start and end points.
    max_tip_length_to_length_ratio : :class:`float`, optional
        :attr:`tip_length` scales with the length of the arrow. Increasing this ratio raises the max value of :attr:`tip_length`.
    max_stroke_width_to_length_ratio : :class:`float`, optional
        :attr:`stroke_width` scales with the length of the arrow. Increasing this ratio ratios the max value of :attr:`stroke_width`.
    kwargs : Any
        Additional arguments to be passed to :class:`Line`.
    """
    def __init__(
        self,
        *args,
        stroke_width=6,
        buff=MED_SMALL_BUFF,
        max_tip_length_to_length_ratio=0.25,
        max_stroke_width_to_length_ratio=5,
        **kwargs,
    ):
        self.max_tip_length_to_length_ratio = max_tip_length_to_length_ratio
        self.max_stroke_width_to_length_ratio = max_stroke_width_to_length_ratio
        tip_shape = kwargs.pop("tip_shape", ArrowTriangleFilledTip)
        super().__init__(*args, buff=buff, stroke_width=stroke_width, **kwargs)
        # TODO, should this be affected when
        # Arrow.set_stroke is called?
        self.initial_stroke_width = self.stroke_width
        self.add_tip(tip_shape=tip_shape)
        self.set_stroke_width_from_length()
    def scale(self, factor, scale_tips=False, **kwargs):
        if self.get_length() == 0:
            return self

        if scale_tips:
            super().scale(factor, **kwargs)
            self.set_stroke_width_from_length()
            return self

        has_tip = self.has_tip()
        has_start_tip = self.has_start_tip()
        if has_tip or has_start_tip:
            old_tips = self.pop_tips()

        super().scale(factor, **kwargs)
        self.set_stroke_width_from_length()

        if has_tip:
            self.add_tip(tip=old_tips[0])
        if has_start_tip:
            self.add_tip(tip=old_tips[1], at_start=True)
        return self

    def get_normal_vector(self) -> np.ndarray:
        p0, p1, p2 = self.tip.get_start_anchors()[:3]
        return normalize(np.cross(p2 - p1, p1 - p0))

    def reset_normal_vector(self):
        """Resets the normal of a vector"""
        self.normal_vector = self.get_normal_vector()
        return self

    def get_default_tip_length(self) -> float:
        """Returns the default tip_length of the arrow.
        """
        max_ratio = self.max_tip_length_to_length_ratio
        return min(self.tip_length, max_ratio * self.get_length())

    def set_stroke_width_from_length(self):
        """Used internally. Sets stroke width based on length."""
        max_ratio = self.max_stroke_width_to_length_ratio
        if config.renderer == "opengl":
            self.set_stroke(
                width=min(self.initial_stroke_width, max_ratio * self.get_length()),
                recurse=False,
            )
        else:
            self.set_stroke(
                width=min(self.initial_stroke_width, max_ratio * self.get_length()),
                family=False,
            )
        return self


### Esta es la función de proyección ortogonal, ya general.
def OrthogonalProjection(VectorA, VectorB, color="#FFFF00", n_rays=25, dashed=True):
    # Vector A will be projected onto vector B.
    # Coordinates of each vector.
    Ax,Ay,_ = VectorA.get_end()
    Bx,By,_ = VectorB.get_end()
    # If vectors are orthogonal, there is no projection.
    if np.dot((Ax,Ay),(Bx,By)) == 0:
        warnings.warn("Vectors are orthogonal.")
        return
    # Coordinates of a vector orthogonal to B, in the desired direction.
    if np.linalg.norm((Ax+By,Ay-Bx)) < np.linalg.norm((Ax-By,Ay+Bx)):
        Ox,Oy = -By,Bx
    else:
        Ox,Oy = By,-Bx
    # List where each of the rays will be stored.
    rays = []
    # List where the coordinates of each ray will be stored.
    rayCoordinates = []
    # Computation of the projection and its norm.
    Px = ((Ax*Bx + Ay*By)/(Bx**2 + By**2)) * Bx
    Py = ((Ax*Bx + Ay*By)/(Bx**2 + By**2)) * By
    projectionNorm = np.linalg.norm((Px,Py))
    # Computation of each of the rays' coordinates.
    h = 1 if np.dot((Ax,Ay),(Bx,By)) > 0 else \
         - 1.3*(np.linalg.norm((Px,Py))/np.linalg.norm((Bx,By)))
    for i in range(0,n_rays+1):
        Rx = 0 + h*i*(Bx/n_rays)
        Ry = 0 + h*i*(By/n_rays)
        rayNorm = np.linalg.norm((Rx,Ry))
        if rayNorm < projectionNorm:
            inter = line_intersection(((0,0),(Ax,Ay)),\
                ((Rx,Ry),(Rx + Ox,Ry + Oy)))
            rayCoordinates.append([inter[0],inter[1]])                
        else:
            rayCoordinates.append((Rx,Ry))
    # Generating each ray.
    for i in rayCoordinates:
                if dashed:
                    ray = DashedLine( [i[0]+10*Ox,i[1]+10*Oy,0], [i[0],i[1],0], \
                        stroke_width=5, buff = 0.05).set_color(color)
                else:
                    ray = Line( [i[0]+10*Ox,i[1]+10*Oy,0], [i[0],i[1],0], \
                        stroke_width=5, buff = 0.05).set_color(color)
                rays.append(ray)
    # Creating a group containing the rays.
    rayGroup = VGroup()
    for i in rays:
        rayGroup.add(i)
    # The function returns the rays, they still need to be animated.
    return(rayGroup)

def Span1d(x,y,number_tips=10):

    x,y = x/np.linalg.norm((x,y)),y/np.linalg.norm((x,y))
    X,Y = 10*x,10*y

    span = VGroup()

    spanLine = Line((-X,-Y,0),(X,Y,0),
                        tip_length=0.2,
                        stroke_color=[BLUE],
                    )
    
    span.add(spanLine)

    for i in range(number_tips):
        spanTip1 = ArrowTriangleFilledTip()
        spanTip1.move_to((x*(i+1),y*(i+1),0)).rotate(np.arctan(y/x)+PI)
        span.add(spanTip1)
        spanTip2 = ArrowTriangleFilledTip()
        spanTip2.move_to((-x*(i+1),-y*(i+1),0)).rotate(np.arctan(y/x))
        span.add(spanTip2)

    return span

class SpanArrow(Arrow):
    def __init__(self, direction=RIGHT, buff=0, number_tips=5, **kwargs):
        self.buff = buff
        if len(direction) == 2:
            direction = np.hstack([direction, 0])
        super().__init__(ORIGIN, direction, buff=buff, **kwargs)
        self.add_tips(number_tips)

    def add_tips(self,number_tips):
        x,y = self.get_end()[0],self.get_end()[1]
        h = np.linalg.norm((x,y))/(np.linalg.norm((x,y))-(DEFAULT_ARROW_TIP_LENGTH/2))
        X, Y = x/h, y/h
        for i in range(number_tips-1,0,-1):
            tip = ArrowTriangleFilledTip(color=self.get_color())
            tip.move_to(((X/number_tips)*i,(Y/number_tips)*i,0)).rotate(self.tip.tip_angle+PI)
            self.add(tip)
        return self

class DoubleSpanArrow(DoubleArrow):
    def __init__(self, *args, **kwargs):
        if "tip_shape_end" in kwargs:
            kwargs["tip_shape"] = kwargs.pop("tip_shape_end")
        if "number_tips" in kwargs:
            number_tips = kwargs["number_tips"]
            kwargs.pop("number_tips")
        else:
            number_tips=10
        if "buff" not in kwargs:
            kwargs["buff"] = 0
        super().__init__(*args, **kwargs)
        self.add_tips(number_tips)

    def add_tips(self,number_tips):
        x1,y1 = self.get_start()[0],self.get_start()[1]
        x2,y2 = self.get_end()[0],self.get_end()[1]
        h = np.linalg.norm((x2-x1,y2-y1))/(np.linalg.norm((x2-x1,y2-y1))-(DEFAULT_ARROW_TIP_LENGTH))
        mx, my = (x1+x2)/2, (y1+y2)/2
        X1, Y1 = mx + ((x1-mx)/h), my + ((y1-my)/h)
        X2, Y2 = mx + ((x2-mx)/h), my + ((y2-my)/h)
        for i in range((number_tips//2)-1,0,-1):
            tip = ArrowTriangleFilledTip(color=self.get_color())
            tip.move_to((mx+((X1-mx)/number_tips)*i*2,my+((Y1-my)/number_tips)*i*2,0)).rotate(self.tip.tip_angle)
            self.add(tip)
        for i in range((number_tips//2)-1,0,-1):
            tip = ArrowTriangleFilledTip(color=self.get_color())
            tip.move_to((mx+((X2-mx)/number_tips)*i*2,my+((Y2-my)/number_tips)*i*2,0)).rotate(self.tip.tip_angle+PI)
            self.add(tip)
        return self
        
