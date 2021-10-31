import argparse
import array
import json

parser = argparse.ArgumentParser()
parser.add_argument('--init', help='called when new game')
parser.add_argument('--iterations', help='number of iterations in game')
parser.add_argument('--last_opponent_move', help='last opponent move')

args = parser.parse_args()

f = open("tData.json")

#load data from json file into a python dict called data
data = json.load(f)

#booleans to check if we identify the opponent's algorithm
algo_check_1 = False

#if it is the first round, initialize a bunch of stuff
if args.init == "true":
    data["num_rounds"] = args.iterations
    data["current_round"] = 0
    data["opp_prev_moves"] = []
    data["algo_detected"] = False
    data["next_moves"] = []
else:
    data["opp_prev_moves"].append(args.last_opponent_move)

if data["algo_detected"] == False:
    #scan opponent previous even moves to see if they are all confess
    for i in range(0, len(data["opp_prev_moves"]) - 1, 2):
        if data["opp_prev_moves"][i] == data["opp_prev_moves"][i+1]:
            algo_check_1 = False
            break
        else:
            algo_check_1 = True

#if true, then the other algorithim is simply switching back and forth
if algo_check_1:
    data["algo_detected"] = True;
    for i in range(5):
        data["next_moves"].append("confess") #push 5 confess to the stack

#if there are more than 10 previous opponent moves in the list, take away the oldest one
if len(data["opp_prev_moves"]) > 10:
    data["opp_prev_moves"].pop(0)

#what to return
if args.last_opponent_move == "zero":
    print("silent")
elif data["current_round"] + 1 == int(data["num_rounds"]):
    print("confess")
else:
    if data["algo_detected"]:
        print(data["next_moves"].pop())
    else:
        print(args.last_opponent_move)

#once the stack is empty, start trying to detect opponent algorithm again
if len(data["next_moves"]) == 0:
    data["algo_detected"] = False

#increase round counter by 1
if args.init != "true":
    data["current_round"] += 1

#update json file with updated dict
with open("tData.json", "w") as outfile:
    json.dump(data, outfile)

#for testing
#print(data)
