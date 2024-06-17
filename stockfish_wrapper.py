import socket
from stockfish import Stockfish


#! ENGINE INITIALIZATION
STOCKFISH_PATH = "D:\workspaces\python projects\chess player\stockfish\stockfish-windows-x86-64-avx2.exe"

stockfish = Stockfish(path=STOCKFISH_PATH, depth=18, parameters={"Threads": 6, "Minimum Thinking Time": 8}) # 18 is the depth of the engine
stockfish.update_engine_parameters({"Hash": 2048})  # 2GB hash


def get_best_move(fen):
    if stockfish.is_fen_valid():
        stockfish.set_fen_position(fen)
        best_move = stockfish.get_best_move()
        return best_move
    else:
        return False