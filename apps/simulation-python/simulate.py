import random, statistics

def run_simulation(agents=10, tasks=1000, fail_rate=0.05):
    processed, latencies = 0, []
    for _ in range(tasks):
        if random.random() < fail_rate:
            continue
        latency = random.uniform(0.1, 1.0)
        latencies.append(latency)
        processed += 1
    throughput = processed / sum(latencies) if latencies else 0
    return {"agents": agents, "tasks": tasks, "processed": processed,
            "throughput": throughput, "median_latency": statistics.median(latencies) if latencies else None}

if __name__ == "__main__":
    print(run_simulation())
