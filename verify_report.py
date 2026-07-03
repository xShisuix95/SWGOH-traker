from swgoh_tracker.history import find_closest_snapshot, compare_snapshots

def test_guild_report_logic():
    print("Testing Guild Report Helper Functions...")

    # Mock Snapshots
    snapshots = [
        "2026-01-28_10-00-00.json",
        "2026-01-27_22-00-00.json",
        "2026-01-27_10-00-00.json",
        "2026-01-20_10-00-00.json"
    ]
    
    # Test Exact Date Match (should pick latest of that day)
    target = "2026-01-27"
    expected = "2026-01-27_22-00-00.json" # Latest of that day
    result = find_closest_snapshot(snapshots, target)
    print(f"Target: {target} -> Found: {result}")
    assert result == expected

    # Test No Match
    target = "2025-01-01"
    result = find_closest_snapshot(snapshots, target)
    print(f"Target: {target} -> Found: {result}")
    assert result is None
    
    print("\nData Sorting Test:")
    # Verify that the sorted order assumption holds if we just sorted strings
    # The formats YYYY-MM-DD_HH-MM-SS sort chronologically if strings are sorted
    sorted_snaps = sorted(snapshots, reverse=True)
    print(f"Sorted: {sorted_snaps}")
    assert sorted_snaps[0] == "2026-01-28_10-00-00.json"
    
    print("\nLogic Verification Passed!")

if __name__ == "__main__":
    test_guild_report_logic()
