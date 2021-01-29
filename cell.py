class Cell:

    def __init__(self, row, column, cell_type):
        self.row = row
        self.column = column
        self.cell_type = cell_type

    def draw(self, canvas, resource, image_size):
        canvas.create_image(self.row * image_size + (image_size / 2) + 2,
                            self.column * image_size + (image_size / 2) + 2, image=resource.get_image(self.cell_type))





