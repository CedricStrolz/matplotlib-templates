import matplotlib.pyplot as plt

class FigureSaver:
    """
    A class to handle saving Matplotlib figures with specific size and multiple formats.
    """

    def __init__(self, filename, width_cm, height_cm, dpi=300):
        """
        Initialize the FigureSaver with given parameters.

        Parameters:
        - filename: Base filename (without extension)
        - width_cm: Width of the figure in centimeters
        - height_cm: Height of the figure in centimeters
        - dpi: Dots per inch for image quality (default: 300)
        """
        self.filename = filename
        self.width_cm = width_cm
        self.height_cm = height_cm
        self.dpi = dpi
        self.formats = ['jpg', 'pdf', 'eps', 'svg']

    def save(self, fig):
        """
        Save the given Matplotlib figure in multiple formats with specified size.

        Parameters:
        - fig: Matplotlib figure object
        """
        # Convert cm to inches (1 cm = 0.393701 inches)
        width_in = self.width_cm * 0.393701
        height_in = self.height_cm * 0.393701

        fig.set_size_inches(width_in, height_in)

        for fmt in self.formats:
            fig.savefig(f"{self.filename}.{fmt}", format=fmt, dpi=self.dpi, bbox_inches='tight')

        print(f"Figure saved as {', '.join([self.filename + '.' + fmt for fmt in self.formats])}")
