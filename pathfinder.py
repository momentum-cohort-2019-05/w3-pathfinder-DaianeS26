from PIL import Image

def get_strings_to_ints(text):
    """Given a string with integers in it, return a list of those integers."""
    list_of_nums = []
    nums_as_strs = split_line(text)

    for num_as_str in nums_as_strs:
        list_of_nums.append(int(num_as_str))
    return list_of_nums

def split_line(line):
    return line.split()

def read_file(filename):
   
    with open(filename) as file:
        return file.readlines()

def get_list_from_file(filename):
  
    lines = read_file(filename)

    list_of_lists = []
    for line in lines:
        list_of_lists.append(get_strings_to_ints(line))
    return list_of_lists


class ElevationMap:
    """
    ElevationMap is a class that takes a matrix (list of lists, 2D)
    of integers and can be used to generate an image of those elevations
    like a standard elevation map.
    """

    def __init__(self, elevations):
        self.elevations = elevations

    def elevation_at_coordinate(self, x, y):
        return self.elevations[y][x]

    def min_elevation(self):
        return min([min(row) for row in self.elevations])

    def max_elevation(self):
        return max([max(row) for row in self.elevations])

    def intensity_at_coordinate(self, x, y, min_elevation, max_elevation):
        """Given an x, y coordinate, return the
        intensity level (used for grayscale in image) of
        the elevation at that coordinate.
        """
        elevation = self.elevation_at_coordinate(x, y)
       
        return (elevation - min_elevation) / (max_elevation - min_elevation) * 255

    def drawing_map(self, filename, width, height):
        image = Image.new('RGBA', (width, height))
        min_elevation = self.min_elevation()
        max_elevation = self.max_elevation()
        for x in range(width):
            for y in range(height):
                intensity = int(self.intensity_at_coordinate(x, y, min_elevation, max_elevation)) 
                image.putpixel((x, y), (intensity, intensity, intensity))
        image.save(filename)

if __name__ == "__main__":
   
    elevations = get_list_from_file('elevation_small.txt')
 
    e_map = ElevationMap(elevations)

    e_map.drawing_map('grey_map.png', 600, 600)