"""Simulated customer preference data for the jPhone NPD example (aimldl.io).
300 customers; jPhone tests 6 prototypes against two rival brands (X and Y).
Attributes: brand, price, camera, battery, screen size, memory.
All data is synthetic, for illustration only."""
import numpy as np, pandas as pd
rng = np.random.default_rng(42)
N = 300
segs = {"Value seeker": 0.30, "Camera lover": 0.25, "Battery first": 0.20, "Power user": 0.25}
# mean importance per segment: Brand, Price, Camera, Battery, Screen, Memory
mu = {"Value seeker":  [10, 40, 15, 15, 8, 12],
      "Camera lover":  [12, 15, 40, 13, 8, 12],
      "Battery first": [10, 18, 13, 37, 8, 14],
      "Power user":    [12, 13, 13, 12, 22, 28]}
def lv(base, sd=0.8):
    return np.clip(np.round(np.array(base, float) + rng.normal(0, sd, len(base))), 1, 7).astype(int)
rows = []
for i in range(N):
    s = rng.choice(list(segs), p=list(segs.values()))
    w = rng.dirichlet(np.array(mu[s]) / 3) * 100
    w = np.round(w).astype(int); w[np.argmax(w)] += 100 - w.sum()
    brand = lv([4, 5.5, 4.5])                      # jPhone (new), X (established), Y
    price = lv([7, 4.5, 1.5]) if s == "Value seeker" else lv([5.5, 4, 2.5])
    cam   = lv([1.5, 4.5, 7]) if s == "Camera lover" else lv([2.5, 4.5, 6])
    bat   = lv([1.5, 7])      if s == "Battery first" else lv([3, 6])
    scr   = lv([2, 4.5, 7])   if s == "Power user" else lv([4, 5, 4])
    mem   = lv([1.5, 4.5, 7]) if s == "Power user" else lv([3.5, 5, 5.5])
    screener = rng.random() < 0.35
    rows.append(dict(
        customer_id=f"C{i+1:03d}", segment=s,
        imp_brand=w[0], imp_price=w[1], imp_camera=w[2], imp_battery=w[3], imp_screen=w[4], imp_memory=w[5],
        brand_jPhone=brand[0], brand_X=brand[1], brand_Y=brand[2],
        r_price_20k=price[0], r_price_25k=price[1], r_price_30k=price[2],
        r_cam_basic=cam[0], r_cam_good=cam[1], r_cam_best=cam[2],
        r_bat_1day=bat[0], r_bat_2days=bat[1],
        r_scr_6_1=scr[0], r_scr_6_5=scr[1], r_scr_6_8=scr[2],
        r_mem_128=mem[0], r_mem_256=mem[1], r_mem_512=mem[2],
        decision_rule="Screen first" if screener else "Trade off",
        dealbreaker_max_price=int(rng.choice([25000, 30000], p=[0.6, 0.4])) if screener else np.nan,
        dealbreaker_min_battery=rng.choice(["2 days", "1 day"]) if screener else None,
        dealbreaker_min_memory=rng.choice(["256 GB", "128 GB"], p=[0.4, 0.6]) if screener else None))
pd.DataFrame(rows).to_csv("jphone_customer_preferences.csv", index=False)
P = lambda n, b, p, c, bt, s, m, role: dict(product=n, brand=b, role=role, price=p, camera=c, battery=bt, screen=s, memory=m)
pd.DataFrame([
    P("jPhone P1", "jPhone", 20000, "Good",  "2 days", '6.5"', "128 GB", "Prototype"),
    P("jPhone P2", "jPhone", 25000, "Best",  "1 day",  '6.5"', "256 GB", "Prototype"),
    P("jPhone P3", "jPhone", 25000, "Good",  "2 days", '6.8"', "256 GB", "Prototype"),
    P("jPhone P4", "jPhone", 30000, "Best",  "2 days", '6.8"', "512 GB", "Prototype"),
    P("jPhone P5", "jPhone", 20000, "Basic", "2 days", '6.1"', "256 GB", "Prototype"),
    P("jPhone P6", "jPhone", 30000, "Best",  "1 day",  '6.1"', "512 GB", "Prototype")]
).to_csv("jphone_prototypes.csv", index=False)
pd.DataFrame([
    P("Phone X", "X", 25000, "Good", "2 days", '6.5"', "128 GB", "Competitor"),
    P("Phone Y", "Y", 30000, "Best", "1 day",  '6.8"', "256 GB", "Competitor")]
).to_csv("competitors.csv", index=False)
