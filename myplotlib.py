
marker_index = 0
marker_list = [ "o", "x", "s", "+", "v", "h", "^", "d" ]
color_index = 0

# my gnuplot color
color_list = [ "#009e73",
               "#56b4e9",
               "#707070",
               "#e54e40",
               "#0072b2",
               "#e69f00", 
               "#000000",
               "#1a1a1a" ,
]

# tab10
color_list = [ "#3c76af",
               "#ee8536",
               "#539d3e",
               "#c43a32",
               "#8d6ab8",
               "#84584e",
               "#d47ebf",
               "#7f7f7f",
               "#bcbc45",
               "#5abbcc",
]

line_index = 0
line_list = [
    "-", "--", "-.", ":"
]

def get_marker():
    global marker_index
    global maker_list
    m = marker_list[marker_index]
    marker_index = (marker_index + 1) % len(marker_list)
    return m

def get_color():
    global color_index
    global color_list
    c = color_list[color_index]
    color_index = (color_index + 1) % len(color_list)
    return c

def get_linestyle():
    global line_index
    global line_list
    l = line_list[line_index]
    line_index = (line_index + 1) % len(line_list)
    return l

def change_aspect_ratio(p, ratio):
    aspect = ((1/ratio) *
              (p.get_xlim()[1] - p.get_xlim()[0]) /
              (p.get_ylim()[1] - p.get_ylim()[0]))
    p.set_aspect(aspect)
    return
