# ggplot2

ggplot2 includes features that:

- let you create many different types of plots

- customize the visual features of a plot

- add labels and annotations to a plot.

## Main conception

- **Aesthetic**:

  An aesthetic is a **visual property of an object** in your plot.

  Think of an aesthetic as a connection or mapping between a visual feature in your plot and a variable in your data.

- **Geom**:

  A geom refers to the **geometric object** used to represent your data.

- **Facet**:

  Facets let you display smaller groups or subsets of your data.

- **Label and Annotate functions**:

  the label and annotate functions let you customize your plot.

## Example

```r
ggplot(data = penguins) + geom_point(mapping = aes(x = flipper_length_mm, y = body_mass_g))
```

- `ggplot()`:

  It **creates a coordinate system** that you can add layers.

  The first argument of the `ggplot()` function is the dataset to use in the plot. In this case.

- `+`: It **adds a new layer** to your plot.

- `geom_point()`:

  The `geom_point()` function uses points to create scatterplots.

  The `geom_bar()` function uses bars to create bar charts, and so on.

- `(mapping = aes(x = flipper_length_mm, y = body_mass_g)`:

  Each geom function in ggplot2 takes a mapping argument. This defines how variables in your dataset are mapped to visual properties.

## Create a ggplot

1. Start with the `ggplot` function and choose a dataset to work with.

2. Add a `geom_function` to display your data.

3. Map the variables you want to plot in the argument of the `aes function`.

The template is as followed:

```r
ggplot(data = <data>) + <geom_function>(mapping = aes(<aesthetic mapping>))
```

## Aesthetic attributes

**Mapping** is an argument that matches up a specific variable in your data set with a specific aesthetic.

- **color**: This allows you to change the color of all of the points on your plot, or the color of each data group.

- **size**: This allows you to change the size of the points on your plot by data group.

- **shape**: This allows you to change the shape of the points on your plot by data group.

- **alpha**: It makes some points on a plot more **transparent**, or see-through, than others.

```r
ggplot(data, aes(x=distance, y=dep_delay, color=carrier, size=air_time, shape=carrier))
```

If you want to change all the color / shape / size of the points, set the parameter outside the `aes()` function.

```r
ggplot(data, aes(x=distance, y=dep_delay, size=air_time, shape=carrier), color=carrier)
```

## Smoothing

Smoothing enables the detection of a **data trend** even when you can't easily notice a trend from the plotted data points.

| Type            | Description                                  | Example                                                                                  |
| --------------- | -------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Loess smoothing | for the plots with **less than 1000 points** |  `ggplot(data, aes(x=, y=))+ geom_point() + geom_smooth(method="loess")`                 |
| Gam smoothing   | for plots with **a large number of points**. |  `ggplot(data, aes(x=, y=))+ geom_point() + geom_smooth(method="gam", formula = y ~s(x)` |

The `geom_jitter()` function creates a scatterplot and then **adds a small amount of random noise** to each point in the plot to **make the points easier to find**.

## Facet

Facets let you display smaller groups or subsets of your data.

- `facet_wrap()`: To facet your plot by a **single variable**

  ```r
  facet_wrap(~speices)
  ```

- `facet_grid()`: To facet your plot with **two variables**

  ```r
  facet_grid(sex~speices)
  ```

## Annotate

Annotate means to **add notes** to a document or diagram to **explain or comment** upon it.

- Title, subtitle and caption:

  add `labs(title=<title>, subtitle=<subtitle>, caption=<caption>)` as a new layer.

- Annotation: put the note wherever you want

  ```r
  annotation("text", x=100, y=200, label="my note")
  ```

## Save the plot

1. `ggsave()`

2. You can open an R graphics device like `png()` or `pdf()`; these will allow you to save your plot as a **.png or .pdf file**. You can also choose to print the plot and then close the device using `dev.off()`.
