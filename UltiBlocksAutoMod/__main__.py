# Import the main code to run
from .runbots import main

# Make sure we're running as the main module (although this might always return true, I'm not sure)
if __name__=="__main__":
    # Run the main script, including any arguments
    import sys
    main(sys.argv)