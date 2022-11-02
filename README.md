# idom-dash

`idom-dash` is a Dash component library that uses [IDOM](https://github.com/idom-team/idom)
a Python package for creating highly interactive user interfaces. To learn more about
IDOM check out its [documentation](https://idom-docs.herokuapp.com/docs/index.html).

# Getting Started

```bash
pip install idom-dash dash==1.19.0
```

Then try out a quick example:

```python
import dash
from dash import html as dash_html

from idom_dash import adapt_layout, configure_app
from idom import component, html, use_state

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
configure_app(app)

@component
def ClickCount():
    count, set_count = use_state(0)
    return html.button(
        {
            "id": "click-counter",
            "onClick": lambda event: set_count(count + 1)
        },
        count
    )

app.layout = adapt_layout(
    dash_html.Div(
        [
            dash_html.H1("A simple click counter"),
            ClickCount(),
        ]
    )
)

if __name__ == "__main__":
    app.run("127.0.0.1", 5000, debug=True)
```

To learn what you can do with IDOM's interactive components, check out
[more examples](https://idom-docs.herokuapp.com/docs/examples.html).

# Developer Installation

Be sure you have [NPM](https://www.npmjs.com/get-npm) installed, then run the following commands to:

1. Clone this repository
2. Perform a developer installation
3. Run the test suite

```bash
git clone https://github.com/idom-team/idom-dash.git
cd idom-dash
pip install -e . -r requirements.txt
npm install
pytest tests
```

## Write your component code in `src/lib/components/IdomDashComponent.react.js`.

-   The demo app is in `src/demo` and you will import your example component code into your demo app.
-   Test your code in a Python environment:
    1. Build your code
        ```
        $ npm run build
        ```
    2. Run and modify the `usage.py` sample dash app:
        ```
        $ python usage.py
        ```
-   Write tests for your component.
    -   A sample test is available in `tests/test_usage.py`, it will load `usage.py` and you can then automate interactions with selenium.
    -   Run the tests with `$ pytest tests`.
    -   The Dash team uses these types of integration tests extensively. Browse the Dash component code on GitHub for more examples of testing (e.g. https://github.com/plotly/dash-core-components)
-   Add custom styles to your component by putting your custom CSS files into your distribution folder (`idom_dash`).
    -   Make sure that they are referenced in `MANIFEST.in` so that they get properly included when you're ready to publish your component.
    -   Make sure the stylesheets are added to the `_css_dist` dict in `idom_dash/__init__.py` so dash will serve them automatically when the component suite is requested.
-   [Review your code](./review_checklist.md)

## Create a production build and publish:

1. Build your code:
    ```
    $ npm run build
    ```
2. Create a Python distribution

    ```
    $ python setup.py sdist bdist_wheel
    ```

    This will create source and wheel distribution in the generated the `dist/` folder.
    See [PyPA](https://packaging.python.org/guides/distributing-packages-using-setuptools/#packaging-your-project)
    for more information.

3. Test your tarball by copying it into a new environment and installing it locally:

    ```
    $ pip install idom_dash-0.0.1.tar.gz
    ```

4. If it works, then you can publish the component to NPM and PyPI:

    1. Publish on PyPI
        ```
        $ twine upload dist/*
        ```
    2. Cleanup the dist folder (optional)
        ```
        $ rm -rf dist
        ```
    3. Publish on NPM (Optional if chosen False in `publish_on_npm`)
        ```
        $ npm publish
        ```
        _Publishing your component to NPM will make the JavaScript bundles available on the unpkg CDN. By default, Dash serves the component library's CSS and JS locally, but if you choose to publish the package to NPM you can set `serve_locally` to `False` and you may see faster load times._

5. Share your component with the community! https://community.plotly.com/c/dash
    1. Publish this repository to GitHub
    2. Tag your GitHub repository with the plotly-dash tag so that it appears here: https://github.com/topics/plotly-dash
    3. Create a post in the Dash community forum: https://community.plotly.com/c/dash
