from src.minesweeper.app import Minesweeper

def main():
    game = Minesweeper()
    
    while True:
        game.new()
        game.run()
        
        
if __name__ == "__main__":
    main()