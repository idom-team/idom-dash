import os
from functools import wraps
from typing import TypeVar

import nox
from nox.sessions import Session

HEADLESS = bool(int(os.environ.get("HEADLESS", "0")))


_Func = TypeVar("_Func")


def pip_upgrade(func: _Func) -> _Func:
    @wraps(func)
    def decorator(session: Session) -> None:
        session.install("--upgrade", "pip", "setuptools", "wheel")
        func(session)

    return decorator


@nox.session
@pip_upgrade
def test(session: Session) -> None:
    session.env.update(os.environ)
    session.install("-r", "requirements/test-env.txt")
    session.install(".")

    session.run("idom", "install", "victory@35.4.0", "@material-ui/core@4.11.3")

    args = ["pytest", "tests"]
    if HEADLESS:
        args.append("--headless")
    session.run(*args)
