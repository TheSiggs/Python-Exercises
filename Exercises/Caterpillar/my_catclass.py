import pygame
import random

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
purple = (255, 0, 255)


class caterpillar:
    def __init__(self):
        x = random.randrange(0, 1000)
        self.status = "healthy"
        self.face_xcoord = x
        self.face_ycoord = 250
        self.body = segment_queue()
        self.food = food_list()
        t = random.randrange(0, 2)
        if t == 0:
            self.travel_direction = 'left'
        else:
            self.travel_direction = 'right'

    def draw_caterpillar(self, screen):
        self.draw_face(screen)
        self.draw_body(screen)
        self.draw_food(screen)

    def draw_face(self, screen):
        x = self.face_xcoord
        y = self.face_ycoord
        pygame.draw.ellipse(screen, red, [x, y, 40, 45])
        pygame.draw.ellipse(screen, black, [x + 6, y + 10, 10, 15])
        pygame.draw.ellipse(screen, black, [x + 24, y + 10, 10, 15])
        pygame.draw.line(screen, black, (x + 11, y), (x + 9, y - 10), 3)
        pygame.draw.line(screen, black, (x + 24, y), (x + 26, y - 10), 3)

    def draw_body(self, screen):
        # traverse the segment queue
        current_node = self.body.head
        while current_node is not None:
            current_node.draw_segment(screen)
            current_node = current_node.next

    def draw_food(self, screen):
        # traverse the segment queue
        current_node = self.food.head
        while current_node is not None:
            current_node.draw_fooditem(screen)
            current_node = current_node.next

    def grow(self):
        if self.travel_direction == 'left' and self.body.length == 0:
            self.body.addSegment(self.face_xcoord + 32, self.face_ycoord)
        elif self.travel_direction == 'left' and self.body.length > 0:
            self.body.addSegment(
                self.face_xcoord + (30 * (self.body.length + 1)), self.face_ycoord)
        if self.travel_direction == 'right' and self.body.length == 0:
            self.body.addSegment(self.face_xcoord - 32, self.face_ycoord)
        elif self.travel_direction == 'right' and self.body.length > 0:
            self.body.addSegment(
                self.face_xcoord - (30 * (self.body.length + 1)), self.face_ycoord)

    def reverse(self):
        if self.travel_direction == 'left':
            self.travel_direction = 'right'
        elif self.travel_direction == 'right':
            self.travel_direction = 'left'

        current_node = self.body.head
        count = 1
        while current_node is not None:
            if self.travel_direction == 'left':
                if count == 1:
                    current_node.xcoord += 65 * count
                else:
                    current_node.xcoord += 60 * count
            elif self.travel_direction == 'right':
                if count == 1:
                    current_node.xcoord -= 65 * count
                else:
                    current_node.xcoord -= 60 * count
            count += 1
            current_node = current_node.next
        return self.travel_direction

    def move_forward(self, screen):
        if self.travel_direction == 'left':
            direction = -1
        if self.travel_direction == 'right':
            direction = 1
        
        self.face_xcoord += 2 * direction
        if self.face_xcoord < 10 or self.face_xcoord > 950:
            caterpillar.reverse(self)

        current_node = self.body.head
        while current_node is not None:
            current_node.xcoord += 2 * direction
            current_node = current_node.next

    def drop_food(self):
        if random.randrange(0, 2) == 0:
            kind = 'nice'
        else:
            kind = 'nasty'

        cat_food = food_item(random.randrange(0, 980), self.face_ycoord, kind)
        cat_food.next = self.food.head
        self.food.head = cat_food
        self.food.length += 1

    def shrink_back(self):
        if self.body.length != 0:
            if self.travel_direction == 'left':
                self.face_xcoord += 30
            if self.travel_direction == 'right':
                self.face_xcoord -= 30

            body_part = self.body.head
            self.body.head = self.body.head.next
            self.body.length = self.body.length - 1
            return body_part



class segment_queue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def isEmpty(self):
        return self.length == 0

    def addSegment(self, x, y):
        node = body_segment(x, y)
        node.next = None
        if self.length == 0:
            self.head = self.last = node
        else:
            last = self.last
            last.next = node
            self.last = node
        self.length += 1


class body_segment:
    def __init__(self, x, y):
        self.xcoord = x
        self.ycoord = y
        self.next = None

    def draw_segment(self, screen):
        x = self.xcoord
        y = self.ycoord
        pygame.draw.ellipse(screen, green, [x, y, 35, 40])
        pygame.draw.line(screen, black, (x + 8, y + 35), (x + 8, y + 45), 3)
        pygame.draw.line(screen, black, (x + 24, y + 35), (x + 24, y + 45), 3)


class food_list:
    def __init__(self):
        self.length = 0
        self.head = None


class food_item:
    def __init__(self, x, y, kind):
        self.xcoord = x
        self.ycoord = y
        self.foodtype = kind
        self.next = None

    def draw_fooditem(self, screen):
        x = self.xcoord
        y = self.ycoord
        if self.foodtype == 'nice':
            pygame.draw.ellipse(screen, yellow, [x, y, 15, 15])
        else:
            pygame.draw.ellipse(screen, purple, [x, y, 15, 15])
