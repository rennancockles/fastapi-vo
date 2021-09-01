# FastAPI View Objects

<p align="center">
    <em>FastAPI-VO, view objects for FastAPI designed for simplicity.</em>
</p>

<p align="center">
  <a href="https://github.com/rennancockles/fastapi-vo/actions?query=workflow%3ALint%20and%20Test" target="_blank">
      <img src="https://img.shields.io/github/workflow/status/rennancockles/fastapi-vo/Lint%20and%20Test?label=Test" alt="Test">
  </a>
  <a href="https://github.com/rennancockles/fastapi-vo/actions?query=workflow%3ARelease" target="_blank">
      <img src="https://img.shields.io/github/workflow/status/rennancockles/fastapi-vo/Release?label=Publish" alt="Publish">
  </a>
  <a href="https://codecov.io/gh/rennancockles/fastapi-vo" target="_blank">
      <img src="https://img.shields.io/codecov/c/github/rennancockles/fastapi-vo?color=%2334D058" alt="Coverage">
  </a>
  <a href="https://pypi.org/project/fastapi-vo/" target="_blank">
      <img src="https://img.shields.io/pypi/v/FastAPI-VO?color=blue" alt="Package version">
  </a>
</p>

---

**Source Code**: <a href="https://github.com/rennancockles/fastapi-vo" target="_blank">https://github.com/rennancockles/fastapi-vo</a>

---

FastAPI-VO is a library for creating simple <a href="https://pydantic-docs.helpmanual.io/" class="external-link" target="_blank">FastAPI</a> view objects just by `picking` or `omitting` parts of a model. It is designed to be simple, intuitive and easy to use.

It is so simple that doesn't need much explanation. Just check some examples below.


## Requirements

A recent and currently supported version of Python (right now, <a href="https://www.python.org/downloads/" class="external-link" target="_blank">Python supports versions 3.6 and above</a>).

**FastAPI-VO** only requires **FastAPI**, but it will be automatically installed when you install FastAPI-VO.

## Installation

<div class="termy">

```console
$ pip install fastapi-vo
---> 100%
Successfully installed fastapi-vo
```

</div>

## Example

For an introduction to FastAPI, see the <a href="https://fastapi.tiangolo.com/" target="_blank">FastAPI documentation</a>.

Here's a quick example. ✨

<details>
<summary>👀 Full code preview</summary>


```Python
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

from fastapi_vo import Omit, Pick


class User(BaseModel):
    username: str
    password: str
    is_active: bool = True
    is_admin: bool = False


Auth = Pick(User, ["username", "password"], classname="Auth")
NoPassword = Omit(User, "password", classname="NoPasswordUser")

app = FastAPI()
johndoe = User(
    username="johndoe",
    password="secret",
    is_admin=False,
    is_active=True,
)
janedoe = User(
    username="janedoe",
    password="janesecret",
    is_admin=True,
    is_active=True,
)


@app.get("/users/", response_model=List[NoPassword])
async def list_users():
    return [johndoe, janedoe]


@app.get("/users/john/", response_model=NoPassword)
async def get_user():
    return johndoe


@app.get("/login/", response_model=NoPassword)
async def login(user: Auth):
    # some authentication logic in here
    return user
```

</details>


### Create a Model

Let's create a model called `user` with:
* `username`
* `password`
* `is_active`
* `is_admin`

```Python
from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str
    is_active: bool = True
    is_admin: bool = False


johndoe = User(
    username="johndoe",
    password="secret",
    is_admin=False,
    is_active=True,
)
```

### Create a Route

Now we are going to create a FastAPI app with a route to get the user data.


```Python hl_lines="1 12 21-23"
from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str
    is_active: bool = True
    is_admin: bool = False


app = FastAPI()
johndoe = User(
    username="johndoe",
    password="secret",
    is_admin=False,
    is_active=True,
)


@app.get("/user/", response_model=User)
async def get_user():
    return johndoe
```

This way, FastAPI will return all the user data, including the **password**, and it is not a good thing to do.

### Omitting a field

Now let's use the **Omit** function to return everything from the user, **but** the password.


```Python hl_lines="4 23"
from fastapi import FastAPI
from pydantic import BaseModel

from fastapi_vo import Omit


class User(BaseModel):
    username: str
    password: str
    is_active: bool = True
    is_admin: bool = False


app = FastAPI()
johndoe = User(
    username="johndoe",
    password="secret",
    is_admin=False,
    is_active=True,
)


@app.get("/user/", response_model=Omit(User, "password"))
async def get_user():
    return johndoe
```

### Multiple variations of the same model

If you want to use multiple variations of the same class, you have to give it a new `classname` to avoid conflicts. Another approach is to assign the value to a **variable** and reuse it.

Check the examples below.

```Python hl_lines="1 15 24-39"
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

from fastapi_vo import Omit


class User(BaseModel):
    username: str
    password: str
    is_active: bool = True
    is_admin: bool = False


NoPassword = Omit(User, "password", classname="NoPasswordUser")

app = FastAPI()
johndoe = User(
    username="johndoe",
    password="secret",
    is_admin=False,
    is_active=True,
)
janedoe = User(
    username="janedoe",
    password="janesecret",
    is_admin=True,
    is_active=True,
)


@app.get("/users/", response_model=List[NoPassword])
async def list_users():
    return [johndoe, janedoe]


@app.get("/users/john/", response_model=NoPassword)
async def get_user():
    return johndoe
```

### Picking a field

Now let's create a login route with another variation of the user model by picking some fields

Check the examples below.


```Python hl_lines="5 15 43-46"
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

from fastapi_vo import Omit, Pick


class User(BaseModel):
    username: str
    password: str
    is_active: bool = True
    is_admin: bool = False


Auth = Pick(User, ["username", "password"], classname="Auth")
NoPassword = Omit(User, "password", classname="NoPasswordUser")

app = FastAPI()
johndoe = User(
    username="johndoe",
    password="secret",
    is_admin=False,
    is_active=True,
)
janedoe = User(
    username="janedoe",
    password="janesecret",
    is_admin=True,
    is_active=True,
)


@app.get("/users/", response_model=List[NoPassword])
async def list_users():
    return [johndoe, janedoe]


@app.get("/users/john/", response_model=NoPassword)
async def get_user():
    return johndoe


@app.get("/login/", response_model=NoPassword)
async def login(user: Auth):
    # some authentication logic in here
    return user
```

## License

This project is licensed under the terms of the MIT license.