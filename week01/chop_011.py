import sys
line = sys.stdin
def main():
	for a in line:
		a = a.strip()
		if len(a) > 2:
			print(a[1:-1])#[1:len(s):-1]
if __name__ == '__main__':
	main()