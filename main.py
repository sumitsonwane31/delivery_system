import json
import math
import os


# -------------------------------
# Utility Function
# -------------------------------
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


# -------------------------------
# Core Simulation Function
# -------------------------------
def run_simulation(file_name):
    with open(file_name) as f:
        data = json.load(f)

    warehouses = data["warehouses"]

    # Agents structure
    agents = {
        aid: {
            "location": loc[:],   # dynamic location
            "distance": 0,
            "packages": 0
        }
        for aid, loc in data["agents"].items()
    }

    # IMPORTANT: store initial location separately
    initial_agents = {aid: loc[:] for aid, loc in data["agents"].items()}

    packages = data["packages"]

    # -------------------------------
    # Step 1: Assign Packages (STATIC)
    # -------------------------------
    assignments = {aid: [] for aid in agents}

    for pkg in packages:
        warehouse_loc = warehouses[pkg["warehouse"]]

        nearest_agent = min(
            initial_agents.keys(),
            key=lambda aid: euclidean_distance(initial_agents[aid], warehouse_loc)
        )

        assignments[nearest_agent].append(pkg)

    # -------------------------------
    # Step 2: Simulate Delivery (DYNAMIC)
    # -------------------------------
    for agent_id, pkgs in assignments.items():
        agent = agents[agent_id]

        for pkg in pkgs:
            warehouse_loc = warehouses[pkg["warehouse"]]
            destination = pkg["destination"]

            # Agent → Warehouse
            d1 = euclidean_distance(agent["location"], warehouse_loc)

            # Warehouse → Destination
            d2 = euclidean_distance(warehouse_loc, destination)

            total_distance = d1 + d2

            agent["distance"] += total_distance
            agent["packages"] += 1

            # Update agent location (REALISTIC)
            agent["location"] = destination

    # -------------------------------
    # Step 3: Generate Report
    # -------------------------------
    report = {}
    best_agent = None
    best_efficiency = float("inf")

    for aid, data in agents.items():
        if data["packages"] == 0:
            efficiency = 0
        else:
            efficiency = data["distance"] / data["packages"]

        report[aid] = {
            "packages_delivered": data["packages"],
            "total_distance": round(data["distance"], 2),
            "efficiency": round(efficiency, 2)
        }

        if data["packages"] > 0 and efficiency < best_efficiency:
            best_efficiency = efficiency
            best_agent = aid

    report["best_agent"] = best_agent

    return report


# -------------------------------
# Run for All Test Cases
# -------------------------------
if __name__ == "__main__":
    for i in range(1, 11):
        file_name = f"test_case_{i}.json"

        if os.path.exists(file_name):
            print(f"\n🚀 Running {file_name}...")

            result = run_simulation(file_name)

            print(json.dumps(result, indent=4))

            # Save output
            output_file = f"report_{i}.json"
            with open(output_file, "w") as f:
                json.dump(result, f, indent=4)

            print(f"✅ Saved: {output_file}")