import pandas as pd
from sqlalchemy import text
from mysql_handler import MySQLManager


# --- Step 1: MySQL setup ---
db = MySQLManager()
db.connect()
db.create_database("mydatabase")
db.close()

# --- Step 2: Get SQLAlchemy engine ---
engine = db.get_sqlalchemy_engine("mydatabase")

# --- Step 3: Load and process CSV ---
df = pd.read_csv("./Data/credit_card.csv")

# Convert date format
df['Week_Start_Date'] = pd.to_datetime(df['Week_Start_Date'], format='%d-%m-%Y')

# --- Step 4: Upload to MySQL ---
df.to_sql(
    name="transaction_detail",
    con=engine,
    if_exists="replace",
    index=False
)

# --- Step 5: Verify ---
with engine.connect() as conn:
    result = conn.execute(text("SELECT COUNT(*) FROM transaction_detail"))
    print(f"✅ {list(result)[0][0]} rows inserted successfully.")
