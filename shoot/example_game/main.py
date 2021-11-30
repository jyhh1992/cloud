""" Example Game

"""
# Sys for clean exiting
import sys

# PyGame and locals
import pygame
from pygame.locals import *

# PyGame AI
import pygame_ai as pai

# Different NPCs and Player
from entities.player import *
from entities.npcs import *

# Ignore this stuff
from area import Area
import camera
from colors import *
import globs
from utils import list_utils
from wall import Wall


def update_keys(keys_pressed):
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(2)
            
        if event.type == KEYDOWN:
            keys_pressed.append(event.key)
                
        if event.type == KEYUP:
            list_utils.remove_if_exists(keys_pressed, event.key)

def blit_text_relative_rect(text_lines, surface, rect, relx, rely, color = colors.BLACK, size = 15):
    font = pygame.font.Font('fonts/AldotheApache.ttf', size)
    rendered_lines = [font.render(line, True, color) for line in text_lines]
    text_height = sum(rendered_line.get_size()[1] for rendered_line in rendered_lines)
    y = (rect.height - text_height)*rely
    for rline in rendered_lines:
        lwidth, lheight = rline.get_size()
        x = rect.left + (rect.width - lwidth)*relx
        surface.blit(rline, (x, y))
        y += lheight

def blit_text_centered_rect(text_lines, surface, rect, color = colors.BLACK, size = 15):
    blit_text_relative_rect(text_lines, surface, rect, 0.5, 0.5, color, size)
    
def change_player_gravity():
    globs.solid_entities.remove(globs.normal_player)
    globs.gravity_player.position = globs.normal_player.position
    globs.solid_entities.add(globs.gravity_player)
    globs.player = globs.gravity_player
    
def change_player_normal():
    globs.solid_entities.remove(globs.gravity_player)
    globs.normal_player.position = globs.gravity_player.position
    globs.solid_entities.add(globs.normal_player)
    globs.player = globs.normal_player

def main():
    # Regular PyGame setup
    screen = pygame.display.set_mode((400, 400))
    globs.screen = screen
    screen_width, screen_height = screen.get_size()
    globs.screen_width, globs.screen_height = screen_width, screen_height
    clock = pygame.time.Clock()
    
    # Initialize sprite groups
    globs.solid_entities = pygame.sprite.Group()
    globs.static_entities = pygame.sprite.Group()
    globs.dinamic_entities = pygame.sprite.Group()
    globs.active_dinamic_entities = pygame.sprite.Group()
    
    # Initialize constants
    globs.gravity = pai.steering.kinematic.SteeringOutput()
    globs.gravity.linear[1] = 30
    globs.drag = pai.steering.kinematic.Drag()
    globs.area_width = 400
    tilesize = 20
    globs.tilesize = tilesize
    n_areas = 17
    stage_width = 2*tilesize + n_areas*globs.area_width + n_areas*tilesize
    stage_height = screen_height
    draw_indicators = False
    
    # Create walls for the stage
    walls = [
        Wall((0, 0), (tilesize, stage_height)),
        Wall((0, 0), (stage_width, tilesize)),
        Wall((stage_width - tilesize, 0), (tilesize, stage_height)),
        Wall((0, stage_height - tilesize), (stage_width, tilesize)),
    ]
    
    # Create a surface for the background
    background = pygame.Surface((stage_width, stage_height)).convert()
    globs.background = background
    background.fill(WHITE)
        
    # Create scrolling camera object
    cam_function = lambda cam, rect: camera.complex_camera(screen_width, screen_height, cam, rect)
    cam = camera.Camera(cam_function, stage_width, stage_height)
    globs.cam = cam
    
    # Player
    globs.normal_player = Player(pos = (0, 0))
    globs.gravity_player = PlayerGravity(pos = (0, 0))
    globs.player = globs.normal_player
    globs.solid_entities.add(globs.player)
    
    # Areas
    areas = []
    npcs = []
    not_solid_npcs = []
    
    # Area 0
    area0 = Area(tilesize, colors.WHITE)
    text = [
        'You can move with WASD',
        '',
        '',
        '',
        'Advance to the right',
        '',
        '',
        '',
        'Press X to exit',
        
    ]
    blit_text_centered_rect(text, background, area0.rect)
    # Player
    globs.player.rect.center = area0.rect.center
    
    # Area 0.1
    area01 = Area(area0.rect.right + tilesize, colors.WHITE)
    text = [
        'If you keep moving you will encounter the first area',
        'When you enter an area, the NPCs there will activate',
        'They will deactivate when you leave it',
        'Every area will show you an aspect of the library',
        '',
        'If you ever get stuck, you can press the directional keys',
        'to teleport to the previos/next area',
    ]
    blit_text_centered_rect(text, background, area01.rect)
    
    # Area 1
    area1 = Area(area01.rect.right + tilesize, colors.RED)
    text = [
        'Kinematic Seek',
        'Seeks the player',
        '',
        'You can press Q any time to show/hide steering indicators',
    ]
    blit_text_relative_rect(text, background, area1.rect, 0.5, 0.15)
    circle = Circle(pos = area1.rect.center, color = colors.RED)
    circle.ai = pai.steering.kinematic.Seek(circle, globs.player)
    area1.entities.append(circle)
    npcs.append(circle)
    areas.append(area1)
    
    # Area 2
    area2 = Area(area1.rect.right + tilesize, colors.GREEN)
    text = [
        'Kinematic Arrive',
        'They arrive near the player and stand still',
    ]
    blit_text_relative_rect(text, background, area2.rect, 0.5, 0.15)
    smaller_rect = area2.rect.inflate(-30, -30)
    circle1 = Circle(pos = smaller_rect.topleft, color = colors.GREEN)
    circle2 = Circle(pos = smaller_rect.topright, color = colors.GREEN)
    circle3 = Circle(pos = smaller_rect.bottomleft, color = colors.GREEN)
    circle4 = Circle(pos = smaller_rect.bottomright, color = colors.GREEN)
    circle1.ai = pai.steering.kinematic.Arrive(circle1, globs.player)
    circle2.ai = pai.steering.kinematic.Arrive(circle2, globs.player)
    circle3.ai = pai.steering.kinematic.Arrive(circle3, globs.player)
    circle4.ai = pai.steering.kinematic.Arrive(circle4, globs.player)
    area2.entities += [circle1, circle2, circle3, circle4]
    npcs += [circle1, circle2, circle3, circle4]
    areas.append(area2)
    
    # Area 3
    area3 = Area(area2.rect.right + tilesize, colors.PURPLE)
    text = [
        'Kinematic Face',
        'Will face the player'
    ]
    blit_text_relative_rect(text, background, area3.rect, 0.5, 0.15)
    triangle = Triangle(pos = area3.rect.center, color = colors.PURPLE)
    triangle.ai = pai.steering.kinematic.Face(triangle, globs.player)
    area3.entities.append(triangle)
    npcs.append(triangle)
    areas.append(area3)
    
    # Area 4
    area4 = Area(area3.rect.right + tilesize, colors.YELLOW)
    text = [
        'Kinematic Path Following',
        'Will follow specified path',
    ]
    blit_text_relative_rect(text, background, area4.rect, 0.5, 0.15)
    circle = Circle(pos = area4.rect.center, color = colors.YELLOW)
    path = pai.steering.path.PathCircumference(area4.rect.center, 100)
    circle.ai = pai.steering.kinematic.FollowPath(circle, path)
    area4.entities.append(circle)
    npcs.append(circle)
    areas.append(area4)
    
    # Area 5
    area5 = Area(area4.rect.right + tilesize, colors.ORANGE)
    text = [
        'Kinematic Path Following',
        'Paths can update dinamically',
        'You can easily make a path be centered on the any',
        'dinamically updated position',
    ]
    blit_text_relative_rect(text, background, area5.rect, 0.5, 0.15)
    smaller_rect = area5.rect.inflate(-50, -50)
    circle1 = Circle(pos = smaller_rect.topleft, color = colors.ORANGE)
    circle2 = Circle(pos = smaller_rect.topright, color = colors.ORANGE)
    circle3 = Circle(pos = smaller_rect.bottomleft, color = colors.ORANGE)
    circle4 = Circle(pos = smaller_rect.bottomright, color = colors.ORANGE)
    path1 = pai.steering.path.PathCircumference(lambda: globs.player.position, 50, 270)
    path2 = pai.steering.path.PathCircumference(lambda: globs.player.position, 50, 0)
    path3 = pai.steering.path.PathCircumference(lambda: globs.player.position, 50, 180)
    path4 = pai.steering.path.PathCircumference(lambda: globs.player.position, 50, 90)
    circle1.ai = pai.steering.kinematic.FollowPath(circle1, path1)
    circle2.ai = pai.steering.kinematic.FollowPath(circle2, path2)
    circle3.ai = pai.steering.kinematic.FollowPath(circle3, path3)
    circle4.ai = pai.steering.kinematic.FollowPath(circle4, path4)
    area5.entities += [circle1, circle2, circle3, circle4]
    npcs += [circle1, circle2, circle3, circle4]
    areas.append(area5)
    
    # Area 6
    area6 = Area(area5.rect.right + tilesize, colors.CYAN)
    text = [
        'You can also use this library to create',
        'Interesting effects like this',
    ]
    blit_text_relative_rect(text, background, area6.rect, 0.5, 0.15)
    smaller_rect = area6.rect.inflate(-50, -50)
    circle1 = NotSolidCircle(pos = smaller_rect.topleft, color = colors.CYAN)
    circle2 = NotSolidCircle(pos = smaller_rect.topright, color = colors.CYAN)
    circle3 = NotSolidCircle(pos = smaller_rect.bottomleft, color = colors.CYAN)
    circle4 = NotSolidCircle(pos = smaller_rect.bottomright, color = colors.CYAN)
    circle5 = NotSolidCircle(pos = smaller_rect.midleft, color = colors.CYAN)
    circle6 = NotSolidCircle(pos = smaller_rect.midright, color = colors.CYAN)
    circle7 = NotSolidCircle(pos = smaller_rect.midtop, color = colors.CYAN)
    circle8 = NotSolidCircle(pos = smaller_rect.midbottom, color = colors.CYAN)
    circle1.ai = pai.steering.kinematic.Seek(circle1, globs.player)
    circle2.ai = pai.steering.kinematic.Seek(circle2, globs.player)
    circle3.ai = pai.steering.kinematic.Seek(circle3, globs.player)
    circle4.ai = pai.steering.kinematic.Seek(circle4, globs.player)
    circle5.ai = pai.steering.kinematic.Seek(circle5, globs.player)
    circle6.ai = pai.steering.kinematic.Seek(circle6, globs.player)
    circle7.ai = pai.steering.kinematic.Seek(circle7, globs.player)
    circle8.ai = pai.steering.kinematic.Seek(circle8, globs.player)
    area6.entities += [circle1, circle2, circle3, circle4, circle5, circle6, circle7, circle8]
    not_solid_npcs += [circle1, circle2, circle3, circle4, circle5, circle6, circle7, circle8]
    areas.append(area6)
    
    # Area 7
    area7 = Area(area6.rect.right + tilesize, colors.WHITE)
    text = [
        'The strength of the libreary\'s movement algorithms comes',
        'with the blended kinematic beahviors, you can blend several',
        'behaviors to create a customized behavior',
        '',
        'This gives you the freedoom to customize how entities move',
        'In your world and opens up for very interesting movement behaviors',
    ]
    blit_text_relative_rect(text, background, area7.rect, 0.5, 0.15)
    #areas.append(area7)
    
    
    # Area 8
    area8 = Area(area7.rect.right + tilesize, colors.GREY)
    text = [
        'Flocking'
    ]
    blit_text_relative_rect(text, background, area8.rect, 0.5, 0.15)
    smaller_rect = area8.rect.inflate(-30, -30)
    x, y = smaller_rect.midright
    triangle1 = Triangle(base = 10, height = 10, pos = (x, y - 30), color = colors.GREY)
    triangle2 = Triangle(base = 10, height = 10, pos = (x, y - 20), color = colors.GREY)
    triangle3 = Triangle(base = 10, height = 10, pos = (x, y - 10), color = colors.GREY)
    triangle4 = Triangle(base = 10, height = 10, pos = (x, y +  0), color = colors.GREY)
    triangle5 = Triangle(base = 10, height = 10, pos = (x, y + 10), color = colors.GREY)
    triangle6 = Triangle(base = 10, height = 10, pos = (x, y + 20), color = colors.GREY)
    triangle7 = Triangle(base = 10, height = 10, pos = (x, y + 30), color = colors.GREY)
    flock = [triangle1, triangle2, triangle3, triangle4, triangle5, triangle6, triangle7]
    triangle1.ai = pai.steering.blended.Flocking(triangle1, pai.utils.list_utils.remove_if_exists_copy(flock, triangle1), globs.player)
    triangle2.ai = pai.steering.blended.Flocking(triangle2, pai.utils.list_utils.remove_if_exists_copy(flock, triangle2), globs.player)
    triangle3.ai = pai.steering.blended.Flocking(triangle3, pai.utils.list_utils.remove_if_exists_copy(flock, triangle3), globs.player)
    triangle4.ai = pai.steering.blended.Flocking(triangle4, pai.utils.list_utils.remove_if_exists_copy(flock, triangle4), globs.player)
    triangle5.ai = pai.steering.blended.Flocking(triangle5, pai.utils.list_utils.remove_if_exists_copy(flock, triangle5), globs.player)
    triangle6.ai = pai.steering.blended.Flocking(triangle6, pai.utils.list_utils.remove_if_exists_copy(flock, triangle6), globs.player)
    triangle7.ai = pai.steering.blended.Flocking(triangle7, pai.utils.list_utils.remove_if_exists_copy(flock, triangle7), globs.player)
    area8.entities += flock
    npcs += flock
    areas.append(area8)
    
    # Area 9
    area9 = Area(area8.rect.right + tilesize, colors.DARK_RED)
    text = [
        'Arrive',
        'With collision avoidance',
        'Well, collision avoidance might still need to improve',
    ]
    blit_text_relative_rect(text, background, area9.rect, 0.5, 0.15)
    x, y = area9.rect.center
    x, y = x - tilesize*2, y - tilesize*2
    walls.append(Wall( (x, y), (tilesize*4, tilesize*4) ))
    circle = Circle(radius = 7, pos = area9.rect.midright, color = colors.DARK_RED)
    circle.ai = pai.steering.blended.Arrive(circle, globs.player, walls)
    area9.entities.append(circle)
    npcs.append(circle)
    areas.append(area9)
    
    # Area 10
    area10 = Area(area9.rect.right + tilesize, colors.DARK_GREEN)
    text = [
        'Wander',
        'With collision avoidance',
        'Again, collision avoidance might need some more work',
    ]
    blit_text_relative_rect(text, background, area10.rect, 0.5, 0.15)
    y = area10.rect.top
    walls.append(Wall( (area10.rect.left, y), (tilesize, area10.rect.height/2 - tilesize/2) ))
    walls.append(Wall( (area10.rect.right-tilesize, y), (tilesize, area10.rect.height/2 - tilesize/2) ))
    _, y = area10.rect.center
    y += tilesize/2
    walls.append(Wall( (area10.rect.left, y), (tilesize, area10.rect.height/2 - tilesize/2) ))
    walls.append(Wall( (area10.rect.right-tilesize, y), (tilesize, area10.rect.height/2 - tilesize/2) ))
    ss_rect = area10.rect.inflate(-tilesize-30, -tilesize-30)
    
    circle1 = Circle(radius = 6, pos = ss_rect.topleft, color = colors.DARK_GREEN)
    circle2 = Circle(radius = 6, pos = ss_rect.topright, color = colors.DARK_GREEN)
    circle3 = Circle(radius = 6, pos = ss_rect.bottomleft, color = colors.DARK_GREEN)
    circle4 = Circle(radius = 6, pos = ss_rect.bottomright, color = colors.DARK_GREEN)
    circle1.ai = pai.steering.blended.Wander(circle1, walls)
    circle2.ai = pai.steering.blended.Wander(circle2, walls)
    circle3.ai = pai.steering.blended.Wander(circle3, walls)
    circle4.ai = pai.steering.blended.Wander(circle4, walls)
    area10.entities += [circle1, circle2, circle3, circle4]
    npcs += [circle1, circle2, circle3, circle4]
    areas.append(area10)
    
    # Area 11
    area11 = Area(area10.rect.right + tilesize, colors.PINK)
    text = [
        'Combining Path Following with other behaviors',
        'can lead to some pretty interesting results',
    ]
    blit_text_relative_rect(text, background, area11.rect, 0.5, 0.15)
    smaller_rect = area11.rect.inflate(-50, -50)
    triangle1 = Triangle(base = 10, height = 10, pos = smaller_rect.midtop   , color = colors.PINK, max_rotation = 60, max_angular_accel = 20)
    triangle2 = Triangle(base = 10, height = 10, pos = smaller_rect.midbottom, color = colors.PINK, max_rotation = 60, max_angular_accel = 20)
    triangle3 = Triangle(base = 10, height = 10, pos = smaller_rect.midright , color = colors.PINK, max_rotation = 60, max_angular_accel = 20)
    triangle1.ai = pai.steering.blended.Surround(triangle1, globs.player, 80)
    triangle2.ai = pai.steering.blended.Surround(triangle2, globs.player, 80)
    triangle3.ai = pai.steering.blended.Surround(triangle3, globs.player, 120)
    area11.entities += [triangle1, triangle2, triangle3]
    npcs += [triangle1, triangle2, triangle3]
    areas.append(area11)
    
    # Area 12
    area12 = Area(area11.rect.right + tilesize, colors.WHITE)
    text = [
        'You will now enter the world of gravity',
        'You\'ll se how this library can also be',
        'integrated with external forces and mechanism',
        'such as jumping'
    ]
    blit_text_relative_rect(text, background, area12.rect, 0.5, 0.15)
    
    # Area 13
    area13 = Area(area12.rect.right + tilesize, colors.LIGHT_GREEN)
    text = [
        'In this world an external force is being applied',
        'To emulate gravity, this is not done by the library',
        'but it does use the lirary\'s functions',
        'in other words, you can emulate any kind of',
        'force or acceleration external to entities',
    ]
    blit_text_relative_rect(text, background, area13.rect, 0.5, 0.15)
    x, y = area13.rect.midbottom
    y -= tilesize
    walls.append(Wall( (x, y), (tilesize, tilesize)))
    x += tilesize
    y -= tilesize
    walls.append(Wall( (x, y), (tilesize, tilesize*2)))
    x += tilesize
    y -= tilesize
    walls.append(Wall( (x, y), (tilesize, tilesize*3)))
    x += tilesize
    y -= tilesize
    walls.append(Wall( (x, y), (tilesize, tilesize*4)))
    x += tilesize
    y -= tilesize*3
    walls.append(Wall( (x, y), (tilesize, tilesize*7)))
    x += tilesize
    y += tilesize*3
    walls.append(Wall( (x, y), (tilesize, tilesize*4)))
    x += tilesize
    y += tilesize*2
    walls.append(Wall( (x, y), (tilesize, tilesize*2)))
    x += tilesize
    y += tilesize
    walls.append(Wall( (x, y), (tilesize, tilesize)))
    x, y = area13.rect.center
    x -= tilesize*8
    y -= tilesize
    walls.append(Wall( (x, y), (tilesize*10, tilesize)))
    x, y = area13.rect.midbottom
    rect1 = Rectangle(pos = (x, y - 30), color = colors.LIGHT_GREEN)
    rect1.ai = pai.steering.kinematic.Seek(rect1, globs.gravity_player)
    area13.entry_actions.append(change_player_gravity)
    area13.exit_actions.append(change_player_normal)
    area13.entities.append(rect1)
    npcs.append(rect1)
    areas.append(area13)
    
    # Area 14
    area14 = Area(area13.rect.right + tilesize, colors.MAGENTA)
    text = [
        'Finally, you can combine entities with and without gravity',
        'Or with an upward external force equal to gravity',
        'However you wish to see it',
    ]
    blit_text_relative_rect(text, background, area14.rect, 0.5, 0.15)
    smaller_rect = area14.rect.inflate(-50, -50)
    player_away_radius = globs.player.rect.width *3
    rect1 = Rectangle(pos = smaller_rect.midright, color = colors.PINK)
    rect1.ai = pai.steering.kinematic.Arrive(rect1, globs.gravity_player, target_radius = player_away_radius)
    triangle1 = Triangle(pos = smaller_rect.center, color = colors.ORANGE)
    triangle1.ai = pai.steering.blended.Arrive(triangle1, globs.gravity_player, walls, target_radius = player_away_radius)
    circle1 = Circle(pos = smaller_rect.topleft, color = colors.PURPLE)
    circle2 = Circle(pos = smaller_rect.midtop, color = colors.PURPLE)
    circle3 = Circle(pos = smaller_rect.topright, color = colors.PURPLE)
    circle1.ai = pai.steering.priority.OscilateHorizontally(circle1, globs.gravity_player, [circle2, circle3])
    circle2.ai = pai.steering.priority.OscilateHorizontally(circle2, globs.gravity_player, [circle1, circle3], start_x = 1)
    circle3.ai = pai.steering.priority.OscilateHorizontally(circle3, globs.gravity_player, [circle1, circle2], start_x = 2)
    area14.entities += [rect1, triangle1, circle1, circle2, circle3]
    npcs += [rect1, triangle1, circle1, circle2, circle3]
    area14.entry_actions.append(change_player_gravity)
    area14.exit_actions.append(change_player_normal)
    areas.append(area14)
    
    area15 = Area(area14.rect.right + tilesize, colors.WHITE)
    text = [
        'And that was it',
    ]
    blit_text_centered_rect(text, background, area15.rect)
    
    globs.dinamic_entities.add(npcs)
    globs.dinamic_entities.add(not_solid_npcs)
    globs.solid_entities.add(npcs)
    
    # Blit walls and add them to their corresponding group
    for wall in walls:
        background.blit(wall.image, wall.rect)
    globs.static_entities.add(walls)
    globs.solid_entities.add(walls)
    
    # Other variables
    keys_pressed = []
    player_steering = pai.steering.kinematic.SteeringOutput()
    current_area = -1
    last_area = -1
    loop_area = -1
    last_loop_area = -1
        
    while True:
        # Get loop time
        tick = clock.tick(60)/100
        
        # Get input
        update_keys(keys_pressed)
        
        # Reset player steering
        player_steering.reset()
        
        # Process input
        for key in keys_pressed:
            if key == K_w:
                player_steering.linear[1] += -globs.player.max_accel
            if key == K_a:
                player_steering.linear[0] += -globs.player.max_accel
            if key == K_s:
                player_steering.linear[1] +=  globs.player.max_accel
            if key == K_d:
                player_steering.linear[0] +=  globs.player.max_accel
            if key == K_SPACE:
                globs.player.jump()
            if key == K_q:
                draw_indicators = not draw_indicators
                pai.utils.list_utils.remove_if_exists(keys_pressed, K_q)
            if key == K_RIGHT and last_area < len(areas)-1:
                x, y = areas[last_area+1].rect.midleft
                globs.player.position = (x + 30, y)
                pai.utils.list_utils.remove_if_exists(keys_pressed, K_RIGHT)
            if key == K_LEFT and last_area > 0:
                x, y = areas[last_area-1].rect.midleft
                globs.player.position = (x + 30, y)
                pai.utils.list_utils.remove_if_exists(keys_pressed, K_LEFT)
            if key == K_x:
                sys.exit(2)
                
        # Handle player steering
        if player_steering.linear.length() > globs.player.max_accel:
            player_steering.linear.normalize_ip()
            player_steering.linear *= globs.player.max_accel
        
        # Blit background to erease previous stuff
        screen.blit(background, cam.apply_norect((0, 0)))
        
        # Update world
        globs.player.update(player_steering, tick)
        for entity in globs.active_dinamic_entities:
            entity.update(tick)
        
        # Check what area the player's in
        colliding = [pygame.Rect.collidepoint(area.rect, globs.player.rect.center) for area in areas]
        last_loop_area = loop_area
        loop_area = pai.utils.list_utils.find_first(colliding, 1)
        
        # Do corresponding actions for area entering/exiting area
        if loop_area != last_loop_area and loop_area >= 0:
            # When entering a new area by teleporting, run exit actions of previous area
            if current_area >= 0 and loop_area != current_area:
                print('exiting area', current_area, 'teleported')
                globs.active_dinamic_entities.remove(areas[current_area].entities)
                for action in areas[current_area].exit_actions:
                    action()
            # Update current area
            current_area = loop_area
            last_area = current_area
            # Run entry actions
            print('entering area', current_area)
            globs.active_dinamic_entities.add(areas[current_area].entities)
            for action in areas[current_area].entry_actions:
                action()
        
        elif loop_area != last_loop_area and loop_area < 0:
            # Run exit actions
            print('exiting area', current_area)
            globs.active_dinamic_entities.remove(areas[current_area].entities)
            for action in areas[current_area].exit_actions:
                action()
            current_area = loop_area
        
        # Draw indicators if flagged
        if draw_indicators:
            for entity in areas[current_area].entities:
                entity.ai.draw_indicators(screen, cam.apply_norect)
            
        # Update camera
        cam.update(globs.player)
        
        # Blit entities
        screen.blit(globs.player.image, cam.apply(globs.player))
        
        for entity in globs.dinamic_entities:
            screen.blit(entity.image, cam.apply(entity))
        
        # Update display
        pygame.display.update()
        
if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
        
