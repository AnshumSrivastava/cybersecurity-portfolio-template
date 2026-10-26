import subprocess, sys, tempfile, unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
PROJECT = ROOT.parent
class ToolkitTests(unittest.TestCase):
    def test_log_fixture_flags_repeated_failures(self):
        result = subprocess.run([sys.executable, ROOT / "log_monitor.py", "--log", PROJECT / "data/auth.log"], text=True, capture_output=True, check=True)
        self.assertIn("192.0.2.44", result.stdout)
    def test_staged_root_is_reported(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); (root / "etc/ssh").mkdir(parents=True); (root / "etc/ssh/sshd_config").write_text("PermitRootLogin no\nPasswordAuthentication no\n")
            result=subprocess.run([sys.executable, ROOT / "cis_audit.py", "--root", root], text=True, capture_output=True, check=True)
            self.assertIn("SSH-01", result.stdout)
if __name__ == "__main__": unittest.main()
