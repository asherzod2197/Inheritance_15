# 15. Uxlash vaqti kuzatuvchisi

class SleepTracker:
    def __init__(self, sleep_type, hours_list):
        self.sleep_type = sleep_type      # "Kecha", "Kunduz", "Tushdan keyin" va h.k.
        self.hours = hours_list           # uxlash soatlari ro'yxati (masalan: [7, 8, 6.5])

    def average_sleep(self):
        """O'rtacha uxlash vaqti (soat)"""
        if not self.hours:
            return 0.0
        return sum(self.hours) / len(self.hours)

    def __str__(self):
        avg = self.average_sleep()
        return f"{self.sleep_type:12} | Kunlar soni: {len(self.hours):2} | O‘rtacha: {avg:4.1f} soat"


# -----------------------------------------------
# Voris sinflar (chiroyliroq chiqish + emoji)
# -----------------------------------------------

class NightSleep(SleepTracker):
    def __str__(self):
        avg = self.average_sleep()
        return f"🌙 Kecha uxlagan  | {len(self.hours):2} kun | o‘rtacha {avg:4.1f} soat"


class DaySleep(SleepTracker):
    def __str__(self):
        avg = self.average_sleep()
        return f"☀️ Kunduz uxlagan | {len(self.hours):2} kun | o‘rtacha {avg:4.1f} soat"


# --------------------------------------------------
# Umumiy natijani chiqarish
# --------------------------------------------------

def show_sleep_statistics(sleep_records):
    print("\n" + "═" * 60)
    print("     UXLASH KUZATUVI — O‘RTACHA SOATLAR     ".center(60))
    print("═" * 60)
    print("Uxlash turi          | Kunlar | O‘rtacha uyqu (soat)")
    print("─" * 60)

    total_hours = 0
    total_days = 0

    for record in sleep_records:
        print(record)
        avg = record.average_sleep()
        days = len(record.hours)
        total_hours += avg * days
        total_days += days

    if total_days > 0:
        overall_avg = total_hours / total_days
        print("─" * 60)
        print(f"Umumiy o‘rtacha uyqu (barcha kunlar):     {overall_avg:4.1f} soat / kun")
    print("═" * 60 + "\n")


# Test ma'lumotlari
uxlashlar = [
    NightSleep("Kecha", [7.0, 8.5, 6.0, 7.5, 8.0]),
    DaySleep("Kunduz", [1.5, 2.0, 0.0, 1.0]),
    NightSleep("Kecha (dam olish)", [9.0, 8.0]),
    DaySleep("Tushdan keyin", [0.8, 1.2, 1.5]),
]

show_sleep_statistics(uxlashlar)


# Sizning misol qiymatlaringiz bilan:
print("\nSizning misol ma'lumotlaringiz:\n")
misol_uxlash = [
    NightSleep("Kecha", [7, 8]),
    DaySleep("Kunduz", [1, 2]),
]

show_sleep_statistics(misol_uxlash)
