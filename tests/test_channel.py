from src.channel import Channel
"""Здесь надо написать тесты с использованием pytest для модуля Channel."""

def test_rename():
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    assert moscowpython.print_info() == 10000

