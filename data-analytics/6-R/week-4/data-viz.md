# Data visualization

## ggplot2

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
