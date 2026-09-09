class VRReplica:
    """Viewstamped Replication protocol node."""
    def __init__(self, replica_id: int, total_nodes: int = 3):
        self.replica_id = replica_id
        self.total_nodes = total_nodes
        self.view_number = 0
        self.status = "NORMAL"
        self.op_number = 0
        self.commit_number = 0
        self.log = []

    def is_primary(self) -> bool:
        return (self.view_number % self.total_nodes) == self.replica_id

    def normal_prepare(self, op: str) -> dict:
        if not self.is_primary():
            return {"error": "Not primary"}
        self.op_number += 1
        self.log.append((self.op_number, op))
        return {
            "view": self.view_number,
            "op_num": self.op_number,
            "op": op
        }

    def start_view_change(self) -> dict:
        self.status = "VIEW_CHANGE"
        self.view_number += 1
        return {
            "replica_id": self.replica_id,
            "new_view": self.view_number,
            "last_op": self.op_number
        }
