import pandas as pd

data = {
    "Name":["User1","User2"],
    "ID Number": ["0000","1111"],
    "Booking Date": ["00-0-00","11-1-11"],
    "Booking Status": ["Confirmed","Canceled"],
    "Payment Status": ["Paid","No"]
}

user = {
    "Name":["User1","User2"]
}

df = pd.DataFrame(data)
df.to_csv(r'./assets/booking.csv', index=False)

du = pd.DataFrame(user)
du.to_csv(r'./assets/user.csv', index=False)