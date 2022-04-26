from utils.code_and_show import example_app

dash.register_page(
    __name__,
    description = "Dash Sample App",
    layout_type = "2Row():1Col()",
    graph = "scatter",
    components = "checklist",
    callback = "1input:1output",
    dataset = "iris"
)

#     description = "This app uses tabs to highlight cultural dimensions on a bar chart.",
#     layout_type = "tabs",
#     components_type = ["dropdown", "card"],
#     graph_type = "bar", 
#     callback_type = "general"

filename = __name__.split("pages.")[1]

def layout():
    return example_app(f"pages/examples/{filename}.py")
