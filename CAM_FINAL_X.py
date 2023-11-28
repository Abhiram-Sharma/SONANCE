import pygame
import pygame.camera

def capture_photo(num):
    # Initialize Pygame
    pygame.init()
    pygame.camera.init()

    # Get a list of available cameras
    cameras = pygame.camera.list_cameras()
    camera = pygame.camera.Camera(cameras[0])
    camera.start()   
    image = camera.get_image()

    pygame.image.save(image,f"CamPic{num}.jpg")

    camera.stop()
    pygame.quit()

    return "Photo has been captured"
