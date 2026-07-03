from swgoh_tracker.history import compare_snapshots
import json

def test_comparison():
    print("Testing Comparison logic...")

    # Mock Data 1 (Old)
    old_data = {
        "units": [
            {
                "data": {
                    "base_id": "JEDIKNIGHTANAKIN",
                    "name": "Jedi Knight Anakin",
                    "rarity": 5,
                    "gear_level": 11,
                    "relic_tier": 0
                }
            },
            {
                "data": {
                    "base_id": "ADMIRALPIETT",
                    "name": "Admiral Piett",
                    "rarity": 7,
                    "gear_level": 12,
                    "relic_tier": 0
                }
            }
        ]
    }

    # Mock Data 2 (New)
    new_data = {
        "units": [
            {
                "data": {
                    "base_id": "JEDIKNIGHTANAKIN",
                    "name": "Jedi Knight Anakin",
                    "rarity": 7,     # Upgrade: 5 -> 7
                    "gear_level": 11,
                    "relic_tier": 0
                }
            },
            {
                "data": {
                    "base_id": "ADMIRALPIETT",
                    "name": "Admiral Piett",
                    "rarity": 7,
                    "gear_level": 13, # Upgrade: 12 -> 13
                    "relic_tier": 5   # Upgrade: 0 -> 5
                }
            },
            {
                 "data": {
                    "base_id": "COMMANDERLUKESKYWALKER", # New Unlock
                    "name": "Commander Luke Skywalker",
                    "rarity": 7,
                    "gear_level": 1,
                    "relic_tier": 0
                }
            }
        ]
    }

    upgrades = compare_snapshots(old_data, new_data)
    
    print("\nResults:")
    for unit, changes in upgrades.items():
        print(f"Unit: {unit}")
        for c in changes:
            print(f"  - {c}")

    # Expected checks
    assert "Jedi Knight Anakin" in upgrades
    assert "Stars: 5 -> 7" in upgrades["Jedi Knight Anakin"]
    
    assert "Admiral Piett" in upgrades
    assert "Gear: 12 -> 13" in upgrades["Admiral Piett"]
    assert "Relic Tier: 0 -> 5" in upgrades["Admiral Piett"]

    assert "Commander Luke Skywalker" in upgrades
    assert any("Unlocked" in c for c in upgrades["Commander Luke Skywalker"])

    print("\nTest Passed!")

if __name__ == "__main__":
    test_comparison()
