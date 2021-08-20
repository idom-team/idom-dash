# There's some sort of race condition going on with the anyio import?
# Some module ends up only partially initialized for some reason...
import anyio._backends._asyncio

from idom_dash.idom_compat import run_daemon_server

from dash.testing.application_runners import import_app


# Basic test for the component rendering.
# The dash_duo pytest fixture is installed with dash (v1.0+)
def test_usage(dash_duo):
    # Start a dash app contained as the variable `app` in `usage.py`
    app = import_app("usage")

    host, port = "127.0.0.1", dash_duo.server.port
    run_daemon_server(app, host, port)
    dash_duo.driver.get(f"http://{host}:{port}/")

    # Get the click counter and check that it reacts to interaction
    click_counter = dash_duo.find_element("#click-counter")

    click_counter.click()
    click_counter.click()
    click_counter.click()

    dash_duo.wait_for_text_to_equal("#click-counter", "3")

    # check that dynamic component is interactable
    material_click_count = dash_duo.find_element(".MuiButtonBase-root")

    material_click_count.click()
    material_click_count.click()
    material_click_count.click()

    dash_duo.wait_for_text_to_equal(".MuiButtonBase-root", "3")
