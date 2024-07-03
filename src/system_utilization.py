import argparse

def run_utilization(utilization):
    # Placeholder function to simulate system utilization
    print(f"Running system at {utilization}% utilization")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run system utilization")
    parser.add_argument('--utilization', type=int, required=True, help="Target system utilization percentage")
    args = parser.parse_args()
    run_utilization(args.utilization)
