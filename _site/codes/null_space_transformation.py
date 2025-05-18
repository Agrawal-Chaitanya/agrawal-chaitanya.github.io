#%%
import manim
# %%

from manim import *

class NullSpaceProjection(ThreeDScene):
    def construct(self):
        # Title
        title = Text("Null Space as Lost Depth in Projection", font_size=36).to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)

        # Create 3D axes
        axes3d = ThreeDAxes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            z_range=[-3, 3],
            x_length=6,
            y_length=6,
            z_length=4,
        )
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        self.add(axes3d)

        # Define a point in 3D
        point3d = Dot3D(point=[1, 1, 2], radius=0.08, color=YELLOW)
        label3d = MathTex(r"\vec{v} = \begin{bmatrix} 1 \\ 1 \\ 2 \end{bmatrix}").next_to(point3d, RIGHT)

        # Projection (null space = z-component is lost)
        projected_point = Dot3D(point=[1, 1, 0], radius=0.08, color=GREEN)
        label_proj = MathTex(r"P\vec{v} = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}").next_to(projected_point, RIGHT)

        # Null space vector (maps to zero under projection)
        null_vec = Arrow3D(start=[0, 0, 0], end=[0, 0, 2], color=RED, thickness=0.02)
        null_label = MathTex(r"\vec{n} = \begin{bmatrix} 0 \\ 0 \\ 2 \end{bmatrix} \in \text{Null}(P)").next_to(null_vec, UP)

        # Add point and projection
        self.play(FadeIn(point3d), Write(label3d))
        self.wait(1)

        # Show projection
        self.play(FadeIn(projected_point), Write(label_proj))
        self.wait(1)

        # Animate a line from 3D point to projection (drop in Z)
        drop_line = DashedLine(point3d.get_center(), projected_point.get_center(), color=BLUE)
        self.play(Create(drop_line))
        self.wait(1)

        # Show the null space vector
        self.play(GrowArrow(null_vec), Write(null_label))
        self.wait(1)

        # Add explanation text
        explanation = Text(
            "Projection to 2D loses depth (z-component).\nThat lost direction is the null space!",
            font_size=28,
        ).to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(3)

        self.play(*[FadeOut(mob) for mob in self.mobjects])

# %%


# manim -pql animation.py NullSpaceProjection
