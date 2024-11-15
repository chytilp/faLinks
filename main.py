import traceback

import uvicorn
from fastapi import FastAPI

from falinks.router.user import router as users_router
from falinks.router.role import router as roles_router
from falinks.router.login import router as login_router

app = FastAPI()
app.include_router(users_router)
app.include_router(roles_router)
app.include_router(login_router)


def main() -> None:
    try:
        port: int = 8000
        uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
    except Exception as err:
        print(f"App ended with an error: {str(err)}, {traceback.format_exc()}")
        raise err


if __name__ == "__main__":
    main()
