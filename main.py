from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/v1/all")
def all_data():
    return {
        "matchs_reels": [{"id":"1","pays":"Angleterre","championnat":"Premier League","match":"Arsenal vs Man City","heure":"20:00","type":"reel","marches":{"1X2":{"V1":2.1}},"prono_gemini":"Over 2.5","confiance":"75%"}],
        "matchs_fifa": [
            {"id":"f1","jeu":"FC24","format":"4x4","championnat_fifa":"Angleterre","match":"Man City FIFA vs Liverpool FIFA","heure":"23:10","type":"fifa","marches":{"1X2":{"V1":1.85}},"prono_gemini":"Over 2.5","confiance":"78%"},
            {"id":"f2","jeu":"FC25","format":"5x5","championnat_fifa":"Italie","match":"Inter FIFA vs AC Milan FIFA","heure":"23:12","type":"fifa","marches":{"1X2":{"V1":2.10}},"prono_gemini":"BTTS Oui","confiance":"72%"}
        ]
    }

@app.get("/v1/coupon/fifa")
def coupon_fifa():
    return {"type":"Coupon FIFA","cote_totale":12.8,"matchs":all_data()["matchs_fifa"]}
