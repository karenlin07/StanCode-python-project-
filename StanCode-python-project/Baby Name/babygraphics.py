"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    gap = (width - 2 * GRAPH_MARGIN_SIZE) / len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE + year_index * gap # calculate the x-coordinate for the specific year
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    # create horizontal lines
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH, fill='black') # bottom line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH, fill='black') # upper line

    years_count = len(YEARS)
    gap = (CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE) // years_count
    # iterate through the years and create vertical lines and their respective year labels
    for i, year in enumerate(YEARS):
        x = GRAPH_MARGIN_SIZE + i * gap
        # create a vertical line for each year
        canvas.create_line(x, GRAPH_MARGIN_SIZE, x, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill='black')
        # create year labels on the bottom
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=str(year), anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # ----- Write your code below this line ----- #
    width = canvas.winfo_reqwidth()  # get canvas width

    # find maximum rank among lookup names
    max_rank = MAX_RANK
    for name in lookup_names:
        # iterate through the years and ranks in the name data
        for year, rank in name_data.get(name, {}).items():
            if rank.isdigit():
                max_rank = max(max_rank, int(rank))

    # check names' historical trend
    for name in lookup_names:
        if name in name_data:
            data = name_data[name]
            color = COLORS[lookup_names.index(name) % len(COLORS)]  #  determine the color for the current name
            #store previous x and y coordinates
            prev_x = None
            prev_y = None
            # Iterate through sorted years
            for year in sorted(YEARS):
                # Get the rank for the current year. if the key does not exist, it returns "*"
                rank = data.get(str(year), '*')
                x = get_x_coordinate(width, YEARS.index(year))

                if rank.isdigit() and int(rank) <= max_rank:
                    rank = int(rank)
                    y = GRAPH_MARGIN_SIZE + (rank / max_rank) * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE)
                    canvas.create_text(x + TEXT_DX, y - 10, text=f"{name} {rank}", anchor=tkinter.SW, fill=color)
                    # connect with the previous point using a line
                    if prev_x is not None and prev_y is not None and prev_y <= max_rank:
                        canvas.create_line(prev_x, prev_y, x, y, fill=color, width=LINE_WIDTH)
                else:
                    y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    # create text on the canvas
                    canvas.create_text(x + TEXT_DX, y + 10, text=f"{name} *", anchor=tkinter.N, fill=color)

                    # connect with previous point using a line
                    if prev_x is not None and prev_y is not None and prev_y <= max_rank:
                        canvas.create_line(prev_x, prev_y, x, y, fill=color, width=LINE_WIDTH)

                prev_x, prev_y = x, y

# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
