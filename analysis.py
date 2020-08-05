from tqdm import tqdm
from scipy.signal import welch


dur = 0
area = 0

crits = []

with open("./data/p0.0001_256/data.txt", "r") as raw, open(
	"./data/p0.0001_256/events.txt", "w"
) as out:
	for line in tqdm(raw.readlines()[3:]):
		strs = line.rstrip(";\n\r ").split(";")
		crit = int(strs[0])
		crits.append(crit)
		if crit == 0 and dur > 0:
			out.write(f"{dur};{area}\n")
			dur = 0
			area = 0
		elif crit > 0:
			dur += 1
			area += crit

N = len(crits)
freq, density = welch(crits, nperseg=N / 10000)
with open("./data/p0.0001_256/nps10000.txt", "w") as file:
	for f, s in zip(freq, density):
		file.write(f"{f};{s}\n")
