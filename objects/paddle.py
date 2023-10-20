from pygame import Surface

class Paddle(Surface):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
