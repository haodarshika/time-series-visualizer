import unittest
import time_series_visualizer

class LinePlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = time_series_visualizer.draw_line_plot()
        self.ax = self.fig.axes[0]

    def test_line_plot_title(self):
        actual = self.ax.get_title()
        expected = "Daily freeCodeCamp Forum Page Views 5/2016-12/2019"
        self.assertEqual(actual, expected, "Expected line plot title to be 'Daily freeCodeCamp Forum Page Views 5/2016-12/2019'")

    def test_line_plot_labels(self):
        actual = self.ax.get_xlabel()
        expected = "Date"
        self.assertEqual(actual, expected, "Expected line plot xlabel to be 'Date'")
        actual = self.ax.get_ylabel()
        expected = "Page Views"
        self.assertEqual(actual, expected, "Expected line plot ylabel to be 'Page Views'")

    def test_line_plot_data(self):
        data = [row.get_ydata() for row in self.ax.get_lines()]
        actual = len(data[0])
        expected = 1304
        self.assertEqual(actual, expected, "Expected line plot to have 1304 data points")

class BarPlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = time_series_visualizer.draw_bar_plot()
        self.ax = self.fig.axes[0]

    def test_bar_plot_labels(self):
        actual = self.ax.get_xlabel()
        expected = "Years"
        self.assertEqual(actual, expected, "Expected bar plot xlabel to be 'Years'")
        actual = self.ax.get_ylabel()
        expected = "Average Page Views"
        self.assertEqual(actual, expected, "Expected bar plot ylabel to be 'Average Page Views'")

    def test_bar_plot_legend_habitants(self):
        actual = len(self.ax.get_legend().get_texts())
        expected = 12
        self.assertEqual(actual, expected, "Expected 12 months in legend")

class BoxPlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = time_series_visualizer.draw_box_plot()
        self.ax = self.fig.axes

    def test_box_plot_number(self):
        actual = len(self.ax)
        expected = 2
        self.assertEqual(actual, expected, "Expected 2 subplots in box plot")

    def test_box_plot_labels(self):
        actual = self.ax[0].get_title()
        expected = "Year-wise Box Plot (Trend)"
        self.assertEqual(actual, expected, "Expected title of first subplot to be 'Year-wise Box Plot (Trend)'")
        actual = self.ax[1].get_title()
        expected = "Month-wise Box Plot (Seasonality)"
        self.assertEqual(actual, expected, "Expected title of second subplot to be 'Month-wise Box Plot (Seasonality)'")

if __name__ == "__main__":
    unittest.main()