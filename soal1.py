from sklearn.datasets import load_iris
from plotnine import (
    ggplot, aes, geom_point, geom_smooth,
    labs, theme_minimal, theme, element_text
)

# Load dataset Iris
iris = load_iris(as_frame=True)
df = iris.frame

# Rename columns
df = df.rename(columns={
    "sepal length (cm)": "sepal_length",
    "petal length (cm)": "petal_length",
    "target": "species_id"
})

# Convert target values to species names
species_map = {
    0: "setosa",
    1: "versicolor",
    2: "virginica"
}
df["species"] = df["species_id"].map(species_map)

# Create scatter plot and regression lines
plot = (
    ggplot(df, aes(
        x="sepal_length",
        y="petal_length",
        color="species"
    ))
    + geom_point(size=2, alpha=0.8)
    + geom_smooth(method="lm", se=True)
    + labs(
        title="Iris Dataset: Sepal Length vs Petal Length",
        x="Sepal Length (cm)",
        y="Petal Length (cm)",
        color="Species"
    )
    + theme_minimal()
    + theme(
        figure_size=(10, 6),
        plot_title=element_text(size=14, weight="bold")
    )
)

# Display and save the plot
print(plot)
plot.save("iris_scatter_plot.png", width=10, height=6, dpi=300)
