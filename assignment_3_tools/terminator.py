import argparse
import array
import json

parser = argparse.ArgumentParser()
parser.add_argument('--init', help='called when new game')
parser.add_argument('--iterations', help='number of iterations in game')
parser.add_argument('--last_opponent_move', help='last opponent move')

args = parser.parse_args()

f = open("tData.json")

data = json.load(f)

#booleans to check if we identify the opponent's algorithm
algo_check_1 = false
algo_check_2 = false


print(data)

#if it is the first round, initialize a bunch of stuff
if args.init == "true":
    data["num_rounds"] = args.iterations
    data["current_round"] = 0
    data["opp_prev_moves"] = []
else:
    data["opp_prev_moves"].append(args.last_opponent_move)

for i in range(0:len(data["opp_prev_moves"]):2):
    if data["opp_prev_moves"][i] == "confess":
        algo_check_1 = true

for i in range(1:len(data["opp_prev_moves"]):2):
d    if data["opp_prev_moves"][i] == "silent":
        algo_check_2 = true

if algo_check_1 and algo_check_2:
    data["algo_detected"] = true;
    for i in range(0:4:):
        data["next_moves"].push("confess")

if len(data["opp_prev_moves"]) > 10:
    data["opp_prev_moves"].pop(0)

if data["algo_detected"]:
    print(data["next_moves"].pop())
else:
    if args.last_opponent_move == "zero":
        print("silent")
    else:
        print(args.last_opponent_move)

if len(data["next_moves"]) == 0:
    data["algo_detected"] = false



data["current_round"] += 1

with open("tData.json", "w") as outfile:
    json.dump(data, outfile)

