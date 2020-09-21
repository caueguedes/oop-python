from .grader import Grader
from .lessons import IntroToPython, Statistics

grader = Grader()
itp_id = grader.register(IntroToPython)
