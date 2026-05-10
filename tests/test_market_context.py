# -*- coding: utf-8 -*-

from src.market_context import detect_market, get_market_guidelines, get_market_role


def test_detects_yfinance_native_symbols_as_global():
    assert detect_market("C38U.SI") == "global"
    assert detect_market("JPYHKD") == "global"
    assert detect_market("JPYHKD=X") == "global"


def test_global_market_role_and_guidelines_do_not_apply_a_share_rules():
    assert get_market_role("C38U.SI", "zh") == "全球市场"

    guidelines = get_market_guidelines("JPYHKD=X", "zh")

    assert "全球市场标的" in guidelines
    assert "不要套用 A 股" in guidelines
