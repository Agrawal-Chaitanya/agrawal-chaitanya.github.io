#%%
import manim
# %%

from manim import *
import numpy as np

class NullSpaceProjection(ThreeDScene):
    def construct(self):
        # Title
        title = Text("Null Space as Lost Depth in Projection", font_size=36).to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)

        # 3D Axes
        axes3d = ThreeDAxes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            z_range=[-3, 3],
            x_length=6,
            y_length=6,
            z_length=4,
        )
        self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)
        self.add(axes3d)

        # Original 3D vector
        point3d = Dot3D(point=[1, 1, 2], radius=0.08, color=YELLOW)
        vector3d = Line(
            start=[0, 0, 0],
            end=[1, 1, 2],
            color=YELLOW
        )
        label3d = MathTex(r"\vec{v} = \begin{bmatrix} 1 \\ 1 \\ 2 \end{bmatrix}")
        self.add_fixed_in_frame_mobjects(label3d)
        label3d.next_to(point3d, RIGHT)

        # Projected point (z = 0)
        projected_point = Dot3D(point=[1, 1, 0], radius=0.08, color=GREEN)
        projected_vector = Line(
            start=[0, 0, 0],
            end=[1, 1, 0],
            color=GREEN
        )
        label_proj = MathTex(r"P\vec{v} = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}")
        self.add_fixed_in_frame_mobjects(label_proj)
        label_proj.next_to(projected_point, RIGHT)

        # Dashed projection line (drop line)
        drop_line = DashedLine(
            start=[1, 1, 2],
            end=[1, 1, 0],
            color=BLUE
        )

        # Null vector (depth direction only) - avoid using Arrow since it has the scale_tips parameter issue
        null_vec = Line(
            start=[0, 0, 0],
            end=[0, 0, 2],
            color=RED
        )
        
        # End dot to indicate direction
        null_end_dot = Dot3D(point=[0, 0, 2], radius=0.08, color=RED)
        
        null_label = MathTex(r"\vec{n} = \begin{bmatrix} 0 \\ 0 \\ 2 \end{bmatrix} \in \text{Null}(P)")
        self.add_fixed_in_frame_mobjects(null_label)
        null_label.move_to([2, 0, 2])  # Positioned for better visibility

        # XY Plane representation (the projection plane)
        xy_plane = Surface(
            lambda u, v: np.array([u, v, 0]),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(10, 10),
            fill_opacity=0.2,
            fill_color=BLUE_A,
            stroke_width=0
        )

        # Animation steps
        self.play(FadeIn(xy_plane))
        self.wait(0.5)
        
        # Original vector
        self.play(Create(vector3d), FadeIn(point3d), Write(label3d))
        self.wait(1)

        # Projected vector
        self.play(Create(projected_vector), FadeIn(projected_point), Write(label_proj))
        self.wait(1)

        # Show projection line
        self.play(Create(drop_line))
        self.wait(1)

        # Show null vector - avoid GrowArrow which uses scale_tips
        self.play(Create(null_vec), FadeIn(null_end_dot), Write(null_label))
        self.wait(1)

        # Explanation at the bottom
        explanation = Text(
            "Projection to 2D loses depth (z-component).\nThat lost direction is the null space!",
            font_size=28,
        ).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(explanation)
        self.play(Write(explanation))
        self.wait(2)
        
        # Add camera rotation to show the visualization from different angles
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        
        # Clean up
        self.play(*[FadeOut(mob) for mob in self.mobjects])



# %%


# manim -pql null_space_transformation.py NullSpaceProjection
