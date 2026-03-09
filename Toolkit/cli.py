import argparse

def build_parser(): 
    parser= argparse.ArgumentParser(description="CTF Helper Toolkit")
    subparsers = parser.add_subparsers(dest="command", required=True)

    scan_parser = subparsers.add_parser("scan", help="Scan a target for vulnerabilities")
    scan_parser.add_argument("target",required=True, help="The target to scan (e.g., IP address or domain)")

    return parser
def handle_scan(args):
    print(f"[SCAN] Would scan target: {args.target}") 

def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "scan":
        handle_scan(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

