from itertools import product
import argparse, sys

parser = argparse.ArgumentParser()
parser.add_argument("-b", "--base", help="Mot de base pour la generation. Exemple : \"entreprise\"", required=True)
parser.add_argument("--numberbefore", help="Nombre de numero avant le mot de base")
parser.add_argument("--numberafter", help="Nombre de numero apres le mot de base")

args = parser.parse_args()

if not len(sys.argv) > 1:
	parser.print_help()
	sys.exit(1)

basicword = args.base

numberbefore = 0
numberafter = 0

if args.numberbefore is not None:
	if args.numberbefore.isdigit():
		numberbefore = int(args.numberbefore)
	else:
		print "L argument \"numberbefore\" doit etre un chiffre"
		sys.exit(1)
if args.numberafter is not None:
	if args.numberafter.isdigit():
		numberafter = int(args.numberafter)
	else:
		print "L argument \"numberafter\" doit etre un chiffre"
		sys.exit(1)

wordlistfinal = []

wordlistupperlower = list(map(''.join, product(*(sorted(set((current.upper(), current.lower()))) for current in basicword))))

wordlistupperlowerwithnumber = []
if numberbefore > 0:
	formatwithzero = "{:0"+str(numberbefore)+"d}"
	numberbefore = numberbefore*"9"
	for i in range(int(numberbefore)+1):
		for current in wordlistupperlower:
			if len(str(i)) < len(str(numberbefore)):
				wordlistupperlowerwithnumber.append(formatwithzero.format(i)+current)
			wordlistupperlowerwithnumber.append(str(i)+current)

if numberafter > 0:
	formatwithzero = "{:0"+str(numberafter)+"d}"
	numberafter = numberafter*"9"
	for i in range(int(numberafter)+1):
		for current in wordlistupperlower:
			if len(str(i)) < len(str(numberafter)):
				wordlistupperlowerwithnumber.append(current+formatwithzero.format(i))
			wordlistupperlowerwithnumber.append(current+str(i))

wordlistupperlowernumberandchar = []

for current in wordlistupperlowerwithnumber:
	wordlistupperlowernumberandchar.append(current.replace('a', '@'))
	wordlistupperlowernumberandchar.append(current.replace('a', '@', 1))
	wordlistupperlowernumberandchar.append(current.replace('o', '0'))
	wordlistupperlowernumberandchar.append(current.replace('o', '0', 1))
	wordlistupperlowernumberandchar.append(current.replace('e', '3'))
	wordlistupperlowernumberandchar.append(current.replace('e', '3', 1))
	wordlistupperlowernumberandchar.append(current.replace('a', '@').replace('o', '0').replace('e', '3'))
	wordlistupperlowernumberandchar.append(current.replace('a', '@', 1).replace('o', '0', 1).replace('e', '3', 1))
	wordlistupperlowernumberandchar.append(current.replace('a', '@').replace('o', '0'))
	wordlistupperlowernumberandchar.append(current.replace('a', '@', 1).replace('o', '0', 1))
	wordlistupperlowernumberandchar.append(current.replace('a', '@').replace('e', '3'))
	wordlistupperlowernumberandchar.append(current.replace('a', '@', 1).replace('e', '3', 1))
	wordlistupperlowernumberandchar.append(current.replace('o', '0').replace('e', '3'))
	wordlistupperlowernumberandchar.append(current.replace('o', '0', 1).replace('e', '3', 1))

wordlistupperlowerandchar = []

for current in wordlistupperlower:
	wordlistupperlowerandchar.append(current.replace('a', '@'))
	wordlistupperlowerandchar.append(current.replace('a', '@', 1))
	wordlistupperlowerandchar.append(current.replace('o', '0'))
	wordlistupperlowerandchar.append(current.replace('o', '0', 1))
	wordlistupperlowerandchar.append(current.replace('e', '3'))
	wordlistupperlowerandchar.append(current.replace('e', '3', 1))
	wordlistupperlowerandchar.append(current.replace('a', '@').replace('o', '0').replace('e', '3'))
	wordlistupperlowerandchar.append(current.replace('a', '@', 1).replace('o', '0', 1).replace('e', '3', 1))
	wordlistupperlowerandchar.append(current.replace('a', '@').replace('o', '0'))
	wordlistupperlowerandchar.append(current.replace('a', '@', 1).replace('o', '0', 1))
	wordlistupperlowerandchar.append(current.replace('a', '@').replace('e', '3'))
	wordlistupperlowerandchar.append(current.replace('a', '@', 1).replace('e', '3', 1))
	wordlistupperlowerandchar.append(current.replace('o', '0').replace('e', '3'))
	wordlistupperlowerandchar.append(current.replace('o', '0', 1).replace('e', '3', 1))

wordlistfinal = wordlistupperlower+wordlistupperlowerwithnumber+wordlistupperlowernumberandchar+wordlistupperlowerandchar

outputfile = open('jajesult.txt', 'w+')
for current in wordlistfinal:
	outputfile.write(current+'\n')
	outputfile.write(current+'!\n')
outputfile.close()