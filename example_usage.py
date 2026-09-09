from client import VRReplica

def main():
    print("=== Viewstamped Replication (VR) Engine ===")
    r0 = VRReplica(replica_id=0, total_nodes=3)
    r1 = VRReplica(replica_id=1, total_nodes=3)

    assert r0.is_primary() is True
    assert r1.is_primary() is False

    prep = r0.normal_prepare("SET_KEY_VAL_X_10")
    print("Normal prepare output:", prep)
    assert prep["op_num"] == 1

    vc = r0.start_view_change()
    print("View change initiated:", vc)
    assert r0.view_number == 1
    # In view 1, primary is 1 % 3 = 1
    r1.view_number = 1
    assert r1.is_primary() is True

    print("Viewstamped Replication verified successfully!")

if __name__ == "__main__":
    main()
