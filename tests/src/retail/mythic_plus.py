import os

CWD = os.path.dirname(__file__)

NAME = "mythic_plus"
LOG = f"{CWD}/../../logs/retail/{NAME}.txt"
OVERRUN = 5
OUTPUT = "Arcanedemon - The Azure Vault +18 (+1)"
SLEEPS = {
    "CHALLENGE_MODE_END": 1,
    "ENCOUNTER_END": 1,
}