import os

import yaml
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(debug=True, openapi_url="/api/v1/openapi.json", docs_url="/api/v1/docs")

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, "oas.yaml")

oas_doc = yaml.safe_load(open(filename))

app.openapi = lambda :oas_doc


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


from controller import product_controller