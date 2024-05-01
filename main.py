import uvicorn
from fastapi import FastAPI
from datetime import date, timedelta
from midsummer import midsummer_date as midsommar

app = FastAPI()


@app.get("/midsummer/{year}")
async def read_midsummer(year: int):
    # Calculate the date of June 20th for the given year
    june_twentieth = date(year, 6, 20)

    # Find the Saturday following June 20th
    midsummer_date = june_twentieth + timedelta(
        days=(5 - june_twentieth.weekday() + 7) % 7
    )

    # Check if the calculated date is beyond June 26th
    if midsummer_date.day > 26:
        # If so, move back to the previous Saturday
        midsummer_date -= timedelta(days=7)

    return {"Midsummer Date": midsommar(year=year)}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
