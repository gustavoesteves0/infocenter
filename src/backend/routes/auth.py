from fastapi import APIRouter
from controllers.auth import UserCreate, Token, register, login_for_access_token, read_users_me

router = APIRouter()

router.post("/register/", response_model=UserCreate)(register)
router.post("/token", response_model=Token)(login_for_access_token)
router.get("/users/me/")(read_users_me)