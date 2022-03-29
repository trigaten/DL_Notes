from email.headerregistry import Group
from typing import Text

from collections import defaultdict
from manim import *

vocabulary = ["the", "is", "cat", "black", "<END>"]
probs = [
        [[0.6, 0.3, 0.05, 0.02, 0.03]], 
        [[0.1, 0.2, 0.9, 0.3, 0.4], [0.8, 0.1, 0.5, 0.3, 0.2]],
        [[0.1, 0.2, 0.1, 0.3, 0.9], [0.8, 0.1, 0.0, 0.3, 0.2]]
]
second_scores = [[0.1, 0.2, 0.9, 0.3, 0.4], [0.8, 0.1, 0.5, 0.3, 0.2]]

def make_beam(probs):
    circles = []
    for i, word in enumerate(vocabulary):
        text = Text(word, font_size=24)
        circle = Circle()  # create a circle
        score = probs[i]
        greens = [PURE_BLUE for i in range(int(score * 100))]
        reds = [PURE_RED for i in range(int((1-score) * 100))]
        # circle.set_fill(average_color(*greens, *reds), opacity=0.5)  # set the color and transparency
        circle.set_color(BLACK)
        circle.set_fill(average_color(*greens, *reds), opacity=0.5) 
        circle.scale(0.6)
        circle_with_text = Group(circle, text)
        circles.append(circle_with_text)
        if i > 0:
            circle_with_text.next_to(circles[i-1], DOWN, buff=0.1)
    
    beam = Group(*circles)
    return beam

class BeamSearch(MovingCameraScene):

    def construct(self):
        scaled = False
        beam_groups = defaultdict(list)
        for time_step, beam_prob_dists in enumerate(probs):
            for index, beam_prob_dist in enumerate(beam_prob_dists):
                beam = make_beam(beam_prob_dist)
                beam_groups[time_step].append(beam)
                # positioning
                position = RIGHT*((time_step-1)*5)
                
                if len(beam_prob_dists) > 1:
                    if not scaled:
                        self.play(self.camera.frame.animate.scale(2))
                        scaled = True

                    if index == 0:
                        position+= UP*4
                    else:
                        position+= DOWN*4

                beam.move_to(position)

            # do arrows
            if time_step > 0:
                if time_step == 1:
                    arrow_1 = Arrow(start=beam_groups[0][0][0], end=beam_groups[1][0][2], color=GOLD)
                    arrow_2 = Arrow(start=beam_groups[0][0][1], end=beam_groups[1][1][2], color=GOLD)
                    arrow1_group = Group(arrow_1, arrow_2)
                    self.play(FadeIn(arrow1_group))
                else:
                    i0 = probs[time_step-1][0].index(max(probs[time_step-1][0]))
                    i1 = probs[time_step-1][1].index(max(probs[time_step-1][1]))
                    arrow_1 = Arrow(start=beam_groups[time_step-1][0][i0], end=beam_groups[time_step][0][2], color=GOLD)
                    arrow_2 = Arrow(start=beam_groups[time_step-1][1][i1], end=beam_groups[time_step][1][2], color=GOLD)
                    arrow1_group = Group(arrow_1, arrow_2)
                    self.play(FadeIn(arrow1_group))
            
            self.play(FadeIn(Group(*beam_groups[time_step])))
        
        # self.play(FadeIn(arrow1_group))
        # self.camera.frame.save_state()
        # # construct beam1
        # beam1 = make_beam(first_scores)
        # beam1.move_to(LEFT*5)
        # self.play(FadeIn(beam1))
        # self.wait(0.3)

        # self.play(self.camera.frame.animate.scale(2))

        # beam2a = make_beam(second_scores[0])
        # beam2a.move_to(UP*4)
        # beam2b = make_beam(second_scores[1])
        # beam2b.move_to(DOWN*4)

        # beam2_group = Group(beam2a, beam2b)


        # arrow_1 = Arrow(start=beam1[0], end=beam2a[2], color=GOLD)
        # arrow_2 = Arrow(start=beam1[1], end=beam2b[2], color=GOLD)
        # arrow1_group = Group(arrow_1, arrow_2)
        
        # self.play(FadeIn(arrow1_group))

        # self.play(FadeIn(beam2_group))

        # beam3a = make_beam(second_scores[0])
        # beam3a.move_to(UP*4 + RIGHT*5)
        # beam3b = make_beam(second_scores[1])
        # beam3b.move_to(DOWN*4 + RIGHT*5)

        # beam3_group = Group(beam3a, beam3b)
        
        
        # self.play(self.camera.scale(0.5))
        # self.play(Create(circle), Create(square))  # show the shapes on screen


