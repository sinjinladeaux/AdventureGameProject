import pygame
import sys

class GameGraphics:
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        
        # Constants
        self.GRID_SIZE = 32  # Size of each grid square in pixels
        self.GRID_WIDTH = 10  # Number of squares in grid width
        self.GRID_HEIGHT = 10  # Number of squares in grid height
        self.SCREEN_WIDTH = self.GRID_WIDTH * self.GRID_SIZE
        self.SCREEN_HEIGHT = self.GRID_HEIGHT * self.GRID_SIZE
        
        # Colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        
        # Set up the display
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Adventure Game")
        
        # Player position (in grid coordinates)
        self.player_x = 0
        self.player_y = 0
        
        # Player rectangle for drawing
        self.player_rect = pygame.Rect(
            self.player_x * self.GRID_SIZE,
            self.player_y * self.GRID_SIZE,
            self.GRID_SIZE,
            self.GRID_SIZE
        )
        
        # Clock for controlling frame rate
        self.clock = pygame.time.Clock()
    
    def handle_input(self):
        """Handle keyboard input for player movement"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return False
                elif event.key == pygame.K_UP and self.player_y > 0:
                    self.player_y -= 1
                elif event.key == pygame.K_DOWN and self.player_y < self.GRID_HEIGHT - 1:
                    self.player_y += 1
                elif event.key == pygame.K_LEFT and self.player_x > 0:
                    self.player_x -= 1
                elif event.key == pygame.K_RIGHT and self.player_x < self.GRID_WIDTH - 1:
                    self.player_x += 1
                
                # Update player rectangle position
                self.player_rect.x = self.player_x * self.GRID_SIZE
                self.player_rect.y = self.player_y * self.GRID_SIZE
        
        return True
    
    def draw(self):
        """Draw the game state"""
        # Clear screen
        self.screen.fill(self.BLACK)
        
        # Draw grid
        for x in range(self.GRID_WIDTH):
            for y in range(self.GRID_HEIGHT):
                pygame.draw.rect(
                    self.screen,
                    self.WHITE,
                    pygame.Rect(
                        x * self.GRID_SIZE,
                        y * self.GRID_SIZE,
                        self.GRID_SIZE,
                        self.GRID_SIZE
                    ),
                    1  # Width of grid lines
                )
        
        # Draw player
        pygame.draw.rect(self.screen, self.RED, self.player_rect)
        
        # Update display
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        running = True
        while running:
            running = self.handle_input()
            self.draw()
            self.clock.tick(60)  # Limit to 60 FPS
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = GameGraphics()
    game.run()
