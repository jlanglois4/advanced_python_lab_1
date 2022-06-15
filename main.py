import re
from pathlib import Path


def main():
	file_path = Path.cwd() / "router.txt"

	ip_address_regex = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

	aList = []
	if file_path.exists():
		with file_path.open() as router_file:
			for line in router_file.readlines():
				if line.__contains__("Active"):
					matches = re.findall(ip_address_regex, line)
					for match in matches:
						aList.append(match)


	final_set = list(sorted(set(aList)))

	for ip_address in final_set:
		print(ip_address)


if __name__ == "__main__":
	main()
