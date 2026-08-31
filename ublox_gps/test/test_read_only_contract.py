from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[1]


def test_rate_configuration_is_suppressed_when_startup_config_is_disabled() -> None:
    gps_header = (PACKAGE_ROOT / "include/ublox_gps/gps.hpp").read_text(
        encoding="utf-8"
    )

    assert "config_on_startup_flag_ &&" in gps_header
    assert "!setRate(T::CLASS_ID, T::MESSAGE_ID, rate)" in gps_header


def test_read_only_node_blocks_configuration_and_rtcm_writes() -> None:
    node_source = (PACKAGE_ROOT / "src/node.cpp").read_text(encoding="utf-8")

    required = [
        'declare_parameter("read_only", false)',
        'declare_parameter("nmea_only", false)',
        "if (nmea_only_ && !read_only_)",
        "if (!read_only_) {\n    this->subscription_ =",
        "if (read_only_) {\n      return true;",
        "void UbloxNode::configureInf() {\n  if (read_only_)",
        "!read_only_ && getRosBoolean(this, \"config_on_startup\")",
        "if (!nmea_only_) {",
    ]
    for literal in required:
        assert literal in node_source, literal
