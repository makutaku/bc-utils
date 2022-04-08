

CONTRACT_MAP = {
    "AEX": {"code": "AE", "cycle": "FGHJKMNQUVXZ", "tick_date": "2008-05-05"},
    "ASX": {"code": "AP", "cycle": "HMUZ", "tick_date": "2019-11-03"},
    "AUD": {"code": "A6", "cycle": "HMUZ", "tick_date": "2009-11-24"},
    "BITCOIN": {"code": "BA", "cycle": "FGHJKMNQUVXZ", "tick_date": "2024-01-01"},
    "BOBL": {"code": "HR", "cycle": "HMUZ", "tick_date": "1999-06-23"},
    "BRENT_W": {"code": "CB", "cycle": "FGHJKMNQUVXZ", "tick_date": "2008-05-05"},
    "BTP": {"code": "II", "cycle": "HMUZ", "tick_date": "1999-06-23"},
    "BUND": {"code": "GG", "cycle": "HMUZ", "tick_date": "1999-06-23"},
    "BUXL": {"code": "GX", "cycle": "HMUZ", "tick_date": "2011-03-31"},
    "CAC": {"code": "MX", "cycle": "FGHJKMNQUVXZ", "tick_date": "2011-05-25"},
    "CAD": {"code": "D6", "cycle": "HMUZ", "tick_date": "2008-05-05"},
    "CANOLA": {"code": "RS", "cycle": "FHKNX", "tick_date": "2008-05-05"},
    "CHF": {"code": "S6", "cycle": "HMUZ", "tick_date": "2008-05-05"},
    "COCOA_NY": {"code": "CC", "cycle": "HKNUZ", "tick_date": "2008-05-04"},
    "COFFEE": {"code": "KC", "cycle": "HKNUZ", "tick_date": "2008-05-04"},
    "COPPER": {"code": "HG", "cycle": "FHJMNUVZ", "tick_date": "2008-05-04"},
    "CORN": {"code": "ZC", "cycle": "HKNUZ", "tick_date": "2008-05-04"},
    "COTTON": {"code": "CT", "cycle": "HKNVZ", "tick_date": "2008-05-04"},
    "CRUDE_W": {"code": "CL", "cycle": "FGHJKMNQUVXZ", "tick_date": "2008-05-05"},
    "DAX": {"code": "DY", "cycle": "HMUZ", "tick_date": "1999-06-23"},
    "DOW": {"code": "YM", "cycle": "HMUZ", "tick_date": "2008-05-04"},
    "DX": {"code": "DX", "cycle": "HMUZ", "tick_date": "2008-05-04"},
    "EDOLLAR": {"code": "GE", "cycle": "HMUZ", "tick_date": "2008-05-05", "days_count": 1000},
    "EUA": {"code": "CK", "cycle": "FGHJKMNQUVXZ", "tick_date": "2025-01-01", "days_count": 400},
    "EUR": {"code": "E6", "cycle": "HMUZ", "tick_date": "2008-05-05"},
    "EURGBP": {"code": "RP", "cycle": "HMUZ", "tick_date": "2008-05-05"},
    "EURIBOR": {"code": "IM", "cycle": "HMUZ", "tick_date": "2011-03-31"},
    "EUROSTX": {"code": "FX", "cycle": "HMUZ", "tick_date": "1999-06-23"},
    "FEEDCOW": {"code": "GF", "cycle": "FHJKQUVX", "tick_date": "2008-05-05"},
    "FTSE100": {"code": "X", "cycle": "HMUZ", "tick_date": "2002-01-01"},
    "GAS_US": {"code": "NG", "cycle": "FGHJKMNQUVXZ", "tick_date": "2008-05-05"},
    "GASOIL": {"code": "LF", "cycle": "FGHJKMNQUVXZ", "tick_date": "2008-05-05"},
    "GASOLINE": {"code": "RB", "cycle": "FGHJKMNQUVXZ", "tick_date": "2008-05-05"},
    "GBP": {"code": "B6", "cycle": "HMUZ", "tick_date": "2008-05-05"},
    "GILT": {"code": "G", "cycle": "HMUZ", "tick_date": "2002-01-01"},
    "GOLD": {"code": "GC", "cycle": "GJMQVZ", "tick_date": "2008-05-04"},
    "HEATOIL": {"code": "HO", "cycle": "FGHJKMNQUVXZ", "tick_date": "2008-05-05"},
    "HANG": {"code": "HS", "cycle": "FGHJKMNQUVXZ", "tick_date": "2016-01-01"},
    "IBXEX_mini": {"code": "EZ", "cycle": "HMUZ", "tick_date": "2025-01-01"},
    "JGB": {"code": "JX", "cycle": "HMUZ", "tick_date": "2027-01-01"},
    "JPY": {"code": "J6", "cycle": "HMUZ", "tick_date": "2008-05-05"},
    "LEANHOG": {"code": "HE", "cycle": "GJKMNQVZ", "tick_date": "2008-05-05"},
    "LIVECOW": {"code": "LE", "cycle": "GJMQVZ", "tick_date": "2008-05-05"},
    "LUMBER": {"code": "LB", "cycle": "FHKNUX", "tick_date": "2009-01-01"},
    "MILK3": {"code": "DL", "cycle": "FGHJKMNQUVXZ", "tick_date": "2008-05-05"},
    "MXP": {"code": "M6", "cycle": "HMUZ", "tick_date": "2008-05-05"},
    "NASDAQ": {"code": "NQ", "cycle": "HMUZ", "tick_date": "2008-05-05"},
    "NIKKEI": {"code": "NY", "cycle": "HMUZ", "tick_date": "2008-05-05"},
    "NZD": {"code": "N6", "cycle": "HMUZ", "tick_date": "2008-05-05"},
    "OAT": {"code": "FN", "cycle": "HMUZ", "tick_date": "1999-06-23"},
    "OATIES": {"code": "ZO", "cycle": "HKNUZ", "tick_date": "2008-07-01"},
    "OJ": {"code": "OJ", "cycle": "FHKNUX", "tick_date": "2008-05-04"},
    "PALLAD": {"code": "PA", "cycle": "HMUZ", "tick_date": "2008-05-05"},
    "PLAT": {"code": "PL", "cycle": "FJNV", "tick_date": "2008-05-05"},
    "RICE": {"code": "ZR", "cycle": "FHKNUX", "tick_date": "2009-01-01"},
    "ROBUSTA": {"code": "RM", "cycle": "FHKNUX", "tick_date": "2010-09-01"},
    "RUSSELL": {"code": "QR", "cycle": "HMUZ", "tick_date": "2008-05-05"},
    "SHATZ": {"code": "HF", "cycle": "HMUZ", "tick_date": "1999-06-23"},
    "SILVER": {"code": "SI", "cycle": "HKNUZ", "tick_date": "2008-05-04"},
    "SMI": {"code": "SZ", "cycle": "HMUZ", "tick_date": "1999-06-23"},
    "SOYBEAN": {"code": "ZS", "cycle": "FHKNQUX", "tick_date": "2008-05-04"},
    "SOYMEAL": {"code": "ZM", "cycle": "FHKNQUVZ", "tick_date": "2008-05-04"},
    "SOYOIL": {"code": "ZL", "cycle": "FHKNQUVZ", "tick_date": "2008-05-04"},
    "SP500": {"code": "ES", "cycle": "HMUZ", "tick_date": "2008-05-05"},
    "STERLING3": {"code": "L", "cycle": "HMUZ", "tick_date": "2011-03-31"},
    "SUGAR": {"code": "SW", "cycle": "HKQVZ", "tick_date": "2009-08-01", "days_count": 300},
    "SUGAR11": {"code": "SB", "cycle": "HKNV", "tick_date": "2008-05-04", "days_count": 200},
    "US10": {"code": "ZN", "cycle": "HMUZ", "tick_date": "2008-05-04"},
    "US2": {"code": "ZT", "cycle": "HMUZ", "tick_date": "2008-05-04"},
    "US30": {"code": "UD", "cycle": "HMUZ", "tick_date": "2008-05-04"},
    "US5": {"code": "ZF", "cycle": "HMUZ", "tick_date": "2008-05-04"},
    "V2X": {"code": "DV", "cycle": "FGHJKMNQUVXZ", "tick_date": "1999-06-23"},
    "VIX": {"code": "VI", "cycle": "FGHJKMNQUVXZ", "tick_date": "2009-11-24"},
    "WHEAT": {"code": "ZW", "cycle": "HKNUZ", "tick_date": "2008-05-04"},
}
