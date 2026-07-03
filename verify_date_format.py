def format_snapshot_display(filename_base):
    # filename_base is YYYY-MM-DD_HH-MM-SS
    try:
        parts = filename_base.split('_')
        date_part = parts[0]
        time_part = parts[1]
        
        y, m, d = date_part.split('-')
        h, mi, s = time_part.split('-')
        
        return f"{d}/{m}/{y[2:]} {h}:{mi}"
    except:
        return filename_base

def test_date_formatting():
    print("Testing Date Formatting...")
    
    # Test Case 1
    input_str = "2026-01-27_22-45-00"
    expected = "27/01/26 22:45"
    result = format_snapshot_display(input_str)
    print(f"Input: {input_str} -> Output: {result}")
    assert result == expected
    
    # Test Case 2 (Different time)
    input_str_2 = "2025-12-05_09-05-30"
    expected_2 = "05/12/25 09:05"
    result_2 = format_snapshot_display(input_str_2)
    print(f"Input: {input_str_2} -> Output: {result_2}")
    assert result_2 == expected_2

    # Verification of Mapping Logic (Mocking the set/dict logic)
    snapshots = ["2026-01-27_22-45-00.json", "2025-12-05_09-05-30.json"]
    display_map = {}
    
    for s in snapshots:
        base = s.replace('.json', '')
        disp = format_snapshot_display(base)
        display_map[disp] = base
    
    print("\nMapping Verification:")
    print(display_map)
    
    # Check lookup
    key = "27/01/26 22:45"
    val = display_map.get(key)
    assert val == "2026-01-27_22-45-00"
    print(f"Lookup {key} -> {val} (Correct)")
    
    print("\nDate Verification Passed!")

if __name__ == "__main__":
    test_date_formatting()
