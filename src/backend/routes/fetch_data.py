from fastapi import FastAPI, APIRouter
from controllers.fetch import fetch_data, fetch_all_data, root

router = APIRouter()

router.get("/")(root)
router.get("/fetch/{class_name}")(fetch_data)
router.get("/fetch-all")(fetch_all_data)